import pygame
from pygame.locals import *
from sys import exit

pygame.init()
pygame.display.set_caption("Vac-Man.exe")

#definição tela props.
larguraTela = 960
alturaTela = 720
x = 100
y = 100
plano_de_fundo = pygame.image.load("labirinto3.jpg")
fonte = pygame.font.SysFont("Arial", 20, True, False)
mensagem_ativa = False
pergunta_feita = True

tela = pygame.display.set_mode((larguraTela, alturaTela))
relogio = pygame.time.Clock()

while True:
    relogio.tick(60)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #definição setas props
    '''
    if pygame.key.get_pressed()[K_LEFT]:
        x -= 5
    if pygame.key.get_pressed()[K_RIGHT]:
        x += 5
    if pygame.key.get_pressed()[K_UP]:
        y -= 5
    if pygame.key.get_pressed()[K_DOWN]:
        y += 5
    '''

    #definição personagem principal
    rectPersonagem = pygame.draw.rect(tela, (255,0,0), (x, y, 40, 40))

    #definição character inimigo + perguntas
    rectInimigo = pygame.draw.rect(tela , (0, 255, 0), (480, 360, 40, 40))

    pergunta = fonte.render("Isso é um exemplo de pergunta...", True, (0, 0, 0))
    resposta1 = fonte.render("Essa seria a resposta1...", True, (0, 0, 0))
    resposta2 = fonte.render("Essa seria a resposta2...", True, (0, 0, 0))
    resposta3 = fonte.render("Essa seria a resposta3...", True, (0, 0, 0))
    
    if rectPersonagem.colliderect(rectInimigo) and pergunta_feita:
        pygame.draw.rect(tela, (255, 255, 255), (250, 400, 800, 250)) #essa linha desenha o fundo do texto
        tela.blit(pergunta, (300, 430)) #essa linha desenha o texto da pergunta
        tela.blit(resposta1, (300, 500))
        tela.blit(resposta2, (300, 550))
        tela.blit(resposta3, (300, 600))

        if pygame.key.get_pressed()[K_ESCAPE]:
            pergunta_feita = False
            mensagem_ativa = False

    #definição limites labirinto
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        cor=tela.get_at((x-1,y))
        cor2=tela.get_at((x-1,y+39))
        if (cor.r<=40) and (cor2.r<=40):
            x=x-5
            if x<1:
                x=1
    if keys[pygame.K_RIGHT]:
        cor=tela.get_at((x+40,y))
        cor2=tela.get_at((x+40,y+39))
        if (cor.r<=40) and (cor2.r<=40):
            x=x+5
            if x>960:
                x=960
    if keys[pygame.K_UP]:
        cor=tela.get_at((x,y-1))
        cor2=tela.get_at((x+39,y-1))
        if (cor.r<=40) and (cor2.r<=40):
            y=y-5
            if y<1:
                y=1
    if keys[pygame.K_DOWN]:
        cor=tela.get_at((x,y+40))
        cor2=tela.get_at((x+39,y+40))
        if (cor.r<=40) and (cor2.r<=40):
            y=y+5
            if y>720:
                y=720

    pygame.display.update()