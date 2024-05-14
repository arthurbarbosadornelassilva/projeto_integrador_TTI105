from ConnectionFactory import ConnectionFactory

class DAO():
    def pegarPergunta():
        #Estou usando esse site https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html
        objeto = ConnectionFactory()
        conexao = objeto.obterConexao()
        cursor = conexao.cursor()

        query = ("SELECT pergunta FROM perguntas "
                 "ORDER BY RAND() ")
        
        cursor.execute(query)

        for pergunta in cursor:
            questao = pergunta

        return questao
    
DAO_object = DAO()
pergunta = DAO.pegarPergunta()
print(pergunta[0])