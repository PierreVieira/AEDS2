import unittest
from trie import Trie


class TestNode(unittest.TestCase):
    def setUp(self):
        pass

    def teste_pesquisa(self):
        chaves = ["teste", "a", "texto", "aresta", "ano",
                  "zebra", "trabalho"]

        arr_palavras = ["ano", "ana", "teste", "testa", "texto", "trabalho", "a"]
        arr_esperado = [True, False, True, False, True, True, True]

        arvore = Trie()

        for palavra in chaves:
            arvore.insere(palavra)

        for i, palavra in enumerate(arr_palavras):
            self.assertEqual(arvore.pesquisa(palavra), arr_esperado[i],
                             f"Erro na árvore de teste: a palavra {palavra} não foi encontrada")

    def teste_preditor(self):
        chaves = ["compor", "comer", "prefacio", "presente", "prever", "praticar"]

        arr_palavras = ["co", "com", "pre", "pr"]
        arr_esperado = [2, 2, 3, 4]

        arvore = Trie()

        for palavra in chaves:
            arvore.insere(palavra)

        for i, palavra in enumerate(arr_palavras):
            self.assertEqual(len(arvore.preditor(palavra)), arr_esperado[i],
                             f"Erro ao tentar prever as palavras com o prefixo {palavra}")


if __name__ == "__main__":
    unittest.main()
