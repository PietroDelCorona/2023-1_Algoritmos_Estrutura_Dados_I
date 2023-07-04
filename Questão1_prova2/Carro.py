
from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.__portas = portas
        self.proximo = None
    
    @property
    def numeroPortas(self):
        return self.__portas
    
    @numeroPortas.setter
    def numeroPortas(self):
        return self.__portas
    
    def informacoes(self):
        super().informacoesVeiculo()
        print("Número de Portas: ", self.__portas)