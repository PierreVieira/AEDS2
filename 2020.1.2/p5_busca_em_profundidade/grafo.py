from typing import List


class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.adjacencias = {}
        self.lista_ligados = []  # criação do atributo ligados para facilitar o debug

    def insere(self, vizinho: "Vertice", peso: int):
        self.adjacencias[vizinho] = peso
        self.lista_ligados.append(vizinho)

    def obtem_valor(self):
        return self.valor

    # Definindo __str__ e __repr__ para facilitar no debug
    def __str__(self):
        valor = self.valor
        return str(valor) + ' | ' + str([vertice.valor for vertice in self.lista_ligados])

    def __repr__(self):
        return self.__str__()


class Grafo:
    def __init__(self):
        self.vertices = {}

    def adiciona_vertice(self, valor_vertice) -> Vertice:
        # importante pois podem haver vertices que não tem arestas
        novo_vertice = Vertice(valor_vertice)
        self.vertices[valor_vertice] = novo_vertice
        return novo_vertice

    def obtem_vertice(self, valor_vertice: str) -> Vertice:
        try:
            return self.vertices[valor_vertice]
        except KeyError:
            raise KeyError(f'O vértice {valor_vertice} não foi encontrado.')

    def adiciona_aresta(self, valor_origem, valor_destino, peso: int = 1):
        try:
            vertice_origem = self.obtem_vertice(valor_origem)
            vertice_destino = self.obtem_vertice(valor_destino)
        except KeyError:
            pass
        else:
            vertice_origem.insere(vertice_destino, peso)

    def _apontados(self, atual: "Vertice") -> List["Vertice"]:
        return self.vertices[atual.valor].lista_ligados

    def e_um_dag(self) -> bool:
        """
        :return: True se o grafo é um dag. False se o grafo não for um dag.
        """
        visitados = set()
        restantes = [[vertice for vertice in self.vertices.values()][0]]
        while restantes:
            atual = restantes.pop()
            visitados.add(atual.valor)
            for apontado in self._apontados(atual):
                if apontado.valor in visitados and apontado.adjacencias != {}:
                    for apontado_do_apontado in self._apontados(apontado):
                        if atual in self._apontados(apontado_do_apontado):
                            return False
                restantes.append(apontado)
        return True

    def ordenacao_topologica(self) -> List:
        """
        :return: Vértices ordenados por dependência
        """
        graus_entrada = self._calcula_grau_entrada_vertices()
        fila = self._vertices_grau_zero(graus_entrada)
        return self._ordem_topologica_baseada_no_grau_de_entrada(fila, graus_entrada)

    def _ordem_topologica_baseada_no_grau_de_entrada(self, fila, graus_entrada) -> List:
        """
        :param fila: fila que contém os vértices de grau 0
        :param graus_entrada: lista de grau de cada vértice
        :return: Vértices ordenados por dependência
        """
        ordem_topologica = []
        while fila:
            vertice = fila.pop()
            ordem_topologica.append(vertice)
            self._atualiza_grau_entrada_vizinhos(fila, graus_entrada, vertice)
        return ordem_topologica

    def _atualiza_grau_entrada_vizinhos(self, fila, graus_entrada, vertice):
        for vizinho in self.vertices[vertice].lista_ligados:
            graus_entrada[vizinho.valor] -= 1
            if graus_entrada[vizinho.valor] == 0:
                fila.append(vizinho.valor)

    def _vertices_grau_zero(self, graus_entrada):
        """
        :param graus_entrada: Lista contendo o valor de grau de entrada dos vértices do grafo.
        :return: lista de valores dos vértices que contém grau 0.
        """
        return list(filter(lambda i: graus_entrada[i] == 0, [i for i in range(len(self))]))

    def _calcula_grau_entrada_vertices(self):
        """
        :return: Lista com o grau de entrada de cada vértice do grafo.
        """
        graus_entrada = [0] * len(self)
        for vertice in self.vertices.keys():
            for vizinho in self.vertices[vertice].lista_ligados:
                graus_entrada[vizinho.valor] += 1
        return graus_entrada

    def __len__(self):
        return len(self.vertices)


def criar_grafo_teste() -> Grafo:
    grafo = Grafo()
    for i in range(11):
        grafo.adiciona_vertice(i)
    adicionar_arestas_grafo(grafo)
    return grafo


def adicionar_arestas_grafo(grafo):
    grafo.adiciona_aresta(0, 1)  # Geometria Analítica e Álgebra Vetorial -> Cálculo 2
    grafo.adiciona_aresta(1, 2)  # Cálculo 1 -> Cálculo 2
    grafo.adiciona_aresta(1, 5)  # Cálculo 1 -> Física 1
    grafo.adiciona_aresta(2, 10)  # Cálculo 2 -> Álgebra Linear
    grafo.adiciona_aresta(2, 3)  # Cálculo 2 -> Cálculo 3
    grafo.adiciona_aresta(2, 6)  # Cálculo 2 -> Física 2
    grafo.adiciona_aresta(3, 4)  # Cálculo 3 -> Cálculo 4
    grafo.adiciona_aresta(5, 8)  # Física 1 -> Física Experimental 1
    grafo.adiciona_aresta(5, 6)  # Física 1 -> Física 2
    grafo.adiciona_aresta(6, 9)  # Física 2 -> Física Experimental 2
    grafo.adiciona_aresta(6, 7)  # Física 2 -> Física 3
    grafo.adiciona_aresta(8, 9)  # Física Experimental 1 -> Física Experimental 2


if __name__ == '__main__':
    dict_materias = {
        0: 'Geometria Analítica e Álgebra Vetorial',
        1: 'Cálculo 1',
        2: 'Cálculo 2',
        3: 'Cálculo 3',
        4: 'Cálculo 4',
        5: 'Física 1',
        6: 'Física 2',
        7: 'Física 3',
        8: 'Física Experimental 1',
        9: 'Física Experimental 2',
        10: 'Álgebra Linear',
    }
    grafo = criar_grafo_teste()
    print(list(map(lambda key: dict_materias[key], grafo.ordenacao_topologica())))
