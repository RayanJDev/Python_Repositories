class Calculadora:
    def adicao(self,x,y):
        try:
            return x + y
        except TypeError:
            return "Error: Valores inválidos"

    def subtracao(self,x,y):
        try:
            return x - y
        except TypeError:
            return "Error: Valores inválidos"

    def multiplicacao(self,x,y):
        try:
            return x * y
        except TypeError:
            return "Error: Valores inválidos"

    def divisao(self,x,y):
        try:
            return x / y
        except TypeError:
            return "Error: Valores inválidos"
        except ZeroDivisionError:
            return "Error: Não é possível dividir por ZERO."

calculadora = Calculadora

print(calculadora.adicao("", 5,2))
print(calculadora.subtracao("", 5,2))
print(calculadora.multiplicacao("", 5,2))
print(calculadora.divisao("", 5,0))