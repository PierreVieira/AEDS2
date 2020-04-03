from math import inf

from desafio_arvore_b.tree_b.celula import Celula
from desafio_arvore_b.tree_b.pagina import Page


class Arvore_b:
    def __init__(self, quantidade_maxima_de_celulas_por_pagina, valor_raiz):
        """
        :param quantidade_maxima_de_celulas_por_pagina: A árvore deve saber a quantidade máxima de células presente em
        cada página
        :param valor_raiz: página presenta na raiz
        """
        self._quantidade_maxima_de_celulas_por_pagina = quantidade_maxima_de_celulas_por_pagina
        pagina_raiz = Page(self._quantidade_maxima_de_celulas_por_pagina)
        pagina_raiz.inserir_celula(Celula(valor_raiz))
        self.raiz = pagina_raiz

    def inserir_elemento(self, valor, page: Page = None):
        """
        :param valor: valor a ser inserido na árvore
        :param page: página recorrente
        :return: None
        """
        if page is None:  # Se estamos fazendo a primeira chamada da função
            page = self.raiz  # A página vira a raiz
        for celula in page:  # Para cada célula na página
            if (valor < celula) and (celula != -inf):  # Se o valor que estou passando como parâmetro é menor que a
                # célula recorrente
                if celula.ponteiro.celula_baixo:  # Se há página embaixo
                    return self.inserir_elemento(valor, celula.ponteiro.celula_baixo)  # Faça uma chamada recursiva
                    # da função passando a página de baixo
            if valor == celula:  # Se o valor já está na célula
                return None  # Saia da função de inserção
        # Se o código chegou aqui, quer dizer que o valor é maior que todas as céluas da página recorrente
        if page[-1].ponteiro.celula_baixo:  # Se há página no último ponteiro da célula
            return self.inserir_elemento(valor, page[-1].ponteiro.celula_baixo)  # Faça uma chamada recursiva da
            # função passando a página que está embaixo do último ponteiro da célula
        try:  # Tente
            page.inserir_celula(Celula(valor))  # Inserir uma célula na página recorrente
        except MemoryError:  # Exceto se ela já estiver cheia
            self._inserir_nova_pagina(valor, page)  # Crie uma nova página

    def _dividir_pagina(self, pagina_a_dividir: Page):
        """
        Divide a página passada como parâmetro
        :param pagina_a_dividir: Página que será dividida
        :return: 2 páginas, uma contendo os valores menores e a outra contendo os valores maiores
        """
        valores_menores = pagina_a_dividir[:len(pagina_a_dividir) // 2]  # Os valores menores pega metade da página
        for c in range(self._quantidade_maxima_de_celulas_por_pagina - len(valores_menores)):
            valores_menores.append(Celula(-inf))
        valores_menores.append(Celula(inf))
        valores_maiores = pagina_a_dividir[len(pagina_a_dividir) // 2:]
        for c in range(self._quantidade_maxima_de_celulas_por_pagina - len(valores_maiores) + 1):
            valores_maiores.append(Celula(-inf))
        valores_menores.sort()
        valores_maiores.sort()
        pagina_valores_menores, pagina_valores_maiores = Page(self._quantidade_maxima_de_celulas_por_pagina), Page(
            self._quantidade_maxima_de_celulas_por_pagina)
        pagina_valores_menores.lista_celulas, pagina_valores_maiores.lista_celulas = valores_menores, valores_maiores
        return pagina_valores_menores, pagina_valores_maiores

    def _inserir_nova_pagina(self, valor, pagina_a_dividir: Page):
        """
        :param valor: valor a ser inserido na árvore
        :param pagina_a_dividir: página que está cheia e que será divida
        :return: None
        """
        pagina_valores_menores, pagina_valores_maiores = self._dividir_pagina(pagina_a_dividir)
        if valor < pagina_valores_maiores.menor_valor:
            celula_que_vai_pra_cima = pagina_valores_menores.pop(
                pagina_valores_menores.index(pagina_valores_menores.maior_valor))
            pagina_valores_menores.inserir_celula(Celula(valor))
        else:
            celula_que_vai_pra_cima = pagina_valores_maiores.pop(
                pagina_valores_maiores.index(pagina_valores_maiores.maior_valor))
            pagina_valores_maiores.inserir_celula(Celula(valor))
        if not pagina_a_dividir.tem_pagina_acima:
            self.raiz = self._criar_nova_pagina_com_um_elemento(celula_que_vai_pra_cima, pagina_valores_menores,
                                                                pagina_valores_maiores)
        else:
            for celula in pagina_a_dividir:
                if celula.ponteiro.celula_cima:
                    try:
                        celula.ponteiro.celula_cima.my_page.inserir_celula_e_atualizar_ref_com_novas_paginas(celula_que_vai_pra_cima, pagina_valores_menores, pagina_valores_maiores)
                        break
                    except MemoryError:
                        pass # Arrumar aqui

    def _criar_nova_pagina_com_um_elemento(self, celula_que_vai_pra_cima, pagina_valores_menores,
                                           pagina_valores_maiores):
        pagina_nova = Page(self._quantidade_maxima_de_celulas_por_pagina)
        celula_que_vai_pra_cima.ponteiro.celula_baixo = pagina_valores_menores
        pagina_nova.inserir_celula(celula_que_vai_pra_cima)
        pagina_nova[-1].ponteiro.celula_baixo = pagina_valores_maiores
        return pagina_nova
