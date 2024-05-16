import pygame
from sys import exit

#ABAIXO ESTAREMOS DEFININDO FUNÇÕES PARA A CRIAÇÃO DE DIFERENTES TELAS DO JOGO

pygame.init()

pygame.display.set_caption("Vac-Man.exe")

largura_tela = 600
altura_tela = 400
x = 100
y = 100
tela = pygame.display.set_mode((largura_tela, altura_tela))
fonte = pygame.font.SysFont("arial", 30, True, True)
relogio = pygame.time.Clock()

#DEFININDO BOOLEAN DO LOOP PRINCIPAL
rodando = True

#DEFININDO O BOOLEAN DE MENU PADRÃO 
cena = "menu_jogo"

#DEFININDO O LOOP
while rodando:
    relogio.tick(30)
    keys = pygame.key.get_pressed()
    
    #DEFININDO BOOLEAN DO JOGO
    if cena == "jogando":
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        texto_padrao = fonte.render("Está rodando", True, "white")
        tela.blit(texto_padrao, ((largura_tela/ 2), (altura_tela/ 2)))

        if keys[pygame.K_0]:
            cena = "fim_jogo"
    
    #DEFININDO BOOLEAN DO GAME OVER
    elif cena == "fim_jogo":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        tela.fill((0, 0, 0))
        texto_final = fonte.render("Game Over", True, "white")
        tela.blit(texto_final, ((largura_tela/ 2), (altura_tela/ 2)))

    #DEFININDO TELA MENU
    elif cena == "menu_jogo":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = "jogando"

    pygame.display.update()