from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo = None, ano = None, cilindradas = None):
        super().__init__(modelo, ano)
        self.cilindradas = cilindradas
    
    def imprimirEspecifico(self):
        super().imprimir()
        print("\nCilindradas: ", self.cilindradas)