import pygame
from pygame.locals import *
from sys import exit
from random import randint #importar "randint" de random

pygame.init()
pygame.display.set_caption("Vac-Man.exe")

larguraTela = 640
alturaTela = 480
eixoX = 320
eixoY = 240
#declaramos variáveis de eixo para a estrutura de colisão
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
    
    rectRed = pygame.draw.rect(tela, (255,0,0), (eixoX, eixoY, 50, 50)) #declaramos os objetos como variáveis
    rectBlue = pygame.draw.rect(tela, (0,0,255), (blueX, blueY, 50, 50))

    if rectRed.colliderect(rectBlue): #adicionaremos uma condição para que Se houver condição: algo acontece
        #aqui embaixo, os eixos permitirão que, tod vez que eu encostar no objeto azul, ele mude de posição na tela
        blueX = randint(40, 600)
        blueY = randint(80, 400)

    pygame.display.update()