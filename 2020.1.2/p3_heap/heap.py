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
        """
        Professor Hasan, caso esteja lendo isso saiba que apaguei o seu código que estava aqui e fiz do meu jeito.
        Funciona da mesma forma :)
        Implementação de Pierre Vieira.
        Refaz o vetor completo do heap
        :param pos_raiz_sub_arvore: Não estou utilizando, é irrelevante na minha implementação.
        :return: None
        """
        tamanho_heap = len(self.arr_heap) - 1
        if tamanho_heap > 2:
            tamanho_metade_heap = tamanho_heap // 2
            while True:
                heap_equilibrado = True
                for i in range(1, tamanho_metade_heap + 1):
                    if i == tamanho_metade_heap and tamanho_heap % 2 == 0:
                        pos_filho_maior = 2 * i
                    else:
                        pos_filho_maior = self.arr_heap.index(max(self.arr_heap[2 * i], self.arr_heap[2 * i + 1]))
                    if self.arr_heap[i] < self.arr_heap[pos_filho_maior]:
                        heap_equilibrado = False
                        self.arr_heap[i], self.arr_heap[pos_filho_maior] = self.arr_heap[pos_filho_maior], self.arr_heap[i]
                if heap_equilibrado:
                    break

    def retira_max(self):
        if len(self.arr_heap) <= 1:
            raise IndexError("Heap Vazio")
        # Faça a retirada do máximo conforme especificação/slides da aula teórica
        maximo = self.arr_heap.pop(self.arr_heap.index(max(self.arr_heap[1:])))
        self.arr_heap.insert(1, self.arr_heap.pop(self.arr_heap.index(self.arr_heap[-1])))
        self.refaz(1)
        return maximo

    def insere(self, item):
        """
        Professor Hasan, caso esteja lendo isso saiba que apaguei o seu código que estava aqui e fiz do meu jeito.
        Funciona da mesma forma :)
        Implementação de Pierre Vieira.
        Insere um elemento no heap.
        :param item: item a ser inserido no heap
        :return: None
        """
        self.arr_heap.append(item)
        self.refaz(1)
