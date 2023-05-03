from Computador import Computador

class Desktop(Computador):
    def __init__(self,modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte =  potenciaDaFonte
    
    @property
    def potenciaDaFonte(self):
        return self._potenciaDaFonte
    
    @potenciaDaFonte.setter
    def potenciaDaFonte(self):
        return self._potenciaDaFonte
    
    def getInformacoes(self):
        print("Potência da Fonte: ", self._potenciaDaFonte)
        return super().getInformacoes()
    

