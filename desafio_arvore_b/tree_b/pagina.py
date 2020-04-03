from desafio_arvore_b.tree_b.celula import Celula
from math import inf


class Page:
    def __init__(self, qtde_max_celulas):
        """
        :param qtde_max_celulas:
        """
        self.__qtde_ponteiros = qtde_max_celulas + 1
        self._lista_celulas = [Celula(-inf) for i in range(self.__qtde_ponteiros)]
        self._lista_celulas[-1] = Celula(inf)

    def inserir_celula(self, celula: Celula):
        for c in range(self.__qtde_ponteiros - 1):
            if self._lista_celulas[c].valor == -inf:
                self._lista_celulas[c] = celula
                self._lista_celulas.sort(key=lambda celula: celula.valor)
                return None
        raise MemoryError('Não foi possível inserir a célula. PÁGINA CHEIA!')

    def remover_celula(self, celula: Celula):
        self._lista_celulas.remove(celula)

    def __len__(self):
        return self.__qtde_ponteiros - 1

    def __getitem__(self, index):
        return self._lista_celulas[index]

    def __setitem__(self, index, value):
        self._lista_celulas[index] = value

    def __str__(self):
        return str(self._lista_celulas)

    def __repr__(self):
        return self.__str__()