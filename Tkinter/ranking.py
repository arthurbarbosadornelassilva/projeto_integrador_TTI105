import customtkinter as ctk
from mysql.connector import connect
from Classes import ConnectionFactory

class RankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ranking")
        self.root.geometry(f"{960}x{680}")

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(self.root, text="Ranking dos Estudantes", font=("Helvetica", 24))
        self.title_label.pack(pady=20)

        self.ranking_frame = ctk.CTkFrame(self.root, width=480, height=300)
        self.ranking_frame.pack(pady=10)

        self.refresh_button = ctk.CTkButton(self.root, text="Recarregar", command=self.load_data)
        self.refresh_button.pack(pady=10)

    def load_data(self):
        for widget in self.ranking_frame.winfo_children():
            widget.destroy()
        
        ranking_data = self.fetch_ranking_data()
        
        if ranking_data:
            titulos = ["Rank", "Nome", "Acertos"]
            for col, header in enumerate(titulos):
                titulos_label = ctk.CTkLabel(self.ranking_frame, text=header, font=("Helvetica", 14, "bold"))
                titulos_label.grid(row=0, column=col, padx=10, pady=5)

            for row, (name, correct_answers) in enumerate(ranking_data, start=1):
                rank_label = ctk.CTkLabel(self.ranking_frame, text=str(row), font=("Helvetica", 14))
                rank_label.grid(row=row, column=0, padx=10, pady=5)

                name_label = ctk.CTkLabel(self.ranking_frame, text=name, font=("Helvetica", 14))
                name_label.grid(row=row, column=1, padx=10, pady=5)

                correct_answers_label = ctk.CTkLabel(self.ranking_frame, text=str(correct_answers), font=("Helvetica", 14))
                correct_answers_label.grid(row=row, column=2, padx=10, pady=5)
        else:
            no_data_label = ctk.CTkLabel(self.ranking_frame, text="Sem data", font=("Helvetica", 14))
            no_data_label.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

    def fetch_ranking_data(self):
        connection = ConnectionFactory.ConnectionFactory()
        conexao = connection.obterConexao()
        cursor = conexao.cursor()

        query = ("SELECT nome, acertos FROM aluno ORDER BY acertos DESC")
        cursor.execute(query)

        ranking_data = []
        for (name, correct_answers) in cursor:
            ranking_data.append((name, correct_answers))

        cursor.close()
        conexao.close()

        return ranking_data

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    app = RankingApp(root)
    root.mainloop()
