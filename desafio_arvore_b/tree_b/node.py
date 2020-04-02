from desafio_arvore_b.tree_b.pointer import Pointer


class Node:
    """O nó agora aponta não mais para um outro nó, mas sim para uma outra página."""

    def __init__(self, value, left: Pointer = None, right: Pointer = None):
        self._left = left
        self._right = right
        self.value = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self.left.esta_apontando_para = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self.right.esta_apontando_para = value

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