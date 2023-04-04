#Aula 03
from Cidade import Cidade

from Pessoa import Pessoa

from Categoria import Categoria

from Pedido import Pedido

from Produto import Produto

c1 = Cidade("Porto Alegre")
p1 = Pessoa("João", "5133224455", c1)
print("Nome da cidade do ", p1.nome, ":", p1.city.nome)
print("-----------------------------")
p1.imprimir()


cat1 = Categoria("Bebidas")
cat2 = Categoria("Alimentos")

prod1 = Produto("Coca-Cola", 7.99, cat1)
prod2 = Produto("Fanta", 6.95, cat1)
prod3 = Produto("Arroz", 3.95, cat2)

ped1 = Pedido("27/03/2023", "Rua A, 100", p1)
print("Total: ", ped1.addProduto( prod1))
print("Total: ", ped1.addProduto( prod2))
ped1.imprimir()




