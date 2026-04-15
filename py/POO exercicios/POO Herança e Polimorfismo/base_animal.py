class Animal:
    def __init__(self, nome):
        self.nome = nome
    def falar(self):
        pass
    def mover(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au au"

    def mover(self):
        return "Correr"

class Gato(Animal):
    def falar(self):
        return "Miau"

    def mover(self):
        return "Arranhar"
class Vaca(Animal):
    def falar(self):
        return "Mu"

    def mover(self):
        return "Comer grama"

class Voador:
    def voar(self):
        return "voando"

class Nadador:
    def nadar(self):
        return "nadando"

class Pato(Animal,Voador,Nadador):
    def falar(self):
        return "Quack"

    def mover(self):
        return f'{self.andar()},{self.nadar()} e {self.voar()}'

    def andar(self):
        return f'O {self.nome} está andando'

class Jacare(Animal,Nadador):
    def falar(self):
        return 'Jacare não fala'
    def mover(self):
        return f'{self.andar()} e {self.nadar()}'
    def andar(self):
        return f'O {self.nome} está andando devagar'

def fazer_som(animal):
    return animal.falar()

def fazer_movimento(animal):
    return animal.mover()

cachorro = Cachorro('Pirata')
gato = Gato('Frajola')
vaca = Vaca('Mimosa')
pato = Pato('Trump')
jacare = Jacare('Lacoste')

print(fazer_som(cachorro))
print(fazer_som(gato))
print(fazer_som(vaca))
print(fazer_som(pato))
print(fazer_som(jacare))

print(fazer_movimento(cachorro))
print(fazer_movimento(gato))
print(fazer_movimento(vaca))
print(fazer_movimento(pato))
print(fazer_movimento(jacare))