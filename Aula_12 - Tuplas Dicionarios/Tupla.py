
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
print("Multiplicar: " + str(c))

print("--------------")



'''Construa um algoritmo que possua uma tupla com os números escritos
por extenso de “zero” a “nove”. Peça ao usuário para digitar um número
de 0 a 9 e retorne a ele o número por extenso, sem usar estruturas
condicionais (if e switch).'''


numeros = "zero","um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"

