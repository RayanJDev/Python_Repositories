class Conta:
    def __init__(self,nome,cpf,numero_da_conta,saldo):
        self.__nome = nome
        self.__cpf = cpf
        self.__numero_da_conta = numero_da_conta
        self.__saldo = saldo
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_numero_da_conta(self):
        return self.__numero_da_conta
    def get_saldo(self):
        return self.__saldo
    def depositar(self,valor_depositado):
         self.__saldo += valor_depositado
    def sacar(self,valor_sacado):
            if valor_sacado > self.__saldo:
                print("Valor maior que o saldo disponível!")
            else:
                self.__saldo-= valor_sacado


conta = Conta("Assis Barreiros","123.654.123-11","123.456",1500)
print(f'Olá {conta.get_nome()}, detentor do CPF {conta.get_cpf()}\n'
      f'O numero da sua conta é {conta.get_numero_da_conta()} e seu saldo atual é R$ {conta.get_saldo()}\n')
print("_"*30)
print(f'Sistema atualizado seu saldo atual é {conta.get_saldo()}')
print("_"*30)
conta.sacar(300)
print(f'Conta após saque:\n'
      f'Seu saldo é {conta.get_saldo()}')
conta.sacar(1100)
print(f'Seu saldo é {conta.get_saldo()}')
#conta.depositar(200)
#print(f'Seu saldo é {conta.get_saldo()}')

print("="*30)

"""
class Televisao:
    def __init__(self, canal, canal_minimo, canal_maximo):
        self.canal = canal
        self.canal_minimo = canal_minimo
        self.canal_maximo = canal_maximo

    def ultimo_canal(self):
        self.canal += 1
        if self.canal + 1 >= 10:
            self.canal = self.canal_minimo

    def primeiro_canal(self):
        self.canal -= 1
        if self.canal - 1 <= 0:
            self.canal = self.canal_maximo


tv1 = Televisao(3, 1, 10)
for canais in range(1,15):
    tv1.ultimo_canal()
    print(f'Trocando para o canal {tv1.canal}')

print("="*30)

tv2 = Televisao(8, 1, 10)
for canais in range(1,15):
    tv2.primeiro_canal()
    print(f'Trocando para o canal {tv2.canal}')
"""