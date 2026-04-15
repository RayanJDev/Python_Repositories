import numpy as np
import matplotlib.pyplot as plt

# 1 - Um CPF é composto por 11 dígitos numéricos

# 2 - Os dois últimos dígitos do CPF são chamados dígitos verificadores, e são para garantir
#     a integridade do número. Eles são calculados com nos 9 primeiros dígitos do CPF

# 3 - Os dígitos verificadores são calculados usando o algoritmo de módulo 11. O primeiro digito verificador é
#     calculado a partir dos 9 primeiros dígitos do CPF. O segundo digito verificador é calculado a partir dos
#     9 primeiros dígitos do CPF, incluindo o primeiro digito verificador.

# 4- Após calcular os dígitos verificadores, eles são comparados com os dígitos originais do CPF.
#    Se os dígitos verificadores calculados coincidirem com os dígitos verificadores originais,
#    o CPF é considerado válido. Caso contrário, é considerado inválido.

# 5- CPFs com todos os dígitos iguais (ex.: 111.111.111-11) ou CPFs
#    com padrões específicos anulados pela Receita Federal.
#
#def validar_cpf(cpf):
#    # Removendo caracteres não numéricos
#    cpf = ''.join(filter(str.isdigit, cpf))
#
#    # Verificando se o CPF possui 11 dígitos
#    if len(cpf) != 11:
#        return False
#
#    # Verificando se todos os dígitos são iguais (caso raro, mas inválido)
#    if cpf == cpf[0] * 11:
#        return False
#
#    # Calculando o primeiro dígito verificador
#    soma_cpf = sum(int(cpf[i]) * (10 -i) for i in range(9))
#    resto_da_soma = soma_cpf % 11
#
#    if resto_da_soma < 2:
#        primeiro_verificador = 0
#    else:
#        primeiro_verificador = 11 - resto_da_soma
#
#    # Verificando o primeiro dígito verificador
#    if int(cpf[9]) != primeiro_verificador:
#        return False
#    # Calculando o segundo dígito verificador
#    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
#    resto = soma % 11
#    if resto < 2:
#        digito_verificador_2 = 0
#    else:
#        digito_verificador_2 = 11 - resto
#
#    # Verificando o segundo dígito verificador
#    if int(cpf[10]) != digito_verificador_2:
#        return False
#
#    # CPF válido
#    return True
#
#cpf = input("Digite seu CPF: ")
#if validar_cpf(cpf):
#    print(f'O cpf {cpf} é valido')
#else:
#    print(f"O CPF {cpf} é inválido.")
#
def buscar_maior_elemento():

    # Inicio números com um array vazio
    numeros = []

    #Implemento um loop para o ‘input’ receber os números no array
    for i in range(6):
        n = int(input("Adicione um número: "))
        numeros.append(n)

    #Começamos assumindo que o primeiro é o maior
    maior_numero = numeros[0]

    #Implemento mais um looping para percorrer o array e validar qual é o maior número
    for n in numeros:
        if n > maior_numero:
            maior_numero = n
    print(f'O maior número digitado é {maior_numero}')

#buscar_maior_elemento()

def buscar_maior_numero():
    numeros = [int(input("Adicione um número: ")) for _ in range(6)]
    print(f'O maior número é {max(numeros)}')
#buscar_maior_numero()

def mover_torre_de_Hanoi(origem,destino):
    disco = origem.pop()
    destino.append(disco)

def imprimir_torres(torre_A,torre_B,torre_C):
    print("A:", torre_A)
    print("B:", torre_B)
    print("C:", torre_C)
    print()

def torres_de_hanoi_recursivo(num_discos, origem, destino, auxiliar):
    if num_discos == 1:
        mover_torre_de_Hanoi(origem,destino)
        #imprimir_torres(torre_A, torre_B,torre_C)
    else:
        torres_de_hanoi_recursivo(num_discos -1, origem, auxiliar, destino)
        mover_torre_de_Hanoi(origem,destino)
        #imprimir_torres(torre_A, torre_B, torre_C)
        torres_de_hanoi_recursivo(num_discos - 1,auxiliar,destino,origem)

#num_disco = 3
#
#torre_A = list(range(num_disco, 0, -1))
#torre_B = []
#torre_C = []
#
#imprimir_torres(torre_A, torre_B, torre_C)
#torres_de_hanoi_recursivo(num_disco,torre_A,torre_C,torre_B)

def procurar_maior_numero(nums, indice = 0, maior = None):
    #Caso base
    if indice == len(nums):
        print(f'O maior número é: {maior}')
        return
    # Se for a primeira vez, define o maior
    if maior is None or nums[indice] > maior:
        maior = nums[indice]
    # Chamada recursiva passando os parâmetros CORRETAMENTE
    procurar_maior_numero(nums,indice + 1, maior)

# Chamando a função
#procurar_maior_numero([2, 34, 12, 240, 1])

np.random.seed(1)
dados = np.random.normal(loc=20, scale=2, size=1000)
print(dados)
plt.hist(dados, color= 'lightblue',ec='red')
plt.show()