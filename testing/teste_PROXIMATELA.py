import pygame
from sys import exit

LARGURATELA = 960
ALTURATELA = 680
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURATELA, ALTURATELA))
        self.relogio = pygame.time.Clock()

        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.tela, self.gameStateManager)
        self.level = Level(self.tela, self.gameStateManager)

        self.states = {'start': self.start, 'level': self.level}
        
    def rodando(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit
                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_RETURN:
                #         self.gameStateManager.set_state('level')

            self.states[self.gameStateManager.get_state()].rodando()

            self.relogio.tick(FPS)
            pygame.display.update()

class Level:
    def __init__ (self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def rodando(self):
        self.display.fill('blue')
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
    game = Game()
    game.rodando()