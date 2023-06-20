#Array de Preços

precos = [10, 20, 30]

def aumentarPreco(p):
    return p *1.1

novosPrecos = map (aumentarPreco, precos)
print(list(novosPrecos))

print("-------------------")

pre = [ (10,20), (30,40)]
def somar(x):
    return x[0] + x[1]

somas = map(somar, pre)
print(list(somas))