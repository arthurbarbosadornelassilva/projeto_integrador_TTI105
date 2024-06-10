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

    if existe == 1 or  "@piaget.com" not in email:
        messagebox.showerror("Falha no cadastro", "Nome ou email inválidos")
    else:
        messagebox.showinfo("Cadastro realizado", "Suas informações foram cadastradas com sucesso")
        dao.registrarAluno(nome, email)
        aluno.setNomeAluno(nome)
        aluno.setEmailAluno(email)


# Configurações iniciais do customtkinter
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")

# Tela Principal
parent = ctk.CTk()
parent.title("Cadastro de Aluno")
parent.geometry(f"{960}x{680}")

# Carregar imagem de fundo
image = Image.open("img/FundoVeiavirus.png")
background_image = ImageTk.PhotoImage(image)

# Label de fundo
background_label = ctk.CTkLabel(parent, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Título da janela
titulo_label = ctk.CTkLabel(background_label, text="Cadastro de Aluno", font=("Arial", 20))
titulo_label.place(relx=0.5, rely=0.1, anchor="center")

# Frame para organizar os widgets
frame = ctk.CTkFrame(background_label)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Entrada Nome
nome_label = ctk.CTkLabel(frame, text="Nome:")
nome_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

nome_entry = ctk.CTkEntry(frame)
nome_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Entrada Email
email_label = ctk.CTkLabel(frame, text="Email:")
email_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

email_entry = ctk.CTkEntry(frame)
email_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Botão de Cadastro
cadastro_botao = ctk.CTkButton(frame, text="Cadastrar", command=salvar_cadastro)
cadastro_botao.grid(row=2, columnspan=2, pady=20)

# Expansão das colunas do grid
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=2)

# Iniciar o loop principal
parent.mainloop()
