import customtkinter as ctk
from tkinter import messagebox
from PIL import ImageTk, Image
import pygame
from random import choice
from sys import exit
from Classes import DAO, Usuario, Pergunta, Resposta, ConnectionFactory

# Declaração variáveis globais
pergunta = Pergunta.Pergunta('font/PixelifySans-SemiBold.ttf', 20, (100, 100))
respostas = Resposta.Resposta('font/PixelifySans-Regular.ttf', 20, 100)

class App:
    def __init__(self):
        self.aluno = Usuario.Usuario()
        self.dao = DAO.DAO()
        self.init_login_screen()

    def init_login_screen(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

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

    def validar_login(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()

        existe = self.dao.existeAluno(nome, email)[0]

        if existe == 1:
            messagebox.showinfo("Sucesso", f"Seja bem vindo, {nome}")
            self.aluno.setNomeAluno(nome)
            self.aluno.setEmailAluno(email)
            global aluno
            aluno = self.aluno

            self.root_login.destroy()
            self.init_ranking_screen()
        else:
            messagebox.showerror("Falha no login", "Nome ou email inválidos")

    def init_ranking_screen(self):
        self.root_ranking = ctk.CTk()
        self.app_ranking = Ranking(self.root_ranking, self)
        self.root_ranking.mainloop()

    def init_game(self):
        self.root_ranking.destroy()
        self.game = Game()
        self.game.rodando()


class Ranking:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.root.title("Ranking")
        self.root.geometry(f"{960}x{680}")

        self.criar_widgets()
        self.carregar_dados()

    def criar_widgets(self):
        self.titulo_label = ctk.CTkLabel(self.root, text="Ranking dos Estudantes", font=("Helvetica", 24))
        self.titulo_label.pack(pady=20)

        self.quadro_ranking = ctk.CTkFrame(self.root, width=480, height=300)
        self.quadro_ranking.pack(pady=10)

        self.botao_recarregar = ctk.CTkButton(self.root, text="Recarregar", command=self.carregar_dados)
        self.botao_recarregar.pack(pady=10)

        self.botao_jogar = ctk.CTkButton(self.root, text="Jogar", command=self.app.init_game)
        self.botao_jogar.pack(pady=10)

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
        conexao = ConnectionFactory.ConnectionFactory().obterConexao()
        cursor = conexao.cursor()

        consulta = "SELECT nome, acertos FROM aluno ORDER BY acertos DESC"
        cursor.execute(consulta)

        dados_ranking = []
        for (nome, acertos) in cursor:
            dados_ranking.append((nome, acertos))

        cursor.close()
        conexao.close()

        return dados_ranking


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Vac-Man')

        self.larguraTela = 960
        self.alturaTela = 680
        self.tela = pygame.display.set_mode((self.larguraTela, self.alturaTela))
        self.relogio = pygame.time.Clock()

        # Definindo mudança das telas
        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.tela, self.gameStateManager)
        self.level1 = Level1(self.tela, self.gameStateManager)
        self.level2 = Level2(self.tela, self.gameStateManager)
        self.level3 = Level3(self.tela, self.gameStateManager)
        self.level4 = Level4(self.tela, self.gameStateManager)
        #self.level5 = Level5(self.tela, self.gameStateManager)

        self.states = {'start': self.start, 'level1': self.level1, 'level2': self.level2, 'level3' : self.level3, 'level4' : self.level4}

    def rodando(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if len(lista_de_colisao) != 0:
                        print(pygame.mouse.get_pos())
                        if pergunta.getMensagemAtiva() == True:
                            self.rectP1 = pygame.Rect(lista_de_colisao[0])
                            self.rectP2 = pygame.Rect(lista_de_colisao[1])
                            self.rectP3 = pygame.Rect(lista_de_colisao[2])

                        if self.rectP1.collidepoint(event.pos):
                            if not escolhaFeita:
                                pergunta.setMensagemAtiva(False)
                                self.escolha = 0
                                respostas.registrarEscolha(self.tela, self.escolha, id_pergunta, aluno.getNomeAluno(), aluno.getEmailAluno())
                                posicao_atual.pop(0)
                                idQuestoesRepetidas.append(id_pergunta)
                        elif self.rectP2.collidepoint(event.pos):
                            if not escolhaFeita:
                                pergunta.setMensagemAtiva(False)
                                self.escolha = 1
                                respostas.registrarEscolha(self.tela, self.escolha, id_pergunta, aluno.getNomeAluno(), aluno.getEmailAluno())
                                posicao_atual.pop(0)
                                idQuestoesRepetidas.append(id_pergunta)
                        elif self.rectP3.collidepoint(event.pos):
                            if not escolhaFeita:
                                pergunta.setMensagemAtiva(False)
                                self.escolha = 2
                                respostas.registrarEscolha(self.tela, self.escolha, id_pergunta, aluno.getNomeAluno(), aluno.getEmailAluno())
                                posicao_atual.pop(0)
                                idQuestoesRepetidas.append(id_pergunta)

            # Para mudança de telas
            controlador_telas = self.states[self.gameStateManager.get_state()]
            controlador_telas.rodando()

            # Para atualizar a tela
            pygame.display.update()
            self.relogio.tick(60)


class Level1:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        # Variáveis padrão
        self.larguraTela = 960
        self.alturaTela = 680
        self.x = 30
        self.y = 65
        self.tela = pygame.display.set_mode((self.larguraTela, self.alturaTela))

        # Variável da fonte
        self.fonte = pygame.font.SysFont("Arial", 20, True, False)
        self.plano_de_fundo = pygame.image.load('img/Fase1.png')

        # Definindo specs inimigo
        self.skin_inimigo = pygame.image.load('img/Virus01.png').convert_alpha()
        self.inimigo = self.skin_inimigo.get_rect()

        # Definindo os objetos:
        self.pergunta = pergunta
        self.respostas = respostas

        # Variáveis das perguntas
        self.dificuldade = "Fácil"
        self.pergunta.setDificuldade(self.dificuldade)
    

        # Definindo os inimigos:
        self.inimigo_atual = None
        self.posicoes_possiveis = [(390, 280), (100, 490), (730, 280), (560, 530)]

        global posicao_atual
        posicao_atual = []
        self.ultima_posicao = None

    def retangulos_inimigos(self, posicao):
        inimigo = self.skin_inimigo.get_rect()
        inimigo.topleft = (posicao)
        return inimigo

    def rodando(self):
        # Movimentação
        keys = pygame.key.get_pressed()
        lado_x = 40
        lado_y = 40
        cor_padrão = (255, 174, 201, 255)

        self.tela.fill((0, 0, 0))
        self.tela.blit(self.plano_de_fundo, (0, 0))

        # Definindo protagonista
        protagonista = pygame.draw.rect(self.tela, (255, 255, 50), (self.x, self.y, lado_x, lado_y))

        # Definindo mensagemAtiva
        self.mensagemAtiva = pergunta.getMensagemAtiva()

        # Definindo variáveis globais improvisadas
        global escolhaFeita
        escolhaFeita = False
        global idQuestoesRepetidas
        idQuestoesRepetidas = []


        # Definindo o retângulo para passar de fase:
        if respostas.getQtdAcertos() == 4:
            proxFase = pygame.draw.rect(self.tela, (255, 0, 0), (900, 565, 40, 40))
            if protagonista.colliderect(proxFase):
                self.gameStateManager.set_state('level2')
                pergunta.setDificuldade('Médio')
                respostas.setQtdAcertos(0)

        if not self.mensagemAtiva:
            if keys[pygame.K_a] and self.x > 5:
                self.x -= 5
                cor_cima = self.tela.get_at((self.x - 1, self.y))
                cor_baixo = self.tela.get_at((self.x - 1, self.y + 39))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.x == self.x
                elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.x += 5

            if keys[pygame.K_d] and self.x < 960 - lado_x - 5:
                self.x += 5
                cor_cima = self.tela.get_at((self.x + 39, self.y))
                cor_baixo = self.tela.get_at((self.x + 39, self.y + 39))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.x == self.x
                elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.x -= 5

            if keys[pygame.K_w] and self.y > 5:
                self.y -= 5
                cor_cima = self.tela.get_at((self.x, self.y - 1))
                cor_baixo = self.tela.get_at((self.x + 39, self.y - 1))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.y == self.y
                elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.y += 5

            if keys[pygame.K_s] and self.y < 720 - lado_y - 5:
                self.y += 5
                cor_cima = self.tela.get_at((self.x, self.y + 39))
                cor_baixo = self.tela.get_at((self.x + 39, self.y + 39))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.y == self.y
                if cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.y -= 5

        # Perguntas:
        # Definindo mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rectMouse = pygame.Rect(mouse_x - 5, mouse_y - 5, 10, 10)

        # Definindo posição do inimigo
        if len(posicao_atual) == 0:
            while True:
                posicao_escolhida = choice(self.posicoes_possiveis)
                if type(self.ultima_posicao) != tuple:
                    posicao_atual.append(posicao_escolhida)
                    self.ultima_posicao = posicao_escolhida
                    break
                else:
                    if self.ultima_posicao != posicao_escolhida:
                        posicao_atual.append(posicao_escolhida)
                        self.ultima_posicao = posicao_escolhida
                        break
        if respostas.getQtdAcertos != 4:
            inimigo = self.retangulos_inimigos(posicao_atual[0])
            i = inimigo

        if not self.mensagemAtiva and respostas.getQtdAcertos() != 4:
            self.tela.blit(self.skin_inimigo, i)
        if protagonista.colliderect((i)):
            self.inimigo_atual = i
            escolhaFeita = False

            if not self.mensagemAtiva:
                self.respostas.setListadeColisao([])
                self.pergunta.definirPergunta(idQuestoesRepetidas)
                idPergunta = self.pergunta.getIdPergunta()
                self.respostas.definirRespostas(idPergunta)
                pergunta.setMensagemAtiva(True)
            if self.mensagemAtiva:
                self.pergunta.exibirPergunta(self.tela, 860, 500, (255, 255, 255))
                altura = self.pergunta.getAlturaTotalPergunta()
                self.respostas.exibirRespostas(self.tela, altura)
                for rect in self.respostas.getListaDeColisao():
                    pygame.draw.rect(self.tela, (0, 0, 255), pygame.Rect(rect))
            
            if len(idQuestoesRepetidas) == pergunta.getQuantidadePerguntas()[0]:
                idQuestoesRepetidas = []
        print(pergunta.getDificuldade())
        # Fita adesiva para o código funcionar
        global lista_de_colisao
        lista_de_colisao = self.respostas.getListaDeColisao()
        global id_pergunta
        id_pergunta = self.pergunta.getIdPergunta()

class Level2:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        # Variáveis padrão
        self.larguraTela = 960
        self.alturaTela = 680
        self.x = 0
        self.y = 540
        self.tela = pygame.display.set_mode((self.larguraTela, self.alturaTela))

        # Variável da fonte
        self.fonte = pygame.font.SysFont("Arial", 20, True, False)
        self.plano_de_fundo = pygame.image.load('img/Fase2.png')

        # Definindo specs inimigo
        self.skin_inimigo = pygame.image.load('img/Virus02.png').convert_alpha()
        self.inimigo = self.skin_inimigo.get_rect()

        # Definindo os objetos:
        self.pergunta = pergunta
        self.respostas = respostas
     
        # Definindo os inimigos:
        self.inimigo_atual = None
        self.posicoes_possiveis = [(85, 240), (420, 240), (760, 240), (590, 535)]

        global posicao_atual
        posicao_atual = []
        self.ultima_posicao = None

    def retangulos_inimigos(self, posicao):
        inimigo = self.skin_inimigo.get_rect()
        inimigo.topleft = (posicao)
        return inimigo

    def rodando(self):
        # Movimentação
        keys = pygame.key.get_pressed()
        lado_x = 40
        lado_y = 40
        cor_padrão = (255, 174, 201, 255)

        self.tela.fill((0, 0, 0))
        self.tela.blit(self.plano_de_fundo, (0, 0))

        # Definindo protagonista
        protagonista = pygame.draw.rect(self.tela, (255, 255, 50), (self.x, self.y, lado_x, lado_y))

        # Definindo mensagemAtiva
        self.mensagemAtiva = pergunta.getMensagemAtiva()

        # Definindo variáveis globais improvisadas
        global escolhaFeita
        escolhaFeita = False
        global idQuestoesRepetidas
        idQuestoesRepetidas = []


        # Definindo o retângulo para passar de fase:
        if respostas.getQtdAcertos() == 4:
            proxFase = pygame.draw.rect(self.tela, (255, 0, 0), (910, 232, 40, 40))
            if protagonista.colliderect(proxFase):
                self.gameStateManager.set_state('level3')
                respostas.setQtdAcertos(0)                

        if not self.mensagemAtiva:
            if keys[pygame.K_a] and self.x > 5:
                self.x -= 5
                cor_cima = self.tela.get_at((self.x - 1, self.y))
                cor_baixo = self.tela.get_at((self.x - 1, self.y + 39))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.x == self.x
                elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.x += 5

            if keys[pygame.K_d] and self.x < 960 - lado_x - 5:
                self.x += 5
                cor_cima = self.tela.get_at((self.x + 39, self.y))
                cor_baixo = self.tela.get_at((self.x + 39, self.y + 39))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.x == self.x
                elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.x -= 5

            if keys[pygame.K_w] and self.y > 5:
                self.y -= 5
                cor_cima = self.tela.get_at((self.x, self.y - 1))
                cor_baixo = self.tela.get_at((self.x + 39, self.y - 1))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.y == self.y
                elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.y += 5

            if keys[pygame.K_s] and self.y < 720 - lado_y - 5:
                self.y += 5
                cor_cima = self.tela.get_at((self.x, self.y + 39))
                cor_baixo = self.tela.get_at((self.x + 39, self.y + 39))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.y == self.y
                if cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.y -= 5

        # Perguntas:
        # Definindo mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rectMouse = pygame.Rect(mouse_x - 5, mouse_y - 5, 10, 10)

        # Definindo posição do inimigo
        if len(posicao_atual) == 0:
            while True:
                posicao_escolhida = choice(self.posicoes_possiveis)
                if type(self.ultima_posicao) != tuple:
                    posicao_atual.append(posicao_escolhida)
                    self.ultima_posicao = posicao_escolhida
                    break
                else:
                    if self.ultima_posicao != posicao_escolhida:
                        posicao_atual.append(posicao_escolhida)
                        self.ultima_posicao = posicao_escolhida
                        break
        if respostas.getQtdAcertos != 4:
            inimigo = self.retangulos_inimigos(posicao_atual[0])
            i = inimigo

        if not self.mensagemAtiva and respostas.getQtdAcertos() != 4:
            self.tela.blit(self.skin_inimigo, i)
        if protagonista.colliderect((i)):
            self.inimigo_atual = i
            escolhaFeita = False

            if not self.mensagemAtiva:
                self.respostas.setListadeColisao([])
                self.pergunta.definirPergunta(idQuestoesRepetidas)
                idPergunta = self.pergunta.getIdPergunta()
                self.respostas.definirRespostas(idPergunta)
                pergunta.setMensagemAtiva(True)
            if self.mensagemAtiva:
                self.pergunta.exibirPergunta(self.tela, 860, 500, (255, 255, 255))
                altura = self.pergunta.getAlturaTotalPergunta()
                self.respostas.exibirRespostas(self.tela, altura)
                for rect in self.respostas.getListaDeColisao():
                    pygame.draw.rect(self.tela, (0, 0, 255), pygame.Rect(rect))
            
            if len(idQuestoesRepetidas) == pergunta.getQuantidadePerguntas()[0]:
                idQuestoesRepetidas = []

        # Fita adesiva para o código funcionar
        global lista_de_colisao
        lista_de_colisao = self.respostas.getListaDeColisao()
        global id_pergunta
        id_pergunta = self.pergunta.getIdPergunta()

class Level3:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        # Variáveis padrão
        self.larguraTela = 960
        self.alturaTela = 680
        self.x = 0
        self.y = 250
        self.tela = pygame.display.set_mode((self.larguraTela, self.alturaTela))

        # Variável da fonte
        self.fonte = pygame.font.SysFont("Arial", 20, True, False)
        self.plano_de_fundo = pygame.image.load('img/Fase3.png')

        # Definindo specs inimigo
        self.skin_inimigo = pygame.image.load('img/Virus03.png').convert_alpha()
        self.inimigo = self.skin_inimigo.get_rect()

        # Definindo os objetos:
        self.pergunta = pergunta
        self.respostas = respostas
     
        # Definindo os inimigos:
        self.inimigo_atual = None
        self.posicoes_possiveis = [(520, 165), (285, 450), (655, 450), (770, 300)]

        global posicao_atual
        posicao_atual = []
        self.ultima_posicao = None

    def retangulos_inimigos(self, posicao):
        inimigo = self.skin_inimigo.get_rect()
        inimigo.topleft = (posicao)
        return inimigo

    def rodando(self):
        # Movimentação
        keys = pygame.key.get_pressed()
        lado_x = 40
        lado_y = 40
        cor_padrão = (255, 174, 201, 255)

        self.tela.fill((0, 0, 0))
        self.tela.blit(self.plano_de_fundo, (0, 0))

        # Definindo protagonista
        protagonista = pygame.draw.rect(self.tela, (255, 255, 50), (self.x, self.y, lado_x, lado_y))

        # Definindo mensagemAtiva
        self.mensagemAtiva = pergunta.getMensagemAtiva()

        # Definindo variáveis globais improvisadas
        global escolhaFeita
        escolhaFeita = False
        global idQuestoesRepetidas
        idQuestoesRepetidas = []


        # Definindo o retângulo para passar de fase:
        if respostas.getQtdAcertos() == 4:
            proxFase = pygame.draw.rect(self.tela, (255, 0, 0), (920, 320, 40, 40))
            if protagonista.colliderect(proxFase):
                self.gameStateManager.set_state('level4')
                pergunta.setDificuldade('Difícil')
                respostas.setQtdAcertos(0)                

        if not self.mensagemAtiva:
            if keys[pygame.K_a] and self.x > 5:
                self.x -= 5
                cor_cima = self.tela.get_at((self.x - 1, self.y))
                cor_baixo = self.tela.get_at((self.x - 1, self.y + 39))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.x == self.x
                elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.x += 5

            if keys[pygame.K_d] and self.x < 960 - lado_x - 5:
                self.x += 5
                cor_cima = self.tela.get_at((self.x + 39, self.y))
                cor_baixo = self.tela.get_at((self.x + 39, self.y + 39))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.x == self.x
                elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.x -= 5

            if keys[pygame.K_w] and self.y > 5:
                self.y -= 5
                cor_cima = self.tela.get_at((self.x, self.y - 1))
                cor_baixo = self.tela.get_at((self.x + 39, self.y - 1))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.y == self.y
                elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.y += 5

            if keys[pygame.K_s] and self.y < 720 - lado_y - 5:
                self.y += 5
                cor_cima = self.tela.get_at((self.x, self.y + 39))
                cor_baixo = self.tela.get_at((self.x + 39, self.y + 39))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.y == self.y
                if cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.y -= 5

        # Perguntas:
        # Definindo mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rectMouse = pygame.Rect(mouse_x - 5, mouse_y - 5, 10, 10)

        # Definindo posição do inimigo
        if len(posicao_atual) == 0:
            while True:
                posicao_escolhida = choice(self.posicoes_possiveis)
                if type(self.ultima_posicao) != tuple:
                    posicao_atual.append(posicao_escolhida)
                    self.ultima_posicao = posicao_escolhida
                    break
                else:
                    if self.ultima_posicao != posicao_escolhida:
                        posicao_atual.append(posicao_escolhida)
                        self.ultima_posicao = posicao_escolhida
                        break
        if respostas.getQtdAcertos != 4:
            inimigo = self.retangulos_inimigos(posicao_atual[0])
            i = inimigo

        if not self.mensagemAtiva and respostas.getQtdAcertos() != 4:
            self.tela.blit(self.skin_inimigo, i)
        if protagonista.colliderect((i)):
            self.inimigo_atual = i
            escolhaFeita = False

            if not self.mensagemAtiva:
                self.respostas.setListadeColisao([])
                self.pergunta.definirPergunta(idQuestoesRepetidas)
                idPergunta = self.pergunta.getIdPergunta()
                self.respostas.definirRespostas(idPergunta)
                pergunta.setMensagemAtiva(True)
            if self.mensagemAtiva:
                self.pergunta.exibirPergunta(self.tela, 860, 500, (255, 255, 255))
                altura = self.pergunta.getAlturaTotalPergunta()
                self.respostas.exibirRespostas(self.tela, altura)
                for rect in self.respostas.getListaDeColisao():
                    pygame.draw.rect(self.tela, (0, 0, 255), pygame.Rect(rect))
            
            if len(idQuestoesRepetidas) == pergunta.getQuantidadePerguntas()[0]:
                idQuestoesRepetidas = []

        # Fita adesiva para o código funcionar
        global lista_de_colisao
        lista_de_colisao = self.respostas.getListaDeColisao()
        global id_pergunta
        id_pergunta = self.pergunta.getIdPergunta()

class Level4:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        # Variáveis padrão
        self.larguraTela = 960
        self.alturaTela = 680
        self.x = 0
        self.y = 320
        self.tela = pygame.display.set_mode((self.larguraTela, self.alturaTela))

        # Variável da fonte
        self.fonte = pygame.font.SysFont("Arial", 20, True, False)
        self.plano_de_fundo = pygame.image.load('img/Fase4.png')

        # Definindo specs inimigo
        self.skin_inimigo = pygame.image.load('img/Virus04.png').convert_alpha()
        self.inimigo = self.skin_inimigo.get_rect()

        # Definindo os objetos:
        self.pergunta = pergunta
        self.respostas = respostas
     
        # Definindo os inimigos:
        self.inimigo_atual = None
        self.posicoes_possiveis = [(210, 315), (450, 475), (685, 255), (685, 450)]

        global posicao_atual
        posicao_atual = []
        self.ultima_posicao = None

    def retangulos_inimigos(self, posicao):
        inimigo = self.skin_inimigo.get_rect()
        inimigo.topleft = (posicao)
        return inimigo

    def rodando(self):
        # Movimentação
        keys = pygame.key.get_pressed()
        lado_x = 40
        lado_y = 40
        cor_padrão = (255, 174, 201, 255)

        self.tela.fill((0, 0, 0))
        self.tela.blit(self.plano_de_fundo, (0, 0))

        # Definindo protagonista
        protagonista = pygame.draw.rect(self.tela, (255, 255, 50), (self.x, self.y, lado_x, lado_y))

        # Definindo mensagemAtiva
        self.mensagemAtiva = pergunta.getMensagemAtiva()

        # Definindo variáveis globais improvisadas
        global escolhaFeita
        escolhaFeita = False
        global idQuestoesRepetidas
        idQuestoesRepetidas = []


        # Definindo o retângulo para passar de fase:
        if respostas.getQtdAcertos() == 4:
            proxFase = pygame.draw.rect(self.tela, (255, 0, 0), (920, 600, 40, 40))
            if protagonista.colliderect(proxFase):
                self.gameStateManager.set_state('level5')
                respostas.setQtdAcertos(0)
                exit()

        if not self.mensagemAtiva:
            if keys[pygame.K_a] and self.x > 5:
                self.x -= 5
                cor_cima = self.tela.get_at((self.x - 1, self.y))
                cor_baixo = self.tela.get_at((self.x - 1, self.y + 39))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.x == self.x
                elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.x += 5

            if keys[pygame.K_d] and self.x < 960 - lado_x - 5:
                self.x += 5
                cor_cima = self.tela.get_at((self.x + 39, self.y))
                cor_baixo = self.tela.get_at((self.x + 39, self.y + 39))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.x == self.x
                elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.x -= 5

            if keys[pygame.K_w] and self.y > 5:
                self.y -= 5
                cor_cima = self.tela.get_at((self.x, self.y - 1))
                cor_baixo = self.tela.get_at((self.x + 39, self.y - 1))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.y == self.y
                elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.y += 5

            if keys[pygame.K_s] and self.y < 720 - lado_y - 5:
                self.y += 5
                cor_cima = self.tela.get_at((self.x, self.y + 39))
                cor_baixo = self.tela.get_at((self.x + 39, self.y + 39))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.y == self.y
                if cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.y -= 5

        # Perguntas:
        # Definindo mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rectMouse = pygame.Rect(mouse_x - 5, mouse_y - 5, 10, 10)

        # Definindo posição do inimigo
        if len(posicao_atual) == 0:
            while True:
                posicao_escolhida = choice(self.posicoes_possiveis)
                if type(self.ultima_posicao) != tuple:
                    posicao_atual.append(posicao_escolhida)
                    self.ultima_posicao = posicao_escolhida
                    break
                else:
                    if self.ultima_posicao != posicao_escolhida:
                        posicao_atual.append(posicao_escolhida)
                        self.ultima_posicao = posicao_escolhida
                        break
        if respostas.getQtdAcertos != 4:
            inimigo = self.retangulos_inimigos(posicao_atual[0])
            i = inimigo

        if not self.mensagemAtiva and respostas.getQtdAcertos() != 4:
            self.tela.blit(self.skin_inimigo, i)
        if protagonista.colliderect((i)):
            self.inimigo_atual = i
            escolhaFeita = False

            if not self.mensagemAtiva:
                self.respostas.setListadeColisao([])
                self.pergunta.definirPergunta(idQuestoesRepetidas)
                idPergunta = self.pergunta.getIdPergunta()
                self.respostas.definirRespostas(idPergunta)
                pergunta.setMensagemAtiva(True)
            if self.mensagemAtiva:
                self.pergunta.exibirPergunta(self.tela, 860, 500, (255, 255, 255))
                altura = self.pergunta.getAlturaTotalPergunta()
                self.respostas.exibirRespostas(self.tela, altura)
                for rect in self.respostas.getListaDeColisao():
                    pygame.draw.rect(self.tela, (0, 0, 255), pygame.Rect(rect))
            
            if len(idQuestoesRepetidas) == pergunta.getQuantidadePerguntas()[0]:
                idQuestoesRepetidas = []

        # Fita adesiva para o código funcionar
        global lista_de_colisao
        lista_de_colisao = self.respostas.getListaDeColisao()
        global id_pergunta
        id_pergunta = self.pergunta.getIdPergunta()        

class Start:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def rodando(self):
        self.display.fill('red')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.gameStateManager.set_state('level4')


class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState

    def get_state(self):
        return self.currentState

    def set_state(self, state):
        self.currentState = state


if __name__ == '__main__':
    app = App()
