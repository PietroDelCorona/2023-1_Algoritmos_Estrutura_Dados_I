from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, id, nome, cpf, matricula):
        super().__init__(id, nome, cpf)
        self.__matricula = matricula
        self.lista_matriculas = []

    @property
    def acessar_matricula(self):
        return self.__matricula
    
    @acessar_matricula.setter
    def acessar_matricula(self):
        return self.__matricula
    
    def marcarPresenca(self):
        print("ID: ", self.id)
        print("Nome: ", self.nome)
        print("CPF: ", self._cpf)
        print("Matrícula: ", self.__matricula)
    
    def matricular(self):
        self.lista_matriculas.append()
    