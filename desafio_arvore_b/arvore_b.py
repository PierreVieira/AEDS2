"""
Autor: Pierre Vieira
"""
from typing import List


class Node:
    """O nó agora aponta não mais para um outro nó, mas sim para uma outra página."""

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.value < other

    def __gt__(self, other):
        return self.value > other

    def __eq__(self, other):
        if type(other) == Node:
            return self.value == other.value
        return self.value == other


class Page:
    def __init__(self, maximo_elementos: int = None, lista_nos: "List" = None):
        """
        A ideia aqui é que o usuário pode informar ou um ou outro parâmetro, porém não pode informar nenhum.
        O usuário escolhe se quer informar o máximo de elementos da página ou se quer informar o que é a página dele com
        o máximo de elementos possíveis.
        Caso o usuário opte por informar a página, o método construtor irá fazer com que o máximo de elementos possíveis
        seja o tamanho da lista informada.
        :param maximo_elementos: máximo de elementos que a página suporta
        :param lista_nos: nós que compõem a página
        """
        if lista_nos is None:  # Se o usuário da classe não informou a lista de nós
            if maximo_elementos is None:  # Se o usuário não informou a quantidade máxima da lista de nós
                raise ValueError('Quando não é informado a lista de nós, deve-se informar a quantidade máxima de nós')
                # Um erro deve ser lançado
            lista_nos = []  # A lista de nós começa com vazio
        if maximo_elementos is not None:  # Se o usuário informou a lista de elementos
            self._maximo_elementos = maximo_elementos  # O máximo de elementos é o value informado pelo usuário
        else:  # senão
            self._maximo_elementos = len(lista_nos)  # O máximo de elementos é o tamanho da lista de nós
        if len(lista_nos) > self._maximo_elementos:  # Se o tamanho da lista de nós é maior que o máximo de elmentos
            raise MemoryError('Não é possível ter uma página com mais elementos do que permitido!')  # Erro
        self._lista_nos = lista_nos  # A lista de nós da página recebe a lista de nós informada

    def eh_possivel_inserir_na_pagina(self):
        """
        Informa se a página pode ter mais um nó dentro dela
        :return: True se é possível inserir, false se não é possível
        """
        return len(self.lista_nos) < self._maximo_elementos  # A inserção será possível quando o tamanho da página
        # for menor que a quantidade máxima de elementos permitidos

    def inserir_elemento(self, elemento: "Node"):
        """
        Insere um elemento na página
        :param elemento: nó a ser inserido na página
        :return: True se o objeto foi inserido, MemoryError se a página já estiver cheia
        """
        if self.eh_possivel_inserir_na_pagina():  # Se for possível inserir na página
            self._insercao_simples_na_pagina(elemento)  # Faz a inserção do elemento na mesma página
        else:  # Se não
            raise MemoryError('Não é possível inserir mais elementos nessa página')  # Erro

    def contem_elemento(self, no: "Node"):
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


class Arvore_b:
    def __init__(self, root: "Page"):
        """
        :param root: a raíz é uma página
        :return: None
        """
        self.root = root

    def elemento_na_arvore(self, value):
        if type(value) != Node:  # Se o usuário não está pesquisando um nó
            no = Node(value)  # Crie um novo nó com o value informado pelo usuário
        else:  # Senão
            no = value  # O nó é o nó informado pelo usuário
        return self._elemento_na_arvore(no)  # Pesquise se o nó informado está na árvore

    def _elemento_na_arvore(self, no, pagina_de_busca: "Page" = None) -> bool:
        """
        :param pagina_de_busca: página inicial em que será feita a busca.
        :param no: no a ser pesquisado na árvore.
        :return: True se achou o elemento, False caso contrário.
        """
        if pagina_de_busca is None:  # Se o usuário não informou a página de busca
            pagina_de_busca = self.root  # A página de busca é a raíz
        if pagina_de_busca.contem_elemento(no):  # Se o elemento está na página de busca
            return True
        # Senão, quer dizer que teremos que descer por algum lado
        for element in pagina_de_busca.lista_nos:
            if no < element:
                if element.left:  # Se tem filho à esquerda
                    return self._elemento_na_arvore(no, element.left)  # Desce pela página da esquerda
                return False  # Se o algoritmo chegou aqui então quer dizer que a árvore não tem o elemento de pesquisa
        # Se o algoritmo chegou até aqui quer dizer que o elemento não é menor que nenhum elemento daquela árvore
        if pagina_de_busca.lista_nos[-1].right is None:  # Se não há filho à direita
            return False  # Não existe o elemento de busca na árvore
        return self._elemento_na_arvore(no, pagina_de_busca.lista_nos[-1].right)  # Desce pela página da direita do
        # último nó da página

    def inserir_elemento(self, value):
        """
        Faz a inserção de um nó em alguma página da árvore
        :return: None
        """
        if type(value) != Node:  # Se o usuário não informou um nó a ser inserido
            value = Node(value)  # O valor informado pelo usuário se transforma em um nó
        node = value  # o nó pega o valor informado pelo usuário
        if not self.elemento_na_arvore(value):  # Se o nó já não está na árvore
            self._insert_node(node)  # Insira o nó

    def _insert_node(self, node, page: "Page" = None):
        """
        :param node: nó a ser inserido na página
        :param page: página recorrente
        :return: None
        """
        if page is None:  # Se é a primeira vez que estamos chamando esse método
            page = self.root  # A página é a raiz
        for element in page.lista_nos:  # Para cada elemento na página recorrente
            if node < element:  # Se o nó que estou querendo inseriri é menor que o elemento
                if element.left:  # Se tem página à esquerda
                    return self._insert_node(node, element.left)  # Desce pra esquerda
                try:  # Senão, tente
                    page.inserir_elemento(node)  # Insira um nó na página recorrente
                except MemoryError:  # Exceto se ocorrer um erro de memória na páina
                    self._nova_pagina(node, page)  # Crie uma nova página e aloque o nó
        if page.lista_nos[-1].right:  # Se tem página à direita do último nó na página
            return self._insert_node(node, page.lista_nos[-1].right)  # Desce para a direita do último nó da página

    def _nova_pagina(self, no: "Node", page: "Page"):
        """
        Esse método será responsável por dividir as páginas e realocar os ponteiros
        :param no: nó a ser inserido na nova página
        :return: None
        """
        elementos_nova_pagina = [page.lista_nos.pop() for i in range(len(page.lista_nos) // 2)]  # Pega metade dos
        # elementos da página recorrente
        nova_pagina = Page(page.maximo_elementos, elementos_nova_pagina)  # Cria uma nova página com esses elementos
        if no < nova_pagina.lista_nos[0]:  # Se o nó é menor que o primeiro elemento da nova página
            page.inserir_elemento(no)  # Insira o nó na página que agora está menor
            no_q_vai_pra_cima = page.lista_nos.pop()  # O nó que vai pra cima é o último elemento dessa página
            no_q_vai_pra_cima.right = nova_pagina  # O nó que vai pra cima recebe no apontador da direita uma nova
            # página
        else:  # Se for maior
            nova_pagina.inserir_elemento(no)  # Insere o nó na nova página
            no_q_vai_pra_cima = nova_pagina.lista_nos.pop(0)  # Remove o primerio elemento na nova página pra mandar
            # ele pra cima
            no_q_vai_pra_cima.right = nova_pagina  # O nó que vai pra cima recebe no apontador da direita a nova página
        self._insert_node(no_q_vai_pra_cima)  # Insere na árvore o nó que vai pra cima
