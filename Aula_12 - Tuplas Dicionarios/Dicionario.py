
filho1 = {"nome":"Júlia", "idade": 14}
filho2 = {"nome":"Carlos", "idade": 10}
filho3 = {"nome":"Maria", "idade": 12}

print(filho1)
print("------------------------")
print("Nome: " + filho1["nome"])
print("------------------------")
print(filho1.keys())
print("------------------------")

for chave, valor in filho1.items():
    print( chave, " - ", valor )

print("------------------------")

for chave in filho1.keys():
    print(chave, " - ", filho1[chave])

print("------------------------")

filhos = filho1, filho2, filho3
print(filhos)
print("------------------------")
filho1["nome"] = "Maria"
print(filhos)


'''Construa um algoritmo que peça ao usuário para informar o nome, a
nota01 e a nota02 de um aluno. Guarde estas informações em um
dicionário. Após, calcule a nota final deste aluno [(nota01 + nota02) /2]
e adicione ao dicionário. Ao final, imprima todos os dados do
dicionário.'''