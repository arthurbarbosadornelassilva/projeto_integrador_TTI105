import pygame
from pygame.locals import *
from sys import exit
from random import choice

pygame.init()

#definição de variáveis pré-definidas

#variáveis da tela
larguraTela = 1280
alturaTela = 720
tela = pygame.display.set_mode((larguraTela, alturaTela))

#variável da fonte
fonte = pygame.font.SysFont("Arial", 20, True, False)

#variáveis das perguntas
mensagemAtiva = False
perguntaFeita = False

#variáveis de respostas ---> ainda não foram utilizadas
respostaAcertada = []          #lista que guarda as perguntas que foram acertadas e permite contagem total das respostas corretas
respostaErrada = []            #lista que guarda as perguntas que foram acertadas e permite contagem total das respostas erradas
respostas = (1, 2, 3)          #variável que define qual respostas das três está correta, por enquanto está definido como uma tupla de 1 a 3
ultimaEscolha = 0              #variável que define qual foi a última escolha de resposta do jogador

#variáveis do inimigo
coordenadaEscolhida = False
coordenadaInimigo = ""
ultimaCoordenada = 0


relogio = pygame.time.Clock()

eixoX = 550
eixoY = 300

while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if not mensagemAtiva:
        if pygame.key.get_pressed()[K_LEFT]:
            eixoX -= 5
        elif pygame.key.get_pressed()[K_RIGHT]:
            eixoX += 5
        elif pygame.key.get_pressed()[K_UP]:
            eixoY -= 5
        elif pygame.key.get_pressed()[K_DOWN]:
            eixoY += 5
    
    rectPersonagem = pygame.draw.rect(tela, (255, 0, 0), (eixoX, eixoY, 50, 50)) 
    
    #teste do aparecimento randoômico do inimigo pela tela
    coordenadasPossiveis = [(300, 150, 50, 50), (300, 450, 50, 50), (800, 150, 50, 50), (800, 450, 50, 50)] #coordenadas possíveis na tela em questão
    
    if not coordenadaEscolhida: 
        if ultimaCoordenada == 0:
            coordenadaEscolhida = True
            print("Coordenada escolhida")                       #Teste para ver se apenas uma passagem de código é feita
            coordenadaInimigo = choice(coordenadasPossiveis)    #esxolhe uma das quatro coordenadas previamente definidas, o código permite que mais ou menos coordenadas sejam definidas 
            perguntaFeita = False                               #define a variável de pergunta feita como falsa, ao ser feita dentro desse if, o código garante que logo após a coordenada 
                                                                #ser escolhida apenas um retângulo será desenhado na tela
        else:
            while ultimaCoordenada == coordenadaInimigo:
                coordenadaEscolhida = True
                print("Coordenada escolhida")
                coordenadaInimigo = choice(coordenadasPossiveis)
                perguntaFeita = False
                                                            
    if not perguntaFeita:
        rectTeste = pygame.draw.rect(tela, (0, 0 , 255), coordenadaInimigo)
    else:
        coordenadaEscolhida = False

    #teste do texto na tela
    mouseX, mouseY = pygame.mouse.get_pos()
    #rect_mouse = pygame.draw.rect(tela, (0, 255, 0), (mouseX-5, mouseY-5, 10, 10))
    rectMouse = pygame.Rect(mouseX - 5, mouseY - 5, 10, 10)

    pergunta = fonte.render("Isso é um exemplo de pergunta...", True, (0, 0, 0))
    resposta1 = fonte.render("A) Essa seria a resposta1...", True, (0, 0, 0))
    resposta2 = fonte.render("B) Essa seria a resposta2...", True, (0, 0, 0))
    resposta3 = fonte.render("C) Essa seria a resposta3...", True, (0, 0, 0))
    
    if rectPersonagem.colliderect(rectTeste) and not perguntaFeita:
        mensagemAtiva = True
        if mensagemAtiva:
            pygame.draw.rect(tela, (255, 255, 255), (250, 400, 800, 250)) #essa linha desenha o fundo do texto
            tela.blit(pergunta, (300, 430)) #essa linha desenha o texto da pergunta
            tela.blit(resposta1, (300, 500))
            tela.blit(resposta2, (300, 550))
            tela.blit(resposta3, (300, 600))
            if pygame.key.get_pressed()[K_z]:
                pergunta_feita = True
                mensagem_ativa = False
    
    pygame.display.update()