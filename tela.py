import customtkinter as ctk
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image


# Funções de callback para os botões (para serem implementadas)
def login():
    print("login button clicked!")
    tela = ctk.CTk()


    teste = ctk.CTkLabel(tela, text = "hello")
    tela.mainloop()


def cadastro():
    print("Cadastro button clicked!")
    # Implementar funcionalidade de cadastro




# Configuração da janela principal
tela_inicial = ctk.CTk()
tela_inicial.title("Vacman Login")
tela_inicial.geometry("960x680")
tela_inicial.resizable(False, False)


# Carregar a imagem de fundo
bg_image = Image.open("img/FundoVeiavirus.png")
bg_photo = ImageTk.PhotoImage(bg_image)


# Configurar o label da imagem de fundo
background_label = Label(tela_inicial, image=bg_photo)
background_label.place(relwidth=1, relheight=1)


# Configurar estilo para o frame
style = ttk.Style()
style.configure("TFrame", background="#dab6fc")


# Configuração do frame de login com cor de fundo lilás
frame = ttk.Frame(tela_inicial, width=280, height=380, relief=tk.GROOVE, style="TFrame")
frame.pack_propagate(False)  # Evita que o frame redimensione automaticamente com base nos widgets filhos


# Centralizar o frame na tela
frame.place(relx=0.5, rely=0.5, anchor=CENTER)


# Adicionar título "VACMAN"
title_label = Label(master=frame, text="VACMAN", font=("Arial", 34, "bold"), fg="#6a0dad", bg="#dab6fc")
title_label.pack(pady=60)


# Botão de Login
login_button = Button(master=frame, text="Login",font=("Arial", 12, "bold"), command=login, bg="#6a0dad", activebackground="#5c0b8a", fg="white", width= 15, height=1)
login_button.pack(pady=15)


# Botão de Cadastro
cadastro_button = Button(master=frame, text="Cadastro", font=("Arial", 12, "bold"),command=cadastro, bg="#6a0dad", activebackground="#5c0b8a", fg="white",  width= 15, height=1)
cadastro_button.pack(pady=15)




# Iniciar a interface
tela_inicial.mainloop()
