import mysql.connector

class ConnectionFactory():
    def __init__(self):
        self.__host = "vacman-vac-man.f.aivencloud.com"
        self.__porta = "15646"
        self.__db = "VacMan"
        self.__usuario = "avnadmin"
        self.__senha = ""
    
    def obterConexao(self):
        conexao = mysql.connector.connect(user = self.__usuario, password = self.__senha, host = self.__host, database = self.__db, port = self.__porta)
