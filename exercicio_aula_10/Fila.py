from Apartamento import Apartamento


class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0
    
    def addApartamento(self, apto):
        if self.ultimo == None:
            self.primeiro = apto
            self.ultimo = apto
        else:
            self.ultimo.proximo = apto
            self.ultimo = apto
        if self.primeiro is None:
            self.primeiro = apto
        self.tamanho += 1
        self.imprimir()    
    
    def removerApartamento(self):
        aux = self.primeiro
        if self.primeiro == None:
            print("Fila Vazia")
        elif self.primeiro.proximo == None:
            self.primeiro = None
            self.ultimo = None
            self.tamanho = 0
        else:
            self.primeiro = self.primeiro.proximo
            self.tamanho -= 1
        self.imprimir()
        return aux  

    
    def imprimir(self):
        texto = ""
        if self.primeiro == None:
            texto = "Fila Vazia"
        else:
            aux = self.primeiro
            while(aux):
                texto += aux.__str__()
                aux = aux.proximo
        print("-----------------")
        print(texto)
        print("Total de elementos: ", str(self.tamanho))
            
