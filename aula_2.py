"""
Construa um algoritmo para implementar a
classe Retângulo que possui os atributos: altura
e largura.

A classe deve ter os seguintes métodos:
- Método construtor
- Método que calcula a área do retângulo
( altura * largura) e retorna o resultado
- Método que imprime os valores dos atributos
"""
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    
    def calcular_area(self):
        return self.base * self.altura 
        
    
    def imprimir_parametros(self):
        print(f"Base: {self.base}, Altura: {self.altura}.")
        


meu_retangulo = Retangulo(5,10)
print("Área do retângulo é: ", meu_retangulo.calcular_area())
meu_retangulo.imprimir_parametros()


        
 
   



            

