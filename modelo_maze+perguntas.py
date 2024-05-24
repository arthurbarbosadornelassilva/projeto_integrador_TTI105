#importando as classes pacote Classes
from Classes import Pergunta, Resposta, DAO
#ativando o pygame
import pygame
from sys import exit

pygame.init()

#BÁSICOS:
#definições básicas e variáveis globais
pygame.display.set_caption('Vac-Man.exe')

larguraTela = 960
alturaTela = 680
x = 30
y = 30
tela = pygame.display.set_mode((larguraTela, alturaTela))

#variável da fonte
fonte = pygame.font.SysFont("Arial", 20, True, False)
plano_de_fundo = pygame.image.load('img/Fundo1.1.png')

#definindo specs inimigo
skin_inimigo = pygame.image.load('img/Virus01.png').convert_alpha()
inimigo = skin_inimigo.get_rect()

#clock do jogo
relogio = pygame.time.Clock()

#variáveis das perguntas
mensagemAtiva = False
perguntaFeita = False

#definindo os objetos:
pergunta = Pergunta.Pergunta('font/PixelifySans-SemiBold.ttf', 20, (100, 100))
respostas = Resposta.Resposta('font/PixelifySans-Regular.ttf', 20, 100)

#definindo os inimigos:
inimigo_atual = None

def retangulos_inimigos(posicao):
    inimigo = skin_inimigo.get_rect()
    inimigo.topleft = (posicao)
    return inimigo

if not perguntaFeita:
    inimigo1 = retangulos_inimigos((350,250))
    inimigo2 = retangulos_inimigos((125, 600))
    inimigo3 = retangulos_inimigos((650, 250))
    inimigo4 = retangulos_inimigos((500, 500))

#lista inimigo
inimigo = [inimigo1, inimigo2, inimigo3, inimigo4]

#LOOP DO JOGO
while True:
    relogio.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            rectP1 = pygame.Rect(respostas.getListaDeColisao()[0])
            rectP2 = pygame.Rect(respostas.getListaDeColisao()[1])
            rectP3 = pygame.Rect(respostas.getListaDeColisao()[2])
        
            if rectP1.collidepoint(event.pos):
                # mensagemAtiva = False
                # perguntaFeita = False
                escolha = 0
                print(inimigo)
            elif rectP2.collidepoint(event.pos):
                # mensagemAtiva = False
                # perguntaFeita = False
                escolha = 1
                inimigo.pop(inimigo.index(inimigo_atual))
                mensagemAtiva = False
            elif rectP3.collidepoint(event.pos):
                mensagemAtiva = False
                perguntaFeita = False
                escolha = 2


    #MOVIMENTAÇÃO
    keys = pygame.key.get_pressed()
    lado_x = 40
    lado_y = 40
    cor_padrão = (255, 174, 201, 255)

    tela.fill((0,0,0))
    tela.blit(plano_de_fundo, (0, 0))
    
    #definindo protagonista
    protagonista = pygame.draw.rect(tela, (255, 255, 50), (x, y, lado_x, lado_y))

    #definindo o retângulo para passar de fase:
    proxFase = pygame.draw.rect(tela, (255, 0, 0), (900, 565, 40, 40))
    if protagonista.colliderect(proxFase):
        pygame.quit()
        exit()

    if not mensagemAtiva:
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

    #PERGUNTAS:
    #definindo mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rectMouse = pygame.Rect(mouse_x - 5, mouse_y - 5, 10, 10)
    
    # -----------
    for i in inimigo:
        if not mensagemAtiva:
            tela.blit(skin_inimigo, i)
        if protagonista.colliderect((i)):
            inimigo_atual = i
            
            if not mensagemAtiva:
                respostas.setListadeColisao([])
                pergunta.definirPergunta()
                idPergunta = pergunta.getIdPergunta()
                respostas.definirRespostas(idPergunta)
                mensagemAtiva = True
            if mensagemAtiva:
                pergunta.exibirPergunta(tela, 860, 500, (255, 255, 255))
                altura = pergunta.getAlturaTotalPergunta()
                respostas.exibirRespostas(tela, altura)
                for rect in respostas.getListaDeColisao():
                    pygame.draw.rect(tela, (0, 0, 255), pygame.Rect(rect))
            
             
    pygame.display.update()