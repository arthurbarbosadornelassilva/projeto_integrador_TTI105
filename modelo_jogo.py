import pygame
from pygame.locals import *
from sys import exit 

pygame.init()

larguraTela = 1280
alturaTela = 720
tela = pygame.display.set_mode((larguraTela, alturaTela)) 
fonte = pygame.font.SysFont("Arial", 20, True, False)
mensagem_ativa = False
pergunta_feita = False

relogio = pygame.time.Clock()

eixoX = 100
eixoY = 100

while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if not mensagem_ativa:
        if pygame.key.get_pressed()[K_LEFT]:
            eixoX -= 5
        if pygame.key.get_pressed()[K_RIGHT]:
            eixoX += 5
        if pygame.key.get_pressed()[K_UP]:
            eixoY -= 5
        if pygame.key.get_pressed()[K_DOWN]:
            eixoY += 5
    
    rectPersonagem = pygame.draw.rect(tela, (255, 0, 0), (eixoX, eixoY, 50, 50))
    if not pergunta_feita:
        rectTeste = pygame.draw.rect(tela, (0, 0 , 255), (300, 300, 50, 50))

    #teste do texto na tela
    pergunta = fonte.render("Isso é um exemplo de pergunta...", True, (0, 0, 0))
    resposta1 = fonte.render("Essa seria a resposta1...", True, (0, 0, 0))
    resposta2 = fonte.render("Essa seria a resposta2...", True, (0, 0, 0))
    resposta3 = fonte.render("Essa seria a resposta3...", True, (0, 0, 0))
    
    if rectPersonagem.colliderect(rectTeste) and not pergunta_feita:
        mensagem_ativa = True
        if mensagem_ativa:
            pygame.draw.rect(tela, (255, 255, 255), (250, 400, 800, 250)) #essa linha desenha o fundo do texto
            tela.blit(pergunta, (300, 430)) #essa linha desenha o texto da pergunta
            tela.blit(resposta1, (300, 500))
            tela.blit(resposta2, (300, 550))
            tela.blit(resposta3, (300, 600))
            if pygame.key.get_pressed()[K_ESCAPE]:
                pergunta_feita = True
                mensagem_ativa = False
    
    pygame.display.update()