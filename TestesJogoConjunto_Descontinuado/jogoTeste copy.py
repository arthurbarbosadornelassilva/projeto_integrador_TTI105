import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Funções de callback para os botões (para serem implementadas)
def login():
    app.init_login_screen()

def cadastro():
    app.init_cadastro_screen()

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
login_button = Button(master=frame, text="Login", font=("Arial", 12, "bold"), command=login, bg="#6a0dad", activebackground="#5c0b8a", fg="white", width=15, height=1)
login_button.pack(pady=15)

# Botão de Cadastro
cadastro_button = Button(master=frame, text="Cadastro", font=("Arial", 12, "bold"), command=cadastro, bg="#6a0dad", activebackground="#5c0b8a", fg="white", width=15, height=1)
cadastro_button.pack(pady=15)

# Iniciar a interface
tela_inicial.mainloop()

import customtkinter as ctk
from PIL import ImageTk, Image
from tkinter import messagebox
from Classes import DAO, Usuario

# DAO instance
dao = DAO.DAO()
# Usuario instance
aluno = Usuario.Usuario()

def salvar_cadastro():
    nome = nome_entry.get()
    email = email_entry.get()

    existe = dao.existeAluno(nome, email)[0]

    if existe == 1 or "@piaget.com" not in email:
        messagebox.showerror("Falha no cadastro", "Nome ou email inválidos")
    else:
        messagebox.showinfo("Cadastro realizado", "Suas informações foram cadastradas com sucesso")
        dao.registrarAluno(nome, email)
        aluno.setNomeAluno(nome)
        aluno.setEmailAluno(email)

