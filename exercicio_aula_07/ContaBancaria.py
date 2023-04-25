from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, nome=None, cpf=None, valor=None):
        self.nome = nome
        self.cpf = cpf
        self.valor = valor
    
    def imprimir(self):
        print("Nome: ", self.nome)
        print("CPF: ", self.cpf)
        print("Valor: ", self.valor)

    @abstractmethod
    def cadastrar_conta():
        pass

    @abstractmethod
    def depositar_valor():
        pass
