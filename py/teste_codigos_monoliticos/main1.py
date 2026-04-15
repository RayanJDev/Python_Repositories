numero = int(input('Insira o numero desejado: '))
def choice_menu():
    print("="*30)
    opcao_escolhida = int(input('Escolha a forma de calculo da tabuada:\n'
  '1- Soma;\n'
  '2- Subtração;\n'
  '3- Multiplicação;\n'
  '4- Divisão;\n'
  '____________________________'))
    print("="*30)
    menu = True
    while menu:
        match opcao_escolhida:
            case 1:
                for i in range(1,11):
                    print(f'{numero} + {i} = {numero + i}')
                    menu = False
                    continue
            case 2:
                for i in range(1,11):
                    # O metodo "abs (absolute number/numero absoluto) #
                    # faz com que o resultado não saia como numero negativo"
                    print(f'{numero} - {i} = {abs(numero - i)}')
                    menu = False
                    continue
            case 3:
                for i in range(1,11):
                    print(f'{numero} * {i} = {numero * i}')
                    menu = False
                    continue
            case 4:
                for i in range(1,11):
                    #O metodo "round" faz com que o resultado saia com 1 casa decimal
                    print(f'{numero} / {i} = {round(numero / i,1)}')
                    menu = False
                    continue
            case _:
                print('ERROR 404 | NOT FOUND!')
                menu = False
                continue

choice_menu()