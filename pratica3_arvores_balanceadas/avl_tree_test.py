import unittest
from pratica3_arvores_balanceadas.avl_tree import *


class TestAVL(unittest.TestCase):
    def assertSegundoNivel(self, raiz_subarvore, arr_nos_esperados, str_direcao):

        if not raiz_subarvore.esquerda:
            self.assertIsNone(arr_nos_esperados[0], f"Referencia a raiz->{str_direcao}->esquerda incorreta")
        else:
            self.assertEqual(raiz_subarvore.esquerda.chave, arr_nos_esperados[0],
                             f"Referencia a raiz->{str_direcao}->esquerda incorreta")
        if not raiz_subarvore.direita:
            self.assertIsNone(arr_nos_esperados[1], f"Referencia a raiz->{str_direcao}->direita incorreta")
        else:
            self.assertEqual(raiz_subarvore.direita.chave, arr_nos_esperados[1],
                             f"Referencia a raiz->{str_direcao}->direita incorreta")

    def arvore_tres_niveis_test(self, nova_raiz, arr_nos_esperados):
        self.assertEqual(nova_raiz.chave, arr_nos_esperados[0], f"A nova raiz não é a {nova_raiz.chave}")
        self.assertEqual(nova_raiz.esquerda.chave, arr_nos_esperados[1], "Referencia a esquerda da raiz incorreta")
        self.assertEqual(nova_raiz.direita.chave, arr_nos_esperados[2], "Referencia a direita da raiz incorreta")
        self.assertSegundoNivel(nova_raiz.esquerda, arr_nos_esperados[3:5], "esquerda")
        self.assertSegundoNivel(nova_raiz.direita, arr_nos_esperados[5:7], "direita")

    def inicializa_nodos(self, arr_chaves):
        arr_nos = [No(chave) for chave in arr_chaves]
        for no in arr_nos:
            no.altura = 1000
        return arr_nos

    def atualiza_altura_test(self, arr_nos, nova_raiz):
        self.assertNotEqual(nova_raiz.altura, 1000, "A atualização da altura está incorreta")
        self.assertNotEqual(arr_nos[0].altura, 1000, "A atualização da altura está incorreta")
        [self.assertEqual(no.altura, 1000, "A atualização da altura está incorreta") for no in arr_nos if
         no.chave != arr_nos[0].chave and no.chave != nova_raiz.chave]

    def test_rotacao_esquerda(self):
        # constroi a arvore teste
        arr_nos = self.inicializa_nodos([13, 6, 15, 14, 17, 18])

        arr_nos[0].esquerda = arr_nos[1]
        arr_nos[0].direita = arr_nos[2]

        arr_nos[2].esquerda = arr_nos[3]
        arr_nos[2].direita = arr_nos[4]

        arr_nos[4].direita = arr_nos[5]

        avl = AVL(arr_nos[0])
        nova_raiz = avl.rotacao_esquerda(arr_nos[0])
        self.atualiza_altura_test(arr_nos, nova_raiz)

        avl = AVL(nova_raiz)
        arr_nos_esperados = [15, 13, 17, 6, 14, None, 18]  # busca em largura na arvore
        self.arvore_tres_niveis_test(nova_raiz, arr_nos_esperados)

    def test_rotacao_direita(self):
        # constroi a arvore teste
        arr_nos = self.inicializa_nodos([13, 6, 15, 4, 14, 3])

        arr_nos[0].esquerda = arr_nos[1]
        arr_nos[0].direita = arr_nos[2]

        arr_nos[1].esquerda = arr_nos[3]
        arr_nos[1].direita = arr_nos[4]

        arr_nos[3].esquerda = arr_nos[5]

        avl = AVL(No(100))
        nova_raiz = avl.rotacao_direita(arr_nos[0])
        self.atualiza_altura_test(arr_nos, nova_raiz)

        arr_nos_esperados = [6, 4, 13, 3, None, 14, 15]
        self.arvore_tres_niveis_test(nova_raiz, arr_nos_esperados)

    def test_rotacao_dupla_esquerda(self):
        # constroi a arvore teste
        arr_nos = self.inicializa_nodos([12, 6, 16, 14, 17, 13])

        arr_nos[0].esquerda = arr_nos[1]
        arr_nos[0].direita = arr_nos[2]

        arr_nos[2].esquerda = arr_nos[3]
        arr_nos[2].direita = arr_nos[4]

        arr_nos[3].esquerda = arr_nos[5]

        avl = AVL(No(100))
        nova_raiz = avl.rotacao_dupla_esquerda(arr_nos[0])
        arr_nos_esperados = [14, 12, 16, 6, 13, None, 17]
        self.arvore_tres_niveis_test(nova_raiz, arr_nos_esperados)

    def test_rotacao_dupla_direita(self):
        # constroi a arvore teste
        arr_nos = self.inicializa_nodos([13, 6, 15, 4, 9, 8])

        arr_nos[0].esquerda = arr_nos[1]
        arr_nos[0].direita = arr_nos[2]

        arr_nos[1].esquerda = arr_nos[3]
        arr_nos[1].direita = arr_nos[4]

        arr_nos[4].esquerda = arr_nos[5]

        avl = AVL(arr_nos[0])
        nova_raiz = avl.rotacao_dupla_direita(arr_nos[0])
        arr_nos_esperados = [9, 6, 13, 4, 8, None, 15]
        self.arvore_tres_niveis_test(nova_raiz, arr_nos_esperados)

    def test_insere(self):
        root = No(10)
        avl = AVL(root)

        root = No(10)
        avl = AVL(root)

        avl.insere(10)
        avl.insere(20)
        avl.insere(30)
        avl.insere(16)
        avl.insere(14)
        avl.insere(15)
        self.assertEqual(avl.raiz.altura, 3, "A árvore não ficou balanceada corretamente")

        root = No(10)
        avl = AVL(root)
        avl.insere(10)
        avl.insere(20)
        avl.insere(30)
        avl.insere(16)
        avl.insere(14)
        avl.insere(15)
        self.assertEqual(avl.raiz.altura, 3, "A árvore não ficou balanceada corretamente")


if __name__ == "__main__":
    unittest.main()
