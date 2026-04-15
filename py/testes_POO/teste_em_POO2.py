from testes_POO.teste_em_POO import Pessoa #importando a classe Pessoa

p2 = Pessoa("Amanda","111.111.111-11",23) # Trabalhando com Polimorfismo
print(f'O nome do(a) cliente é: {p2.get_nome()} ')
print(f'O cpf do(a) cliente é: {p2.get_cpf()}')
print(f'A idade do(a) cliente é: {p2.get_idade()}')