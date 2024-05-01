import pygame
from sys import exit

pygame.init()

pygame.display.set_caption('Vac-Man.exe')

larguraTela = 960
alturaTela = 720
x = 300
y = 300
tela = pygame.display.set_mode((larguraTela, alturaTela))
plano_de_fundo = pygame.image.load('img\Sem título.png')
relogio = pygame.time.Clock()

while True:
    relogio.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    #Em LIMITETELA a configuração dos limites das bordas era feita de maneira diferente desta aqui
    keys = pygame.key.get_pressed()
    lado_x = 70
    lado_y = 70

    if keys[pygame.K_LEFT] and x > 5:
        x -=5
    if keys[pygame.K_RIGHT] and x < 960 -lado_x -5:
        x += 5
    if keys[pygame.K_UP] and y > 5:
        y -= 5
    if keys[pygame.K_DOWN] and y < 720 -lado_y -5:
        y += 5

    tela.fill((0,0,0))
    tela.blit(plano_de_fundo, (-10, 0))
    pygame.draw.rect(tela, (0, 255, 255), (x, y, lado_x, lado_y))

    pygame.display.update()