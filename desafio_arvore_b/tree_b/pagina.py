from typing import List

from desafio_arvore_b.tree_b.no import Node


class Page:
    def __init__(self, maximo_elementos, apontada_por: Node = None):
        self.maximo_elementos = maximo_elementos
        self._lista_elementos: List = []
        self.apontada_por = apontada_por

    def inserir_elemento(self, no: Node):
        if self._pode_inserir_elemento():
            no.my_page = self
            self._lista_elementos.append(no)
            self._lista_elementos.sort(key=lambda node: node.value)
            self._atualizar_referencias()
        else:
            raise MemoryError('Página cheia')

    def alocar_pagina(self, page):
        primeiro_elemento_da_pagina_a_ser_inserida = page[0]  # Pega o primeiro elemento da página
        for no in self._lista_elementos:  # Para cada nó na lista de elementos
            if no > primeiro_elemento_da_pagina_a_ser_inserida:  # Se o nó é maior que o primeiro elemento
                no.left = page  # A referência esquerda desse nó pega a página passada como parâmetro
                self._atualizar_referencias()  # Atualize todas as referências da página
                return None  # Saia do método
        raise KeyError('Não há nenhum apontador adequado para a página informada')  # Não foi possível alocar a página

    def pop(self, index=None):
        if index is None:
            return self._lista_elementos.pop()
        return self._lista_elementos.pop(index)

    def index(self, element):
        return self._lista_elementos.index(element)

    def _pode_inserir_elemento(self):
        if self.maximo_elementos - len(self._lista_elementos) > 0:
            return True
        return False

    def _atualizar_referencias(self):
        for c in range(len(self._lista_elementos) - 1):
            self._lista_elementos[c].right = self._lista_elementos[c + 1].left

    @property
    def lista_elementos(self):
        return self._lista_elementos

    @lista_elementos.setter
    def lista_elementos(self, lista: List):
        self._lista_elementos = lista

    def __getitem__(self, index):
        """
        :param index: índice do elemento requerido
        :return: elemento requerido
        """
        return self._lista_elementos[index]

    def __iter__(self):
        return self._lista_elementos.__iter__()

    def __len__(self):
        return self._lista_elementos.__len__()

    def __str__(self):
        return str(self._lista_elementos)

    def __repr__(self):
        return self.__str__()
