"""
r: leitura do arquivo de texto
w: escrita(sobrescreve o conteúdo do arquivo de texto)
a: adiciona/anexa ao final do arquivo
r+: leitura e escrita
"""
import re

arquivo = "arquivo.txt"

def ler_arquivo(arqu):
    with open(arqu,'r',encoding='utf-8') as file:
        return file.read() 

def digitar_letra():
    letra = input("Digite a letra que procura: ").strip()

    if len(letra) != 1 or not letra.isalpha():
        print("Digite apenas uma letra!")
        return None
    return letra

def buscar_primeira_letra(texto, letra):
    padrao = rf"\b{re.escape(letra)}\w*"
    return re.findall(padrao,texto,re.IGNORECASE)

def main():
    texto = ler_arquivo(arquivo)
    letra = digitar_letra()

    if letra is None:
        return

    nomes_encontrados = buscar_primeira_letra(texto, letra)

    print(f'\nNomes encontrados com a letra {letra}: ')
    for nome in nomes_encontrados:
        print(nome)

    print(f'Quantidade encontrada: {len(nomes_encontrados)}')

if __name__ == "__main__":
    main()
