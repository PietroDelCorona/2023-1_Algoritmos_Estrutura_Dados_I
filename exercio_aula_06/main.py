from Pessoa import Pessoa

from Fisica import Fisica

from Juridica import Juridica

p1 = Pessoa("1", "João", "Rua B, 1265", "325689")
f1 = Fisica("1", "João", "Rua B, 1265", "325689", "56984712846", 18, 76, 1.75)

p2 = Juridica("564","Mercado do Zé", "Rua C, 567", "3514-8978", "23568-0001", "56574", 235)

p1.imprimeNome()
f1.imprime_CPF()
f1.imprimeTelefone()
f1.calculaIMC()

print("-------------------")

p2.imprimeCNPJ()
p2.emitirNotaFiscal()
