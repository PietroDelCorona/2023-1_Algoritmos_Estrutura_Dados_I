'''Construa um algoritmo de busca contendo um vetor de números
inteiros de 20 posições.
• O algoritmo deve ter duas funções, uma para busca sequencial e
outra para busca binária.
• Coloque um contador em cada função para contar as iterações de
cada função.
• Peça ao usuário que informe o valor que deseja procurar.
• Então informe ao usuário se este valor existe no vetor e quantas
iterações foram necessárias em cada função'''

def busca_sequencial(vetor, elemento):
    contador = 0
    for i in range(len(vetor)):
        contador += 1
        if vetor[i] == elemento:
            return True, contador 
    return False, contador

def busca_binaria(vetor, elemento):
    inicio = 0
    fim = len(vetor) - 1
    contador = 0

    while inicio <= fim:
        contador += 1
        meio = (inicio + fim) // 2
        if vetor[meio] == elemento:
            return True, contador
        elif vetor[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    return False, contador



vetor = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40)

valor = int(input("Digite o valor que você deseja procurar: "))

encontrado_sequencial, contador_sequencial = busca_sequencial(vetor, valor)

if encontrado_sequencial == True:
    print(f"O valor {valor} foi encontrado na Busca Sequencial após {contador_sequencial} iterações.")
else:
    print(f"O valor {valor} não foi encontrado na Busca Sequencial após {contador_sequencial} iterações.")

encontrado_binario, contador_binario = busca_binaria(vetor, valor)

if encontrado_binario == True:
    print(f"O valor {valor} foi encontrado na Busca Binária após {contador_binario} iterações.")
else:
    print(f"O valor {valor} não foi encontrado na Busca Binária após {contador_binario} iterações.")