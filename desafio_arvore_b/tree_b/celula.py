from desafio_arvore_b.tree_b.ponteiro import Ponteiro


class Celula:
    def __init__(self, valor, my_page=None):
        self.ponteiro = Ponteiro()
        self.valor = valor
        self.my_page = my_page
        self.ponteiro.cima = self

    def __lt__(self, other):
        if type(other) == Celula:
            return self.valor < other.valor
        return self.valor < other

    def __gt__(self, other):
        if type(other) == Celula:
            return self.valor > other.valor
        return self.valor > other

    def __eq__(self, other):
        return self.valor == other

    def __str__(self):
        return f'{self.valor}'

    def __repr__(self):
        return self.__str__()
