from Classes import ConnectionFactory

class DAO():
    #Métodos de pergunta e resposta
    def pegarPergunta(self):
        #Estou usando esse site https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html
        connection = ConnectionFactory.ConnectionFactory()
        conexao = connection.obterConexao()
        cursor = conexao.cursor()

        query = ("SELECT pergunta, idPergunta FROM perguntas "
                 "ORDER BY RAND() "
                 "LIMIT 1;")
        cursor.execute(query)

        for item in cursor:
            pergunta = item[0]
            idPergunta = item[1]
        
        cursor.close()
        conexao.close()
        
        return pergunta, idPergunta
    
    def registrarErro(self, idPergunta):
        connection = ConnectionFactory.ConnectionFactory()
        conexao = connection.obterConexao()
        cursor = conexao.cursor()

        
        query = ("UPDATE perguntas "
                 "SET qtdErros = qtdErros + 1 "
                 f"WHERE idPergunta = {idPergunta};")
        cursor.execute(query)
        conexao.commit()
        
        cursor.close()
        conexao.close()

    def adicionarPergunta(self, novaPergunta, novaDificuldade):
        connection = ConnectionFactory.ConnectionFactory()
        conexao = connection.obterConexao()
        cursor = conexao.cursor()

        query = ("INSERT INTO perguntas(pergunta, dificuldade) "
                 f"VALUES ({novaPergunta}, {novaDificuldade}) ")
        cursor.execute(query)
        conexao.commit()

        query = ("SELECT idPergunta FROM perguntas "
                 f"WHERE pergunta = {novaPergunta}")
        cursor.execute(query)

        for item in cursor:
            idPergunta = item

        cursor.close()
        conexao.close()

        return idPergunta
    
    def removerPergunta(self, pergunta):
        connection = ConnectionFactory.ConnectionFactory()
        conexao = connection.obterConexao()
        cursor = conexao.cursor()

        query = ("DELETE FROM perguntas "
                 f"WHERE pergunta = {pergunta}")
        cursor.execute(query)
        conexao.commit()

        query = ("SELECT idPergunta FROM perguntas "
                 f"WHERE pergunta = {pergunta}")
        cursor.execute(query)

        for item in cursor:
            idPergunta = item

        cursor.close()
        conexao.close()

        return idPergunta
    
    def modificarPergunta(self, pergunta, novaPergunta=None, novaDificuldade=None):
        connection = ConnectionFactory.ConnectionFactory()
        conexao = connection.obterConexao()
        cursor = conexao.cursor()

        if novaPergunta != None and novaDificuldade != None:
            query = ("UPDATE perguntas "
                    f"SET pergunta = {novaPergunta}, dificuldade = {novaDificuldade} "
                    f"WHERE pergunta = {pergunta};")
        elif novaPergunta != None:
            query = ("UPDATE perguntas "
                    f"SET pergunta = {novaPergunta} "
                    f"WHERE pergunta = {pergunta};")
        elif novaDificuldade != None:
            query = ("UPDATE perguntas "
                    f"SET dificuldade = {novaDificuldade} "
                    f"WHERE pergunta = {pergunta};")
        cursor.execute(query)
        conexao.commit()

        cursor.close()
        conexao.close()

    def pegarRespostas(self, idPergunta):
        connection = ConnectionFactory.ConnectionFactory()
        conexao = connection.obterConexao()
        cursor = conexao.cursor()

        query = ("SELECT resposta, respostaCorreta FROM respostas "
                 f"WHERE idPergunta = {idPergunta} "
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
        
        return (respostas, respostaCorreta)
    
    def adicionarRespostas(self, idPergunta, listaRespostaCorreta:tuple, novasRespostas:tuple):
        connection = ConnectionFactory.ConnectionFactory()
        conexao = connection.obterConexao()
        cursor = conexao.cursor()

        for resposta in novasRespostas:
            respostaCorreta = listaRespostaCorreta[novasRespostas.index(resposta)]
            query = ("INSERT INTO respostas(resposta, respostaCorreta, idPergunta) "
                    f"VALUES ({resposta}, {respostaCorreta}, {idPergunta}) ")
            cursor.execute(query)
            conexao.commit()

        cursor.close()
        conexao.close()
    
    def removerRespostas(self, idPergunta):
        connection = ConnectionFactory.ConnectionFactory()
        conexao = connection.obterConexao()
        cursor = conexao.cursor()

        query = ("DELETE FROM respostas "
                 f"WHERE idPergunta = {idPergunta}")
        cursor.execute(query)
        conexao.commit()

        cursor.close()
        conexao.close()
    
    def modificarRespostas(self, idPergunta, novaListaRespostaCorreta:tuple, novaRespostas=None):
        connection = ConnectionFactory.ConnectionFactory()
        conexao = connection.obterConexao()
        cursor = conexao.cursor()
        respostas = []

        if novaRespostas != None:
            query = ("SELECT resposta FROM respostas "
                     f"WHERE idPergunta = {idPergunta}")
            cursor.execute(query)

            for item in cursor:
                respostas.append(item)

            for resposta in novaRespostas:
                antigaResposta = respostas[novaRespostas.index(resposta)]
                respostaCorreta = novaListaRespostaCorreta[novaRespostas.index(resposta)]
                if type(resposta) == str:
                    query = ("UPDATE respostas "
                            f"SET resposta = {novaRespostas}, respostaCorreta = {respostaCorreta} "
                            f"WHERE resposta = {antigaResposta};")
                else:
                    query = ("UPDATE respostas "
                            f"SET respostaCorreta = {respostaCorreta} "
                            f"WHERE resposta = {antigaResposta};")

                cursor.execute(query)
                conexao.commit()

        cursor.close()
        conexao.close()
    
    #Métodos de aluno e professor
    def registrarAluno(self, nome, email):
        connection = ConnectionFactory.ConnectionFactory()
        conexao = connection.obterConexao()
        cursor = conexao.cursor()

        query = ("INSERT INTO aluno (nome, email) "
                 f"VALUES (\'{nome}\', \'{email})\')")
        cursor.execute(query)
        conexao.commit()

        cursor.close()
        conexao.close()

    def existeAluno(self, nome, email):
        connection = ConnectionFactory.ConnectionFactory()
        conexao = connection.obterConexao()
        cursor = conexao.cursor()

        query = ("SELECT EXISTS (SELECT nome, email FROM aluno "
                 f"WHERE nome = \'{nome}\' AND email = \'{email})\'")
        existe = cursor.execute(query)
        
        cursor.close()
        conexao.close()

        return existe
    
    def registrarProfessor(self, nome, email):
        connection = ConnectionFactory.ConnectionFactory()
        conexao = connection.obterConexao()
        cursor = conexao.cursor()

        query = ("INSERT INTO professor (nome, email) "
                 f"VALUES (\'{nome}\', \'{email})\')")
        cursor.execute(query)
        conexao.commit()

        cursor.close()
        conexao.close()
    
    def existeProfessor(self, nome, email):
        connection = ConnectionFactory.ConnectionFactory()
        conexao = connection.obterConexao()
        cursor = conexao.cursor()

        query = ("SELECT EXISTS (SELECT nome, email FROM professor "
                 f"WHERE nome = \'{nome}\' AND email = \'{email})\')")
        cursor.execute(query)

        for item in cursor:
            existe = item
        
        cursor.close()
        conexao.close()

        return existe