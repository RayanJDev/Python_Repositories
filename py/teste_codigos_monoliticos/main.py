import time

notas = [8,9,10,5]
# O metodo "sum (soma)" soma todos os valores do array
# O metodo "len (length/quantidade)" define a quantidade de valores num array
media = sum(notas)/len(notas)
print(f'A media das notas é {media}')
print("="*30)
def func(x=[]):
    x.append(1)
    return x
print(func())
print(func())

print("="*30)

def multiplicador(numero):
    global a  # todas as referências à variável a são para a global
    a = 2  # a global será alterado
    print(f"Dentro da função,  variável  vale: {a}")
    return a * numero


a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"A variável B vale: {b}")
print(f"Fora da função, a variável A vale: {a}")

print("="*30)

def func():
    x = 1
    print(x)
x = 10
func()
print(x)

print("="*30)

def valores_da_func(num,string):
    print(f'Valores dentro da função são {num} e {string}')

valor_do_numero = 10
valor_da_string = "Banana"
valores_da_func(valor_do_numero,valor_da_string)

print("="*30)

def soma_numeros(a,b):
    try:
        resultado = a + b
        return resultado
    except TypeError :
        print("Erro: Entrada Inválida")
    except Exception as e:
        print(f'Erro inesperado: {e}')
        return None
print(soma_numeros(2,3))
#print(soma_numeros("a" + 3))
print(soma_numeros(True,3))
print(soma_numeros([1,2],3))
print("="*30)

firstNumber,secondNumber,bollean = (int(input("Digite um número inteiro:\n")),
                                    float(input("Digite um número de ponto flutuante:\n ")),
                                    bool(input("Digite um valor booleano (True ou False):\n")))
print("-"*30)
print(f'Numero inteiro: {firstNumber} (Tipo: {type(firstNumber)})')
print(f'Numero de ponto flutuante: {secondNumber} (Tipo: {type(secondNumber)})')
print(f'Valor Booleano {bollean} (Tipo: {type(bollean)})')


print("="*30)

bill: dict[str, float] = {
    "apple": 3.14,
    "watermelon": 15.92,
    "pineapple": 6.53,
}
completed: tuple[str] = ("DONE",)
succeeded: tuple[int, str] = (1, "SUCCESS")
statuses: tuple[str, ...] = (
    "DONE", "SUCCESS", "FAILED", "ERROR",
)
codes: list[int] = (0, 1, -1, -2)

print(bill)
print(completed)
print(succeeded)
print(statuses)