import customtkinter as ctk
from mysql.connector import connect
from Classes import ConnectionFactory

class AplicativoRanking:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Ranking")
        self.raiz.geometry(f"{960}x{680}")

        self.criar_widgets()
        self.carregar_dados()

    def criar_widgets(self):
        self.titulo_label = ctk.CTkLabel(self.raiz, text="Ranking dos Estudantes", font=("Helvetica", 24))
        self.titulo_label.pack(pady=20)

        self.quadro_ranking = ctk.CTkFrame(self.raiz, width=480, height=300)
        self.quadro_ranking.pack(pady=10)

        self.botao_recarregar = ctk.CTkButton(self.raiz, text="Recarregar", command=self.carregar_dados)
        self.botao_recarregar.pack(pady=10)

    def carregar_dados(self):
        for widget in self.quadro_ranking.winfo_children():
            widget.destroy()

        dados_ranking = self.buscar_dados_ranking()

        if dados_ranking:
            titulos = ["Rank", "Nome", "Acertos"]
            for col, cabecalho in enumerate(titulos):
                titulo_label = ctk.CTkLabel(self.quadro_ranking, text=cabecalho, font=("Helvetica", 14, "bold"))
                titulo_label.grid(row=0, column=col, padx=10, pady=5)

            for linha, (nome, acertos) in enumerate(dados_ranking, start=1):
                rank_label = ctk.CTkLabel(self.quadro_ranking, text=str(linha), font=("Helvetica", 14))
                rank_label.grid(row=linha, column=0, padx=10, pady=5)

                nome_label = ctk.CTkLabel(self.quadro_ranking, text=nome, font=("Helvetica", 14))
                nome_label.grid(row=linha, column=1, padx=10, pady=5)

                acertos_label = ctk.CTkLabel(self.quadro_ranking, text=str(acertos), font=("Helvetica", 14))
                acertos_label.grid(row=linha, column=2, padx=10, pady=5)
        else:
            sem_dados_label = ctk.CTkLabel(self.quadro_ranking, text="Sem dados", font=("Helvetica", 14))
            sem_dados_label.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

    def buscar_dados_ranking(self):
        conexao = ConnectionFactory.ConnectionFactory()
        conexao = conexao.obterConexao()
        cursor = conexao.cursor()

        consulta = "SELECT nome, acertos FROM aluno ORDER BY acertos DESC"
        cursor.execute(consulta)

        dados_ranking = []
        for (nome, acertos) in cursor:
            dados_ranking.append((nome, acertos))

        cursor.close()
        conexao.close()

        return dados_ranking

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    raiz = ctk.CTk()
    app = AplicativoRanking(raiz)
    raiz.mainloop()

