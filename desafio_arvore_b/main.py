"""
Autor: Pierre Vieira
Github: https://github.com/PierreVieira/LAEDS_II/tree/master/desafio_arvore_b
"""
from random import sample

from desafio_arvore_b.tree_b.arvore_b import Tree_b


def teste_de_insercao(qtde_maxima_elementos_por_pagina, raiz, valores):
    arvore_b = Tree_b(qtde_maxima_elementos_por_pagina, raiz)
    for value in valores:
        arvore_b.insert(value)
    return arvore_b


def mensagem_de_busca(arvore: Tree_b, value):
    if arvore.find(value):
        print(f'O valor {value} foi encontrado na árvore.')
    else:
        print(f'O valor {value} não foi encontrado na árvore.')


def teste_de_busca(arvore, valores_a_serem_pesquisados):
    for value in valores_a_serem_pesquisados:
        mensagem_de_busca(arvore, value)


arvore1 = teste_de_insercao(4, 11, [8, 11, 27, 31, 25, 16, 59, 53, 52, 21, 36, 48, 78, 81, 75, 95, 90, 91, 72, 63, 20, 35])
print(arvore1.conteudo())
print('\n\n')
arvore2 = teste_de_insercao(4, 20, [20, 10, 40, 50, 30, 55, 3, 11, 4, 28, 36, 33, 52, 17, 25, 13, 45, 9, 43, 8, 48])
print(arvore2.conteudo())
