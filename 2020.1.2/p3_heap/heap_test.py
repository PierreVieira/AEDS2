import unittest
from heap import *


class TestHeap(unittest.TestCase):
    def test_caminho_heap(self):
        arr_vals = [1, 2, 5]
        arr_esperado_esq = [2, 4, 10]
        arr_esperado_dir = [3, 5, 11]
        arr_esperado_pai = [0, 1, 2]
        objHeap = MaxHeap()
        [self.assertEqual(arr_esperado_esq[i], objHeap.esquerda(val),
                          f"Valor de filho a esquerda incorreto para o nodo posição {val}") for i, val in
         enumerate(arr_vals)]
        [self.assertEqual(arr_esperado_dir[i], objHeap.direita(val),
                          f"Valor de filho a direita incorreto para o nodo posição {val}") for i, val in
         enumerate(arr_vals)]
        [self.assertEqual(arr_esperado_pai[i], objHeap.pai(val), f"Valor de pai incorreto para o nodo posição {val}")
         for i, val in enumerate(arr_vals)]

    def test_refaz(self):
        # refaz um heap simples de 3 nodos
        obj_heap = MaxHeap()
        # heap que nao precisa alteração
        obj_heap.arr_heap = [None, 12, 9, 6]
        obj_heap.refaz(1)
        self.assertListEqual(obj_heap.arr_heap, [None, 12, 9, 6],
                             f"A operação refaz não foi realizada corretamente. Lista de entrada: {[None, 12, 9, 6]}")
        # heap pequeno, faz uma alteração a esquerda
        obj_heap.arr_heap = [None, 12, 15, 6]
        obj_heap.refaz(1)
        self.assertListEqual(obj_heap.arr_heap, [None, 15, 12, 6],
                             f"A operação refaz não foi realizada corretamente. Lista de entrada: {[None, 12, 15, 6]}")

        # heap pequeno, faz uma alteração a direita
        obj_heap.arr_heap = [None, 12, 9, 15]
        obj_heap.refaz(1)
        self.assertListEqual(obj_heap.arr_heap, [None, 15, 9, 12],
                             f"A operação refaz não foi realizada corretamente. Lista de entrada: {[None, 12, 9, 15]}")

        # heap grande, a partir do filho a esquerda faz uma alteração a direita e depois a esquerda
        obj_heap.arr_heap = [None, 12, 2, 6, 4, 5, -3, 0, 1, -1, 3, -2]
        obj_heap.refaz(2)
        self.assertListEqual(obj_heap.arr_heap, [None, 12, 5, 6, 4, 3, -3, 0, 1, -1, 2, -2],
                             f"A operação refaz não foi realizada corretamente. Resultado esperado: {[None, 12, 5, 6, 4, 3, -3, 0, 1, -1, 2, -2]} resultado obtido: {obj_heap.arr_heap}. Lista de entrada: {[None, 12, 2, 6, 4, 5, -3, 0, 1, -1, 3, -2]}")

        # heap grande, a partir do filho a esquerda faz uma alteração a esquerda e depois a direita
        print("-------------")
        obj_heap.arr_heap = [None, 12, 2, 4, 6, 5, -3, 0, -1, 3, 3, -2]
        obj_heap.refaz(2)
        self.assertListEqual(obj_heap.arr_heap, [None, 12, 6, 4, 3, 5, -3, 0, -1, 2, 3, -2],
                             f"A operação refaz não foi realizada corretamente. Resultado esperado: {[None, 12, 6, 4, 3, 5, -3, 0, -1, 2, 3, -2]} resultado obtido: {obj_heap.arr_heap}. Lista de entrada: {[None, 12, 2, 4, 6, 5, -3, 0, -1, 3, 3, -2]}")

    def test_retira_max(self):
        obj_heap = MaxHeap()
        obj_heap.arr_heap = [None, 12, 9, 4, 7, 5, -3, 0, -1, 2, 3, -2]

        max_val = obj_heap.retira_max()
        self.assertListEqual(obj_heap.arr_heap, [None, 9, 7, 4, 2, 5, -3, 0, -1, -2, 3],
                             f"A operação test_retira_max não finalizou com o Heap esperado. ")

    def test_insere(self):
        arr_test = [-1, 8, 11, 14]
        arr_heap_esperado = [[None, 12, 9, 6, 4, 3, 5, 2, 1, -1],
                             [None, 12, 9, 6, 8, 3, 5, 2, 1, 4],
                             [None, 12, 11, 6, 9, 3, 5, 2, 1, 4],
                             [None, 14, 12, 6, 9, 3, 5, 2, 1, 4],
                             ]
        objHeap = MaxHeap()

        # testa inserção no heap vazio
        for val_inserir in arr_test:
            objHeap = MaxHeap()
            objHeap.insere(val_inserir)
            self.assertListEqual([None, val_inserir], objHeap.arr_heap,
                                 f"Inserção incorreta ao inserir o valor {val_inserir} no heap {[None, 12, 9, 6, 4, 3, 5, 2, 1]}, esperado: {[None, val_inserir]} obtido: {objHeap.arr_heap}")

        for i, val_inserir in enumerate(arr_test):
            objHeap = MaxHeap()
            objHeap.arr_heap = [None, 12, 9, 6, 4, 3, 5, 2, 1]
            objHeap.insere(val_inserir)
            self.assertListEqual(arr_heap_esperado[i], objHeap.arr_heap,
                                 f"Inserção incorreta ao inserir o valor {val_inserir} no heap {[None, 12, 9, 6, 4, 3, 5, 2, 1]}, esperado: {arr_heap_esperado[i]} obtido: {objHeap.arr_heap}")


if __name__ == "__main__":
    unittest.main()
