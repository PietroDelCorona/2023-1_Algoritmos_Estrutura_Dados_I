from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, potenciaDoMotor, qtdPortas):
        super().__init__(potenciaDoMotor)
        self.qtdPortas = qtdPortas
    
    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print("Qtd Portas: ", self.qtdPortas)


