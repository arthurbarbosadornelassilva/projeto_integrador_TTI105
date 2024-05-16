from pygame import Rect, font, Surface, draw, sprite
class Janela():
    #Atributos
    def __init__(self):
        self.__tamanhoJanela = (960, 680)
    
    #Métodos
    def criarTela():
        pass
    def adicionarBotao(self, x = int, y = int, largura = int, altura = int):
        Rect(x, y, largura, altura)
    
    def adicionarTexto(self, texto = str, x = int, y = int, largura = int, altura = int, fonte = str, tamanhoFonte = int, corTexto = tuple, corFundo = tuple):
        text = font.SysFont(fonte, tamanhoFonte, True, False).render(texto, True, corTexto, corFundo)
        Surface.blit(text)

    def adicionarSprite(self, protagonista, inimigo):
        pass
    
    def adicionarCampoDeEntrada(self):
        pass