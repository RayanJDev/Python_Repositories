import tkinter as tk
from tkinter import messagebox

# Criando a janela
janela = tk.Tk()
janela.title("Calcula Números")

#Implementando a função que rá realizar a soma
def somar_numeros():
    try:
        primeiro_numero = float(entry_numero1.get())
        segundo_numero = float(entry_numero2.get())
        resultado = primeiro_numero / segundo_numero
        messagebox.showinfo("Resultado",f'O quociente da divisão é {resultado}')
    except ValueError:
        messagebox.showerror("Error: Value","Digite valores válidos!")
    except ZeroDivisionError:
        messagebox.showerror("Error: Zero Division","Não é possível dividir por zero!")

# Criando os widgets
label_numero1 = tk.Label(janela, text= "Número 1: ")
label_numero1.grid(row = 0,
                   column = 0,
                   padx = 10,
                   pady = 5,
                   sticky = "e")

entry_numero1 = tk.Entry(janela)
entry_numero1.grid(row = 0,
                   column = 1,
                   padx = 10,
                   pady = 5)

label_numero2 = tk.Label(janela, text="Número 2:")
label_numero2.grid(row=1,
                column=0,
                padx=10,
                pady=5,
                sticky="e")

entry_numero2 = tk.Entry(janela)
entry_numero2.grid(row=1,
                column=1,
                padx=10,
                pady=5)

botao_somar = tk.Button(janela, text="Executar", command=somar_numeros)
botao_somar.grid(row=2,
                 columnspan=2,
                 padx=10,
                 pady=5)

# Rodando o loop principal
janela.mainloop()
