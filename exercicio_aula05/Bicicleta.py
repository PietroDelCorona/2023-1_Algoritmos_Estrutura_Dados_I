from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, numMarchas, bagageiro):
        super().__init__(marca, qtdRodas, modelo, velocidade)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro
    
    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print("Número de Marchas", self.numMarchas)
        print("Bagageiro: ", self.bagageiro)
        