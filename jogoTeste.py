import customtkinter as ctk
from tkinter import messagebox, END, StringVar
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import pygame
from random import choice
from sys import exit
from Classes import DAO, Usuario, Pergunta, Resposta, ConnectionFactory
import time

# Declaração variáveis globais
pergunta = Pergunta.Pergunta('font/PixelifySans-SemiBold.ttf', 20, (100, 100))
respostas = Resposta.Resposta('font/PixelifySans-Regular.ttf', 20, 100)

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
        self.vida = 8

        # Definindo mudança das telas
        self.gameStateManager = GameStateManager('tela_inicial')
        self.tela_inicial = TelaInicial(self.tela, self.gameStateManager)
        
        # Telas de cadastro e login
        self.tela_cadrasto = TelaCadastro(self.tela, self.gameStateManager)
        self.cadastro_aluno = CadastroAluno(self.gameStateManager)
        self.cadastro_professor = CadastroProfessor(self.gameStateManager)
        self.tela_login = TelaLogin(self.tela, self.gameStateManager)
        self.login_aluno = LoginAluno(self.gameStateManager)
        self.login_professor = LoginProfessor(self.gameStateManager)
        self.tela_professor = TelaProfessor(self.tela, self.gameStateManager)

        # Telas de jogo
        self.start = Start(self.tela, self.gameStateManager)
        self.level1 = Level1(self.tela, self.gameStateManager)
        self.level2 = Level2(self.tela, self.gameStateManager)
        self.level3 = Level3(self.tela, self.gameStateManager)
        self.level4 = Level4(self.tela, self.gameStateManager)
        self.level5 = Level5(self.tela, self.gameStateManager)
        self.final = Final(self.tela, self.gameStateManager)
        self.game_over = GameOver(self.tela, self.gameStateManager)

        self.states = {'tela_inicial' : self.tela_inicial, 'start': self.start, 'level1': self.level1, 'level2': self.level2, 'level3' : self.level3, 'level4' : self.level4, 
                       'level5' : self.level5, 'final' : self.final, 'cadastro' : self.tela_cadrasto, 'cadastro_aluno' : self.cadastro_aluno, 'cadastro_professor' : self.cadastro_professor, 
                       'login' : self.tela_login, 'login_aluno' : self.login_aluno, 'login_prof' : self.login_professor, 'tela_professor' : self.tela_professor, 'game_over' : self.game_over}

    def rodando(self):
        lista_de_niveis = ['level1', 'level2', 'level3', 'level4', 'level5', 'final']
        global vida
        vida = self.vida
        global escolhaFeita
        escolhaFeita = False
        global fase_final
        fase_final = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(escolhaFeita)
                    if pergunta.getMensagemAtiva() == True and not fase_final:
                        self.rectP1 = pygame.Rect(lista_de_colisao[0])
                        self.rectP2 = pygame.Rect(lista_de_colisao[1])
                        self.rectP3 = pygame.Rect(lista_de_colisao[2])

                        if self.rectP1.collidepoint(event.pos):
                            if not escolhaFeita:
                                escolhaFeita = True
                                pergunta.setMensagemAtiva(False)
                                self.escolha = 0
                                vida += respostas.registrarEscolha(self.tela, self.escolha, id_pergunta, aluno.getNomeAluno(), aluno.getEmailAluno())
                                posicao_atual.pop(0)
                                idQuestoesRepetidas.append(id_pergunta)
                        elif self.rectP2.collidepoint(event.pos):
                            if not escolhaFeita:
                                escolhaFeita = True
                                pergunta.setMensagemAtiva(False)
                                self.escolha = 1
                                vida += respostas.registrarEscolha(self.tela, self.escolha, id_pergunta, aluno.getNomeAluno(), aluno.getEmailAluno())
                                posicao_atual.pop(0)
                                idQuestoesRepetidas.append(id_pergunta)
                        elif self.rectP3.collidepoint(event.pos):
                            if not escolhaFeita:
                                escolhaFeita = True
                                pergunta.setMensagemAtiva(False)
                                self.escolha = 2
                                respostas.registrarEscolha(self.tela, self.escolha, id_pergunta, aluno.getNomeAluno(), aluno.getEmailAluno())
                                vida += respostas.registrarEscolha(self.tela, self.escolha, id_pergunta, aluno.getNomeAluno(), aluno.getEmailAluno())
                                posicao_atual.pop(0)
                                idQuestoesRepetidas.append(id_pergunta)
                        
                    elif pergunta.getMensagemAtiva() == True and fase_final:
                        self.rectP1 = pygame.Rect(lista_de_colisao[0])
                        self.rectP2 = pygame.Rect(lista_de_colisao[1])
                        self.rectP3 = pygame.Rect(lista_de_colisao[2])
                        self.rectP4 = pygame.Rect(lista_de_colisao[3])
                        self.rectP5 = pygame.Rect(lista_de_colisao[4])

                        if self.rectP1.collidepoint(event.pos):
                            if not escolhaFeita:
                                escolhaFeita = True
                                pergunta.setMensagemAtiva(False)
                                self.escolha = 0
                                vida += respostas.registrarEscolha(self.tela, self.escolha, id_pergunta, aluno.getNomeAluno(), aluno.getEmailAluno())
                                posicao_atual.pop(0)
                                idQuestoesRepetidas.append(id_pergunta)
                        elif self.rectP2.collidepoint(event.pos):
                            if not escolhaFeita:
                                escolhaFeita = True
                                pergunta.setMensagemAtiva(False)
                                self.escolha = 1
                                vida += respostas.registrarEscolha(self.tela, self.escolha, id_pergunta, aluno.getNomeAluno(), aluno.getEmailAluno())
                                posicao_atual.pop(0)
                                idQuestoesRepetidas.append(id_pergunta)
                        elif self.rectP3.collidepoint(event.pos):
                            if not escolhaFeita:
                                escolhaFeita = True
                                pergunta.setMensagemAtiva(False)
                                self.escolha = 2
                                respostas.registrarEscolha(self.tela, self.escolha, id_pergunta, aluno.getNomeAluno(), aluno.getEmailAluno())
                                vida += respostas.registrarEscolha(self.tela, self.escolha, id_pergunta, aluno.getNomeAluno(), aluno.getEmailAluno())
                                posicao_atual.pop(0)
                                idQuestoesRepetidas.append(id_pergunta)
                        elif self.rectP4.collidepoint(event.pos):
                            if not escolhaFeita:
                                escolhaFeita = True
                                pergunta.setMensagemAtiva(False)
                                self.escolha = 3
                                respostas.registrarEscolha(self.tela, self.escolha, id_pergunta, aluno.getNomeAluno(), aluno.getEmailAluno())
                                vida += respostas.registrarEscolha(self.tela, self.escolha, id_pergunta, aluno.getNomeAluno(), aluno.getEmailAluno())
                                posicao_atual.pop(0)
                                idQuestoesRepetidas.append(id_pergunta)
                        elif self.rectP5.collidepoint(event.pos):
                            if not escolhaFeita:
                                escolhaFeita = True
                                pergunta.setMensagemAtiva(False)
                                self.escolha = 4
                                respostas.registrarEscolha(self.tela, self.escolha, id_pergunta, aluno.getNomeAluno(), aluno.getEmailAluno())
                                vida += respostas.registrarEscolha(self.tela, self.escolha, id_pergunta, aluno.getNomeAluno(), aluno.getEmailAluno())
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
        self.fonte = pygame.font.Font('font/PixelifySans-Bold.ttf', 25)

        # Variável da fonte
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

        # Variável coração
        self.skin_coracao =pygame.image.load('img/Coracao_2.png')
        # Variável personagem
        self.skin_personagem = pygame.image.load('img/linf_b.png')

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
        self.tela.blit(self.skin_personagem, (self.x, self.y))

        # Definindo protagonista
        #protagonista = self.skin_personagem.get_rect()

        # Definindo mensagemAtiva
        self.mensagemAtiva = pergunta.getMensagemAtiva()

        # Definindo variáveis globais improvisadas
        global escolhaFeita
        escolhaFeita = False
        global idQuestoesRepetidas
        idQuestoesRepetidas = []

        # Definindo o retângulo para passar de fase:
        if respostas.getQtdAcertos() >= 4:
            proxFase = pygame.draw.rect(self.tela, (255, 0, 0), (900, 565, 40, 40))
            if protagonista.colliderect(proxFase):
                self.gameStateManager.set_state('level2')
                pergunta.setDificuldade('Médio')
                respostas.setQtdAcertos(0)

        # Definindo game over
        if vida == 0:
                self.gameStateManager.set_state('game_over')
                self.x, self.y = 30, 65
        
        # Definindo coração
        pygame.draw.rect(self.display, (255, 255, 255), (10, 12, 120, 30))
        texto_vida = self.fonte.render(str(vida), True, (0, 0, 0))
        self.display.blit(self.skin_coracao, (0, -4))
        self.display.blit(texto_vida, (65, 10))


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
        if respostas.getQtdAcertos() < 4:
            inimigo = self.retangulos_inimigos(posicao_atual[0])
            i = inimigo

            if not self.mensagemAtiva:
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
        self.fonte = pygame.font.Font('font/PixelifySans-Bold.ttf', 25)

        # Variável da fonte
        self.plano_de_fundo = pygame.image.load('img/Fase2.png')

        # Definindo specs inimigo
        self.skin_inimigo = pygame.image.load('img/Virus02.png').convert_alpha()
        self.inimigo = self.skin_inimigo.get_rect()

        # Definindo os objetos:
        self.pergunta = pergunta
        self.respostas = respostas

        # Variável coração
        self.skin_coracao =pygame.image.load('img/Coracao_2.png')

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

        # Definindo coração
        pygame.draw.rect(self.display, (255, 255, 255), (10, 12, 120, 30))
        texto_vida = self.fonte.render(str(vida), True, (0, 0, 0))
        self.display.blit(self.skin_coracao, (0, -4))
        self.display.blit(texto_vida, (65, 10))

        # Definindo o retângulo para passar de fase:
        if respostas.getQtdAcertos() >= 4:
            proxFase = pygame.draw.rect(self.tela, (255, 0, 0), (910, 232, 40, 40))
            if protagonista.colliderect(proxFase):
                posicao_atual.pop()
                self.gameStateManager.set_state('level3')
                respostas.setQtdAcertos(0)

        # Definindo game over
        if vida == 0:
                self.gameStateManager.set_state('game_over')
                self.x, self.y = 0, 540
        
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
        if respostas.getQtdAcertos() < 4:
            inimigo = self.retangulos_inimigos(posicao_atual[0])
            i = inimigo

            if not self.mensagemAtiva:
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
        self.fonte = pygame.font.Font('font/PixelifySans-Bold.ttf', 25)

        # Variável da fonte
        self.plano_de_fundo = pygame.image.load('img/Fase3.png')

        # Definindo specs inimigo
        self.skin_inimigo = pygame.image.load('img/Virus03.png').convert_alpha()
        self.inimigo = self.skin_inimigo.get_rect()

        # Definindo os objetos:
        self.pergunta = pergunta
        self.respostas = respostas
     
        # Variável coração
        self.skin_coracao =pygame.image.load('img/Coracao_2.png')
        
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
        if respostas.getQtdAcertos() >= 4:
            proxFase = pygame.draw.rect(self.tela, (255, 0, 0), (920, 320, 40, 40))
            if protagonista.colliderect(proxFase):
                self.gameStateManager.set_state('level4')
                pergunta.setDificuldade('Difícil')
                respostas.setQtdAcertos(0)                

        # Definindo game over
        if vida == 0:
                self.gameStateManager.set_state('game_over')
                self.x, self.y = 0, 250
        
        # Definindo coração
        pygame.draw.rect(self.display, (255, 255, 255), (10, 12, 120, 30))
        texto_vida = self.fonte.render(str(vida), True, (0, 0, 0))
        self.display.blit(self.skin_coracao, (0, -4))
        self.display.blit(texto_vida, (65, 10))
        
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
        if respostas.getQtdAcertos() < 4:
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
        self.fonte = pygame.font.Font('font/PixelifySans-Bold.ttf', 25)

        # Variável da fonte
        self.plano_de_fundo = pygame.image.load('img/Fase4.png')

        # Definindo specs inimigo
        self.skin_inimigo = pygame.image.load('img/Virus04.png').convert_alpha()
        self.inimigo = self.skin_inimigo.get_rect()

        # Definindo os objetos:
        self.pergunta = pergunta
        self.respostas = respostas
     
        # Variável coração
        self.skin_coracao =pygame.image.load('img/Coracao_2.png')
        
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
        if respostas.getQtdAcertos() >= 4:
            proxFase = pygame.draw.rect(self.tela, (255, 0, 0), (920, 600, 40, 40))
            if protagonista.colliderect(proxFase):
                posicao_atual.pop()
                self.gameStateManager.set_state('level5')
                pergunta.setDificuldade('Vest')
                respostas.setQtdAcertos(0)                

        # Definindo game over
        if vida == 0:
                self.gameStateManager.set_state('game_over')
                self.x, self.y = 0, 320
        
        # Definindo coração
        pygame.draw.rect(self.display, (255, 255, 255), (10, 12, 120, 30))
        texto_vida = self.fonte.render(str(vida), True, (0, 0, 0))
        self.display.blit(self.skin_coracao, (0, -4))
        self.display.blit(texto_vida, (65, 10))
        
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
        if respostas.getQtdAcertos() < 4:
            inimigo = self.retangulos_inimigos(posicao_atual[0])
            i = inimigo

            if not self.mensagemAtiva:
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

