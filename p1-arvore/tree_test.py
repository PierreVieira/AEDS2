import unittest
from tree import Node


class TestNode(unittest.TestCase):
    def setUp(self):
        self.arr_tests = []

        self.arr_tests.append(Node(5))

        self.arr_tests.append(Node(3))
        self.arr_tests[1].insert(4)
        self.arr_tests[1].insert(5)
        self.arr_tests[1].insert(6)
        self.arr_tests[1].insert(8)
        self.arr_tests[1].insert(9)
        self.arr_tests[1].insert(10)
        self.arr_tests[1].insert(15)

        self.arr_tests.append(Node(5))
        self.arr_tests[2].insert(3)
        self.arr_tests[2].insert(4)
        self.arr_tests[2].insert(8)
        self.arr_tests[2].insert(6)
        self.arr_tests[2].insert(10)
        self.arr_tests[2].insert(9)

        self.arr_tests.append(Node(3))
        self.arr_tests[3].insert(4)
        self.arr_tests[3].insert(5)
        self.arr_tests[3].insert(10)
        self.arr_tests[3].insert(6)
        self.arr_tests[3].insert(8)
        self.arr_tests[3].insert(9)
        self.arr_tests[3].insert(15)

        self.arr_tests.append(Node(8))

        self.arr_tests.append(Node(6))
        self.arr_tests[5].insert(5)
        self.arr_tests[5].insert(4)
        self.arr_tests[5].insert(3)
        self.arr_tests[5].insert(10)
        self.arr_tests[5].insert(9)
        self.arr_tests[5].insert(8)
        self.arr_tests[5].insert(15)

        self.arr_tests.append(Node(5))
        self.arr_tests[6].insert(3)
        self.arr_tests[6].insert(4)
        self.arr_tests[6].insert(8)
        self.arr_tests[6].insert(6)
        self.arr_tests[6].insert(10)
        self.arr_tests[6].insert(9)

    def test_to_sorted_array(self):
        arr_expected = [3, 4, 5, 6, 8, 9, 10, 15]

        self.assertListEqual(self.arr_tests[0].to_sorted_array(), [5], "Erro na primeira árvore de teste")

        for i in range(1, 4):
            if i == 2:
                self.assertListEqual(self.arr_tests[i].to_sorted_array(), [3, 4, 5, 6, 8, 9, 10],
                                     f"Erro na árvore de teste posição {i}")
            else:
                self.assertListEqual(self.arr_tests[i].to_sorted_array(), arr_expected,
                                     f"Erro na árvore de teste posição {i}")

    def test_max_depth(self):
        arr_expected = [1, 8, 4, 7]

        for i in range(0, 4):
            self.assertEqual(arr_expected[i], self.arr_tests[i].max_depth(), f"Erro na árvore posição {i}")

    def test_position_node(self):
        arr_expected = [61, 1, 12, 3]

        for i in range(3, 7):
            self.assertEqual(self.arr_tests[i].position_node(8), arr_expected[i - 3],
                             f"Erro na árvore de teste posição {i - 3}")


if __name__ == "__main__":
    unittest.main()
