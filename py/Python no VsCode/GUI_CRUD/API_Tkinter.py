import tkinter as tk
from tkinter import messagebox, ttk
import requests

API_URL = "http://127.0.0.1:5000"

class AppUsuarios:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Usúarios")
        self.root.geometry("550x450")

        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10)

        frame_botoes = tk.Frame(self.root)
        frame_botoes.pack(pady=10)

        frame_tabela = tk.Frame(self.root)
        frame_tabela.pack(pady=10, fill=tk.BOTH, expand=True)

        tk.Label(frame_form, text="Email:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_email = tk.Entry(frame_form, width=40)
        self.entry_email.grid(row=0, column=1, padx=5,pady=5)

        tk.Label(frame_form, text="Senha:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_senha = tk.Entry(frame_form, width=40, show="*")
        self.entry_senha.grid(row=1, column=1, padx=5,pady=5)

        tk.Button(frame_botoes, text= "Cadastrar", command=self.criar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text= "Deletar", command=self.deletar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text= "Atualizar", command=self.atualizar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text= "Limpar Campos", command=self.limpar_campos).pack(side=tk.LEFT, padx=5)

        self.tree = ttk.Treeview(frame_tabela, columns=("ID","Email"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Email", text="Email")
        self.tree.column("ID", width=50, anchor=tk.CENTER)
        self.tree.column("Email", width=400, anchor=tk.W)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10)

        self.listar()
    
    def criar(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        if not email or not senha:
            messagebox.showerror("Aviso","Preencha o email e a senha!")
            return
        dados = {"email": email, "password": senha}
        try:
            resposta = requests.post(f"{API_URL}/criar_usuario", json=dados)
            messagebox.showinfo("Sucesso","Usuário criado com sucesso!")
            self.listar()
        except Exception as e:
            messagebox.showerror("Erro ao salvar o dado " + e)
    
    def deletar(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso","Selecione um usuario na tabela para deletar!")
            return
        id_usuario = self.tree.item(selecionado[0])['values'][0]
        email_usuario = self.tree.item(selecionado[0])['values'][1]

        confirmar = messagebox.askyesno("Confirmar",f"Deseja realmente deletar o usuario {email_usuario}?")

        if confirmar:
            try:
                resposta = requests.delete(f'{API_URL}/deletar_usuario/{id_usuario}')
                messagebox.showinfo("Sucesso","Usuario deletado com sucesso!")
                self.limpar_campos()
                self.listar()
            except Exception as e:
                messagebox.showerror("Erro","Erro ao deletar na API!")
    
    def selecionar_linha(self, event):
        selecionado = self.tree.selection()
        if selecionado:
            valores = self.tree.item(selecionado[0])['values']
            self.limpar_campos()
            self.entry_email.insert(0, valores[1])
    
    def limpar_campos(self):
        self.entry_email.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)
    
    def atualizar(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso","Selecione um usuario na tabela para atualizar!")
            return
        id_usuario =  self.tree.item(selecionado[0])["values"][0]
        novo_email = self.entry_email.get()
        nova_senha = self.entry_senha.get()

        if not novo_email or not nova_senha:
            messagebox.showwarning("Aviso","O campo de email ou senha não podem estar vazios!")
            return
        dados = {"email": novo_email, "senha": nova_senha} 
        try:
            resposta = requests.post(f"{API_URL}/atualizar_usuario/{id_usuario}", json=dados)
            messagebox.showinfo("Sucesso","Usuario atualizado com sucesso!")
            self.limpar_campos()
            self.listar()
        except Exception as e:
            messagebox.showerror("Erro","Erro ao atualizar" + e)


    def listar(self):
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        try:
            resposta = requests.get(f'{API_URL}/listar_usuarios')
            if resposta.status_code == 200:
                usuarios = resposta.json()
                for u in usuarios:
                    self.tree.insert("", tk.END, values=[u["id"],u["email"]])
                
        except Exception as e:
            messagebox.showerror('Erro','Erro ao executar a API')

if __name__ == "__main__":
    root = tk.Tk()
    app = AppUsuarios(root)
    root.mainloop()