from desafio_arvore_b.tree_b.arvore_b import Node


def construir_lista_nos(*args):
    return list(Node(i) for i in args)


def pesquisar_elemento(arvore_b, elemento):
    if arvore_b.elemento_na_arvore(elemento):
        print(f'O elemento {elemento} está na árvore.')
    else:
        print(f'O elemento {elemento} não está na árvore.')
