class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c, base, altura):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
        self.base = base
        self.altura = altura

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c

    def calcular_area(self):
        return self.base * self.altura /2

    def imprimir_parametros(self):
        print(f"O lado A mede: {self.lado_a}. \nO lado B mede: {self.lado_b}. \nO lado C mede: {self.lado_c}.")
        print(f"A Base do triângulo mede: {self.base}. \nA altura do triângulo mede: {self.altura}.")


meu_triangulo = Triangulo(5,5,5,7,10)
print("O perímetro do triângulo mede: ", meu_triangulo.calcular_perimetro())
print("A área do triângulo é: ", meu_triangulo.calcular_area())
meu_triangulo.imprimir_parametros()
