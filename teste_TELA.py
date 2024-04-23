import pygame #import da biblioteca pygame
from pygame.locals import * #import das funções do pygame
from sys import exit

pygame.init() #comando para iniciar os atributos do pygame

larguraTela = 640
alturaTela = 480

tela = pygame.display.set_mode((larguraTela, alturaTela)) #criando objeto TELA e seus atributos, definidos como variáveis
pygame.display.set_caption("Vac-Man.exe") #método para definir o nome do jogo no alto da janela

while True: #criação do loop principal do jogo
    for event in pygame.event.get(): #atributos necessários para a criação da opção de saída do pygame (senão o programa buga)
        if event.type == QUIT:
            pygame.quit()
            exit() #indica o fim do loop for, desligando os atributos deste loop
    pygame.display.update() #atualiza o display a cada ação do jogador, senão o jogo fica estático e não funciona
