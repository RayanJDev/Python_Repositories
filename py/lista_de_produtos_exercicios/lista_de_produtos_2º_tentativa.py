from time import sleep

def escolher_servicos_do_cliente():
    servicos: dict[str, float] ={
        "musculação": 89.90,
        "pilates": 49.50,
        "jump": 51.70
    }
    print("OLÁ! ADICIONE OS SERVIÇOS DE PREFERÊNCIA AO SEU PLANO:")
    servicos_escolhido = []
    while True:
        print()
        escolha_do_cliente = input("Escolha o serviços de sua preferência: ").lower()
        print("-"*40)
        if escolha_do_cliente == "sair":
            break
        if escolha_do_cliente in servicos:
            servicos_escolhido.append(escolha_do_cliente)
        else:
            print("SERVIÇO INVALIDO|TENTE NOVAMENTE")
            for i in range (3):
                print('.',end='')
                sleep(2.0)

    return servicos_escolhido,servicos
###################################################################
print("BEM VINDO(A) A ACADEMIA R.FITNESS")
print("-"*40)
print("Serviços disponíveis:\n"
      "* Musculação: R$89,90\n"
      "* Pilates: R$49,50\n"
      "* Jump: R$51,70")
print("-"*40)
###################################################################
lista_de_escolha, valor_servicos = escolher_servicos_do_cliente()
valor_do_plano = 0
for valor in lista_de_escolha:
        valor_do_plano += valor_servicos[valor]
print(f'O valor total do seu plano é: {valor_do_plano:.2f}')