import pygame
from random import randint

pygame.init()

#VARIÁVEIS GLOBAIS
largura_tela = 720
altura_tela = 480
x  = 80
y = 80
lado_x = 40
lado_y = 40
fonte = pygame.font.SysFont("Helvetica", 40, False, False)
tela = pygame.display.set_mode((largura_tela, altura_tela))
#eixos de p2 (precisam ser definidos fora do loop do jogo, senão o p2 fica maluco)
p2_x = randint(20, 700)
p2_y = randint(20, 460)
#clock
relogio = pygame.time.Clock()
rodando = True

#LOOP JOGO (sem usar o EXIT)
while rodando:
    relogio.tick(60)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    # definindo movimentação p1 (o keys precisa ser declarado dentro do loop do jogo para que haja movimento)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= 5
    if keys[pygame.K_RIGHT] and x < 720 - lado_x - 5:
        x += 5
    if keys[pygame.K_UP] and y > 5:
        y -= 5
    if keys[pygame.K_DOWN] and y < 480 - lado_y -5:
        y += 5

    #definindo retângulos
    tela.fill((0,0,0))
    p1 = pygame.draw.rect(tela, (255, 255, 255, 130), (x, y, lado_x, lado_y))

    #definindo movimento aleatório de p2
    p2 = pygame.draw.rect(tela, (0, 0, 255), (p2_x, p2_y, lado_x, lado_y))

    #colisão simples
    if p1.colliderect(p2):
        p2_x = randint(20, 700)
        p2_y = randint(20, 460)

     #GERANDO TEXTO
    mensagem = f'Joguinho Bom'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255, 100))
    tela.blit(texto_formatado, (450, 50))
    
    pygame.display.update()