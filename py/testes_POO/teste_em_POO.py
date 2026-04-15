#Definindo a classe Pessoa
class Pessoa:
    #Definindo os atributos da classe Pessoa
    def __init__(self,nome,cpf,idade):
        #Tornando os atributos da classe privados
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
    #Implementando pelo metodo GET uma forma de acessar os atributos
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_idade(self):
        return self.__idade
#Implementando o metodo principal e passando os atributos
def main(nome,cpf,idade):
    p1 = Pessoa("Rayan","121.***.***-**",27) # Intanciando o objeto pessoa a variavel 'p1'
    # Imprimindo no console os valores Settados da Classe para 'p1'
    print(f'Nome do cliente: {p1.get_nome()}')
    print(f'CPF do cliente: {p1.get_cpf()}')
    print(f'Idade do cliente: {p1.get_idade()}')

#if __name__ == "__main__":
main("","",0) # Executando o metodo main