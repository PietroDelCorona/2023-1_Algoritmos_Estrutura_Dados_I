from No import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

  
    def imprimir(self):
        if self.inicio == None:
            print("Lista vazia")
        else:
            print("-----------")
            aux = self.inicio
            while( aux ):
                print(aux.dado)
                aux = aux.proximo
            print("Total de elementos: ", str(self.tamanho))

    def imprimirReverso(self):
        if self.fim == None:
            print("Lista vazia")
        else:
            print("------------")
            aux = self.fim
            while( aux ):
                print(aux.dado)
                aux = aux.anterior
            print("Total de elementos: ", str(self.tamanho))
    
    def addOrdenado(self,valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
        elif valor < self.inicio.dado:
            nodo.proximo = self.inicio
            self.inicio = nodo
        else:
            atual = self.inicio
            while atual.proximo and valor > atual.proximo.dado:
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo
        self.tamanho += 1
        self.imprimir()
    
    def addReverso(self, valor):
        nodo = No(valor)
        if
        elif valor < self.fim.dado:
            nodo.anterior = self.fim
            self.fim = nodo
        self.imprimirReverso()
    
    

    
    
