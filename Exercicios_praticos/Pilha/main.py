from Livro import Livro
from Pilha import Pilha

l1 = Livro("Cegueira Moral", "Zygmunt Bauman", 250)
l2 = Livro("Como Mudar o Mundo", "Eric Hobsbawn", 400)
l3 = Livro("Filosofia em Comum", "Marcia Tiburi", 280)


pilha = Pilha()

pilha.add(l1)
pilha.add(l2)
pilha.add(l3)

pilha.remover()


