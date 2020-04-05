from typing import List

from desafio_arvore_b.tree_b.no import Node


class Page:
    def __init__(self, maximo_elementos, apontada_por: Node = None):
        self.maximo_elementos = maximo_elementos
        self._lista_elementos: List = []
        self.apontada_por = apontada_por

    def inserir_elemento(self, no: Node):
        if self.pode_inserir_elemento(no):
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

    def pode_inserir_elemento(self, valor):
        if (self.maximo_elementos - len(self._lista_elementos) > 0) and not self._busca_binaria(valor):
            return True
        return False

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
        for c in range(len(self._lista_elementos) - 1):
            if self._lista_elementos[c + 1].left:  # Se tem apontador à esquerda do próximo nó:
                self._lista_elementos[c].right = self._lista_elementos[c + 1].left

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

    def __getvalor__(self, index):
        """
        :param index: índice do elemento requerido
        :return: elemento requerido
        """
        return self._lista_elementos[index]

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
