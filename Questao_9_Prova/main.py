from Aluno import Aluno

a1 = Aluno(10, "João Marcelo Pires", "561897789-65", "200694678")

print(f"O nome do aluno é: {a1.nome}")
print(f"A matrícula do aluno é: {a1.acessar_matricula}")

a1.marcarPresenca()