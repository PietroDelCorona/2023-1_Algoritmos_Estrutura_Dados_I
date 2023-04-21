from Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cnpj, inscricaoEstadual, quantidadeFuncionarios):
        super().__init__(codigo, nome, endereco, telefone)
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.quantidadeFuncionarios = quantidadeFuncionarios
    
    @property
    def cnpj(self):
        return self.__cnpj
    
    @property
    def inscricaoEstadual(self):
        return self.__inscricaoEstadual
    
    def getInscricaoEstadual(self):
        return self.__inscricaoEstadual
    
    def imprimeCNPJ():
        pass
    
    def emitirNotaFiscal():
        pass
