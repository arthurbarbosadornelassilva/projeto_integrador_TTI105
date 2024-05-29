# ativando o pygame
import pygame
from sys import exit

class Game_movimentos:
    def __init__ (self):
        pygame.init()
        pygame.display.set_caption('Vac-Man.exe')

        #definições básicas e variáveis globais
        self.larguraTela = 960
        self.alturaTela = 680
        # self.x = 30
        # self.y = 30
        self.tela = pygame.display.set_mode((self.larguraTela, self.alturaTela))
        # self.plano_de_fundo = pygame.image.load('img\Fundo1.1.png')
        # self.fonte = pygame.font.SysFont('arial', 20, False, False)
        # #definindo specs inimigo
        # self.skin_inimigo = pygame.image.load('img\Virus01.png').convert_alpha()
        # self.inimigo = self.skin_inimigo.get_rect()

        #clock do jogo
        self.relogio = pygame.time.Clock()

        #DEFININFO MUDANÇA DAS TELAS:
        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.tela, self.gameStateManager)
        self.level = Level(self.tela, self.gameStateManager)

        self.states = {'start': self.start, 'level': self.level}

#LOOP DO JOGO
    def rodando(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            #PARA MUDANÇA DE TELAS
            self.states[self.gameStateManager.get_state()].rodando()

            #PARA ATUALIZAR A TELA
            pygame.display.update()
            self.relogio.tick(60)

class Level:
    def __init__ (self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        #definições básicas e variáveis globais
        self.larguraTela = 960
        self.alturaTela = 680
        self.x = 30
        self.y = 30
        self.tela = pygame.display.set_mode((self.larguraTela, self.alturaTela))
        self.plano_de_fundo = pygame.image.load('img\Fundo1.1.png')
        self.fonte = pygame.font.SysFont('arial', 20, False, False)
        #definindo specs inimigo
        self.skin_inimigo = pygame.image.load('img\Virus01.png').convert_alpha()
        self.inimigo = self.skin_inimigo.get_rect()
    def rodando(self):
        #Em LIMITETELA a configuração dos limites das bordas era feita de maneira diferente desta aqui
        #Além disso, aqui é possível utilizar o 'get_at' como identificador de cor e limitador da tela
        keys = pygame.key.get_pressed()
        lado_x = 40
        lado_y = 40
        cor_padrão = (255, 174, 201, 255)

        self.tela.fill((0,0,0))
        self.tela.blit(self.plano_de_fundo, (0, 0))
        #definindo protagonista
        self.protagonista = pygame.draw.rect(self.tela, (255, 255, 50), (self.x, self.y, lado_x, lado_y))

        #definindo o retângulo para passar de fase:
        proxFase = pygame.draw.rect(self.tela, (255, 0, 0), (915, 580, 50, 60))
        if self.protagonista.colliderect(proxFase):
            mensagem = self.fonte.render("Game Over", False, "yellow")
            self.tela.blit(mensagem, (self.larguraTela/2 - 40, 320))
        
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
        
        def retangulos_inimigos(posicao):
            skin_inimigo = pygame.image.load("img\Virus01.png")
            inimigo = skin_inimigo.get_rect()
            inimigo.topleft = (posicao)
            self.tela.blit(skin_inimigo, inimigo)
            return inimigo

        inimigo1 = retangulos_inimigos((350,250))
        inimigo2 = retangulos_inimigos((125, 565))
        inimigo3 = retangulos_inimigos((650, 250))
        inimigo4 = retangulos_inimigos((500, 500))
        
        if self.protagonista.colliderect(inimigo1):
            print('colidiu')
        elif self.protagonista.colliderect(inimigo2):
            print('colidiu')
        elif self.protagonista.colliderect(inimigo3):
            print('colidiu')
        elif self.protagonista.colliderect(inimigo4):
            print('colidiu')    
        #self.display.fill('blue')

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
    jogo = Game_movimentos()
    jogo.rodando()
    jogo.retangulos_inimigos()