import pygame
from pygame.locals import *
from sys import exit 

pygame.init()
pygame.display.set_caption("Vac-Man.exe")

larguraTela = 640
alturaTela = 480
#aqui abaixo definimos as variáveis de movimentação dos objetos
eixoX = larguraTela/2 #vai fazer o objeto aparecer no meio da tela (mas dá pra colocar onde quiser)
eixoY = 0 #vai fazer com que o objeto surja a partir do eixo Y = 0 (canto superior no caso do Pygame)

tela = pygame.display.set_mode((larguraTela, alturaTela))
relogio = pygame.time.Clock() #variável para controle da taxa frames, Importante para movimentação e velocidade dos objetos 

while True:
    relogio.tick(30) #define a quantidade de frames do jogo
    tela.fill((0,0,0)) #mantém a tela atrás do objeto "retângulo" preta, impedindo o erro que ocorre na declaração da linha 24 (abaixo)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    pygame.draw.rect(tela, (255,0,0), (eixoX, eixoY, 50, 50)) #definimos as posções X e Y do objeto com o valor das variáveis de eixoX e eixoY 
    if eixoY == alturaTela: #definição de movimentos automáticos
        eixoY = 0
    eixoY += 4 #a cada interação do loop principal, a variável eixoY recebe ela + (quantidade) --> o valor colocado pode definir a velocidade do obj. também
    
    pygame.display.update()
