class No:
    def __init__(self, chave=None):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1

    @property
    def altura_subarvore_esquerda(self):
        if self.esquerda is None:
            return 0
        return self.esquerda.altura

    @property
    def altura_subarvore_direita(self):
        if self.direita is None:
            return 0

        return self.direita.altura

    @property
    def equilibrio(self):
        return self.altura_subarvore_esquerda - self.altura_subarvore_direita

    def atualiza_altura(self):
        self.altura = 1 + max(self.altura_subarvore_esquerda,
                              self.altura_subarvore_direita)

    # Definindo str e repr para facilitar no debug
    def __str__(self):
        return str(self.chave)

    def __repr__(self):
        return self.__str__()


class AVL:
    def __init__(self, raiz):
        self.raiz = raiz

    def imprime(self):
        self._imprime(self.raiz)

    def _imprime(self, raiz_sub_arvore):

        print(raiz_sub_arvore.chave, end="\n")
        if raiz_sub_arvore.esquerda:
            print(f"---------Esquerda de {raiz_sub_arvore.chave}-------")
            self._imprime(raiz_sub_arvore.esquerda)

        if raiz_sub_arvore.direita:
            print(f"---------Direita  de {raiz_sub_arvore.chave}-------")
            self._imprime(raiz_sub_arvore.direita)

    def rotacao_esquerda(self, raiz_sub_arvore):
        """
        *Filho da direita vira nova raiz.
        *Filho da esquerda do filho da direita vira filho da direita do filho da esquerda.
        *A raiz original vira filho da esquerda da nova raiz.
        :param raiz_sub_arvore: nó em que será aplicada a rotação.
        :return: None
        """
        nova_raiz_sub_arvore = None
        nova_raiz_sub_arvore, nova_raiz_sub_arvore.esquerda, nova_raiz_sub_arvore.esquerda.direita, nova_raiz_sub_arvore.direita.esquerda = raiz_sub_arvore.direita, raiz_sub_arvore, raiz_sub_arvore.direita.esquerda, raiz_sub_arvore.esquerda
        # Matando as referências de troca
        nova_raiz_sub_arvore.direita.esquerda = None

        # Atualizando as alturas
        nova_raiz_sub_arvore.esquerda.atualiza_altura()
        nova_raiz_sub_arvore.direita.atualiza_altura()
        nova_raiz_sub_arvore.atualiza_altura()
        return nova_raiz_sub_arvore

    def rotacao_direita(self, raiz_sub_arvore):
        nova_raiz_sub_arvore = None
        return nova_raiz_sub_arvore

    def rotacao_dupla_esquerda(self, raiz_sub_arvore):

        return None

    def rotacao_dupla_direita(self, raiz_sub_arvore):

        return None

    def insere(self, chave):
        self.raiz = self._insere(chave, self.raiz)

    def _insere(self, chave, raiz_sub_arvore):
        # Inserção - alterando subarvores se necessario
        if not raiz_sub_arvore:
            return No(chave)
        elif chave < raiz_sub_arvore.chave:
            raiz_sub_arvore.esquerda = self._insere(chave, raiz_sub_arvore.esquerda)
        elif chave > raiz_sub_arvore.chave:
            raiz_sub_arvore.direita = self._insere(chave, raiz_sub_arvore.direita)
        else:
            # raiz desta subarvore não é modificada quando a chave é a mesma - e não realiza inserção
            return raiz_sub_arvore

        # altura atualizada
        raiz_sub_arvore.atualiza_altura()

        # Rebalanceia a árvore de tal forma que o equilibrio sempre fique entre -1 e 1
        # Caso 1 - ??
        if raiz_sub_arvore.equilibrio > 1 and chave < raiz_sub_arvore.esquerda.chave:
            return None

        # Caso 2 - ??
        if raiz_sub_arvore.equilibrio < -1 and chave > raiz_sub_arvore.direita.chave:
            return None

        # Caso 3 - ??
        if raiz_sub_arvore.equilibrio > 1 and chave > raiz_sub_arvore.esquerda.chave:
            return None

        # Caso 4 - ??
        if raiz_sub_arvore.equilibrio < -1 and chave < raiz_sub_arvore.direita.chave:
            return None

        # caso já esteja equilibrado, a raiz subarvore não é modificada
        return raiz_sub_arvore
