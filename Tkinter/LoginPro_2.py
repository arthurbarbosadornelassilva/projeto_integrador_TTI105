import customtkinter as ctk
import tkinter
from Classes import  DAO, Usuario
from tkinter import messagebox
from PIL import ImageTk, Image

# default
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

# DAO
dao = DAO.DAO()
# Usuario
professor = Usuario.Usuario()

def validar_login():
    nome = nome_entry.get()
    email = email_entry.get()

    existe = dao.existeProfessor(nome, email)[0]

    if existe == 1:
        messagebox.showinfo("Sucesso", f"Seja bem vindo, {nome}")
        professor.setNomeProfessor(nome)
        professor.setEmailProfessor(email)

    else:
        messagebox.showerror("Falha no login", "Nome ou email inválidos")

def new_window():
    # Tela sucesso-
    root_new = ctk.CTk()
    root_new.geometry(f"{960}x{680}")
    root_new.title("Sucesso professor")

    # Tela sucesso login
    frame_new = ctk.CTkFrame(master=root_new, width=450, height=450, corner_radius=10)
    frame_new.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    label_new = ctk.CTkLabel(master=frame_new, width=200, height=60, corner_radius=10,
                              fg_color=("gray70", "gray35"), text="You have successfully logged-in")
    label_new.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    root_new.mainloop()

# Tela login
root_login = ctk.CTk()
root_login.geometry(f"{960}x{680}")
root_login.title("LOGIN PROFESSOR")

# imagem fundo carregar
image = Image.open("img/FundoVeiavirus.png")
background_image = ImageTk.PhotoImage(image)

# fundo label
background_label = ctk.CTkLabel(root_login, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# frame janela
frame = ctk.CTkFrame(master=root_login, width=450, height=450, corner_radius=10)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

label_1 = ctk.CTkLabel(master=frame, width=400, height=60, corner_radius=10,
                       fg_color=("gray70", "gray35"), text="Faça o login Professor!")
label_1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

nome_entry = ctk.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Nome")
nome_entry.place(relx=0.5, rely=0.52, anchor=tkinter.CENTER)

email_entry = ctk.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Email")
email_entry.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

button_login = ctk.CTkButton(master=frame, text="LOGIN", corner_radius=6, command=validar_login, width=400)
button_login.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

root_login.mainloop()
