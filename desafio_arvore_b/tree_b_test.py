"""
Autor: Pierre Vieira
Github: https://github.com/PierreVieira/LAEDS_II/tree/master/desafio_arvore_b
"""

import unittest
from desafio_arvore_b.tree_b.arvore_b import Tree_b


class Tree_b_Test(unittest.TestCase):
    def arvore_com_elementos(self, qtde_maxima_elementos_por_pagina, raiz, valores):
        arvore_b = Tree_b(qtde_maxima_elementos_por_pagina, raiz)
        for value in valores:
            arvore_b.insert(value)
        return arvore_b

    def test_insert(self):
        arvore1 = self.arvore_com_elementos(2, 11, [8, 11, 27, 31, 25, 16, 59, 53, 52, 21, 36, 48, 78, 81, 75, 95, 90, 91, 72, 63, 20, 35])
        arvore2 = self.arvore_com_elementos(2, 20, [20, 10, 40, 50, 30, 55, 3, 11, 4, 28, 36, 33, 52, 17, 25, 13, 45, 9, 43, 8, 48])
