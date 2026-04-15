"""
r: leitura do arquivo de texto
w: escrita(sobrescreve o conteúdo do arquivo de texto)
a: adiciona/anexa ao final do arquivo
r+: leitura e escrita
"""
import re
from collections import  Counter

#with open('arquivo.txt',"r",encoding= "utf-8") as arquivo:
    #linhas = arquivo.readlines()
    #procura_sobrenome = str(input("Digite o sobrenome que procura: \n"))
    #for linha in linhas:
    #    print(linha)
    #for linha in linhas:
    #    sobrenome = linha.strip()
    #    if sobrenome == procura_sobrenome:
    #        contador_de_sobrenome = contador_de_sobrenome + 1
    #        print(f'O sobrenome {procura_sobrenome} foi encontrado {contador_de_sobrenome} vezes!!!')
    #    else:
    #        print(f'\nO sobrenome {procura_sobrenome} não foi encontrado!!')
    #        break


def imprimir_arquivo(arquivo):
    with open(arquivo,'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(linha)


def contar_sobrenome_eficiente(arquivo, sobrenome):
    with open(arquivo, 'r', encoding='utf-8') as f:
        # Lê o arquivo, converte p/ minúsculo e acha todas as palavras
        palavras = re.findall(r'\b\w+\b', f.read().lower(), re.IGNORECASE)
    # Cria o contador
    contagem = Counter(palavras)
    return contagem.get(sobrenome.lower(), 0)
resultado = contar_sobrenome_eficiente("arquivo.txt","GROTT")
imprimir_arquivo('arquivo.txt')
print(f'\nO sobrenome aparece {resultado}x')