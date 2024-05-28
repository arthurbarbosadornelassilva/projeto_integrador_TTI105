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
        self.__dificuldade = 0
        self.__quantidadePerguntas = 0
        self.__alturaTotalPergunta = 0

    #Métodos
    def definirPergunta(self, questoesRepetidas):
        dao = DAO.DAO()
        while True:
            self.__pergunta, self.__idPergunta, self.__quantidadePerguntas = dao.pegarPergunta(self.__dificuldade)
            if self.__idPergunta not in questoesRepetidas:
                break

    def exibirPergunta(self, tela, largura = int, altura = int, corFundo = tuple):
        fonte = font.Font(self.__fonte, self.__tamanhoFonte)
        texto = self.__pergunta.split()
        espaco = fonte.size(' ')[0]
        larguraMax, alturaMax = (largura, altura)
        x, y = (self.__coordenadas[0], self.__coordenadas[1])
 
        draw.rect(tela, corFundo, (self.__coordenadas[0] - 50, self.__coordenadas[1] - 30, largura, altura)) #Desenha a caixa que recebe as perguntas e respostas
        draw.rect(tela, 'Black', (self.__coordenadas[0] - 50, self.__coordenadas[1] - 30, largura, altura), 5) #Desenha a borda da caixa
        for palavra in texto:
            pergunta = fonte.render(palavra, True, (0, 0, 0))
            if x + pergunta.get_width() > larguraMax:
                x = self.__coordenadas[0]
                y += pergunta.get_height()
            Surface.blit(tela, pergunta, (x, y))
            x += pergunta.get_width() + espaco
        
        self.__alturaTotalPergunta = y

    def alterarPergunta(self, funcao, pergunta, novaPergunta=None, novaDificuldade=None):
        dao = DAO.DAO()
        match funcao:
            case "adicionar":
                dao.adicionarPergunta(novaPergunta, novaDificuldade)
            case "modificar":
                dao.modificarPergunta(pergunta, novaPergunta, novaDificuldade)
            case "remover":
                dao.removerPergunta(pergunta)

    #Getters
    def getIdPergunta(self):
        return self.__idPergunta
    
    def getAlturaTotalPergunta(self):
        return self.__alturaTotalPergunta
    
    def getQuantidadePerguntas(self):
        return self.__quantidadePerguntas
    
    #Setters
    def setDificuldade(self, dificuldade):
        self.__dificuldade = dificuldade