class App:
    def __init__(self):
        self.aluno = Usuario.Usuario()
        self.dao = DAO.DAO()
        self.init_tela_inicial()

    def init_tela_inicial(self):
        self.tela_inicial = ctk.CTk()
        self.tela_inicial.title("Vacman Login")
        self.tela_inicial.geometry("960x680")
        self.tela_inicial.resizable(False, False)

        # Carregar a imagem de fundo
        bg_image = Image.open("img/FundoVeiavirus.png")
        bg_photo = ImageTk.PhotoImage(bg_image)

        # Configurar o label da imagem de fundo
        background_label = Label(self.tela_inicial, image=bg_photo)
        background_label.place(relwidth=1, relheight=1)

        # Configurar estilo para o frame
        style = ttk.Style()
        style.configure("TFrame", background="#dab6fc")

        # Configuração do frame de login com cor de fundo lilás
        frame = ttk.Frame(self.tela_inicial, width=280, height=380, relief=tk.GROOVE, style="TFrame")
        frame.pack_propagate(False)  # Evita que o frame redimensione automaticamente com base nos widgets filhos

        # Centralizar o frame na tela
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Adicionar título "VACMAN"
        title_label = Label(master=frame, text="VACMAN", font=("Arial", 34, "bold"), fg="#6a0dad", bg="#dab6fc")
        title_label.pack(pady=60)

        # Botão de Login
        login_button = Button(master=frame, text="Login", font=("Arial", 12, "bold"), command=self.init_login_screen, bg="#6a0dad", activebackground="#5c0b8a", fg="white", width=15, height=1)
        login_button.pack(pady=15)

        # Botão de Cadastro
        cadastro_button = Button(master=frame, text="Cadastro", font=("Arial", 12, "bold"), command=self.init_cadastro_screen, bg="#6a0dad", activebackground="#5c0b8a", fg="white", width=15, height=1)
        cadastro_button.pack(pady=15)

        self.tela_inicial.mainloop()

    def init_login_screen(self):
        self.tela_inicial.destroy()
        self.root_login = ctk.CTk()
        self.root_login.geometry(f"{960}x{680}")
        self.root_login.title("LOGIN ALUNO")

        image = Image.open("img/FundoVeiavirus.png")
        background_image = ImageTk.PhotoImage(image)

        background_label = ctk.CTkLabel(self.root_login, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame = ctk.CTkFrame(master=self.root_login, width=450, height=450, corner_radius=10)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        label_1 = ctk.CTkLabel(master=frame, width=400, height=60, corner_radius=10, fg_color=("gray70", "gray35"), text="Faça seu login Aluno!")
        label_1.place(relx=0.5, rely=0.3, anchor="center")

        self.nome_entry = ctk.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Nome")
        self.nome_entry.place(relx=0.5, rely=0.52, anchor="center")

        self.email_entry = ctk.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Email")
        self.email_entry.place(relx=0.5, rely=0.6, anchor="center")

        button_login = ctk.CTkButton(master=frame, text="LOGIN", corner_radius=6, command=self.validar_login, width=400)
        button_login.place(relx=0.5, rely=0.7, anchor="center")

        self.root_login.mainloop()

    def init_cadastro_screen(self):
        self.tela_inicial.destroy()
        self.root_cadastro = ctk.CTk()
        self.root_cadastro.title("Cadastro de Aluno")
        self.root_cadastro.geometry(f"{960}x{680}")

        image = Image.open("img/FundoVeiavirus.png")
        background_image = ImageTk.PhotoImage(image)

        background_label = ctk.CTkLabel(self.root_cadastro, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        titulo_label = ctk.CTkLabel(background_label, text="Cadastro de Aluno", font=("Arial", 20))
        titulo_label.place(relx=0.5, rely=0.1, anchor="center")

        frame = ctk.CTkFrame(background_label)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        nome_label = ctk.CTkLabel(frame, text="Nome:")
        nome_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.nome_entry_cadastro = ctk.CTkEntry(frame)
        self.nome_entry_cadastro.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        email_label = ctk.CTkLabel(frame, text="Email:")
        email_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.email_entry_cadastro = ctk.CTkEntry(frame)
        self.email_entry_cadastro.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        cadastro_botao = ctk.CTkButton(frame, text="Cadastrar", command=self.salvar_cadastro)
        cadastro_botao.grid(row=2, columnspan=2, pady=20)

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=2)

        self.root_cadastro.mainloop()

    def salvar_cadastro(self):
        nome = self.nome_entry_cadastro.get()
        email = self.email_entry_cadastro.get()

        existe = self.dao.existeAluno(nome, email)[0]

        if existe == 1 or "@piaget.com" not in email:
            messagebox.showerror("Falha no cadastro", "Nome ou email inválidos")
        else:
            messagebox.showinfo("Cadastro realizado", "Suas informações foram cadastradas com sucesso")
            self.dao.registrarAluno(nome, email)
            self.aluno.setNomeAluno(nome)
            self.aluno.setEmailAluno(email)

    def validar_login(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()

        if self.dao.existeAluno(nome, email)[0] == 1:
            self.root_login.destroy()
            self.init_ranking_screen()
        else:
            messagebox.showerror("Erro de Login", "Nome ou email inválidos")

    def init_ranking_screen(self):
        self.root_ranking = ctk.CTk()
        self.root_ranking.geometry(f"{960}x{680}")
        self.root_ranking.title("Ranking")

        bg_image = Image.open("img/FundoVeiavirus.png")
        bg_photo = ImageTk.PhotoImage(bg_image)

        background_label = Label(self.root_ranking, image=bg_photo)
        background_label.place(relwidth=1, relheight=1)

        frame = ttk.Frame(self.root_ranking, width=280, height=380, relief=tk.GROOVE, style="TFrame")
        frame.pack_propagate(False)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        title_label = Label(master=frame, text="Ranking", font=("Arial", 34, "bold"), fg="#6a0dad", bg="#dab6fc")
        title_label.pack(pady=60)

        jogar_button = Button(master=frame, text="Jogar", font=("Arial", 12, "bold"), command=self.init_game_screen, bg="#6a0dad", activebackground="#5c0b8a", fg="white", width=15, height=1)
        jogar_button.pack(pady=15)

        self.root_ranking.mainloop()

    def init_game_screen(self):
        self.root_ranking.destroy()
        # Inicializar a lógica do jogo aqui

if __name__ == '__main__':
    app = App()
