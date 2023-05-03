from Computador import Computador

from Desktop import Desktop

from Notebook import Notebook



n1 = Notebook( "Notebook Dell Inspiron 15", "preto", 3.115, "15 horas")

d1 = Desktop( "PC Intel Core i7", "cinza", 6.425 , "500W")


print("Total: ", n1.cadastrar(n1))
print("Total: ", d1.cadastrar(d1))