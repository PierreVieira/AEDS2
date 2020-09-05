from typing import List


class Node:

    def __init__(self, key, left: "Node" = None, right: "Node" = None):
        self.key = key
        self.left = left
        self.right = right

    def print_tree(self):
        """
        Imprime a arvore a partir do nodo atual
        <Faz o percurso em ordem infixa>
        """
        if self.left:
            self.left.print_tree()
        print(self.key, end=" ")
        if self.right:
            self.right.print_tree()

    def insert(self, key) -> bool:
        """
        Insere um nodo na árvore que a chave "key"
        """
        if key < self.key:
            if self.left:
                return self.left.insert(key)
            else:
                self.left = Node(key)
                return True
        elif key > self.key:
            if self.right:
                return self.right.insert(key)
            else:
                self.right = Node(key)
                return True
        else:
            return False

    def search(self, key, cont_search=None, retornar_cont_search=False):
        """
        :param key: valor a ser encontrado
        :param cont_search: contador de chamadas o método recursivo
        :param retornar_cont_search: identifica se deve ou não retornar o contador de chamadas, se for falso não retorna.
        :return: True / False / True, cont_search / False, cont_search
        """
        if cont_search is None:  # Se o contador não foi passado como parâmetro
            cont_search = 1  # O valor inicial do contador é 1
        if key < self.key:  # Se o elemento que estou procurando é menor que o nó atual
            if self.left:  # Se tem filho à esquerda
                if retornar_cont_search:  # Se devemos retornar o cont_search
                    return self.left.search(key, cont_search + 1, True)  # Desça o ramo à esquerda informando que
                    # deve retornar o cont_search
                return self.left.search(key, cont_search + 1)  # Desça o ramo à esquerda
        elif key > self.key:  # Se o elemento que estou procurando é maior que o nó atual
            if self.right:  # Se tem filho à direita
                if retornar_cont_search:  # Se devemos retornar o cont_search:
                    return self.right.search(key, cont_search + 1, True)  # Desça o ramo à direita informando que deve
                    # retornar o cont_search
                return self.right.search(key, cont_search + 1)  # Desça o ramo à direita
        else:  # Caso o elemento que estou procurando é igual ao atual
            if retornar_cont_search:  # Se o usuário escolheu retornar o contador de chamadas
                return True, cont_search  # Retorne verdadeiro e o valor de cont_search
            return True  # Retorne verdadeiro
        # Elemento não existe na árvore
        if retornar_cont_search:  # Se o usuário não escolheu retornar o contador de chamadas
            return False, cont_search  # Retorne falso e o valor de cont_search
        return False  # Retorne falso

    def to_sorted_array(self, arr_result: List = None) -> List:
        """
        Aplica o caminhamento em ordem infixa
        :param arr_result: Parametro com os itens já adicionados.
        :return: Lista com os elementos ordenados.
        """
        if arr_result is None:  # Se não foi informado o valor de arr_result
            arr_result = []  # arr_result começa como uma lista vazia
        if self.left:  # Se há nó à esquerda
            self.left.to_sorted_array(arr_result=arr_result)  # Desça pela esquerda
        arr_result.append(self.key)  # O array adiciona o valor da raiz
        if self.right:  # Se há nó à direita
            self.right.to_sorted_array(arr_result=arr_result)  # Desça pela direita
        return arr_result  # Retorne o array (estará ordenado)

    def max_depth(self, current_max_depth: int = 0, alturas_raiz_folha: List = None) -> int:
        """
        Faz basicamente um caminho prefixo em busca da maior altura.
        :param alturas_raiz_folha: Lista de alturas da raiz até a folha.
        :param current_max_depth: Valor representando a maior distancia até então ao chamar pela primeira vez,
        não é necessário usa-lo.
        :return: maior distancia entre o nodo raiz e a folha.
        """
        if alturas_raiz_folha is None:  # Se não foi informado a lista de alturas
            alturas_raiz_folha = []
        alturas_raiz_folha.append(current_max_depth)  # Caminho prefixo
        if self.left:  # Se há nó à esquerda
            self.left.max_depth(current_max_depth + 1, alturas_raiz_folha=alturas_raiz_folha)  # Desça
            # pela esquerda
        if self.right:  # Se há nó à direita
            self.right.max_depth(current_max_depth + 1, alturas_raiz_folha=alturas_raiz_folha)  # Desça
            # pela direita
        return max(alturas_raiz_folha) + 1  # Retorne a maior distância entre a raiz e a folha mais distante
