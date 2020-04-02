from desafio_arvore_b.tree_b.page import Page_b
from desafio_arvore_b.tree_b.node import Node


class Arvore_b:
    def __init__(self, root: Page_b):
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

    def _elemento_na_arvore(self, no, pagina_de_busca: Page_b = None) -> bool:
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

    def _insert_node(self, node, page: Page_b = None):
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

    def _nova_pagina(self, no: "Node", page: Page_b):
        """
        Esse método será responsável por dividir as páginas e realocar os ponteiros
        :param no: nó a ser inserido na nova página
        :return: None
        """
        elementos_nova_pagina = [page.lista_nos.pop() for i in range(len(page.lista_nos) // 2)]  # Pega metade dos
        # elementos da página recorrente
        nova_pagina = Page_b(page.maximo_elementos, elementos_nova_pagina)  # Cria uma nova página com esses elementos
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
