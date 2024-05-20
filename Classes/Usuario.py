class Usuario():
    #Atributos
    def __init__(self):
        self.__nomeProfessor = str
        self.__emailProfessor = str
        self.__nomeAluno = str
        self.__emailAluno = str

    #Métodos
    #Setters
    def setNomeAluno(self, nomeAluno):
        self.__nomeAluno = nomeAluno

    def setEmailAluno(self, emailALuno):
        self.__emailAluno = emailALuno
    
    def setNomeProfessor(self, nomeProfessor):
        self.__nomeProfessor = nomeProfessor

    def setEmailProfessor(self, emailProfessor):
        self.__emailProfessor = emailProfessor

    #Getters
    def getNomeAluno(self, nomeAluno):
        return self.__nomeAluno
    
    def getEmailAluno(self, emailAluno):
        return self.__emailAluno
    
    def getNomeProfessor(self, nomeProfessor):
        return self.__nomeProfessor
    
    def getEmailProfessor(self, emailProfessor):
        return self.__emailProfessor