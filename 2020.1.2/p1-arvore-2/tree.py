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

    def is_balanced(self) -> bool:
        """
            Retorna true caso a árvore seja balanceada, false caso não seja
        """
        if self._is_possible_identify_not_is_balanced():
            return False
        if self.left:
            return self.left.is_balanced()
        if self.right:
            return self.right.is_balanced()
        return True

    # def sorted_array_to_balanced_tree(self, array: List, start: int, end: int):
    #     return []
    def sorted_array_to_balanced_tree(self, array):
        array1, array2 = array[0:len(array) // 2], array[len(array) // 2:len(array)]
        array3 = [array2.pop(0)]
        while len(array1) > 0 or len(array2) > 0:
            try:
                retirado1 = array1.pop(len(array1) // 2)
            except IndexError:
                pass
            else:
                array3.append(retirado1)
            try:
                retirado2 = array2.pop(len(array2) // 2)
            except IndexError:
                pass
            else:
                array3.append(retirado2)
        return array3

    def to_balanced_tree(self) -> "Node":
        array_tree = self.to_sorted_array()
        array_for_balanced = self.sorted_array_to_balanced_tree(array_tree)
        no = Node(array_for_balanced[0])
        for i in range(1, len(array_for_balanced)):
            no.insert(array_for_balanced[i])
        return no

    def _is_possible_identify_not_is_balanced(self) -> bool:
        if self.left and self.right:
            if abs(self.right.max_depth() - self.left.max_depth()) > 1:
                return True
        elif self.left:
            if abs(0 - self.left.max_depth()) > 1:
                return True
        elif self.right:
            if abs(self.right.max_depth() - 0) > 1:
                return True
        return False
