from desafio_arvore_b.tree_b.no import Node
from desafio_arvore_b.tree_b.pagina import Page


class Tree_b:
    def __init__(self, root, maximo_elementos_pagina):
        pagina_da_raiz = Page(maximo_elementos_pagina)
        pagina_da_raiz.inserir_elemento(Node(root))
        self.root = pagina_da_raiz

    def insert(self, value):
        """
        A árvore não admite valores repetidos, portanto se value já estiver na árvore o mesmo será ignorado.
        :param value: valor a ser inserido na árvore.
        :return: None
        """
        self._insert_recursive(Node(value), self.root)  # Faz uma inserção recursiva do nó

    def _insert_recursive(self, node: Node, page: Page):
        """
        :param node: nó a ser inserido na árvore e, consequentemente, em uma página
        :param page: página recorrente
        :return: None
        """
        for no_pagina in page:  # Para cada nó na página recorrente
            if node < no_pagina:  # Se o nó a ser inserido é menor que o nó recorrente
                if no_pagina.left:  # Se tem página à esquerda
                    return self._decida_oq_fazer_se_tiver_referencia_a_esquerda_na_insercao_recursiva(no_pagina, node, page)
                break  # Se não referência para a esquerda, saia do laço
            elif no_pagina == node:  # Se o nó recorrente é igual o nó a ser inserido
                return None  # Saia da função (elemento já está na árvore)
        if node > page[-1]:  # Se o nó é maior que o último elemento da página
            if page[-1].right:  # Se tem página à direita
                return self._insert_recursive(node, page[-1].right)  # Desça pela página da direita
        return self._insercao_definida(node, page)  # Faça uma inserção do nó na página definida

    def _decida_oq_fazer_se_tiver_referencia_a_esquerda_na_insercao_recursiva(self, no_pagina: Node, node: Node,
                                                                              page: Page):
        """
        Essa função é chamada dentro do for da insert_recursive. Essa situação ocorre em uma determinada situação em que
        existe referência para o nó à esquerda do nó que está sendo percorrido pelo for (no_pagina) da referida função
        :param no_pagina: nó que está sendo percorrido por um for
        :param node: nó que será inserido na árvore
        :param page: página recorrente da função recursiva insert_recursive
        :return: None
        """
        if no_pagina.left.pode_inserir_elemento(node):  # Se pode inserir elemento na esquerda
            return self._insert_recursive(node, no_pagina.left)  # Faça uma chamada recursiva passando a
            # página da esquerda
        else:  # Se não pode inserir na esquerda
            if no_pagina.right is None:  # Se não tem página à direita
                nova_pagina = Page(page.maximo_elementos)  # Crie uma nova página
                no_pagina.right = nova_pagina  # Associe o apontador direito à nova página criada
            elif node < no_pagina:  # Se o nó é menor que o nó da página recorrente
                return None  # Retorne None (o nó não deve ser inserido na árvore)
            return self._insert_recursive(node, no_pagina.right)  # Insira na página à direita

    def _insercao_definida(self, node: Node, page: Page):
        """
        Após a inserção recursiva já ter sido executada, esse método irá finalmente inserir o nó na árvore
        :param node: nó que será inserido
        :param page: página em que irá ocorrer a inserção
        :return: None
        """
        try:  # Tente
            page.inserir_elemento(node)  # Inserir o nó na página recorrente
        except MemoryError:  # Exceto se ela já estiver cheia
            self._new_page(node, page)  # Crie uma nova página para a àrvore

    def _new_page(self, node: Node, page_to_division: Page):
        """
        :param node: nó a ser inserido na árvore e, consequentemente, em uma nova página
        :param page_to_division: página que irá ser dividida
        :return: None
        """
        pagina_valores_minimos, pagina_valores_maximos = self._dividir_pagina(page_to_division)  # Pega as duas páginas
        if node < pagina_valores_maximos[0]:  # Se o nó é menor que o primeiro elemento da página com os maiores valores
            pagina_valores_minimos.inserir_elemento(node)  # O nó que iria ser inserido é inserido junto aos menores
            no_q_vai_subir = pagina_valores_minimos.pop()  # O nó que vai subir é o último nó dos valores mínimos
        else:  # Senão (se ele é maior)
            pagina_valores_maximos.inserir_elemento(node)  # O nó que iria ser inserido é inserido junto aos maiores
            no_q_vai_subir = pagina_valores_maximos.pop(0)  # O nó que vai subir é o primeiro nó dos valores máximos
        if page_to_division.apontada_por is None:  # Se a página não estiver sendo apontada por nenhum nó
            self._change_root(no_q_vai_subir, pagina_valores_minimos, pagina_valores_maximos)  # Mude a raíz da árvore
        else:  # Senão
            no_q_vai_subir.left = pagina_valores_minimos  # O apontador esquerdo nó que sobe aponta para a página de
            # valores mínimos
            page_to_division.apontada_por.my_page.inserir_elemento(no_q_vai_subir)  # A página que apontava para a
            # página dividia tem como um dos seues elementos o nó que sobe
            page_to_division.apontada_por.my_page.alocar_pagina(pagina_valores_maximos)  # A página que apontava para
            # a página dividida tem a responsabilidade de fazer com que um nó aponte para a página de valores maiores

    def _dividir_pagina(self, page) -> (Page, Page):
        """
        :param page: página que será dividia
        :return: página com os valores menores e uma outra página com os valores maiores
        """
        valores_minimos, valores_maximos = page[:len(page) // 2], page[len(page) // 2:]
        pagina_valores_minimos, pagina_valores_maximos = Page(page.maximo_elementos), Page(page.maximo_elementos)
        pagina_valores_minimos.lista_elementos, pagina_valores_maximos.lista_elementos = valores_minimos, valores_maximos
        return pagina_valores_minimos, pagina_valores_maximos

    def _change_root(self, node: Node, pagina_valores_minimos: Page, pagia_valores_maximos: Page):
        """
        :param node: nó que irá ser o único elemento da raíz (pelo menos até esse momento)
        :param pagina_valores_minimos: página com os valores mínimos da operação anterior
        :param pagia_valores_maximos: página com os valores máximos da operação anterior
        :return: None
        """
        nova_raiz_valor = node  # O novo nó da raiz pega o nó passado como parâmetro
        nova_raiz_valor.left, nova_raiz_valor.right = pagina_valores_minimos, pagia_valores_maximos  # Atualiza os
        # ponteiros direito e esquerdo do nó que estará na página raiz
        nova_pagina_raiz = Page(pagia_valores_maximos.maximo_elementos)
        nova_pagina_raiz.inserir_elemento(nova_raiz_valor)  # A nova página raiz insere o nó raiz
        self.root = nova_pagina_raiz  # Muda a raíz da árvore atual
