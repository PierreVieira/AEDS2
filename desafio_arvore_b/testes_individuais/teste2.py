from desafio_arvore_b.tree_b.arvore_b import *
from desafio_arvore_b.testes_individuais.funcoes_uteis_de_teste import *
arvore_b = Arvore_b(Page(4, construir_lista_nos(1, 3, 4, 7)))
pesquisar_elemento(arvore_b, 3)
arvore_b.inserir_elemento(8)
pesquisar_elemento(arvore_b, 8)