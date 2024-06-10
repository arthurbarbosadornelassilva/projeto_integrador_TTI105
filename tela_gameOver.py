import pygame
from sys import exit
from os import path

pygame.init()

class GameOver:
    #definições básicas e variáveis globais
    pygame.display.set_caption('Game Over')

    larguraTela = 960
    alturaTela = 680
    x = 30
    y = 30
    tela = pygame.display.set_mode((larguraTela, alturaTela))
    plano_de_fundo = pygame.image.load('img\Fundo veia.png')

    #Fonte
    fonte = pygame.font.Font('font/PixelifySans-Bold.ttf', 76)

    #clock do jogo
    relogio = pygame.time.Clock()

    #LOOP DO JOGO
    while True:
        relogio.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        #Em LIMITETELA a configuração dos limites das bordas era feita de maneira diferente desta aqui
        #Além disso, aqui é possível utilizar o 'get_at' como identificador de cor e limitador da tela
        keys = pygame.key.get_pressed()
        lado_x = 40
        lado_y = 40
        cor_padrão = (255, 174, 201, 255)

        tela.fill((255,45,70))
        titulo = fonte.render("Game Over", True, (0, 0, 0))

        tela.blit(titulo, (larguraTela // 2 - titulo.get_width() // 2, 235)) 

        pygame.display.update()