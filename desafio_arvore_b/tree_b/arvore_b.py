from math import inf

from desafio_arvore_b.tree_b.celula import Celula
from desafio_arvore_b.tree_b.pagina import Page


class Arvore_b:
    def __init__(self, quantidade_maxima_de_celulas_por_pagina, valor_raiz):
        pagina_raiz = Page(quantidade_maxima_de_celulas_por_pagina)
        pagina_raiz.inserir_celula(Celula(valor_raiz))
        self.raiz = pagina_raiz

    def inserir_elemento(self, valor, page: Page = None):
        if page is None:
            page = self.raiz
        for celula in page:
            if (valor < celula) and (celula != -inf):
                if celula.ponteiro.celula_baixo:
                    return self.inserir_elemento(valor, celula.ponteiro.celula_baixo)
            if valor == celula:  # Se o valor já está na célula
                return None  # Saia da função de inserção
        # Se o código chegou aqui, quer dizer que o valor é maior que todas as céluas da página recorrente
        if page[-1].ponteiro.celula_baixo:
            return self.inserir_elemento(valor, page[-1].ponteiro.celula_baixo)
        try:
            page.inserir_celula(Celula(valor))
        except MemoryError:
            self.inserir_nova_pagina(page)

    def inserir_nova_pagina(self, pagina_a_dividir):
        pass
