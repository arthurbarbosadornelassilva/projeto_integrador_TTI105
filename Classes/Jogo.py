import pygame

class Jogo():
    def __init__(self, plano_de_fundo):
        self.largura_tela = 960
        self.altura_tela = 680
        self.plano_de_fundo = plano_de_fundo
        self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        self.relogio = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        self.cor_padrão = (255, 174, 201, 255)

    def movimentar(self, keys):
        tela = self.tela
        cor_padrão = self.cor_padrão

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


    def contar_vidas():
        pass

    def iniciar_fase():
        pass

    def finalizar_fase():
        pass

    def pausar_jogo():
        pass

    def sair_jogo():
        pass

    def mutar_sons():
        pass

    def exibir_desempenho():
        pass