class Level5:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        # Variáveis padrão
        self.larguraTela = 960
        self.alturaTela = 680
        self.x = 0
        self.y = 630
        self.tela = pygame.display.set_mode((self.larguraTela, self.alturaTela))
        self.fonte = pygame.font.Font('font/PixelifySans-Bold.ttf', 25)
        
        # Variável da fonte
        self.plano_de_fundo = pygame.image.load('img/Fase5.png')

        # Definindo specs inimigo
        self.skin_inimigo = pygame.image.load('img/final_boss.png').convert_alpha()
        self.inimigo = self.skin_inimigo.get_rect()

        # Definindo os objetos:
        self.pergunta = pergunta
        self.respostas = respostas
        
        # Variável coração
        self.skin_coracao =pygame.image.load('img/Coracao_2.png')
        
        # Definindo os inimigos:
        self.inimigo_atual = (360, 190)

        self.listaGRANDONA = [1, 1, 1, 1, 1, 1, 1, 1]

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

        # variável final
        self.fase_final = True
        global fase_final
        fase_final = self.fase_final

        if fase_final == True:
            global posicao_atual
            posicao_atual = self.listaGRANDONA

        # Definindo o retângulo para passar de fase:
        if respostas.getQtdAcertos() >= 5:
            self.gameStateManager.set_state('final')
            respostas.setQtdAcertos(0)

        # Definindo game over
        if vida == 0:
                self.gameStateManager.set_state('game_over')
                self.x, self.y = 0, 630
        
        # Definindo coração
        pygame.draw.rect(self.display, (255, 255, 255), (10, 12, 120, 30))
        texto_vida = self.fonte.render(str(vida), True, (0, 0, 0))
        self.display.blit(self.skin_coracao, (0, -4))
        self.display.blit(texto_vida, (65, 10))
        
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
        
        i= self.retangulos_inimigos(self.inimigo_atual)
        self.tela.blit(self.skin_inimigo, i)
        if protagonista.colliderect((i)):
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

