from desafio_arvore_b.tree_b.arvore_b import Tree_b


def teste1():
    arvore_b = Tree_b(11, 4)
    arvore_b.insert(53)
    arvore_b.insert(36)
    arvore_b.insert(95)
    arvore_b.insert(8)
    pass


def teste2():
    arvore_b = Tree_b(11, 4)
    for n in [8, 11, 27, 31, 25, 16, 48]:
        arvore_b.insert(n)
    pass


# teste1()
teste2()
