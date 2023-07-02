#                Praticando com dicionários

pessoa = {
    "nome": "Pietro",
    "idade": 29,
    "altura": 1.75,
    "temFilhos": False
}

print(pessoa)
print("---------------------------")

print(pessoa["nome"])
print("---------------------------")

pessoa["nome"] = "Júlia"
pessoa["idade"] = 25
pessoa["altura"] = 1.60

print(pessoa)
print("---------------------------")

pessoa["email"] = "j@email.com"
print(pessoa)
print("---------------------------")

del pessoa["temFilhos"]
print(pessoa)

print("---------------------------")

print("Exercício de Dicionário")

'''Construa um algoritmo que peça ao usuário para informar o nome, a
nota01 e a nota02 de um aluno. Guarde estas informações em um
dicionário. Após, calcule a nota final deste aluno [(nota01 + nota02) /2]
e adicione ao dicionário. Ao final, imprima todos os dados do
dicionário.'''


nome_aluno = input("Digite o nome do aluno: ")
nota_1 = float(input("Digite a primeira nota do aluno: "))
nota_2 = float(input("Digite a segunda nota do aluno: "))

aluno = {
    "Nome": nome_aluno,
    "Nota 1": nota_1,
    "Nota 2": nota_2
}

nota_final = (nota_1 + nota_2)/2

aluno["Nota Final"] = nota_final

print(aluno)