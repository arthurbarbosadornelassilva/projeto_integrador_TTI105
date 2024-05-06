import pygame
from pygame.locals import *
from sys import exit

pygame.init()
pygame.display.set_caption("Vac-Man.exe")

larguraTela = 640
alturaTela = 480
eixoX = 320
eixoY = 240

tela = pygame.display.set_mode((larguraTela, alturaTela))
relogio = pygame.time.Clock()

while True:
    relogio.tick(60)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        #a partir daqui programaremos os controladores de movimento definindo as teclas e usando a varável 'event' para movimentação
        '''
        if event.type == KEYDOWN: 
            if  event.key == K_LEFT: #LEFT refere-se a seta pra esquerda
                eixoX -= 10
            if event.key == K_RIGHT: #RIGHT a da direita
                eixoX += 10
            if event.key == K_UP: #UP a pra cima
                eixoY -= 10
            if event.key == K_DOWN: #DOWN a pra baixo
                eixoY += 10
        '''
                
    #as condições abaixo definem a movimentação dos objetos com a tecla pressionada
    if pygame.key.get_pressed()[K_LEFT]:
        eixoX -= 5
    if pygame.key.get_pressed()[K_RIGHT]:
        eixoX += 5
    if pygame.key.get_pressed()[K_UP]:
        eixoY -= 5
    if pygame.key.get_pressed()[K_DOWN]:
        eixoY += 5
    
    pygame.draw.rect(tela, (255,0,0), (eixoX, eixoY, 50, 50))

    pygame.display.update()