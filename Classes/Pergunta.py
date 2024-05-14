from pygame import font, draw, Surface

class Pergunta():
    #Atributos
    def __init__(self, fonte = str, tamanhoFonte = int, coordenadas = tuple):
        self.__fonte = fonte
        self.__tamanhoFonte = tamanhoFonte
        self.__coordenadas = coordenadas
        self.__mensagemAtiva = bool
        self.__perguntaFeita = bool
        self.__pergunta = str
        self.__perguntaCorreta = bool

    #Métodos
    def pegarPergunta():
        #Resolver esta aqui com o banco de dados
        pass

    def exibirPergunta(self, tela, largura = int, altura = int, corFundo = tuple):
        self.__mensagemAtiva = True
        draw.rect(tela, corFundo, (self.__coordenadas[0], self.__coordenadas[1], largura, altura))
        pergunta = font.SysFont(self.__fonte, self.__tamanhoFonte, True, False).render(self.__pergunta, True, (0, 0, 0))
        Surface.blit(pergunta, (self.__coordenadas[0] + 50, self.__coordenadas[1] + 30))
        
    def registrarPergunta():
        #Resolver esta aqui com o banco de dados
        pass

    def alterarPergunta(self, pergunta = str):
        #Resolver esta aqui com o banco de dados
        pass