from random import choice
posicao_atual = []
posicoes_possiveis = ((1,1), (2,2), (3,3))
ultima_posicao = None

if len(posicao_atual) == 0:
    ultima_posicao = choice(posicoes_possiveis)

print(ultima_posicao)