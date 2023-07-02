# Praticando com Tuplas

print("Prática de tuplas")
carros = "Uno", "Doblo", "Toro", "Hilux"


print(carros)
print("--------------------------")


print(carros[1])
print("--------------------------")

print(carros[1:3])
print("--------------------------")

print(carros[:-2])
print("--------------------------")

for car in carros:
    print(car)
print("--------------------------")

for cont in range(len(carros)):
    print("Posição ", cont, " - Carro: ", carros[cont])
print("--------------------------")

for index, car in enumerate(carros):
    print("Posição ",index, " - Carro: ", car) 
print("--------------------------")

print(sorted(carros))
print("--------------------------")

print("Exercício de Tupla")

'''Construa um algoritmo que possua uma tupla com os números escritos
por extenso de “zero” a “nove”. Peça ao usuário para digitar um número
de 0 a 9 e retorne a ele o número por extenso, sem usar estruturas
condicionais (if e switch).'''

numeros = "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"


while True:

    numero_usuario = int(input("Digite o número de 0 a 9: "))

    try:
        print("Número por extenso: ", numeros[numero_usuario])
        break
    except:
        print("Número inválido. Tente novamente")
    