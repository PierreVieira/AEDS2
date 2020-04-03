from desafio_arvore_b.tree_b.celula import Celula
from desafio_arvore_b.tree_b.pagina import Page


class Arvore_b:
    def __init__(self, quantidade_maxima_de_celulas_por_pagina, valor_raiz):
        pagina_raiz = Page(quantidade_maxima_de_celulas_por_pagina)
        pagina_raiz.inserir_celula(Celula(valor_raiz))
        self.raiz = pagina_raiz

