import customtkinter as ctk
from tkinter import messagebox
from PIL import ImageTk, Image
from Classes import DAO

# DAO 
dao = DAO.DAO()

def validar_login():
    nome = nome_entry.get()
    email = email_entry.get()

    existe = dao.existeAluno(nome, email)

    if existe:
        messagebox.showinfo("Sucesso", f"Seja bem vindo, {nome}")
        # Open new window upon successful login
        new_window()
    else:
        messagebox.showerror("Falha no login", "Nome ou email inválidos")

def new_window():
    # Janela de sucesso
    root_new = ctk.CTk()
    root_new.geometry(f"{960}x{680}")
    root_new.title("New Window")

    # Labels da janela
    frame_new = ctk.CTkFrame(master=root_new, width=450, height=450, corner_radius=10)
    frame_new.place(relx=0.5, rely=0.5, anchor="center")

    label_new = ctk.CTkLabel(master=frame_new, width=200, height=60, corner_radius=10,
                              fg_color=("gray70", "gray35"), text="You have successfully logged-in")
    label_new.place(relx=0.5, rely=0.3, anchor="center")

    root_new.mainloop()

# Configurações iniciais do customtkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

# Janela de login
root_login = ctk.CTk()
root_login.geometry(f"{960}x{680}")
root_login.title("LOGIN ALUNO")

# Carregar imagem de fundo
image = Image.open("img/FundoVeiavirus.png")
background_image = ImageTk.PhotoImage(image)

# Label de fundo
background_label = ctk.CTkLabel(root_login, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Caixa de texto e escritas em cima
frame = ctk.CTkFrame(master=root_login, width=450, height=450, corner_radius=10)
frame.place(relx=0.5, rely=0.5, anchor="center")

label_1 = ctk.CTkLabel(master=frame, width=400, height=60, corner_radius=10,
                       fg_color=("gray70", "gray35"), text="Faça seu login Aluno!")
label_1.place(relx=0.5, rely=0.3, anchor="center")

nome_entry = ctk.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Nome")
nome_entry.place(relx=0.5, rely=0.52, anchor="center")

email_entry = ctk.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Email")
email_entry.place(relx=0.5, rely=0.6, anchor="center")

button_login = ctk.CTkButton(master=frame, text="LOGIN", corner_radius=6, command=validar_login, width=400)
button_login.place(relx=0.5, rely=0.7, anchor="center")

root_login.mainloop()
