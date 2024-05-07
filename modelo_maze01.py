import pygame
from sys import exit

pygame.init()

pygame.display.set_caption('Vac-Man.exe')

larguraTela = 960
alturaTela = 680
x = 30
y = 30
tela = pygame.display.set_mode((larguraTela, alturaTela))
plano_de_fundo = pygame.image.load('img\Fundo1.1.png')
relogio = pygame.time.Clock()

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

    if keys[pygame.K_LEFT] and x > 5:
        x -=5
        cor_cima = tela.get_at((x - 1, y))
        cor_baixo = tela.get_at((x - 1, y + 40))
        if cor_cima != cor_padrão or cor_baixo != cor_padrão:
            x += 5
    
    if keys[pygame.K_RIGHT] and x < 960 -lado_x -5:
        x += 5
        cor_cima = tela.get_at((x + 40 , y))
        cor_baixo = tela.get_at((x + 40, y + 40))
        if cor_cima != cor_padrão or cor_baixo != cor_padrão:
            x -= 5


    if keys[pygame.K_UP] and y > 5:
        y -= 5
        cor_cima = tela.get_at((x, y - 1))
        cor_baixo = tela.get_at((x + 40, y -1))
        if cor_cima != cor_padrão or cor_baixo != cor_padrão:
            y += 5

    if keys[pygame.K_DOWN] and y < 720 -lado_y -5:
        y += 5
        cor_cima = tela.get_at((x, y + 40))
        cor_baixo = tela.get_at((x + 40, y + 40))
        if cor_cima != cor_padrão or cor_baixo != cor_padrão:
            y -= 5

    tela.fill((0,0,0))
    tela.blit(plano_de_fundo, (0, 0))
    protagonista = pygame.draw.rect(tela, (255, 255, 200), (x, y, lado_x, lado_y))

    #definindo o retângulo para passar de fase:
    proxFase = pygame.draw.rect(tela, (255, 0, 0), (900, 550, 40, 40))
    if protagonista.colliderect(proxFase):
        pygame.quit()
        exit()

    pygame.display.update()