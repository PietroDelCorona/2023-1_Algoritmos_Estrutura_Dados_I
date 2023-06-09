
class Pessoa:
    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def telefone(self):
        return self.__telefone
    
    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self):
        return self._endereco
    
    @telefone.setter
    def telefone(self):
        return self.__telefone
    
    def imprimeNome(self):
        print("Nome: ", self.nome)
    
    def imprimeTelefone(self):
        print("Telefone: ", self.__telefone)
