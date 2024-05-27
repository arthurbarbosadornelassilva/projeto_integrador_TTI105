from Classes import DAO
from pygame import font, Surface, Rect

class Resposta():
    #Atributos
    def __init__(self, fonte = str, tamanhoFonte = int, X = int):
        self.__fonte = fonte
        self.__tamanhoFonte = tamanhoFonte
        self.__coordenadaX = X
        self.__respostas = tuple
        self.__respostaCorreta = int
        self.__listaRespostaCorreta = list
        self.__listaDeColisao = []
        self.__dificuldade = ""
    
    #Métodos
    def definirRespostas(self, idPergunta):
        dao = DAO.DAO()
        self.__respostas, self.__listaRespostaCorreta = dao.pegarRespostas(idPergunta)


    def exibirRespostas(self, tela, altura):
        altura += 50
        adicionalY = 0
        letras = ("A) ", "B) ", "C) ", "D) ", "E) ")
        fonte = font.Font(self.__fonte, self.__tamanhoFonte)
        
        espaco = fonte.size(' ')[0]
        larguraMax, alturaMax = (860, 450)
        x, y = (self.__coordenadaX, altura)
        
        for i in self.__respostas:
            texto = (letras[self.__respostas.index(i)] + self.__respostas[self.__respostas.index(i)]).split()
            
            rectColisao = [self.__coordenadaX - 10, y + adicionalY, 25, 25]
            for palavra in texto:
                resposta = fonte.render(palavra, True, (0, 0, 0))
                if x + resposta.get_width() > larguraMax:
                    x = self.__coordenadaX
                    y += resposta.get_height()
                Surface.blit(tela, resposta, (x, y + adicionalY))
                x += resposta.get_width() + espaco
            x = self.__coordenadaX
            adicionalY += resposta.get_height() + 25
            if len(self.__listaDeColisao) < 3:
                self.__listaDeColisao.append(rectColisao)

            if self.__listaRespostaCorreta[self.__respostas.index(i)]:
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
        resposta = font.Font(self.__fonte, self.__tamanhoFonte, True, False).render(f"{letras[escolha]}" + self.__respostas[escolha], True, (255, 0, 0))
    
    def alterarRespostas(self, funcao, idPergunta, listaRespostaCorreta, novasRespostas=None):
        dao = DAO.DAO()
        match funcao:
            case "adicionar":
                dao.adicionarRespostas(idPergunta, listaRespostaCorreta, novasRespostas)
            case "modificar":
                dao.modificarRespostas(idPergunta, listaRespostaCorreta, novasRespostas)
            case "remover":
                dao.removerRespostas(idPergunta)

    #Getters e Setters
    def getListaDeColisao(self):
        return self.__listaDeColisao
    
    def setListadeColisao(self, listaDeColisao):
        self.__listaDeColisao = listaDeColisao