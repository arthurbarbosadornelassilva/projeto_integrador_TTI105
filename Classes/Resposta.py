from pygame import font, Surface

class Resposta():
    #Atributos
    def __init__(self, fonte = str, tamanhoFonte = int, coordenadas = tuple):
        self.__fonte = fonte
        self.__tamanhoFonte = tamanhoFonte
        self.__coordenadas = coordenadas
        self.__respostas = tuple
        self.__respostaCorreta = int
        self.caixaDeColisao = tuple
        self.__dificuldade = ""
    
    #Métodos
    def pegarRespostas(self):
        #Resolver este aqui com o banco de dados
        pass

    def exibirRespostas(self, tela):
        adicionalY = 0
        letras = ("A) ", "B) ", "C) ", "D) ", "E) ")

        for i in self.__respostas:
            resposta = font.SysFont(self.__fonte, self.__tamanhoFonte, True, False).render(f"{letras[i]}" + self.__respostas[i], True, (0, 0, 0))
            Surface.blit(resposta, (self.__coordenadas[0], self.__coordenadas[1] + adicionalY))
            adicionalY += 50
    
    def registrarEscolha(self, escolha):
        if escolha == self.__respostaCorreta:
            True
        else:
            False
        #Ressolver este aqui com o banco de dados
        pass

    def alterarRespostas(self, respostas = tuple):
        #Ressolver este aqui com o banco de dados
        pass
    
    def exibrErro(self, escolha):
        letras = ("A) ", "B) ", "C) ", "D) ", "E) ")
        resposta = font.SysFont(self.__fonte, self.__tamanhoFonte, True, False).render(f"{letras[escolha]}" + self.__respostas[escolha], True, (255, 0, 0))