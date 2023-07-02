
jogadores = "João", "Maria", "Júlia", "Suzy", "José"

print("--------------")
print(jogadores)
print("--------------")
print(jogadores[1])
print("--------------")
print(jogadores[1:3])
print("--------------")
print(jogadores[1:-1])
print("--------------")
print(jogadores[:-2])

def calcular(x,y):
    return x+y, x-y, x*y, x/y

result = calcular(10,5)
print(result)
print("--------------")
a, b, c, d = calcular(10,5)
print(result)
print("Soma: " + str(a))
print("Subtrair: " + str(b))
print("Multiplicar: " + str(c))
print("Dividir: " + str(d))

print("--------------")



'''Construa um algoritmo que possua uma tupla com os números escritos
por extenso de “zero” a “nove”. Peça ao usuário para digitar um número
de 0 a 9 e retorne a ele o número por extenso, sem usar estruturas
condicionais (if e switch).'''

print("------Exercício de Tupla---------")

numeros_extenso = "zero","um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"
print(numeros_extenso)
print("-----------------------")

while True:
    numero_usuario = int(input("Digite um número de 0 a 9: "))

    try:
        print("Número por extenso:", numeros_extenso[numero_usuario])
    except:
        print("Número inválido. Tente novamente.")
        break
        





