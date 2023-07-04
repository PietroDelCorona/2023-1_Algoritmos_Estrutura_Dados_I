
from Veiculo import Veiculo

class Drone(Veiculo):
    def __init__(self, marca, modelo, helices):
        super().__init__(marca, modelo)
        self._helices = helices
        self.proximo = None

    @property
    def numeroHelices(self):
        return self._helices
    
    @numeroHelices.setter
    def numeroHelices(self):
        return self._helices
    
    def informacoes(self):
        super().informacoesVeiculo()
        print("Número de Hélices: ", self._helices)