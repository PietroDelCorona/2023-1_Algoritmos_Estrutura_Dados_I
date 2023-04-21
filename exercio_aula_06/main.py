from Pessoa import Pessoa

from Fisica import Fisica

from Juridica import Juridica

p1 = Pessoa("1", "João", "Rua B, 1265", "325689")
f1 = Fisica("1", "João", "Rua B, 1265", "325689", "56984712846", 18, 76, 1.75)

p1.imprimeNome()
f1.imprime_CPF()
f1.imprimeTelefone()
f1.calculaIMC()



