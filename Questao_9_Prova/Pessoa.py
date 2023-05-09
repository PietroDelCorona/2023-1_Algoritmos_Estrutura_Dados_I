from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, id, nome, cpf):
        self.id = id
        self.nome = nome
        self._cpf = cpf
    
    @property
    def consultar_cpf(self):
        return self._cpf
    
    @consultar_cpf.setter
    def consultar_cpf(self):
        return self._cpf

    @abstractmethod
    def marcarPresenca():
        pass

    def matricular():
        pass