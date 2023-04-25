
from ContaBancaria import ContaBancaria


class ContaCorrente(ContaBancaria):
    def __init__(self, nome=None, cpf=None, valor=None, pagamentos=None):
        super().__init__(nome, cpf, valor)
        self.pagamentos = pagamentos
    
    def cadastrar_conta(self):
       pass        

    def depositar_valor():
        pass
    
