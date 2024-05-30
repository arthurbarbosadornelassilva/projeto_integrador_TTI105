
import customtkinter as ctk
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conectar ao banco de dados e criar a tabela se não existir
def connect_db():
    conn = sqlite3.connect('perguntas.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS perguntas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        dificuldade TEXT,
                        questao TEXT,
                        resposta1 TEXT,
                        resposta2 TEXT,
                        resposta3 TEXT,
                        resposta4 TEXT,
                        resposta5 TEXT,
                        resposta_correta TEXT)''')
    conn.commit()
    conn.close()

# Função para adicionar pergunta ao banco de dados
def add_question():
    conn = sqlite3.connect('perguntas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO perguntas (dificuldade, questao, resposta1, resposta2, resposta3, resposta4, resposta5, resposta_correta) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (variable1.get(), questao_entry.get("1.0", END).strip(), response_widgets[0][1].get(), response_widgets[1][1].get(), response_widgets[2][1].get(),
                    response_widgets[3][1].get(), response_widgets[4][1].get(), correct_response_var.get()))
    conn.commit()
    conn.close()
    fetch_questions()
    clear_fields()
    # print(f'Resposta correta: {correct_response_var.get()}')  # Print da resposta correta

# Função para buscar todas as perguntas do banco de dados
def fetch_questions():
    conn = sqlite3.connect('perguntas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM perguntas")
    rows = cursor.fetchall()
    conn.close()
    update_treeview(rows)

# Função para atualizar o treeview
def update_treeview(rows):
    for row in tree.get_children():
        tree.delete(row)
    for row in rows:
        tree.insert("", "end", values=row)

# Função para deletar pergunta
def delete_question():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        question_id = item['values'][0]
        conn = sqlite3.connect('perguntas.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM perguntas WHERE id = ?", (question_id,))
        conn.commit()
        conn.close()
        fetch_questions()

# Função para atualizar pergunta
def update_question():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        question_id = item['values'][0]
        conn = sqlite3.connect('perguntas.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE perguntas SET dificuldade = ?, questao = ?, resposta1 = ?, resposta2 = ?, resposta3 = ?, resposta4 = ?, resposta5 = ?, resposta_correta = ? WHERE id = ?",
                       (variable1.get(), questao_entry.get("1.0", END).strip(), response_widgets[0][1].get(), response_widgets[1][1].get(), response_widgets[2][1].get(),
                        response_widgets[3][1].get(), response_widgets[4][1].get(), correct_response_var.get(), question_id))
        conn.commit()
        conn.close()
        fetch_questions()
        print(f'Resposta correta atualizada: {correct_response_var.get()}')  # Print da resposta correta

# Função para preencher campos ao selecionar uma pergunta
def fill_fields(event):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        question = item['values']
        variable1.set(question[1])
        questao_entry.delete("1.0", END)
        questao_entry.insert(END, question[2])
        for i in range(5):
            response_widgets[i][1].delete(0, END)
        response_widgets[0][1].insert(0, question[3])
        response_widgets[1][1].insert(0, question[4])
        response_widgets[2][1].insert(0, question[5])
        response_widgets[3][1].insert(0, question[6])
        response_widgets[4][1].insert(0, question[7])
        correct_response_var.set(question[8])
        update_response_combobox()

# Função para limpar campos
def clear_fields():
    questao_entry.delete("1.0", END)
    for i in range(5):
        response_widgets[i][1].delete(0, END)
    correct_response_var.set('')

# Atualizar campos de resposta conforme a dificuldade
def update_response_fields(*args):
    difficulty = variable1.get()
    if difficulty == 'Difícil':
        for i in range(5):
            response_widgets[i][0].place(x=20, y=220 + 60 * i)
            response_widgets[i][1].place(x=60, y=220 + 60 * i)
    else:
        for i in range(3):
            response_widgets[i][0].place(x=20, y=220 + 60 * i)
            response_widgets[i][1].place(x=60, y=220 + 60 * i)
        for i in range(3, 5):
            response_widgets[i][0].place_forget()
            response_widgets[i][1].place_forget()
    update_response_combobox()

def update_response_combobox(*args):
    difficulty = variable1.get()
    if difficulty == 'Difícil':
        values = [response_widgets[i][1].get() for i in range(5)]
    else:
        values = [response_widgets[i][1].get() for i in range(3)]
    correct_response_combo['values'] = values
    correct_response_var.set('')


tela = ctk.CTk()
tela.title("Perguntas Management System")
tela.geometry("960x680")
tela.config(bg='#161c25')
tela.resizable(False, False)

font1 = ('Arial', 15, 'bold')
font2 = ('Arial', 10, 'bold')

dificuldade_label = ctk.CTkLabel(tela, font=font1, text='Dificuldade: ', text_color='#fff', bg_color="#161C25")
dificuldade_label.place(x=20, y=40)
options = ['Fácil', 'Médio', 'Difícil']
variable1 = StringVar()
dificuldade_options = ctk.CTkComboBox(tela, font=font1, text_color='#000', fg_color='#fff', width=90, variable=variable1, values=options, state='readonly')
dificuldade_options.set('Fácil')
dificuldade_options.place(x=110, y=40)
variable1.trace("w", update_response_fields)

questao_label = ctk.CTkLabel(tela, font=font1, text='Questão: ', text_color='#fff', bg_color="#161C25")
questao_label.place(x=20, y=90)
questao_entry = ctk.CTkTextbox(tela, font=font1, text_color='#000', fg_color="#fff", border_width=2, width=320, height=70)
questao_entry.place(x=20, y=120)

response_widgets = []
for i in range(5):
    resposta_label = ctk.CTkLabel(tela, font=font1, text=f'R{i+1}:', text_color='#000', bg_color="#161C25")
    resposta_textbox = ctk.CTkEntry(tela, font=font1, text_color='#000', fg_color='#fff', width=280)
    resposta_textbox.bind("<KeyRelease>", update_response_combobox)  # Update combobox values on key release
    response_widgets.append((resposta_label, resposta_textbox))


correct_response_var = StringVar()
correct_response_label = ctk.CTkLabel(tela, font=font1, text='Selecione a resposta correta:', text_color='#fff', bg_color="#161C25")
correct_response_label.place(x=20, y=530)
correct_response_combo = ttk.Combobox(tela, font=font1, textvariable=correct_response_var, state='readonly', width=5)
correct_response_combo.place(x=250, y=530)

add_button = ctk.CTkButton(tela, font=font1, text_color="#fff", text="Adicionar", fg_color="#05A312", hover_color="#00850B", bg_color="#161C25", border_color="#F15704", cursor="hand2", corner_radius=15, width=100, command=add_question)
add_button.place(x=20, y=600)

update_button = ctk.CTkButton(tela, font=font1, text_color="#fff", text="Atualizar", fg_color="#FF5002", hover_color="#FF5002", bg_color="#161C25", border_color="#F15704", border_width=2, cursor="hand2", corner_radius=15, width=100, command=update_question)
update_button.place(x=130, y=600)

delete_button = ctk.CTkButton(tela, font=font1, text_color="#fff", text="Deletar", fg_color="#E40404", hover_color="#AE0000", bg_color="#161C25", border_color="#E40404", border_width=2, cursor="hand2", corner_radius=15, width=100, command=delete_question)
delete_button.place(x=235, y=600)

style = ttk.Style(tela)
style.theme_use("clam")
style.configure("Treeview", font=font2, foreground="#fff", background="#000", fieldbackground="#313837")
style.map("Treeview", background=[("selected", "#1A8F2D")])

tree = ttk.Treeview(tela, height=30)
tree["columns"] = ("id", "dificuldade", "questao")
tree.column('#0', width=0, stretch=tk.NO)
tree.column("id", anchor=tk.CENTER, width=60)
tree.column("dificuldade", anchor=tk.CENTER, width=100)
tree.column("questao", anchor=tk.CENTER, width=420)
tree.heading("id", text='ID')
tree.heading("dificuldade", text='Dificuldade')
tree.heading("questao", text='Questão')
tree.place(x=360, y=20)
tree.bind("<ButtonRelease-1>", fill_fields)


connect_db()
fetch_questions()
update_response_fields()  # Initial call to display the default number of response fields
tela.mainloop()

