"""
Autor: Pierre Vieira
Github: https://github.com/PierreVieira/LAEDS_II/tree/master/desafio_arvore_b
"""
from typing import List

from desafio_arvore_b.tree_b.no import Node
from desafio_arvore_b.tree_b.pagina import Page


class Tree_b:
    def __init__(self, maximo_elementos_pagina, root=None, pagina_da_raiz: Page = None):
        if pagina_da_raiz is None:
            pagina_da_raiz = Page(maximo_elementos_pagina, 1)
        if root is not None:
            pagina_da_raiz.inserir_elemento(Node(root))
        self.root = pagina_da_raiz

    def insert(self, value):
        """
        A árvore não admite valores repetidos, portanto se value já estiver na árvore o mesmo será ignorado.
        :param value: valor a ser inserido na árvore.
        :return: None
        """
        self._insert_recursive(Node(value), self.root)  # Faz uma inserção recursiva do nó

    def find(self, valor):
        """
        :param valor: valor a ser pesquisado na árvore.
        :return: True se o valor procurado está na árvore. False se o valor procurado não está na árvore.
        """
        return self._find(Node(valor), self.root)

    def qtde_niveis(self):
        """
        :return: Quantidade de níveis presentes na árvore
        """
        return self._qtde_niveis(self.root[0], 1)

    def _qtde_niveis(self, node: Node, cont: int):
        """
        :param node: nó recorrente
        :param cont: contador de níveis
        :return: quantidade de níveis da árvore
        """
        if node.left:
            return self._qtde_niveis(node.left[0], cont + 1)
        return cont

    def _find(self, no_a_procurar: Node, pagina_recorrente: Page):
        """
        :param no_a_procurar: nó a ser pesquisado na árvore.
        :return: True se o nó procurado está na árvore. False se o nó procurado não está na árvore.
        """
        if pagina_recorrente.encontrou(no_a_procurar):  # Se a página tem o nó que estou procurando
            return True  # Retorne verdadeiro (elemento encontrado)
        for no_recorrente in pagina_recorrente:  # Para cada nó na página recorrente
            if no_a_procurar < no_recorrente:  # Se o nó que estou procurando é menor que o nó recorrente
                if no_recorrente.left:  # Se o nó recorrente possui apontador à esquerda
                    return self._find(no_a_procurar, no_recorrente.left)  # Desça pela esquerda
        if no_a_procurar > pagina_recorrente[-1]:  # Se o nó que estou pesquisando é maior que o último nó da página
            if pagina_recorrente[-1].right:  # Se o último nó da direita tem apontador à direita
                return self._find(no_a_procurar, pagina_recorrente[-1].right)  # Desça pela direita
        return False  # Retorne falso  (elemento não encontrado)

    def _insert_recursive(self, node: Node, page: Page):
        """
        :param node: nó a ser inserido na árvore e, consequentemente, em uma página
        :param page: página recorrente
        :return: None
        """
        for no_pagina in page:  # Para cada nó na página recorrente
            if node < no_pagina:  # Se o nó a ser inserido é menor que o nó recorrente
                if no_pagina.left:  # Se tem página à esquerda
                    return self._decida_oq_fazer_se_tiver_referencia_a_esquerda_na_insercao_recursiva(no_pagina, node,
                                                                                                      page)
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
                nova_pagina = Page(page.maximo_elementos, no_pagina.my_page.nivel + 1)  # Crie uma nova página
                no_pagina.right = nova_pagina  # Associe o apontador direito à nova página criada
            elif node < no_pagina:  # Se o nó é menor que o nó da página recorrente
                if no_pagina.left.encontrou(node):  # Se a página da esquerda já tem o nó
                    return None  # Retorne None (o nó não deve ser inserido na árvore)
                return self._insert_recursive(node, no_pagina.left)  # Desça pela esquerda
            return self._insert_recursive(node, no_pagina.right)  # Desça pela direita

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
            try:  # Tente
                page_to_division.apontada_por.my_page.inserir_elemento(no_q_vai_subir)  # A página que apontava para
                # a página dividia tem como um dos seues elementos o nó que sobe
            except MemoryError:  # Exceto se a página estiver cheia
                self._new_page(no_q_vai_subir, page_to_division.apontada_por.my_page)  # Crie uma nova página
                no_q_vai_subir.right = None
            finally:
                page_to_division.apontada_por.my_page.alocar_pagina(pagina_valores_maximos)  # A página que apontava
                # para a página dividida tem a responsabilidade de fazer com que um nó aponte para a página de
                # valores maiores

    def _dividir_pagina(self, page) -> (Page, Page):
        """
        :param page: página que será dividia
        :return: página com os valores menores e uma outra página com os valores maiores
        """
        valores_minimos, valores_maximos = page[:len(page) // 2], page[len(page) // 2:]  # Faz um slice na página
        pagina_valores_minimos, pagina_valores_maximos = Page(page.maximo_elementos, page.nivel + 1), Page(
            page.maximo_elementos, page.nivel + 1)
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
        nova_pagina_raiz = Page(pagia_valores_maximos.maximo_elementos, nivel=1)
        nova_pagina_raiz.inserir_elemento(nova_raiz_valor)  # A nova página raiz insere o nó raiz
        self.root = nova_pagina_raiz  # Muda a raíz da árvore atual

    @property
    def conteudo(self):
        """
        :return: Todo o conteúdo da árvore por nível string
        """
        niveis = self._lista_niveis()  # Recebe uma lista contendo as páginas separadas por nível
        string_retorno = ''
        for i in range(len(niveis)):
            string_retorno += str(niveis[i])[1:-1].replace(',', '').center(len(str(niveis[-1])))+'\n'
        return string_retorno[:-1]  # Ignora o último \n no final

    def _lista_niveis(self):
        """
        :return: Todo o conteúdo da árvore por nível em formato de lista
        """
        quantidade_de_niveis = self.qtde_niveis()  # Descobre a quantidade total de níveis da árvore
        lista_niveis = [[] for i in range(quantidade_de_niveis)]
        for i in range(0, quantidade_de_niveis):
            lista_niveis[i].extend(self.paginas_do_nivel(i + 1))
        return lista_niveis

    def paginas_do_nivel(self, nivel_de_interesse):
        """
        :param nivel_de_interesse: nível em que estamos pesquisando
        :return: Lista de todas as páginas que estão no nível passado como parâmetro
        """
        return self._paginas_do_nivel(nivel_de_interesse, self.root)

    def _paginas_do_nivel(self, nivel_de_interesse: int, pagina: Page) -> List:
        """
        :param nivel_de_interesse: nível em que estamos pesquisando
        :param pagina: página de recorrência
        :return: Lista de todas as páginas que estão no nível passado como parâmetro
        :raise: KeyError quando o nível informado pelo usuário não está presente em nenhuma página da árvore
        """
        if pagina.nivel != nivel_de_interesse:  # Se o nível da página atual é diferente do nível de interesse
            if pagina[0].left:  # Se o primeiro nó da página aponta para uma página à esquerda
                return self._paginas_do_nivel(nivel_de_interesse, pagina[0].left)  # Desça pela esquerda
            else:  # Se não há
                raise KeyError('Não há uma página chave para os valores com o nível especificado')  # KeyError
        else:  # Encontramos a página com o nível de interesse
            return self._todas_as_paginas_irmas(pagina)  # Retorne todas as páginas do nível requisitado

    def _todas_as_paginas_irmas(self, pagina: Page) -> List:
        """
        :param pagina: página que irá ser feita o início da pesquisa
        :return: todas as páginas irmãs desse nível
        """
        lista_de_retorno = []  # A lista de retorno começa vazia
        while True:  # Loop "infinito"
            lista_de_retorno.append(pagina)  # A lista de retorno armazena a página
            if pagina.brother_right:  # Se essa página tiver uma irmã à direita
                pagina = pagina.brother_right  # Ande pela direita
            else:  # Se não
                return lista_de_retorno  # Retorne a lista de retorno
