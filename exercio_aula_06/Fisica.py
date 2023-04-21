from Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        super().__init__(codigo, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    @property
    def cpf_acesso(self):
        return self.__cpf
    
    @cpf_acesso.setter
    def cpf(self):
        return self.__cpf 
    
      
    def imprime_CPF(self):
        print("CPF: ", self.__cpf)

    def calculaIMC(self):
        peso = self.peso
        altura_quad = self.altura * self.altura
        indice = peso / altura_quad
        if indice < 18.5:
            print(f"O seu IMC é de {indice:.2f}. Está abaixo do peso.")
        elif (indice > 18.5) and (indice <= 24.9):
            print(f"O seu IMC é de {indice:.2f}. Está no peso normal.")
        elif (indice >= 25) and (indice <= 29.9):
            print(f"O seu IMC é de {indice:.2f}. Está com sobrepeso.")
        elif (indice >= 30) and (indice <= 34.9):
            print(f"O seu IMC é de {indice:.2f}. Está com obesidade grau 1.")
        elif (indice >= 35) and (indice <= 39.9):
            print(f"O seu IMC é de {indice:.2f}. Está com obesidade grau 2.")
        elif indice > 40:
            print(f"O seu IMC é de {indice:.2f}. Está com obesidade grau 3.") 
            

        