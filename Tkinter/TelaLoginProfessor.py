import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from Classes import DAO, Usuario

dao = DAO.DAO()
# Função para validar o login
def validar_login():
    nome = nome_entry.get()
    email = email_entry.get()

    existe = dao.existeProfessor(nome, email)

    if existe:
        messagebox.showinfo("Sucesso", "Seja bem vindo, ")
        return nome, email
    else:
        messagebox.showerror("Falha no login", "Nome ou email inválidos")

# Tela Principal
parent = tk.Tk()
parent.title("Formulário de login")

# Entrada Nome
nome_label = tk.Label(parent, text="Nome:")
nome_label.pack()

nome_entry = tk.Entry(parent)
nome_entry.pack()

# Entrada email
email_label = tk.Label(parent, text="Email:")
email_label.pack()

email_entry = tk.Entry(parent)  
email_entry.pack()

# Botão Login
login_botao = tk.Button(parent, text="Login", command=validar_login)
login_botao.pack()

#FUncionar
parent.mainloop()