class Final:
    #definições básicas e variáveis globais
    pygame.display.set_caption('Parabéns')

    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.WIDTH, self.HEIGHT = 960, 680
        #Fonte
        self.fonte = pygame.font.Font('font/PixelifySans-Bold.ttf', 36)

    
    def rodando(self):
        #LOOP DO JOGO
        # Cor de fundo
        bg_image = pygame.image.load("img/fundo_win.png")
        bg_image = pygame.transform.scale(bg_image, (self.WIDTH, self.HEIGHT))


        # Criar o botão
        button_radius = 20  # Define o raio para os cantos arredondados do botão
        menu_button = create_rounded_button(470, 250, 80, 40, (106, 13, 173), button_radius, text="Menu", text_color=(255, 255, 255), font_size=40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()      
        self.display.blit(bg_image, (0,0))  # Preencher a tela com a cor de fundo
        draw_text("Você venceu, seu corpo foi protegido!", self.fonte, (255,255,255), self.display, self.WIDTH // 1.91,120)


        # Desenhar o botão com bordas arredondadas
        if draw_rounded_button(self.display, menu_button):
            self.gameStateManager.set_state('tela_inicial')
            time.sleep(.10)

class TelaInicial:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.fonte = pygame.font.Font('font/PixelifySans-Bold.ttf', 85)
        self.WIDTH, self.HEIGHT = 960, 680

    def rodando(self):
        pygame.display.set_caption("Tela inicial")

        # Cor de fundo
        bg_image = pygame.image.load("img/fundoofc.png")
        bg_image = pygame.transform.scale(bg_image, (self.WIDTH, self.HEIGHT))

        # Criar o botão
        button_radius = 20  # Define o raio para os cantos arredondados do botão
        cadastro_button = create_rounded_button(395, 430, 200, 60, (106, 13, 173), button_radius, text="Cadastro", text_color=(255, 255, 255), font_size=40)
        login_button = create_rounded_button(395, 500, 200, 60, (106, 13, 173), button_radius, text="Login", text_color=(255, 255, 255), font_size=40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        self.display.blit(bg_image, (0,0))  # Preencher a tela com a cor de fundo
        draw_text("VACMAN", self.fonte, (255,255,255), self.display, self.WIDTH // 1.91,330)


        # Desenhar o botão com bordas arredondadas
        if draw_rounded_button(self.display, cadastro_button):
            self.gameStateManager.set_state('cadastro')
            time.sleep(.10)
        if draw_rounded_button(self.display, login_button):
            self.gameStateManager.set_state('login')
            time.sleep(.10)

class TelaCadastro:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.fonte = pygame.font.Font('font/PixelifySans-Bold.ttf', 85)
        self.WIDTH, self.HEIGHT = 960, 680
    
    def rodando(self):
        # Cor de fundo
        bg_image = pygame.image.load("img/fundoofc.png")
        bg_image = pygame.transform.scale(bg_image, (self.WIDTH, self.HEIGHT))

        # Criar o botão
        button_radius = 20  # Define o raio para os cantos arredondados do botão
        cadastro_aluno_button = create_rounded_button(380, 410, 240, 60, (106, 13, 173), button_radius, text="Cadastro Aluno", text_color=(255, 255, 255), font_size=40)
        cadastro_prof_button = create_rounded_button(380, 480, 240, 60, (106, 13, 173), button_radius, text="Cadastro Prof", text_color=(255, 255, 255), font_size=40)
        voltar_button = create_rounded_button(470, 570, 80, 40, (106, 13, 173), button_radius, text="voltar", text_color=(255, 255, 255), font_size=30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        self.display.blit(bg_image, (0,0))  # Preencher a tela com a cor de fundo
        draw_text("CADASTRO", self.fonte, (255,255,255), self.display, self.WIDTH // 1.91,330)


        # Desenhar o botão com bordas arredondadas
        if draw_rounded_button(self.display, cadastro_aluno_button):
            self.gameStateManager.set_state('cadastro_aluno')
            time.sleep(.10)
        if draw_rounded_button(self.display, cadastro_prof_button):
            self.gameStateManager.set_state('cadastro_professor')
            time.sleep(.10)
        if draw_rounded_button(self.display, voltar_button):
            self.gameStateManager.set_state('tela_inicial')
            time.sleep(.10)

class CadastroAluno:
    def __init__(self, gameStateManager):
        self.aluno = Usuario.Usuario()
        self.dao = DAO.DAO()
        self.gameStateManager = gameStateManager

    def rodando(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        self.root_cadastro = ctk.CTk()
        self.root_cadastro.geometry(f"{960}x{680}")
        self.root_cadastro.title("CADASTRO ALUNO")

        image = Image.open("img/FundoVeiavirus.png")
        background_image = ImageTk.PhotoImage(image)

        background_label = ctk.CTkLabel(self.root_cadastro, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame = ctk.CTkFrame(master=self.root_cadastro, width=450, height=450, corner_radius=10)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        label_1 = ctk.CTkLabel(master=frame, width=400, height=60, corner_radius=10, fg_color=("gray70", "gray35"), text="Faça seu cadastro Aluno!")
        label_1.place(relx=0.5, rely=0.3, anchor="center")

        self.nome_entry = ctk.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Nome")
        self.nome_entry.place(relx=0.5, rely=0.52, anchor="center")

        self.email_entry = ctk.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Email")
        self.email_entry.place(relx=0.5, rely=0.6, anchor="center")

        button_cadastro = ctk.CTkButton(master=frame, text="CADASTRO", corner_radius=6, command=self.validar_cadastro, width=400)
        button_cadastro.place(relx=0.5, rely=0.7, anchor="center")

        self.root_cadastro.mainloop()

    def validar_cadastro(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()

        existe = self.dao.existeAluno(nome, email)[0]

        if existe == 1:
            messagebox.showerror("Falha no cadastro", "Nome ou email inválidos")
        else:
            messagebox.showinfo("Sucesso", f"Seja bem vindo, {nome}")
            self.dao.registrarAluno(nome, email)
            self.aluno.setNomeAluno(nome)
            self.aluno.setEmailAluno(email)
            global aluno
            aluno = self.aluno

            self.root_cadastro.destroy()
            self.gameStateManager.set_state('start')

class CadastroProfessor:
    def __init__(self, gameStateManager):
        self.professor = Usuario.Usuario()
        self.dao = DAO.DAO()
        self.gameStateManager = gameStateManager

    def rodando(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        self.root_cadastro = ctk.CTk()
        self.root_cadastro.geometry(f"{960}x{680}")
        self.root_cadastro.title("CADASTRO PROFESSOR")

        image = Image.open("img/FundoVeiavirus.png")
        background_image = ImageTk.PhotoImage(image)

        background_label = ctk.CTkLabel(self.root_cadastro, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame = ctk.CTkFrame(master=self.root_cadastro, width=450, height=450, corner_radius=10)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        label_1 = ctk.CTkLabel(master=frame, width=400, height=60, corner_radius=10, fg_color=("gray70", "gray35"), text="Faça seu cadastro Professor!")
        label_1.place(relx=0.5, rely=0.3, anchor="center")

        self.nome_entry = ctk.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Nome")
        self.nome_entry.place(relx=0.5, rely=0.52, anchor="center")

        self.email_entry = ctk.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Email")
        self.email_entry.place(relx=0.5, rely=0.6, anchor="center")

        button_cadastro = ctk.CTkButton(master=frame, text="CADASTRO", corner_radius=6, command=self.validar_cadastro, width=400)
        button_cadastro.place(relx=0.5, rely=0.7, anchor="center")

        self.root_cadastro.mainloop()

    def validar_cadastro(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()

        existe = self.dao.existeProfessor(nome, email)[0]

        if existe == 1:
            messagebox.showerror("Falha no cadastro", "Nome ou email inválidos")
        else:
            messagebox.showinfo("Sucesso", f"Seja bem vindo, {nome}")
            self.professor.setNomeAluno(nome)
            self.professor.setEmailAluno(email)
            self.dao.registrarProfessor(nome, email)

            professor = self.professor

            self.root_cadastro.destroy()
            self.gameStateManager.set_state('tela_professor')

    def init_game(self):
        self.gameStateManager.set_state('tela_professor')

class TelaLogin:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.fonte = pygame.font.Font('font/PixelifySans-Bold.ttf', 85)
        self.WIDTH, self.HEIGHT = 960, 680
    
    def rodando(self):
        # Cor de fundo
        bg_image = pygame.image.load("img/fundoofc.png")
        bg_image = pygame.transform.scale(bg_image, (self.WIDTH, self.HEIGHT))

        # Criar o botão
        button_radius = 20  # Define o raio para os cantos arredondados do botão
        login_aluno_button = create_rounded_button(380, 410, 240, 60, (106, 13, 173), button_radius, text="Login Aluno", text_color=(255, 255, 255), font_size=40)
        login_prof_button = create_rounded_button(380, 480, 240, 60, (106, 13, 173), button_radius, text="Login Prof", text_color=(255, 255, 255), font_size=40)
        voltar_button = create_rounded_button(470, 570, 80, 40, (106, 13, 173), button_radius, text="voltar", text_color=(255, 255, 255), font_size=30)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        self.display.blit(bg_image, (0,0))  # Preencher a tela com a cor de fundo
        draw_text("LOGIN", self.fonte, (255,255,255), self.display, self.WIDTH // 1.91,330)


        # Desenhar o botão com bordas arredondadas
        if draw_rounded_button(self.display, login_aluno_button):
            self.gameStateManager.set_state('login_aluno')
            time.sleep(.10)
        if draw_rounded_button(self.display, login_prof_button):
            self.gameStateManager.set_state('login_prof')
            time.sleep(.10)
        if draw_rounded_button(self.display, voltar_button):
            self.gameStateManager.set_state('tela_inicial')
            time.sleep(.10)

class LoginProfessor:
    def __init__(self, gameStateManager):
        self.professor = Usuario.Usuario()
        self.dao = DAO.DAO()
        self.gameStateManager = gameStateManager

    def rodando(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        self.root_login = ctk.CTk()
        self.root_login.geometry(f"{960}x{680}")
        self.root_login.title("LOGIN PROFESSOR")

        image = Image.open("img/FundoVeiavirus.png")
        background_image = ImageTk.PhotoImage(image)

        background_label = ctk.CTkLabel(self.root_login, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        frame = ctk.CTkFrame(master=self.root_login, width=450, height=450, corner_radius=10)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        label_1 = ctk.CTkLabel(master=frame, width=400, height=60, corner_radius=10, fg_color=("gray70", "gray35"), text="Faça seu login Professor!")
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

        existe = self.dao.existeProfessor(nome, email)[0]

        if existe == 1:
            messagebox.showinfo("Sucesso", f"Seja bem vindo, {nome}")
            self.professor.setNomeProfessor(nome)
            self.professor.setEmailProfessor(email)
            professor = self.professor

            self.root_login.destroy()
            self.gameStateManager.set_state('tela_professor')
        else:
            messagebox.showerror("Falha no login", "Nome ou email inválidos")
          
class LoginAluno:
    def __init__(self, gameStateManager):
        self.aluno = Usuario.Usuario()
        self.dao = DAO.DAO()
        self.gameStateManager = gameStateManager

    def rodando(self):
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
            self.gameStateManager.set_state('start')
        else:
            messagebox.showerror("Falha no login", "Nome ou email inválidos")
  
class Start:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        pygame.display.set_caption("Explicação do Jogo de Labirinto")
        self.font = pygame.font.Font(None, 25)

        # Carregar imagens
        self.up_arrow = pygame.image.load("img/w.png")
        self.down_arrow = pygame.image.load("img/s.png")
        self.left_arrow = pygame.image.load("img/a.png")
        self.right_arrow = pygame.image.load("img/d.png")
        self.space = pygame.image.load("img/space.png")


    def rodando(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            self.display.fill((0,0,0))# Desenha o fundo personalizado
            draw_text("Como jogar o Vacman:", self.font, (255, 255, 255), self.display, 110, 20)
            draw_text("São 4 fases + 1 com o final boss. Cada fase tem 4 virus que precisam ser derrotados para avançar de fase, ", self.font, (255, 255, 255), self.display, 455, 50)  
            draw_text("você derrota eles acertando corretamente as perguntas, que são geradas ao encostar neles.", self.font, (255,255,255), self.display, 395, 80)       
    
            draw_text("Use as setas do teclado para mover o personagem:", self.font, (255, 255, 255), self.display, 230, 140)

            # Desenhar setas e textos explicativos
            self.display.blit(self.up_arrow, (50, 180))
            draw_text("Mover para cima", self.font, (255, 255, 255), self.display, 200, 205)

            self.display.blit(self.down_arrow, (50, 260))
            draw_text("Mover para baixo", self.font, (255, 255, 255), self.display, 203, 285)

            self.display.blit(self.left_arrow, (50, 340))
            draw_text("Mover para a esquerda", self.font, (255, 255, 255), self.display, 225, 365)

            self.display.blit(self.right_arrow, (50, 420))
            draw_text("Mover para a direita", self.font, (255, 255, 255), self.display, 210, 445)

            self.display.blit(self.space, (50, 500))
            draw_text("Pausar o jogo", self.font, (255, 255, 255), self.display, 240, 525)

            draw_text("Pressione Enter para começar o jogo", self.font, (255, 255, 255), self.display, 170, 600)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            global vida
            vida = 8
            self.gameStateManager.set_state('level1')

class TelaProfessor:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.fonte = pygame.font.Font('font/PixelifySans-Bold.ttf', 85)
        self.WIDTH, self.HEIGHT = 960, 680
        pygame.display.set_caption("Tela Professor")

    def rodando(self):
         # Criar o botão
        button_radius = 20  # Define o raio para os cantos arredondados do botão
        alterar_pergunta_button = create_rounded_button(350, 320, 250, 60, (106, 13, 173), button_radius, text="Alterar Pergunta", text_color=(255, 255, 255), font_size=40)
        ver_rank_button = create_rounded_button(350, 390, 250, 60, (106, 13, 173), button_radius, text="Ver Ranking", text_color=(255, 255, 255), font_size=40)

        # Loop principal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        self.display.fill((0,0,0))  # Preencher a tela com a cor de fundo
        draw_text("Bem Vindo Professor(a)", self.fonte, (255,255,255), self.display, self.WIDTH // 1.91,150)


        # Desenhar o botão com bordas arredondadas
        if draw_rounded_button(self.display, ver_rank_button):
            self.root_ranking = ctk.CTk()
            self.app_ranking = Ranking(self.root_ranking, self)
            self.root_ranking.mainloop()
        if draw_rounded_button(self.display, alterar_pergunta_button):
            AlterarPerguntas()

class GameOver:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.fonte = pygame.font.Font('font/PixelifySans-Bold.ttf', 35)
        self.WIDTH, self.HEIGHT = 960, 680
        pygame.display.set_caption("Tela GameOver")
    
    def rodando(self):
        # Cor de fundo
        bg_image = pygame.image.load("img/fundo_perdeu.png")
        bg_image = pygame.transform.scale(bg_image, (self.WIDTH, self.HEIGHT))

        # Criar o botão
        button_radius = 20  # Define o raio para os cantos arredondados do botão
        botao_jogar_nova = create_rounded_button(380, 320, 240, 60, (106, 13, 173), button_radius, text="Tentar de novo", text_color=(255, 255, 255), font_size=40)
        menu_button = create_rounded_button(470, 450, 80, 40, (106, 13, 173), button_radius, text="Menu", text_color=(255, 255, 255), font_size=30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        self.display.blit(bg_image, (0,0))  # Preencher a tela com a cor de fundo
        draw_text("Você falhou, seu corpo foi dominado!", self.fonte, (255,255,255), self.display, self.WIDTH // 1.91,78)


        # Desenhar o botão com bordas arredondadas
        if draw_rounded_button(self.display, botao_jogar_nova):
            global vida
            vida = 8
            self.gameStateManager.set_state('level1')
        if draw_rounded_button(self.display, menu_button):
            self.gameStateManager.set_state('tela_inicial')
            time.sleep(.10)

class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState

    def get_state(self):
        return self.currentState

    def set_state(self, state):
        self.currentState = state

# Funções para criar botões 
# Função para criar um botão com bordas arredondadas
def create_rounded_button(x, y, width, height, color, radius, text=" ", text_color=(0, 0, 0), font_size=30):
    button = {}  # Dicionário para armazenar os atributos do botão
    button['width'] = width
    button['height'] = height
    button['color'] = color
    button['radius'] = radius
    button['rect'] = pygame.Rect(x, y, width, height)
    button['clicked'] = False
    button['text'] = text
    button['text_color'] = text_color
    button['font'] = pygame.font.SysFont(None, font_size)
    button['text_surface'] = button['font'].render(button['text'], True, button['text_color'])
    return button

# Função para desenhar um botão com bordas arredondadas
def draw_rounded_button(surface, button):
    action = False
    # Get mouse position
    pos = pygame.mouse.get_pos()
    # Check mouseover and clicked conditions
    if button['rect'].collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1 and button['clicked'] == False:
            button['clicked'] = True
            action = True
    if pygame.mouse.get_pressed()[0] == 0:
        button['clicked'] = False
    # Draw rounded button on screen
    pygame.draw.rect(surface, button['color'], button['rect'], border_radius=button['radius'])
    # Draw text on button
    text_rect = button['text_surface'].get_rect(center=button['rect'].center)
    surface.blit(button['text_surface'], text_rect)
    return action

#desenha texto
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

#alterar perguntas
def AlterarPerguntas():
    #DAO instance
    dao = DAO.DAO()
    
    # Variáveis para funcionar
    valores = None

    # Função para adicionar pergunta ao banco de dados
    def add_question():
        lista_respostas = []
        lista_respostas_corretas = []
        dao.adicionarPergunta(questao_entry.get("1.0", END).strip(), variable1.get())
        idPergunta = dao.pegarPergunta(variable1.get())[1]
        for resposta in valores:
            lista_respostas.append(resposta)
            if resposta == correct_response_var.get():
                lista_respostas_corretas.append(1)
            else:
                lista_respostas_corretas.append(0)
        dao.adicionarRespostas(idPergunta, lista_respostas_corretas, lista_respostas)


        fetch_questions()
        clear_fields()

    # Função para buscar todas as perguntas do banco de dados
    def fetch_questions():
        linhas = dao.pegarMultiplasPerguntas()
        update_treeview(linhas)

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
            idPergunta = item['values'][0]
            dao.removerPergunta(idPergunta)
            dao.removerRespostas(idPergunta)
            fetch_questions()

    # Função para atualizar pergunta
    def update_question():
        selected_item = tree.selection()
        if selected_item:
            lista_respostas = []
            lista_respostas_corretas = []

            item = tree.item(selected_item)
            idPergunta = item['values'][0]
            dao.modificarPergunta(idPergunta, questao_entry.get("1.0", END).strip(), variable1.get())
            for resposta in valores:
                lista_respostas.append(resposta)
                if resposta == correct_response_var.get():
                    lista_respostas_corretas.append(1)
                else:
                    lista_respostas_corretas.append(0)
            dao.modificarRespostas(idPergunta, lista_respostas_corretas, lista_respostas)
            
            fetch_questions()
            print(f'Resposta correta atualizada: {correct_response_var.get()}')  # Print da resposta correta

    # Função para preencher campos ao selecionar uma pergunta
    def fill_fields(event):
        selected_item = tree.selection()
        if selected_item:
            item = tree.item(selected_item)
            questao = item['values']
            resposta = dao.pegarMultiplasRespostas(questao[0])
            variable1.set(questao[1])
            questao_entry.delete("1.0", END)
            questao_entry.insert(END, questao[2])
            for i in range(5):
                response_widgets[i][1].delete(0, END)

            dificuldade = variable1.get()
            if dificuldade == 'Vest':    
                response_widgets[0][1].insert(0, resposta[0][0])
                response_widgets[1][1].insert(0, resposta[1][0])
                response_widgets[2][1].insert(0, resposta[2][0])
                response_widgets[3][1].insert(0, resposta[3][0])
                response_widgets[4][1].insert(0, resposta[4][0])
            else:
                response_widgets[0][1].insert(0, resposta[0][0])
                response_widgets[1][1].insert(0, resposta[1][0])
                response_widgets[2][1].insert(0, resposta[2][0])
            for i in resposta:
                if i[1] == 1:
                    resposta_correta = resposta[resposta.index(i)][0]
            
            correct_response_var.set(resposta_correta)
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
        if difficulty == 'Vest':
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
        if difficulty == 'Vest':
            values = [response_widgets[i][1].get() for i in range(5)]
        else:
            values = [response_widgets[i][1].get() for i in range(3)]
        correct_response_combo['values'] = values
        correct_response_var.set('')

        global valores
        valores = values


    tela = ctk.CTk()
    tela.title("Perguntas Management System")
    tela.geometry("960x680")
    tela.config(bg='#161c25')
    tela.resizable(False, False)

    font1 = ('Arial', 15, 'bold')
    font2 = ('Arial', 10, 'bold')

    dificuldade_label = ctk.CTkLabel(tela, font=font1, text='Dificuldade: ', text_color='#fff', bg_color="#161C25")
    dificuldade_label.place(x=20, y=40)
    options = ['Fácil', 'Médio', 'Difícil', 'Vest']
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
        resposta_label = ctk.CTkLabel(tela, font=font1, text=f'R{i+1}:', text_color='#FFFFFF', bg_color="#161C25")
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


    fetch_questions()
    update_response_fields()  
    tela.mainloop()

if __name__ == '__main__':
    app = Game()
    app.rodando()