
from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, nome=None, cpf=None, valor=None, depositos=None):
        super().__init__(nome, cpf, valor)
        self.depositos = depositos
    
    def cadastrar_conta():
        pass

    def depositar_valor():
        pass