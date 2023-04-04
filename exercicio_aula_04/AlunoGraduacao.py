from Aluno import Aluno

class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        super().__init__(codigo, nome, matricula)
        self.semestre = semestre
    
    def imprimir(self):
        print("------------------------")
        print("Código: ", self.codigo)
        print("Nome: ", self.nome)
        print("Matrícula: ", self.matricula)
        print("Semestre: ", self.semestre)
        print("------------------------")
