from DAO import DAO
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
    def exibirRespostas(self, tela):
        dao = DAO()

        adicionalY = 0
        letras = ("A) ", "B) ", "C) ", "D) ", "E) ")
        self.__respostas, listaRespostaCorreta = dao.pegarRespostas
        
        for i in self.__respostas:
            resposta = font.SysFont(self.__fonte, self.__tamanhoFonte, True, False).render(f"{letras[self.__respostas.index(i)]}" + self.__respostas[i], True, (0, 0, 0))
            Surface.blit(resposta, (self.__coordenadas[0], self.__coordenadas[1] + adicionalY))
            adicionalY += 50

            if listaRespostaCorreta[self.__respostas.index(i)]:
                self.__respostaCorreta = self.__respostas.index(i)
    
    def registrarEscolha(self, escolha):
        dao = DAO()
        if escolha == self.__respostaCorreta:
            #contagemAcertos += 1 -> atributo da classe jogo
            return True
        else:
            #vida -= 1 -> atributo da classe jogo
            self.exibrErro(escolha)
            dao.registrarErro()

    def alterarRespostas(self, respostas = tuple):
        #Ressolver este aqui com o banco de dados
        pass
    
    def exibrErro(self, escolha):
        letras = ("A) ", "B) ", "C) ", "D) ", "E) ")
        resposta = font.SysFont(self.__fonte, self.__tamanhoFonte, True, False).render(f"{letras[escolha]}" + self.__respostas[escolha], True, (255, 0, 0))