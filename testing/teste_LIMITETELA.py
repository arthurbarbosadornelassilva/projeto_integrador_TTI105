import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
pygame.display.set_caption("Vac-Man.exe")

larguraTela = 640
alturaTela = 480
eixoX = 320
eixoY = 240
blueX = randint(40, 600)
blueY = randint(80, 400)

tela = pygame.display.set_mode((larguraTela, alturaTela))
relogio = pygame.time.Clock()

while True:
    relogio.tick(60)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_LEFT]:
        eixoX -= 5
    if pygame.key.get_pressed()[K_RIGHT]:
        eixoX += 5
    if pygame.key.get_pressed()[K_UP]:
        eixoY -= 5
    if pygame.key.get_pressed()[K_DOWN]:
        eixoY += 5
    
    rectRed = pygame.draw.rect(tela, (255,0,0), (eixoX, eixoY, 50, 50)) 
    rectBlue = pygame.draw.rect(tela, (0,0,255), (blueX, blueY, 50, 50))
    #limite da tela será definido por uma linha invisível no canto máximo (último pixel) --> INICIALMENTE, até encontrar uma opção melhor
    lineRight = pygame.draw.rect(tela, (0,255,0), (638, 0, 2, 480))    # --> funcionou
    lineLeft = pygame.draw.rect(tela, (0,255,0), (0, 0, 2, 480))       # --> funcionou
    lineDown = pygame.draw.rect(tela, (0,255,0), (0, 478, 638, 2))     # --> funcionou
    lineUp = pygame.draw.rect(tela, (0,255,0), (0, 0, 638, 2))         # --> funcionou

    if rectRed.colliderect(rectBlue):
        blueX = randint(40, 600)
        blueY = randint(80, 400)
    #programação do impacto parede direita
    if rectRed.colliderect(lineRight) and pygame.key.get_pressed()[K_RIGHT]:
        eixoX -= 5
         #programação do impacto parede esquerda
    if rectRed.colliderect(lineLeft) and pygame.key.get_pressed()[K_LEFT]:
        eixoX += 5
         #programação do impacto parede cima
    if rectRed.colliderect(lineUp) and pygame.key.get_pressed()[K_UP]:
        eixoY += 5
         #programação do impacto parede baixo
    if rectRed.colliderect(lineDown) and pygame.key.get_pressed()[K_DOWN]:
        eixoY -= 5

    pygame.display.update()