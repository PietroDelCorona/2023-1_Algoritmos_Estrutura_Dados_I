class Veiculo:
    def __init__(self, marca, qtdRodas, modelo):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = 0
    
  
    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        if self.velocidade - valor < 0:
            self.velocidade = 0
        else:
            self.velocidade -= valor
        self.velocidade -= valor

        
    def imprimir_informacoes(self):
        print("Marca: ", self.marca)
        print("Qtd Rodas: ", self.qtdRodas)
        print("Modelo: ", self.modelo)
        print("Velocidade Atual: ", self.velocidade)
    
   