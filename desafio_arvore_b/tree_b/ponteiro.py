class Ponteiro:
    def __init__(self, celula_cima=None, celula_baixo=None):
        self.celula_cima = celula_cima
        self._celula_baixo = celula_baixo

    @property
    def celula_baixo(self):
        return self._celula_baixo

    @celula_baixo.setter
    def celula_baixo(self, value):
        self._celula_baixo = value

    def remover_referencia_de_cima(self):
        self.celula_cima = None

    def remover_referencia_de_baixo(self):
        self.celula_baixo = None

    def __str__(self):
        return f'{self.celula_cima}\n↑\n↓{self.celula_baixo}'

    def __repr__(self):
        return self.__str__()
