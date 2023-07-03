'''
1. Construa a classe Torre e a classe Apartamento. A classe
Torre deve possuir os atributos id, nome e endereço. A
classe Apartamento deve conter os atributos, id, número do
apartamento, número da vaga de garagem e torre.

2. Este condomínio representado no exercício 1 não possui
vagas de garagem para todos os apartamentos. Isso faz com
que exista uma fila de espera por vagas. Implemente uma
fila de espera que contenha os métodos para adicionar
apartamentos na fila, retirar apartamentos informando o
número da vaga que este apartamento receberá e um
método para imprimir a fila de espera.
'''

from Apartamento import Apartamento
from Torre import Torre
from Fila import Fila

torreA = Torre("A", "Rua a, 100")
torreB = Torre("A", "Rua b, 150")

ap01 = Apartamento("101", torreA)
ap02 = Apartamento("102", torreA)
ap03 = Apartamento("103", torreB)
ap04 = Apartamento("104", torreB)
ap05 = Apartamento("105", torreB)

ap01.vaga = 1
ap02.vaga = 2

fila = Fila()
fila.addApartamento(ap03)
fila.addApartamento(ap04)
fila.addApartamento(ap05)

vaga = ap02.vaga
ap02.vaga = None
fila.addApartamento(ap02)
x = fila.removerApartamento()
x.vaga = vaga












