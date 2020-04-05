"""
Autor: Pierre Vieira
Github: https://github.com/PierreVieira/LAEDS_II/tree/master/desafio_arvore_b
"""

from desafio_arvore_b.tree_b.arvore_b import Tree_b
from desafio_arvore_b.tree_b.no import Node
from desafio_arvore_b.tree_b.pagina import Page


def teste_de_insercao1():
    arvore_b = Tree_b(11, 4)
    arvore_b.insert(53)
    arvore_b.insert(36)
    arvore_b.insert(95)
    arvore_b.insert(8)
    pass


def teste_de_insercao2():
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


def teste_de_insercao3():
    faz_no = lambda value: Node(value)
    lista_raiz = list(map(faz_no, [25, 52, 75, 90]))
    pagina_raiz = Page(4)
    pagina_raiz.lista_elementos = lista_raiz
    arvore = Tree_b(4, pagina_da_raiz=pagina_raiz)
    lista_pagina1 = list(map(faz_no, [8, 11, 16, 21]))
    lista_pagina2 = list(map(faz_no, [27, 31, 36, 48]))
    lista_pagina3 = list(map(faz_no, [53, 59, 63, 72]))
    lista_pagina4 = list(map(faz_no, [78, 81]))
    lista_pagina5 = list(map(faz_no, [91, 95]))
    pagina1, pagina2, pagina3, pagina4, pagina5 = Page(4), Page(4), Page(4), Page(4), Page(4)
    pagina1.lista_elementos = lista_pagina1
    pagina2.lista_elementos = lista_pagina2
    pagina3.lista_elementos = lista_pagina3
    pagina4.lista_elementos = lista_pagina4
    pagina5.lista_elementos = lista_pagina5
    arvore.root[0].left = pagina1
    arvore.root[1].left = pagina2
    arvore.root[2].left = pagina3
    arvore.root[3].left = pagina4
    arvore.root[3].right = pagina5
    arvore.root._atualizar_referencias()
    arvore.insert(20)
    arvore.insert(35)
    pass

# teste_de_insercao1()
arvore = teste_de_insercao2()
teste_de_insercao3()