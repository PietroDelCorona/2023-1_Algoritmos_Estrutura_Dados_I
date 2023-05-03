from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

        
    @property 
    def tempoDeBateria(self):
        return self.__tempoDeBateria
    
    @tempoDeBateria.setter
    def tempoDeBateria(self):
        return self.__tempoDeBateria
    
    
    def getInformacoes(self):
        print("Tempo de Bateria: ", self.__tempoDeBateria)
        return super().getInformacoes()        
        

    def cadastrar():
        pass
