def listar_produtos():
    print("LISTA DE PRODUTOS\n"
          "* Arroz - 29,90\n"
          "* Feijão - 17,40\n"
          "* Açúcar - 24,50\n"
          "* Café - 54,60\n"
          "* Biscoito - 6,90\n"
          "* Sabonete - 10,99\n"
          "* Talher Descartável - 2,99\n")

def selecionar_produtos():
    lista: dict[str, float] = {
        "arroz": 29.90,
        "feijão": 17.40,
        "açúcar": 24.50,
        "café": 54.60,
        "biscoito": 6.90,
        "sabonete": 10.99,
        "talher descartável": 2.99
    }

    produtos_escolhidos = []

    while True:
        escolhendo_produto = input("Digite o nome do produto (ou 'sair' para finalizar): ").lower()
        if escolhendo_produto == "sair":
            break
        if escolhendo_produto in lista:
            # Se ainda estiver a escolher produtos dentro de lista
            # será adicionado +1 >>>('append') produto_escolhido do ‘input’ escolhendo_produto
            produtos_escolhidos.append(escolhendo_produto)
        else:
            print("Produto não encontrado. Tente novamente.")
    # Imprimo e retorno o valor da lista e dos produtos_escolhidos
    print(f"\nProdutos selecionados: {produtos_escolhidos}\n")
    return produtos_escolhidos, lista

def calcular_total(produtos, lista_precos):
    total = 0
    for produto in produtos:
        quantidade = int(input(f"Digite a quantidade de '{produto}': "))
        total += lista_precos[produto] * quantidade
    return total

# Execução do programa
listar_produtos()
produtos, lista_precos = selecionar_produtos()
valor_total = calcular_total(produtos, lista_precos)

print(f"\nValor total da compra: R$ {valor_total:.2f}")