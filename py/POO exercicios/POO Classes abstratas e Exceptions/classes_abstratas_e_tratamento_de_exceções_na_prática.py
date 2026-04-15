from abc import ABC, abstractmethod

# Classe Abstrata
class Veiculo(ABC):

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def ligar(self):
        pass

# Subclasses
class Carro(Veiculo):
    def mover(self):
        return "O carro está em movimento."
    def ligar(self):
        return "O carro está ligado."

class Bicicleta(Veiculo):
    def mover(self):
        return "A bicicleta está em movimento."
    def ligar(self):
        return "Não é possivel ligar uma bicicleta."
class Aviao(Veiculo):
    def mover(self):
        return "O avião está voando."
    def ligar(self):
        return "O avião está ligado e pronto para o vôo."

# Instanciando Objetos das Subclasses
carro = Carro()
bicicleta = Bicicleta()

print(carro.mover())
print(bicicleta.mover())

print(carro.ligar())
print(bicicleta.ligar())