import tkinter as tk
from tkinter import messagebox, ttk
import requests

API_URL = "http://127.0.0.1:5000"

class App_Users:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Usúarios")
        self.root.geometry("550x450")

        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        table_frame = tk.Frame(self.root)
        table_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        tk.Label(frame_form, text="Email:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_email = tk.Entry(frame_form, width=40)
        self.entry_email.grid(row=0, column=1, padx=5,pady=5)

        tk.Label(frame_form, text="Senha:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_password = tk.Entry(frame_form, width=40, show="*")
        self.entry_password.grid(row=1, column=1, padx=5,pady=5)

        tk.Button(button_frame, text= "Cadastrar", command=self.create).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text= "Deletar", command=self.deletar).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text= "Atualizar", command=self.atualizar).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text= "Limpar Campos", command=self.clear_fields).pack(side=tk.LEFT, padx=5)

        self.tree = ttk.Treeview(table_frame, columns=("ID","Email"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Email", text="Email")
        self.tree.column("ID", width=50, anchor=tk.CENTER)
        self.tree.column("Email", width=400, anchor=tk.W)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10)

        self.list_requests()
    
    def create(self):
        email = self.entry_email.get()
        password = self.entry_password.get()

        if not email or not password:
            messagebox.showerror("Aviso","Preencha o email e a senha!")
            return
        data = {"email": email, "password": password}
        try:
            response = requests.post(f"{API_URL}/criar_usuario", json=data)
            messagebox.showinfo("Sucesso","Usuário criado com sucesso!")
            self.list_requests()
        except Exception as e:
            messagebox.showerror("Erro ao salvar o dado " + e)
    
    def delete(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Aviso","Selecione um usuario na tabela para deletar!")
            return
        user_id = self.tree.item(selected[0])['values'][0]
        email_usuario = self.tree.item(selected[0])['values'][1]

        confirmar = messagebox.askyesno("Confirmar",f"Deseja realmente deletar o usuario {email_usuario}?")

        if confirmar:
            try:
                response = requests.delete(f'{API_URL}/deletar_usuario/{user_id}')
                messagebox.showinfo("Sucesso","Usuario deletado com sucesso!")
                self.clear_fields()
                self.list_requests()
            except Exception as e:
                messagebox.showerror("Erro","Erro ao deletar na API!")
    
    def select_row(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0])['values']
            self.clear_fields()
            self.entry_email.insert(0, values[1])
    
    def clear_fields(self):
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
    
    def update(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Aviso","Selecione um usuario na tabela para atualizar!")
            return
        user_id =  self.tree.item(selected[0])["values"][0]
        new_email = self.entry_email.get()
        new_password = self.entry_password.get()

        if not new_email or not new_password:
            messagebox.showwarning("Aviso","O campo de email ou password não podem estar vazios!")
            return
        data = {"email": new_email, "password": new_password} 
        try:
            response = requests.post(f"{API_URL}/atualizar_usuario/{user_id}", json=data)
            messagebox.showinfo("Sucesso","Usuario atualizado com sucesso!")
            self.clear_fields()
            self.list_requests()
        except Exception as e:
            messagebox.showerror("Erro","Erro ao atualizar" + e)


    def list_requests(self):
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        try:
            response = requests.get(f'{API_URL}/listar_usuarios')
            if response.status_code == 200:
                usuarios = response.json()
                for u in usuarios:
                    self.tree.insert("", tk.END, values=[u["id"],u["email"]])
                
        except Exception as e:
            messagebox.showerror('Erro','Erro ao executar a API')

if __name__ == "__main__":
    root = tk.Tk()
    app = App_Users(root)
    root.mainloop()
