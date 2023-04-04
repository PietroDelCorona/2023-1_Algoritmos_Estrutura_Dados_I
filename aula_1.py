'''
Construir um algoritmo que contenha 3 listas, cada lista contendo:
 - Nomes de produtos
 - Preços de cada produto
 - Quantidades de cada produto

Construir uma função para imprimir um dos produtos da lista e uma função para retirar um dos produtos das listas.
As funções devem receber um parâmetro que será usado para acessar a posição dos itens das listasque serão impressos 
ou retirados
'''

nomes_produtos = ["Coca-Cola", "Fanta Laranja", "Sprite", "Guaraná", "Pepsi", "Guaraná Jesus"]

preco_produtos = [2.70, 2.75, 2.95, 2.65, 3.10, 3.30]

quantidade_produtos = [30, 15, 25, 20, 18, 23]

def imprimir_produtos():
    produto = int(input("Digite aqui a posição do produto na lista: "))
    print(nomes_produtos[produto])
    print(preco_produtos[produto])
    print(quantidade_produtos[produto], "unidades")
    print(preco_produtos[produto]*quantidade_produtos[produto], "reais")

def excluir_produtos():
    product = input("Digite aqui o nome do produto que você quer excluir: ")
    nomes_produtos.remove(product)
    print(nomes_produtos)
   
    

def menu():
    while True:
        escolha = input("""
        MENU
        =========
        1- Imprimir a lista de produtos da lista
        2 - Excluir o(s) produtos selecionado(s)
        Digite "fim" para encerrar o programa.
        Escolha: """)
        if escolha == '1':
            imprimir_produtos()
            #preco_final = preco_produtos * quantidade_produtos      
        if escolha == '2':
            excluir_produtos()
        if escolha == 'fim':
            print("Obrigado por utilizar esse menu!")
            break

menu()

    
        
    
