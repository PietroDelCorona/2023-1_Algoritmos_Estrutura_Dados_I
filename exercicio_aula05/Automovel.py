from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self,  marca, qtdRodas, modelo, velocidade, potenciaDoMotor):
        super().__init__(marca, qtdRodas, modelo, velocidade)
        self.potenciaDoMotor = potenciaDoMotor

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print("Potência do Motor: ", self.potenciaDoMotor)