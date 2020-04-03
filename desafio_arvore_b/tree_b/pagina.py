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
        for c in range(len(self._lista_celulas)):
            self._lista_celulas[c].my_page = self

    def inserir_celula(self, celula: Celula):
        for c in range(self.__qtde_ponteiros - 1):
            if self.lista_celulas[c].valor == -inf:
                self.lista_celulas[c] = celula
                self.lista_celulas[c].my_page = self
                self.lista_celulas.sort(key=lambda celula: celula.valor)
                if self.lista_celulas[-2].ponteiro.celula_baixo is None and self.lista_celulas[-1].ponteiro.celula_baixo is not None:
                    # Se a célula que acabou de ser inserida foi inserida na última posição e não tem referência pra
                    # baixo e o último ponteiro tem uma referência pra baixo, então troque as referências
                    self.lista_celulas[-2].ponteiro.celula_baixo, self.lista_celulas[-1].ponteiro.celula_baixo = \
                        self.lista_celulas[-1].ponteiro.celula_baixo, self.lista_celulas[-2].ponteiro.celula_baixo
                return None
        raise MemoryError('Não foi possível inserir a célula. PÁGINA CHEIA!')

    def inserir_celula_e_atualizar_ref_com_novas_paginas(self, celula, maiores, menores):
        pass

    def index(self, celula):
        for i in range(len(self.lista_celulas) - 1):
            if celula == self.lista_celulas[i]:
                return i + 1
        return IndexError('A célula informada não está na página')

    def pop(self, index=None):
        if index is None:
            index = self.__len__() - 1
        retirado = self._lista_celulas.pop(index)
        retirado.my_page = None
        self._lista_celulas.append(Celula(-inf))
        self._lista_celulas.sort()
        return retirado

    @property
    def tem_pagina_acima(self):
        """
        :return: True se tiver uma página a cima da página. False caso contrário
        """
        for celula in self.lista_celulas:
            if celula.ponteiro.celula_cima is not None:
                return True
        return False

    @property
    def menor_valor(self):
        for v in self._lista_celulas:
            if v != -inf:
                return v
        return -inf

    @property
    def maior_valor(self):
        for i in range(len(self._lista_celulas) - 1):
            if self._lista_celulas[i] != -inf:
                return self._lista_celulas[i]
        return -inf

    @property
    def lista_celulas(self):
        return self._lista_celulas

    @lista_celulas.setter
    def lista_celulas(self, lista):
        self._lista_celulas = lista
        for c in range(len(self._lista_celulas) - 1):
            self._lista_celulas[c].my_page = self

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
