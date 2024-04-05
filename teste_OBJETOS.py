import pygame
from pygame.locals import *
from sys import exit 

pygame.init()

larguraTela = 640
alturaTela = 480
tela = pygame.display.set_mode((larguraTela, alturaTela)) #pq mais um parênteses? Porque esta informação se enquadra dentro de uma tupla (n é necessário, mas melhora a indentação)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #ainda no loop, serão desenhados os objetos na tela
    pygame.draw.rect(tela, (255, 0, 0), (200, 300,     40, 50)) #desenhar um quadrilátero
                    #  |       |           |               |
                    #local //cor(RGB) //posição(X,Y) //tamanho(rect)
    
    pygame.draw.circle(tela, (0,255,0), (300, 250), 40) #desenhar um círculo
                                                #   |
                                                #raio do círculo //
    pygame.draw.line(tela, (0,0,255), (400, 200), (400, 250),   5) #desenhar uma linha
                                    #       |       |           |
                                    #inicioLinha// finalLinha// espessuraLinha

    pygame.display.update()