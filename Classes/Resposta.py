from Classes import DAO
from pygame import font, Surface, Rect, mixer

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
        self.__qtdAcertos = 0
    
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
            if len(self.__listaDeColisao) < 5:
                self.__listaDeColisao.append(rectColisao)

            if self.__listaRespostaCorreta[self.__respostas.index(i)]:
                self.__respostaCorreta = self.__respostas.index(i)
    
    def registrarEscolha(self, tela, escolha, idPergunta, nomeJogador, emailJogador):
        dao = DAO.DAO()
        if escolha == self.__respostaCorreta:
            dao.registrarAcerto(nomeJogador, emailJogador)
            self.__qtdAcertos += 1
            mixer.Sound('sound\Sucesso.mp3').play()
            return 0
        else:
            dao.registrarErro(idPergunta)
            mixer.Sound('sound\Falha.mp3').play()
            return -1
    
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
    def getRespostaCorreta(self):
        return self.__respostaCorreta
    def getListaDeColisao(self):
        return self.__listaDeColisao
    def getQtdAcertos(self):
        return self.__qtdAcertos
    
    def setListadeColisao(self, listaDeColisao):
        self.__listaDeColisao = listaDeColisao
    def setQtdAcertos(self, qtdAcertos):
        self.__qtdAcertos = qtdAcertos