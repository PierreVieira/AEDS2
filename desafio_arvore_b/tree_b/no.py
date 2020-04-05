"""
Autor: Pierre Vieira
Github: https://github.com/PierreVieira/LAEDS_II/tree/master/desafio_arvore_b
"""

class Node:
    def __init__(self, value, right=None, left=None, my_page=None):
        self.value = value
        self._right = right
        self._left = left
        self.my_page = my_page

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value
        value.apontada_por = self

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value
        value.apontada_por = self

    def __eq__(self, other):
        if type(other) == Node:
            return self.value == other.value
        return self.value == other

    def __lt__(self, other):
        if type(other) == Node:
            return self.value < other.value
        return self.value < other

    def __gt__(self, other):
        if type(other) == Node:
            return self.value > other.value
        return self.value > other

    def __str__(self):
        return f'{str(self.value)}'

    def __repr__(self):
        return self.__str__()
