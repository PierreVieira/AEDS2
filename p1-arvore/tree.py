from typing import List


class Node:
    def __init__(self, key, left: "Node" = None, right: "Node" = None):
        self.key = key
        self.left = left
        self.right = right

    def print_tree(self):
        """
        Imprime a arvore a partir do nodo atual
        """
        # posORDER:

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

    def search(self, key) -> bool:
        """
        Retorna verdadeiro caso a chave `key` exista na árvore
        """
        if key < self.key:
            if self.left:
                return self.left.search(key)
        elif key > self.key:
            if self.right:
                return self.right.search(key)
        else:
            return True
        return False

    def to_sorted_array(self, arr_result: List = None) -> List:
        """
        Retorna um vetor das chaves ordenadas.
        arr_result: Parametro com os itens já adicionados.
        """
        if arr_result is None:
            arr_result = []

        if self.left:
            self.left.to_sorted_array(arr_result)

        arr_result.append(self.key)

        if self.right:
            self.right.to_sorted_array(arr_result)
        return arr_result

    def max_depth(self, current_max_depth: int = 0) -> int:
        """
        Calcula a maior distancia entre o nodo raiz e a folha
        current_max_depth: Valor representando a maior distancia até então
                           ao chamar pela primeira vez, não é necessário usa-lo
        """
        current_max_depth = current_max_depth + 1
        val_left, val_right = current_max_depth, current_max_depth

        if self.left:
            val_left = self.left.max_depth(current_max_depth)
        if self.right:
            val_right = self.right.max_depth(current_max_depth)

        if val_left > val_right:
            return val_left
        else:
            return val_right

    def position_node(self, key, current_position: int = 1) -> int:
        """
            Retorna a posição do nodo desejado na árvore
            current_position: representa a posição da árvore naquele momento
                           ao chamar pela primeira vez, não é necessário usa-lo
        """
        if key == self.key:
            return current_position
        elif key < self.key:
            if self.left:
                return self.left.position_node(key, 2 * current_position)
        elif key > self.key:
            if self.right:
                return self.right.position_node(key, 2 * current_position + 1)
        return 0
