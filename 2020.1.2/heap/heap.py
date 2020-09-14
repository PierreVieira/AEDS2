from functools import total_ordering


class MaxHeap:
    def __init__(self):
        # inicia com o heap com um elemento sentinela (que nunca será acessado)
        self.arr_heap = [None]

    def __str__(self):
        return str(self.arr_heap[1:])

    def __repr__(self):
        return str(self)

    # Os metodos esquerda, direita e pai serão usados nos demais metodos do heap
    def esquerda(self, i: int) -> int:
        """
            Retorna a posição do filho a esquerda de i
        """
        return 2 * i

    def direita(self, i: int) -> int:
        """
            Retorna a posição do filho a direita de i
        """
        return 2 * i + 1

    def pai(self, i: int) -> int:
        """
        Retorna a posição do pai do i-ésimo nó
        """
        return i // 2

    @property
    def pos_ultimo_item(self):
        return len(self.arr_heap) - 1

    def refaz(self, pos_raiz_sub_arvore: int):

        # maior_filho é inicializado com o da esquerda de pos raiz subarvore
        pos_pai = pos_raiz_sub_arvore
        pos_maior_filho = self.esquerda(pos_pai)

        # obtem o item raiz da subarvore do heap
        val_raiz_sub_arvore = self.arr_heap[pos_raiz_sub_arvore]

        while pos_maior_filho <= self.pos_ultimo_item:
            # se a posição do filho a esquerda não for a ultima do vetor,
            # atualize, se necessario, o pos_maior_filho considerando o filho a direita
            if pos_maior_filho < self.pos_ultimo_item:
                if self.arr_heap[self.esquerda(pos_raiz_sub_arvore)] < self.arr_heap[self.direita(pos_raiz_sub_arvore)]:
                    pos_maior_filho = self.direita(pos_raiz_sub_arvore)

            # caso o valor da  raiz desta subarvore (val_raiz_sub_arvore)
            # possua um valor maior que o de seus filhos,
            # finaliza o while 
            if val_raiz_sub_arvore > self.arr_heap[pos_maior_filho]:
                break

            # realize a troca conforme especificação
            self.arr_heap[pos_maior_filho], val_raiz_sub_arvore = val_raiz_sub_arvore, self.arr_heap[pos_maior_filho]
            try:
                if self.arr_heap[pos_maior_filho] < self.arr_heap[pos_maior_filho * 2]:
                    self.arr_heap[pos_maior_filho], self.arr_heap[pos_maior_filho * 2] = self.arr_heap[pos_maior_filho * 2], self.arr_heap[pos_maior_filho]
                elif self.arr_heap[pos_maior_filho] < self.arr_heap[pos_maior_filho * 2 + 1]:
                    self.arr_heap[pos_maior_filho], self.arr_heap[pos_maior_filho * 2 + 1] = self.arr_heap[pos_maior_filho * 2 + 1], self.arr_heap[pos_maior_filho]
            except IndexError:
                pass

            # prepare as variáveis pos_pai e pos_maior_filho para a proxima iteração
            # substitua os "None" das duas linhas abaixo apropriadamente
            pos_pai = self.pai(pos_maior_filho)
            pos_maior_filho = self.esquerda(pos_pai)

        # atualize a posição pos_pai apropriadamente
        self.arr_heap[pos_pai] = val_raiz_sub_arvore
        pass

    def retira_max(self):
        if len(self.arr_heap) <= 1:
            raise IndexError("Heap Vazio")
        # Faça a retirada do máximo conforme especificação/slides da aula teórica
        maximo = self.arr_heap.pop(self.arr_heap.index(max(self.arr_heap[1:])))
        ultimo = self.arr_heap.pop()
        self.arr_heap.insert(1, ultimo)
        self.refaz(1)
        return maximo

    def insere(self, item):
        pass
        # self.arr_heap.append(None)
        # pos_inserir = self.pos_ultimo_item
        # pai_pos_inserir = self.pai(pos_inserir)
        #
        # # substitua o "None" apropriadamente
        # while pos_inserir > 1 and None:
        #     # realiza a atualização (substitua os "None")
        #     self.arr_heap[None] = None
        #
        #     # ajusta para a proxima iteração (substitua os None apropriadamente)
        #     pos_inserir = None
        #     pai_pos_inserir = None
        #
        # # finalize o insere apropriadamente
        # None
