"""
Autor: Pierre Vieira
"""


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
            self._maximo_elementos = maximo_elementos  # O máximo de elementos é o valor informado pelo usuário
        else:  # senão
            self._maximo_elementos = len(lista_nos)  # O máximo de elementos é o tamanho da lista de nós
        if len(lista_nos) > self._maximo_elementos:  # Se o tamanho da lista de nós é maior que o máximo de elmentos
            raise MemoryError('Não é possível ter uma página com mais elementos do que permitido!')  # Erro
        self._lista_nos = lista_nos  # A lista de nós da página recebe a lista de nós informada

    def inserir_elemento(self, elemento: "Node", pagina_sem_pai: "Page" = None):
        if len(self.lista_nos) < self._maximo_elementos:  # Se o tamanho atual da minha página for menor que o máximo
            # permitido
            if pagina_sem_pai is not None:
                self._insercao_simples_na_pagina(elemento, pagina_sem_pai=pagina_sem_pai)
            else:
                self._insercao_simples_na_pagina(elemento)  # Faz a inserção do elemento na mesma página
        else:
            raise MemoryError('Não é possível inserir mais elementos nessa página')  # Erro

    def contem_elemento(self, no):
        """
        :param no: nó a ser pesquisado na página
        :return: True se o nó está na pagina. False caso contrário
        """
        if no in [e.value for e in self.lista_nos]:
            return True
        return False

    def _insercao_simples_na_pagina(self, elemento, pagina_sem_pai: "Page" = None):
        """
        Adiciona o elemento na página recorrente e ordena a lista
        :param elemento: Elemento a ser inserido na página
        :return: None
        """
        self._lista_nos.append(elemento)  # Insere um elemento na página
        self._lista_nos.sort(key=lambda no: no.value)  # Ordena a página pelo parâmetro de valor do nó
        if pagina_sem_pai is not None:
            self._atualizar_apontadores(
                pagina_sem_pai=pagina_sem_pai)  # Faz a atualização dos apontadores dos nós igualando algumas
            # referências
        else:
            self._atualizar_apontadores()

    def _atualizar_apontadores(self, pagina_sem_pai: "Page" = None):
        for c in range(len(self.lista_nos) - 1):
            if self.lista_nos[c + 1].right is None and self.lista_nos[c + 1].left is None:  # Se o próximo nó que
                # estou passando não está com nenhum apontador
                if pagina_sem_pai is not None:  # Se há uma página sem pai
                    self.lista_nos[c + 1].right = pagina_sem_pai  # O próximo nó pega esse página sem pai
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
    def __init__(self, raiz: "Page"):
        """
        :param raiz: a raíz é uma página
        :return: None
        """
        self.raiz = raiz

    def elemento_na_arvore(self, valor, pagina_de_busca: "Page" = None) -> bool:
        """
        :param pagina_de_busca: página inicial em que será feita a busca.
        :param valor: valor a ser pesquisado na árvore.
        :return: True se achou o elemento, False caso contrário.
        """
        if pagina_de_busca is None:  # Se o usuário não informou a página de busca
            pagina_de_busca = self.raiz  # A página de busca é a raíz
        if pagina_de_busca.contem_elemento(Node(valor)):  # Se o elemento está na página de busca
            return True
        # Senão, quer dizer que teremos que descer por algum lado
        for element in pagina_de_busca.lista_nos:
            if valor < element:
                if element.left:  # Se tem filho à esquerda
                    return self.elemento_na_arvore(valor, element.left)  # Desce pela página da esquerda
                return False  # Se o algoritmo chegou aqui então quer dizer que a árvore não tem o elemento de pesquisa
        # Se o algoritmo chegou até aqui quer dizer que o elemento não é menor que nenhum elemento daquela árvore
        if pagina_de_busca.lista_nos[-1].right is None:  # Se não há filho à direita
            return False  # Não existe o elemento de busca na árvore
        return self.elemento_na_arvore(valor, pagina_de_busca.lista_nos[-1].right)  # Desce pela página da direita do
        # último nó da página

    def inserir_elemento(self, valor, pagina_sem_pai: "Page" = None):
        """
        Faz a inserção de um nó em alguma página da árvore
        :param pagina_sem_pai: página desalocada
        :return: None
        """
        if not self.elemento_na_arvore(valor):
            if pagina_sem_pai is not None:
                self._insert_element(Node(valor), pagina_sem_pai=pagina_sem_pai)
            else:
                self._insert_element(Node(valor))

    def _insert_element(self, node: "Node", page: "Page" = None, pagina_sem_pai: "Page" = None):
        """
        Método recursivo de inserção
        :param node: Elemento a ser inserido na página recorrente
        :param page: Página recorrente em que o elemento será inserido
        :return: None
        """
        if page is None:  # Se o método está sendo chamado pela primeira vez
            page = self.raiz  # A página em que iremos tentar a inserção é a raíz
        for element in page.lista_nos:
            if node < element:  # Se o nó que quero inserir é menor que o elemento recorrente
                if element.left is None:
                    break
                if pagina_sem_pai is not None:
                    return self._insert_element(node, page=element.left, pagina_sem_pai=pagina_sem_pai)
                else:
                    return self._insert_element(node, page=element.left)  # Insira na página à esquerda
        try:  # Tente inserir o elemento na página recorrente
            if pagina_sem_pai is not None:
                page.inserir_elemento(node, pagina_sem_pai=pagina_sem_pai)
            else:
                page.inserir_elemento(node)  # Chama o método de inserção da página para inserir o valor nela
        except MemoryError:  # Exceto se ela estiver cheia
            self._inserir_elemento_em_nova_pagina(node, page)

    def _inserir_elemento_em_nova_pagina(self, node: "Node", page: "Page"):
        pagina_vazia = Page(
            maximo_elementos=self.raiz.maximo_elementos)  # Cria uma página vazia com o mesmo tamanho da página
        # recorrente.
        pagina_vazia.lista_nos = [page.lista_nos.pop() for i in range(len(page.lista_nos) // 2)]
        pagina_nao_mais_vazia = pagina_vazia
        pagina_nao_mais_vazia.lista_nos.sort(key=lambda node: node.value)
        # A linha anterior pegou metade dos elementos da página recorrente e jogou em outra página
        if node < pagina_nao_mais_vazia.lista_nos[0]:  # Se o valor que estou querendo inserir é menor
            # que o primeiro elemento da nova página
            try:  # Tente inserir o elemento na página antiga
                page.inserir_elemento(node)
            except MemoryError:
                print('A página continua cheia.')
        else:  # Se ele é maior
            try:  # Então insere na página nova
                pagina_nao_mais_vazia.inserir_elemento(node)
            except MemoryError:
                print('A página nova está cheia')  # Situação impossível
        self.inserir_elemento(page.lista_nos.pop(), pagina_sem_pai=pagina_nao_mais_vazia)  # Joga o último elemento da
        # página antiga pra cima e esse elemento agora aponta para a página nova


if __name__ == '__main__':
    construir_lista_nos = lambda *args: list(Node(i) for i in args)
    pagina = Page(lista_nos=construir_lista_nos(29))
    pagina.lista_nos[0].left = Page(lista_nos=construir_lista_nos(8, 15))
    pagina.lista_nos[0].right = Page(lista_nos=construir_lista_nos(37, 45, 60))
    pagina.lista_nos[0].left.lista_nos[0].left = Page(lista_nos=construir_lista_nos(1, 3, 4, 7))
    pagina.lista_nos[0].left.lista_nos[1].left = Page(lista_nos=construir_lista_nos(10, 12, 13, 14))
    pagina.lista_nos[0].left.lista_nos[1].right = Page(lista_nos=construir_lista_nos(18, 20, 25))
    pagina.lista_nos[0].right.lista_nos[0].left = Page(lista_nos=construir_lista_nos(30, 36))
    pagina.lista_nos[0].right.lista_nos[1].left = Page(lista_nos=construir_lista_nos(40, 41, 42, 43))
    pagina.lista_nos[0].right.lista_nos[2].left = Page(lista_nos=construir_lista_nos(51, 52))
    pagina.lista_nos[0].right.lista_nos[2].right = Page(lista_nos=construir_lista_nos(70, 77, 83))
    arvore_b = Arvore_b(pagina)
    arvore_b.inserir_elemento(19)
    print(arvore_b.elemento_na_arvore(11))
