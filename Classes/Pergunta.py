from Classes import DAO
from pygame import font, draw, Surface

class Pergunta():
    #Atributos
    def __init__(self, fonte = str, tamanhoFonte = int, coordenadas = tuple):
        self.__fonte = fonte
        self.__tamanhoFonte = tamanhoFonte
        self.__coordenadas = coordenadas
        self.__pergunta = str
        self.__idPergunta = str
        self.__mensagemAtiva = bool
        self.__alturaTotalPergunta = 0

    #Métodos
    def definirPergunta(self):
        dao = DAO.DAO()
        self.__pergunta, self.__idPergunta = dao.pegarPergunta()

    def exibirPergunta(self, tela, largura = int, altura = int, corFundo = tuple):
        fonte = font.Font(self.__fonte, self.__tamanhoFonte)
        texto = self.__pergunta.split()
        espaco = fonte.size(' ')[0]
        larguraMax, alturaMax = (860, 450)
        x, y = (self.__coordenadas[0], self.__coordenadas[1])

        draw.rect(tela, corFundo, (self.__coordenadas[0] - 50, self.__coordenadas[1] - 30, largura, altura))
        for palavra in texto:
            pergunta = fonte.render(palavra, True, (0, 0, 0))
            if x + pergunta.get_width() > larguraMax:
                x = self.__coordenadas[0]
                y += pergunta.get_height()
            Surface.blit(tela, pergunta, (x, y))
            x += pergunta.get_width() + espaco
        
        self.__alturaTotalPergunta = y

    def alterarPergunta(self, funcao, pergunta):
        match funcao:
            case "adicionar":
                pass
            case "modificar":
                pass
            case "remover":
                pass

    #Getters
    def getIdPergunta(self):
        return self.__idPergunta
    
    def getAlturaTotalPergunta(self):
        return self.__alturaTotalPergunta