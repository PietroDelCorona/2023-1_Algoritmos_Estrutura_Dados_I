
from Desktop import Desktop

from Notebook import Notebook



n1 = Notebook( "Notebook Dell Inspiron 15", "preto", 3.115, "15 horas")

d1 = Desktop( "PC Intel Core i7", "cinza", 6.425 , "500W")


print(f"O preço do Notebook é: R${n1.cadastrar(n1)},00")
print(f"O modelo do Desktop é: {d1.modelo}")

n1.getInformacoes()

d1.getInformacoes()