class Pedido:
    def __init__(self, data, endereco, cliente):
        self.id = None
        self.data = data
        self.end = endereco
        self.cliente = cliente
        self.produtos = []

    def addProduto(self, produto):
        self.produtos.append( produto)
        total = 0
        for prod in self.produtos:
            total += prod.preco
        return total
    
    def imprimir(self):
        print("Data: ", self.data)
        print("Endereço: ", self.end)
        print("Cidade do Cliente: ", self.cliente.nome)
        print("Cidade do Cliente: ", self.cliente.city.nome)
        print("Produtos: ")
        total = 0
        if len( self.produtos ) == 0:
            print("Pedido vazio!")
        else:
            for prod in self.produtos:
                total += prod.preco
                print("------------------")
                print("Produto: ", prod.nome)
                print("Preço: ", prod.preco)
                print("Categoria: ", prod.categoria.nome)
            print("------------------")
            print("Total: ", total)