#importando pacote Classes e random
from Classes import Pergunta, Resposta, DAO
from random import choice
#ativando o pygame
import pygame
from sys import exit

#VERSÃO DEFINITIVA DO JOGO:
#TELA JOGO:
class Game:
    def __init__ (self):
        pygame.init()
        pygame.display.set_caption('Vac-Man')

        self.larguraTela = 960
        self.alturaTela = 680
        self.tela = pygame.display.set_mode((self.larguraTela, self.alturaTela))
        self.relogio = pygame.time.Clock()

        #DEFININFO MUDANÇA DAS TELAS:
        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.tela, self.gameStateManager)
        self.level = Level(self.tela, self.gameStateManager)

        self.states = {'start': self.start, 'level': self.level}

    def rodando(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
            #PARA MUDANÇA DE TELAS
            controlador_telas = self.states[self.gameStateManager.get_state()]
            controlador_telas.rodando()

            #PARA ATUALIZAR A TELA
            pygame.display.update()
            self.relogio.tick(60)

#TELA LEVEL:
class Level:
    def __init__ (self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        #variáveis padrão
        self.larguraTela = 960
        self.alturaTela = 680
        self.x = 30
        self.y = 30
        self.tela = pygame.display.set_mode((self.larguraTela, self.alturaTela))

        #variável da fonte
        self.fonte = pygame.font.SysFont("Arial", 20, True, False)
        self.plano_de_fundo = pygame.image.load('img/Fundo1.1.png')

        #definindo specs inimigo
        self.skin_inimigo = pygame.image.load('img/Virus01.png').convert_alpha()
        self.inimigo = self.skin_inimigo.get_rect()

        #clock do jogo
        # self.relogio = pygame.time.Clock()

        #variáveis das perguntas
        self.mensagemAtiva = False
        self.dificuldade = 1
        self.escolhaFeita = False
        self.idQuestoesRepetidas = []

        #definindo os objetos:
        self.pergunta = Pergunta.Pergunta('font/PixelifySans-SemiBold.ttf', 20, (100, 100))
        self.respostas = Resposta.Resposta('font/PixelifySans-Regular.ttf', 20, 100)

        #definindo os inimigos:
        self.inimigo_atual = None

        self.posicoes_possiveis = [(350, 250), (125, 600), (650, 250), (500, 500)]
        self.posicao_atual = []
        self.ultima_posicao = None

    def retangulos_inimigos(self, posicao):
        inimigo = self.skin_inimigo.get_rect()
        inimigo.topleft = (posicao)
        return inimigo

    def rodando(self):
        #MOVIMENTAÇÃO
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.rectP1 = pygame.Rect(self.respostas.getListaDeColisao()[0])
                self.rectP2 = pygame.Rect(self.respostas.getListaDeColisao()[1])
                self.rectP3 = pygame.Rect(self.respostas.getListaDeColisao()[2])
            
                if self.rectP1.collidepoint(event.pos):
                    self.mensagemAtiva = False
                    self.escolha = 0
                    self.respostas.registrarEscolha(self.tela, self.escolha,)
                elif self.rectP2.collidepoint(event.pos):
                    self.mensagemAtiva = False
                    self.escolha = 1
                    
                elif self.rectP3.collidepoint(event.pos):
                    self.mensagemAtiva = False
                    self.escolha = 2
        
        keys = pygame.key.get_pressed()
        lado_x = 40
        lado_y = 40
        cor_padrão = (255, 174, 201, 255)

        self.tela.fill((0,0,0))
        self.tela.blit(self.plano_de_fundo, (0, 0))
        
        #definindo protagonista
        protagonista = pygame.draw.rect(self.tela, (255, 255, 50), (self.x, self.y, lado_x, lado_y))

        #definindo o retângulo para passar de fase:
        proxFase = pygame.draw.rect(self.tela, (255, 0, 0), (900, 565, 40, 40))
        if protagonista.colliderect(proxFase):
            exit

        if not self.mensagemAtiva:
            if keys[pygame.K_LEFT] and self.x > 5:
                self.x -= 5
                cor_cima = self.tela.get_at((self.x - 1, self.y))
                cor_baixo = self.tela.get_at((self.x - 1, self.y + 39))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.x == self.x
                elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.x += 5

            if keys[pygame.K_RIGHT] and self.x < 960 -lado_x -5:
                self.x += 5
                cor_cima = self.tela.get_at((self.x + 39 , self.y))
                cor_baixo = self.tela.get_at((self.x + 39, self.y + 39))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.x == self.x
                elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.x -= 5

            if keys[pygame.K_UP] and self.y > 5:
                self.y -= 5
                cor_cima = self.tela.get_at((self.x, self.y - 1))
                cor_baixo = self.tela.get_at((self.x + 39, self.y - 1))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.y == self.y
                elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.y += 5

            if keys[pygame.K_DOWN] and self.y < 720 -lado_y -5:
                self.y += 5
                cor_cima = self.tela.get_at((self.x, self.y + 39))
                cor_baixo = self.tela.get_at((self.x + 39, self.y + 39))
                if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
                    self.y == self.y
                if cor_cima != cor_padrão or cor_baixo != cor_padrão:
                    self.y -= 5

        #PERGUNTAS:
        #definindo mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rectMouse = pygame.Rect(mouse_x - 5, mouse_y - 5, 10, 10)

        #definindo posição do inimigo
        if len(self.posicao_atual) == 0:
            while True:
                posicao_escolhida = choice(self.posicoes_possiveis)
                if type(self.ultima_posicao) != tuple:
                    self.posicao_atual.append(posicao_escolhida)
                    self.ultima_posicao = posicao_escolhida
                    break
                else:
                    if self.ultima_posicao != posicao_escolhida:
                        self.posicao_atual.append(posicao_escolhida)
                        self.ultima_posicao = posicao_escolhida
                        break
        inimigo = self.retangulos_inimigos(self.posicao_atual[0]) 
        i = inimigo
        
        # -----------
        
        if not self.mensagemAtiva:
            self.tela.blit(self.skin_inimigo, i)
        if protagonista.colliderect((i)):
            inimigo_atual = i
            
            if not self.mensagemAtiva:
                self.respostas.setListadeColisao([])
                self.pergunta.definirPergunta()
                idPergunta = self.pergunta.getIdPergunta()
                self.respostas.definirRespostas(idPergunta)
                self.mensagemAtiva = True
            if self.mensagemAtiva:
                self.pergunta.exibirPergunta(self.tela, 860, 500, (255, 255, 255))
                altura = self.pergunta.getAlturaTotalPergunta()
                self.respostas.exibirRespostas(self.tela, altura)
                for rect in self.respostas.getListaDeColisao():
                    pygame.draw.rect(self.tela, (0, 0, 255), pygame.Rect(rect))

        #DEFININDO MUDANÇA PARA START
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.gameStateManager.set_state('start')

class Start:
    def __init__ (self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def rodando(self):
        self.display.fill('red')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.gameStateManager.set_state('level')

class GameStateManager:
    def __init__ (self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state

if __name__ == '__main__':
    jogo = Game()
    jogo.rodando()