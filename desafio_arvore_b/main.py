"""
Autor: Pierre Vieira
Github: https://github.com/PierreVieira/LAEDS_II/tree/master/desafio_arvore_b
"""

from desafio_arvore_b.tree_b.arvore_b import Tree_b


def teste_de_insercao():
    arvore_b = Tree_b(4, 11)
    for value in [8, 11, 27, 31, 25, 16, 59, 53, 52, 21, 36, 48, 78, 81, 75, 95, 90, 91, 72, 63, 20, 35]:
        arvore_b.insert(value)
    return arvore_b


def mensagem_de_busca(arvore: Tree_b, value):
    if arvore.find(value):
        print(f'O valor {value} foi encontrado na árvore.')
    else:
        print(f'O valor {value} não foi encontrado na árvore.')


def teste_de_busca(arvore):
    for value in [8, 11, 27, 31, 25, 16, 59, 53, 52, 21, 36, 48, 78, 81, 75, 95, 90, 91, 72, 63, 20, 35]:
        mensagem_de_busca(arvore, value)
    mensagem_de_busca(arvore, 3)
    mensagem_de_busca(arvore, 88)


arvore = teste_de_insercao()
# print(arvore.conteudo)
