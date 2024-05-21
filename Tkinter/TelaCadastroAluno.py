import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from Classes import DAO

dao = DAO.DAO()

def salvar_cadastro():
    nome = nome_entry.get()
    email = email_entry.get()

    existe = dao.existeAluno(nome, email)

    if existe or "@piaget.com" not in email:
        messagebox.showerror("Falha no login", "Nome ou email inválidos")
    else:
        messagebox.showinfo("Suas informações foram cadastradas com sucesso")
        dao.registrarAluno(nome, email)

# Tela Principal
parent = tk.Tk()
parent.title("Formulário de cadastro")

# Centrazlização da tela
parent.geometry("480x340+725+350")

# Entrada Nome
nome_label = tk.Label(parent, text="Nome:")
nome_label.place(x=145, y=45, width=180, height=30)

nome_entry = tk.Entry(parent)
nome_entry.place(x=175, y=80)

# Entrada email
email_label = tk.Label(parent, text="Email:")
email_label.place(x=145, y=105, width=180, height=30)

email_entry = tk.Entry(parent)  
email_entry.place(x=175, y=140)

# Botão Login
login_botao = tk.Button(parent, text="Login", command=salvar_cadastro)
login_botao.place(x=185, y=170, width=100)

#FUncionar
parent.mainloop()