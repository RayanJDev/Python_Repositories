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
    lista: dict[str,float] = {
          "arroz" : 29.90,
          "feijão" : 17.40,
          "açúcar" : 24.50,
          "café" : 54.60,
          "biscoito" : 6.90,
          "sabonete" : 10.99,
          "talher descartável": 2.99}
    #Aqui se cria um Array vazio para um lista vazia
    produtos_escolhidos = []
    # Utilizo o while para que ENQUANTO não digitar "sair" eu posso #
    # continuar a adicionar produtos na lista
    while True:
        produto_selecionado = input("Digite o nome do produto (ou 'sair' para finalizar): ").lower()
        if produto_selecionado == "sair":
            break
        # O metodo append() ajuda a adicionar mais ‘item’ #
        # a lista ENQUANTO a condição for VERDADEIRA
        if produto_selecionado in lista:
            produtos_escolhidos.append(produto_selecionado)
        else:
            print("Produto invalido")
    # Imprimo a lista inserida no input
    print(f'Produtos selecionados:\n {produtos_escolhidos}\n')
    return produtos_escolhidos, lista

def calcular_produtos(produtos,lista_precos):
    total_produtos = 0
    for produto in produtos:
        quantidade = int(input(f"Digite a quantidade de '{produto}' :"))
        total_produtos += lista_precos[produto] * quantidade
    return total_produtos

#Executa o programa
listar_produtos()
produtos, lista_precos = selecionar_produtos()
valor_total = calcular_produtos(produtos,lista_precos)

print(f'Valor total: {valor_total:.2f}\n')

