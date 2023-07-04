# Array de Salários dos Funcionarios

salarios = [3000, 3200, 4000]

def aumentarSalario(s):
    return s *1.15

novosSalarios = map (aumentarSalario, salarios)
print(list(novosSalarios))



