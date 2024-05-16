from ConnectionFactory import ConnectionFactory

class DAO():
    def __init__(self):
        self.__idPergunta = int

    def pegarPergunta(self):
        #Estou usando esse site https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html
        connection = ConnectionFactory()
        conexao = connection.obterConexao()
        cursor = conexao.cursor()

        query = ("SELECT pergunta, idPergunta FROM perguntas "
                 "ORDER BY RAND() "
                 "LIMIT 1;")
        cursor.execute(query)

        for item in cursor:
            pergunta = item[0]
            self.__idPergunta = item[1]
        
        cursor.close()
        conexao.close()

        print(pergunta)
        return pergunta
    
    def registrarErro(self):
        connection = ConnectionFactory()
        conexao = connection.obterConexao()
        cursor = conexao.cursor()

        
        query = ("UPDATE perguntas "
                 "SET qtdErros = qtdErros + 1 "
                 f"WHERE idPergunta = {self.__idPergunta};")
        cursor.execute(query)
        conexao.commit()
        
        cursor.close()
        conexao.close()

    def pegarRespostas(self):
        connection = ConnectionFactory()
        conexao = connection.obterConexao()
        cursor = conexao.cursor()

        query = ("SELECT resposta, respostaCorreta FROM respostas "
                 f"WHERE idPergunta = {self.__idPergunta} "
                 "ORDER BY RAND()")
        cursor.execute(query)

        respostas = []
        respostaCorreta = []
        for item in cursor:
            respostas.append(item[0])
            respostaCorreta.append(item[1])
        
        respostas = tuple(respostas)
        respostaCorreta = tuple(respostaCorreta)

        cursor.close()
        conexao.close()
        
        return respostas, respostaCorreta