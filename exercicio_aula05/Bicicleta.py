from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, numMarchas, bagageiro):
        super().__init__(marca, qtdRodas, modelo)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro
    
    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print("Número de Marchas", self.numMarchas)
        if self.bagageiro :
            print("Bagageiro: ", self.bagageiro)
        else:
            print("Não há bagageiro!")
        