from Lista import Lista

lista = Lista()

lista.addInicio("Marcelo")
lista.addInicio("Pietro")
lista.addFim("Gabriela")
lista.addInicio("Nathália")
# Nathália, Pietro, Marcelo, Gabriela

print("-------------------")
lista.removerInicio()
lista.imprimir()
print("-------------------")
lista.removerFim()
lista.imprimir()
