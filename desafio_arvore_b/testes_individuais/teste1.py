from desafio_arvore_b.tree_b.arvore_b import *
from desafio_arvore_b.testes_individuais.funcoes_uteis_de_teste import *
from desafio_arvore_b.tree_b.page import Page

pagina = Page_b(lista_nos=construir_lista_nos(29))
pagina.lista_nos[0].left = Page(4, lista_nos=construir_lista_nos(8, 15))
pagina.lista_nos[0].right = Page(4, lista_nos=construir_lista_nos(37, 45, 60))
pagina.lista_nos[0].left.lista_nos[0].left = Page(4, lista_nos=construir_lista_nos(1, 3, 4, 7))
pagina.lista_nos[0].left.lista_nos[1].left = Page(4, lista_nos=construir_lista_nos(10, 12, 13, 14))
pagina.lista_nos[0].left.lista_nos[1].right = Page(4, lista_nos=construir_lista_nos(18, 20, 25))
pagina.lista_nos[0].right.lista_nos[0].left = Page(4, lista_nos=construir_lista_nos(30, 36))
pagina.lista_nos[0].right.lista_nos[1].left = Page(4, lista_nos=construir_lista_nos(40, 41, 42, 43))
pagina.lista_nos[0].right.lista_nos[2].left = Page(4, lista_nos=construir_lista_nos(51, 52))
pagina.lista_nos[0].right.lista_nos[2].right = Page(4, lista_nos=construir_lista_nos(70, 77, 83))
arvore_b = Arvore_b(pagina)
pesquisar_elemento(arvore_b, 10)
pesquisar_elemento(arvore_b, 36)
pesquisar_elemento(arvore_b, 41)
arvore_b.inserir_elemento(11)
pesquisar_elemento(arvore_b, 11)
pesquisar_elemento(arvore_b, 12)