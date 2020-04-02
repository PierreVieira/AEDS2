from typing import List

from desafio_arvore_b.tree_b.node import Node


class Page:
    def __init__(self, maximo_elementos: int = None, lista_nos: List = None):
        if lista_nos is None:  # Se o usuário da classe não informou a lista de nós
            if maximo_elementos is None:  # Se o usuário não informou a quantidade máxima da lista de nós
                raise ValueError('Quando não é informado a lista de nós, deve-se informar a quantidade máxima de nós')
                # Um erro deve ser lançado
            self._lista_nos = []  # A lista de nós começa com vazio
        if maximo_elementos is not None:  # Se o usuário informou a lista de elementos
            self._maximo_elementos = maximo_elementos  # O máximo de elementos é o value informado pelo usuário
        else:  # senão
            self._maximo_elementos = len(lista_nos)  # O máximo de elementos é o tamanho da lista de nós
        if len(lista_nos) > self._maximo_elementos:  # Se o tamanho da lista de nós é maior que o máximo de elmentos
            raise MemoryError('Não é possível ter uma página com mais elementos do que permitido!')  # Erro

    @property
    def lista_nos(self):
        return self._lista_nos

    @property
    def maximo_elementos(self):
        return self._maximo_elementos

    @lista_nos.setter
    def lista_nos(self, lista):
        self._lista_nos = lista

    def __str__(self):
        return str(self.lista_nos)

    def __repr__(self):
        return self.__str__()


class Page_b(Page):
    def __init__(self, maximo_elementos: int = None, lista_nos: List = None):
        """
        A ideia aqui é que o usuário pode informar ou um ou outro parâmetro, porém não pode informar nenhum.
        O usuário escolhe se quer informar o máximo de elementos da página ou se quer informar o que é a página dele com
        o máximo de elementos possíveis.
        Caso o usuário opte por informar a página, o método construtor irá fazer com que o máximo de elementos possíveis
        seja o tamanho da lista informada.
        :param maximo_elementos: máximo de elementos que a página suporta
        :param lista_nos: nós que compõem a página
        """
        super().__init__(maximo_elementos, lista_nos)
        self._lista_nos = lista_nos  # A lista de nós da página recebe a lista de nós informada
        self._apontada_por = None

    def eh_possivel_inserir_na_pagina(self):
        """
        Informa se a página pode ter mais um nó dentro dela
        :return: True se é possível inserir, false se não é possível
        """
        return len(self.lista_nos) < self._maximo_elementos  # A inserção será possível quando o tamanho da página
        # for menor que a quantidade máxima de elementos permitidos

    def inserir_elemento(self, elemento: Node):
        """
        Insere um elemento na página
        :param elemento: nó a ser inserido na página
        :return: True se o objeto foi inserido, MemoryError se a página já estiver cheia
        """
        if self.eh_possivel_inserir_na_pagina():  # Se for possível inserir na página
            self._insercao_simples_na_pagina(elemento)  # Faz a inserção do elemento na mesma página
        else:  # Se não
            raise MemoryError('Não é possível inserir mais elementos nessa página')  # Erro

    def contem_elemento(self, no: Node):
        """
        :param no: nó a ser pesquisado na página
        :return: True se o nó está na pagina. False caso contrário
        """
        return no in self.lista_nos

    def _insercao_simples_na_pagina(self, elemento):
        """
        Adiciona o elemento na página recorrente e ordena a lista
        :param elemento: Elemento a ser inserido na página
        :return: None
        """
        self._lista_nos.append(elemento)  # Insere um elemento na página
        self._lista_nos.sort(key=lambda no: no.value)  # Ordena a página pelo parâmetro de value do nó
        self._atualizar_apontadores()

    def _atualizar_apontadores(self):
        """
        Atualiza os apontadores dos nós
        :return: None
        """
        for c in range(len(self.lista_nos) - 1):
            self.lista_nos[c].right = self.lista_nos[c + 1].left  # O apontador da direita de um no a(n) é o
            # apontador da esquerda de um nó a(n-1)
