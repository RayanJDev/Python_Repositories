import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

def conectar():
    return sqlite3.connect('agenda.db')

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contatos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT NOT NULL
                    )
        """)

        conexao.commit()

    except Exception as erro:
        messagebox.showerror("ERROR",f'FALHA AO CRIAR TABELA!')

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

def inserir_contato(nome, telefone):

        nome = nome.strip()
        telefone = telefone.strip()

        if not nome or not telefone:
            limpar_campos()
            messagebox.showerror("Aviso","Insira dados válidos.")
            return

        telefone = ''.join(filter(str.isdigit, telefone))

        if len(telefone) < 11:
            limpar_campos()
            messagebox.showerror("Aviso","Telefone Inválido")
            return
        conexao = None

        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO contatos (nome, telefone) VALUES (?, ?)",
                (nome, telefone)
                )
            conexao.commit()

            limpar_campos()
            listar_contatos()

        except Exception as erro:
            if conexao:
                conexao.rollback()
                messagebox.showerror("Erro", f"Erro ao inserir contato:\n{erro}")
        finally:
            if conexao:
                conexao.close()

def listar_contatos():
    for i in arvore_listagem.get_children():
        arvore_listagem.delete(i)
    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT id, nome, telefone
            FROM contatos
            ORDER BY nome
        """)
        
        contatos = cursor.fetchall()

        for indice, contato in enumerate(contatos, start=1):
            id_real, nome, telefone = contato

            arvore_listagem.insert(
                "",
                tk.END,
                iid=str(id_real),
                values=(indice, nome, telefone)
            )
    except Exception as erro:
        messagebox.showerror("Erro", f"Erro ao listar contatos:\n{erro}")

    finally:
        if conexao:
            conexao.close()

def deletar_contato():
    item_selecionado = arvore_listagem.selection()

    if not item_selecionado:
        messagebox.showwarning("Aviso", "Selecione um contato para deletar")
        return

    id_real = item_selecionado[0]

    valores = arvore_listagem.item(item_selecionado)['values']
    #id_contato = valores[0]
    nome_contato = valores[1]

    confirmacao = messagebox.askyesno("Confirmar", f"Deletar realmente deletar {valores[1]}")

    if not confirmacao:
        return
    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM contatos WHERE id = ?", (id_real,))
        conexao.commit()
        limpar_campos()
        listar_contatos()
    except Exception as erro:
        if conexao:
            conexao.rollback()
        messagebox.showerror("Erro", f"Erro ao deletar contato:\n{erro}")

    finally:
        if conexao:
            conexao.close()

def editar_contato():
    item_selecionado = arvore_listagem.selection()

    if not item_selecionado:
        messagebox.showwarning("Aviso", "Selecione um contato para editar")
        return

    id_contato = item_selecionado[0]

    novo_nome = entry_nome.get().strip()
    novo_telefone = entry_telefone.get().strip()

    if not novo_nome or not novo_telefone:
        messagebox.showerror("Aviso","Erro ao Editar os campos")
        return

    telefone_numeros = ''.join(filter(str.isdigit, novo_telefone))

    if len(telefone_numeros) < 11:
        messagebox.showerror("Aviso","Telefone Inválido")
        return
    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE contatos
            SET nome = ?, telefone = ?
            WHERE id = ?
            """,
            (novo_nome,novo_telefone,id_contato)
        )

        if cursor.rowcount == 0:
            messagebox.showerror("Aviso","Contato não encontrado!")
            return
        conexao.commit()

        limpar_campos()
        listar_contatos()

    except Exception as erro:
        if conexao:
            conexao.rollback()

        messagebox.showerror("Aviso",f"Erro ao editar o contato: \n {erro}")

    finally:
        if conexao:
            conexao.close()

def preencher_campos(event):
    item_selecionado = arvore_listagem.selection()
    if not item_selecionado:
        return

    valores = arvore_listagem.item(item_selecionado[0])["values"]

    if len(valores) < 3:
        messagebox.showwarning("Aviso", "Dados do contato incompletos.")
        return

    entry_nome.delete(0, tk.END)
    entry_nome.insert(0, valores[1])

    entry_telefone.delete(0, tk.END)
    entry_telefone.insert(0, valores[2])

interface = tk.Tk()
interface.title("Agenda")
interface.geometry("400x450")

tk.Label(interface, text="Nome:").pack(pady=10)
entry_nome = tk.Entry(interface)
entry_nome.pack(pady=5)

tk.Label(interface, text="Telefone:").pack(pady=5)
entry_telefone = tk.Entry(interface)
entry_telefone.pack(pady=5)

frame_botoes = tk.Frame(interface)
frame_botoes.pack(pady=20)

botao_salvar = tk.Button(frame_botoes, text="Salvar Contato", bg="#d1ffd1",
                         command=lambda: inserir_contato(entry_nome.get(), entry_telefone.get()))
botao_salvar.grid(row=0, column=0, padx=5)

botao_deletar = tk.Button(frame_botoes, text="Deletar", bg="#ffd1d1", command=deletar_contato)
botao_deletar.grid(row=0, column=1, padx=5)

botao_editar = tk.Button(frame_botoes, text="Editar", bg="#fff5d1", command=editar_contato)
botao_editar.grid(row=0, column=2, padx=5)

colunas = ("ID", "Nome", "Telefone")
arvore_listagem = ttk.Treeview(interface, columns=colunas, show='headings')
arvore_listagem.heading('ID', text='ID')
arvore_listagem.heading('Nome', text="Nome")
arvore_listagem.heading('Telefone', text='Telefone')
arvore_listagem.column('ID', width=30)
arvore_listagem.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

arvore_listagem.bind("<<TreeviewSelect>>", preencher_campos)

criar_tabela()
listar_contatos()
interface.mainloop()