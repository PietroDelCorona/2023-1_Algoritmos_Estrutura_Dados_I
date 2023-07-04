'''
Construa um software em Python que implemente uma Fila de carros e uma Fila de drones.

As classes carro e drone herdam da classe veículo os atributos e comuns às duas classes.

A classe carro é composta dos atributos marca, modelo e portas. O atributo portas é fortemente privado.

A classe drone é composta dos atributos marca, modelo e quantidade de hélices. O atributo quantidade de hélices é fracamente privado.

Todas classes devem ter um método para imprimir as informações dos seus respectivos atributos.

Implemente uma tela com um menu (funcionando) que permita ao usuário:

-> Adicionar e remover carros da Fila.

-> Adicionar e remover drones da Fila.

-> Imprimir a Fila de carros e a Fila de drones.

'''

from Carro import Carro
from Drone import Drone
from FilaCarro import FilaCarro
from FilaDrone import FilaDrone

carro01 = Carro("Fiat", "Palio", 4)
carro02 = Carro("Renault", "Sandero", 2)
carro03 = Carro("Volkswagen", "Gol", 4)

drone01 = Drone("Multilaser", "Drone Fênix", 4)
drone02 = Drone("DJI","Drone Spark", 6)
drone03 = Drone("DJI", "Drone Phantom", 8)
'''
filaCarro = FilaCarro()
    filaCarro.addCarro(carro01)
    filaCarro.addCarro(carro02)
    filaCarro.addCarro(carro03)
'''


def adicionarCarros():
    carro01.vaga = 1

    filaCarro = FilaCarro()
    filaCarro.addCarro(carro02)
    filaCarro.addCarro(carro03)

    vaga = carro01.vaga
    carro01.vaga = None
    filaCarro.addCarro(carro01)
    x = filaCarro.removerCarro()
    x.vaga = vaga

    

def removerCarros():
    filaCarro = FilaCarro()
    filaCarro.removerCarro()


def adicionarDrones():
    drone01.vaga = 1

    filaDrone = FilaDrone()
    filaDrone.addDrone(drone02)
    filaDrone.addDrone(drone03)

    vaga = drone01.vaga
    drone01.vaga = None
    filaDrone.addDrone(carro01)
    x = filaDrone.removerDrone()
    x.vaga = vaga


def removerDrones():
    filaDrone = FilaDrone()
    filaDrone.removerDrone()


def imprimirCarros():
    filaCarro = FilaCarro()
    filaCarro.imprimir()

def imprimirDrones():
    filaDrone = FilaDrone()
    filaDrone.imprimir()

def menu():
    while True:
        escolha = input("""
        MENU
        ===========
        1 - Adicionar carros em uma fila
        2 - Remover carros em uma fila
        3 - Adicionar drones em uma fila
        4 - Remover drones em uma fila
        5 - Imprimir a fila de carros
        6 - Imprimir a fila de drones
        Digite fim para sair do menu
        Escolha: """)
        if escolha == '1':
            adicionarCarros()            
        if escolha == '2':
            removerCarros()
        if escolha == '3':
            adicionarDrones()
        if escolha == '4':
            removerDrones()
        if escolha == '5':
            imprimirCarros()
        if escolha == '6':
            imprimirDrones()
        if escolha == 'fim':
            print("Obrigado por utilizar esse menu!")
            break

menu()