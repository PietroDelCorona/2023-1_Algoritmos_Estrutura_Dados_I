from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self,  marca, qtdRodas, modelo, potenciaDoMotor):
        super().__init__(marca, qtdRodas, modelo)
        self.potenciaDoMotor = potenciaDoMotor

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print("Potência do Motor: ", self.potenciaDoMotor)