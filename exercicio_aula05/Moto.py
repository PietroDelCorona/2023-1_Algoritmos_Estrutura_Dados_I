from Automovel import Automovel

class Moto(Automovel):
    def __init__(self, potenciaDoMotor, partidaEletrica):
        super().__init__(potenciaDoMotor)
        self.partidaEletrica = partidaEletrica
    
    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        if self.partidaEletrica:
            print("Partida Elétrica: ", self.partidaEletrica)
        else:
            print("Não tem partida elétrica")


