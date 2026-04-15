"""
r: leitura do arquivo de texto
w: escrita(sobrescreve o conteúdo do arquivo de texto)
a: adiciona/anexa ao final do arquivo
r+: leitura e escrita
"""
import re
from collections import  Counter

def procurar_letra(arquivo):
    with open(arquivo,'r',enconding='utf-8'):
        
