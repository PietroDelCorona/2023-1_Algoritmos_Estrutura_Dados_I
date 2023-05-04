from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria
        self.computadores= []

        
    @property 
    def tempoDeBateria(self):
        return self.__tempoDeBateria
    
    @tempoDeBateria.setter
    def tempoDeBateria(self):
        return self.__tempoDeBateria
    
    
    def getInformacoes(self):
        super().getInformacoes() 
        print("Tempo de Bateria: ", self.__tempoDeBateria)
               
    
    def cadastrar(self, computador):
        self.computadores.append (computador)
        total = 0
        for comput in self.computadores:
            total += comput.preco
        return total
