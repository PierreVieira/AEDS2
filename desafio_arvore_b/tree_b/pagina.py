"""
Autor: Pierre Vieira
Github: https://github.com/PierreVieira/LAEDS_II/tree/master/desafio_arvore_b
"""

from typing import List

from desafio_arvore_b.tree_b.no import Node


class Page:
    def __init__(self, maximo_elementos, apontada_por: Node = None):
        self.maximo_elementos = maximo_elementos
        self._lista_elementos: List = []
        self.apontada_por = apontada_por
        self._brother_right = None  # Página irmã à direita
        self._brother_left = None  # Página irmã à esquerda

    def inserir_elemento(self, no: Node):
        """
        :param no: nó a ser inserido na página
        :return: None
        :raise: MemoryError no caso da página já estar cheia
        """
        if self.pode_inserir_elemento(no):  # Se o nó pode ser inserdio na página
            no.my_page = self  # O nó entende que está nessa página a partir de agora
            self._lista_elementos.append(no)  # A lista de elementos recebe o nó como um de seus elementos
            self._lista_elementos.sort(key=lambda node: node.value)  # Ordena a lista de nós
            self._atualizar_referencias()  # Atualiza as referências dos ponteiros
        else:  # Se o nó não pode ser inserido
            raise MemoryError('Página cheia')  # MemoryError. A memória da página está cheia.

    def alocar_pagina(self, page):
        """
        :param page: página que será alocada na árvore, por meio de uma referenciação de algum nó definido neste método
        :return: True se a página foi inserida com sucesso.
        :raise: KeyError no caso em que a página não pode ser alocada.
        """
        for no in self._lista_elementos:  # Para cada nó na lista de elementos
            if no.right is None:
                no.right = page
                self._atualizar_referencias()
                return True
        raise KeyError('Não há nenhum apontador adequado para a página informada')  # Não foi possível alocar a página

    def pode_inserir_elemento(self, valor):
        """
        :param valor: valor a ser inserido na página.
        :return: True se o elemento pode ser inserido. False se o elemento não pode ser inserido
        """
        if (self.maximo_elementos - len(self._lista_elementos) > 0) and not self.encontrou(valor):
            return True
        return False

    def encontrou(self, valor):
        """
        :param valor: valor a ser pesquisado na página
        :return: True se o elemento está na página. False caso contrário
        """
        return self._busca_binaria(valor)

    def pop(self, index=None):
        """
        :param index: Índice de remoção do elemento
        :return: Nó retirado da lista de elementos
        """
        if index is None:  # Se o usário não informou o índice de remoção
            no_retirado = self._lista_elementos.pop()
        else:  # Se informou
            no_retirado = self._lista_elementos.pop(index)
        self._atualizar_referencias()  # Atualize as referências dos ponteiros
        no_retirado.my_page = None  # O nó retirado agora não pertence a nenhuma página
        return no_retirado  # Retorne o nó retirado

    def index(self, element):
        return self._lista_elementos.index(element)

    def _atualizar_referencias(self):
        """
        Atualiza as referências dos ponteiros presentes nos nós da página.
        :return: None
        """
        self._atualizar_filhos()
        self._atualizar_irmaos()

    def _atualizar_filhos(self):
        """
        Atualiza os filhos dos nós da página. Ou seja, atualiza as págians filhas da página atual.
        :return: None
        """
        for c in range(len(self._lista_elementos) - 1):
            if self._lista_elementos[c + 1].left:  # Se tem apontador à esquerda do próximo nó:
                self._lista_elementos[c].right = self._lista_elementos[c + 1].left  # O ponteiro da direita recebe o
                # próximo ponteiro da esquerda
            else:  # Se não tiver
                self._lista_elementos[c + 1].left = self._lista_elementos[c].right  # O próximo ponteiro da esquerda
                # vira o ponteiro atual da direita

    def _atualizar_irmaos(self):
        """
        :return: Atualiza todos os irmãos de todos os filhos dessa página
        """
        for node in self:  # Para cada nó nessa página
            if node.left:  # Se há página à esquerda
                node.left.brother_right = node.right  # A página à esquerda tem como irmão à direita a página à direita
        # Fazendo a ponte
        if self.apontada_por:  # Se a página está sendo apontada por outra página (isso evita problemas com a raíz)
            if self.lista_elementos[-1].right:  # Se o último nó aponta para uma página à direita
                if self.brother_right:
                    self.lista_elementos[-1].right.brother_right = self.brother_right[0].left  # Faça a ponte

    def _busca_binaria(self, no, lista=None, begin=0, end=None):
        """
        Optou-se por implementar o algoritmo de busca binária para encontrar um elemento na página uma vez que a lista
        de nós estará sempre ordenada. Isso implica em um menor gasto computacional, que antes liner agora será feito em
        escala logarítmica.
        :param no: valor a ser pesquisado
        :return: True se o elemento encontra-se na lista de nós. False caso contrário.
        """
        if lista is None:
            lista = self._lista_elementos
        if end is None:  # Se o end é None, então estamos fazendo a primeira chamada à função
            end = len(lista) - 1  # Logo a posição final deve ser o tamanho da lista - 1
        if begin <= end:  # Se a sublista é válida
            m = (begin + end) // 2  # Meio da lista
            if no == lista[m]:  # Se o meio da lista é o elemento que estamos pesquisando
                return True
            if no < lista[m]:  # Se o ítem pesquisado for menor que o ítem que está no meio da lista
                return self._busca_binaria(no, lista, begin, m - 1)  # Faça a pesquisa pela esquerda
            return self._busca_binaria(no, lista, m + 1, end)  # Senão, quer dizer que ele está a direita da lista
        return False  # Caso o elemento não esteja na lista retorne False

    @property
    def lista_elementos(self):
        return self._lista_elementos

    @lista_elementos.setter
    def lista_elementos(self, lista: List):
        lista_atualizada = []  # Inicialize uma nova lista
        for no in lista:  # Para cada nó na lista informada como parâmetro
            no.my_page = self  # Atualize a página em que o nó da lista informada se encontra
            lista_atualizada.append(no)  # Insira esse nó na nova lista
        self._lista_elementos = lista_atualizada  # Sobrescreva a lista de elementos

    def matar_irmaos(self):
        self.brother_left, self._brother_right = None, None

    @property
    def brother_left(self):
        return self._brother_left

    @brother_left.setter
    def brother_left(self, value):
        self._brother_left = value

    @property
    def brother_right(self):
        return self._brother_right

    @brother_right.setter
    def brother_right(self, value):
        if value:
            value._brother_left, self._brother_right = self, value

    def __getitem__(self, index):
        return self._lista_elementos[index]

    def __iter__(self):
        return self._lista_elementos.__iter__()

    def __len__(self):
        return self._lista_elementos.__len__()

    def __str__(self):
        return str(self._lista_elementos)

    def __repr__(self):
        return self.__str__()
