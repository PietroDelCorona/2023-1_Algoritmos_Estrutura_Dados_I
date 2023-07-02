from No import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    
    def addInicio(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
        else:
            nodo.proximo = self.inicio
            self.inicio = nodo
        self.tamanho += 1
        self.imprimir()

    def removerInicio(self):
        if self.inicio == None:
            print("A lista está vazia")
        elif self.inicio.proximo == None:
            self.inicio = None
            self.tamanho -= 1            
        else:
            self.inicio = self.inicio.proximo     
        self.tamanho -= 1
        

    def addFim(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
        else:
            aux = self.inicio
            while aux.proximo:
                aux = aux.proximo
            aux.proximo = nodo        
        self.tamanho += 1
        self.imprimir()

    def removerFim(self):
        if self.inicio == None:
            print("A lista está vazia")
        elif self.inicio.proximo == None:
            self.inicio = None
            self.tamanho = 0
        else:
            ant = self.inicio
            aux = self.inicio.proximo
            while aux.proximo:
                ant = aux
                aux = aux.proximo
            ant.proximo = None
        self.tamanho -= 1
              

    def imprimir(self):
        if self.inicio == None:
            print("A lista está vazia")
        else:
            print("------------------")
            aux = self.inicio
            while(aux):
                print(aux.dado)
                aux = aux.proximo
            print("Total de elementos: ", str(self.tamanho))