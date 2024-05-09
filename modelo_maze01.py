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
        x -= 5
        cor_cima = tela.get_at((x - 1, y))
        cor_baixo = tela.get_at((x - 1, y + 39))
        if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
            x == x
        elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
            x += 5

    if keys[pygame.K_RIGHT] and x < 960 -lado_x -5:
        x += 5
        cor_cima = tela.get_at((x + 39 , y))
        cor_baixo = tela.get_at((x + 39, y + 39))
        if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
            x == x
        elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
            x -= 5

    if keys[pygame.K_UP] and y > 5:
        y -= 5
        cor_cima = tela.get_at((x, y - 1))
        cor_baixo = tela.get_at((x + 39, y - 1))
        if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
            y == y
        elif cor_cima != cor_padrão or cor_baixo != cor_padrão:
            y += 5

    if keys[pygame.K_DOWN] and y < 720 -lado_y -5:
        y += 5
        cor_cima = tela.get_at((x, y + 39))
        cor_baixo = tela.get_at((x + 39, y + 39))
        if cor_cima == (255, 0, 0, 255) or cor_baixo == (255, 0, 0, 255):
            y == y
        if cor_cima != cor_padrão or cor_baixo != cor_padrão:
            y -= 5
    

    tela.fill((0,0,0))
    tela.blit(plano_de_fundo, (0, 0))
    protagonista = pygame.draw.rect(tela, (255, 255, 50), (x, y, lado_x, lado_y))

    #definindo o retângulo para passar de fase:
    proxFase = pygame.draw.rect(tela, (255, 0, 0), (900, 565, 40, 40))
    if protagonista.colliderect(proxFase):
        pygame.quit()
        exit()

    #definindo os inimigos:
    class inimigos:
        
        def base(posicao):
            return pygame.draw.rect(tela, (255, 0, 0), posicao)
        
    inimigo1 = inimigos.base((350, 250, 40, 40))
    inimigo2 = inimigos.base((125, 600, 40, 40))
    inimigo3 = inimigos.base((650, 250, 40, 40))
    inimigo4 = inimigos.base((500, 500, 40, 40))

    if protagonista.colliderect(inimigo1):
        print('colidiu')
    elif protagonista.colliderect(inimigo2):
        print('colidiu')
    elif protagonista.colliderect(inimigo3):
        print('colidiu')
    elif protagonista.colliderect(inimigo4):
        print('colidiu')

    #definindo função de pause:

    pygame.display.update()