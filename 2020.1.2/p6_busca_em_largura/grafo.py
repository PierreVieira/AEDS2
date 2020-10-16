from typing import List, Dict


class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.adjacencias = {}

    def insere(self, vizinho: "Vertice", peso: int):
        self.adjacencias[vizinho] = peso

    def obtem_valor(self):
        return self.valor

    # definindo __str__ e __repr__ para facilitar no debug
    def __str__(self):
        return str(self.valor)

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

    def adiciona_aresta(self, valor_origem, valor_destino, peso: int = 1):
        vertice_origem = self.obtem_vertice(valor_origem)
        vertice_destino = self.obtem_vertice(valor_destino)
        if vertice_origem is not None and vertice_destino is not None:
            vertice_origem.insere(vertice_destino, peso)

    def obtem_vertice(self, valor_vertice) -> Vertice:
        if valor_vertice in self.vertices:
            return self.vertices[valor_vertice]

    def _inicializa_distancias(self, distancia):
        for vertice in self.vertices.values():
            distancia[vertice] = float("inf")

    def _calcula_grau_separacao(self, distancia, vertice_inicial):
        fila = [vertice_inicial]
        distancia[vertice_inicial] = 0
        while len(fila) > 0:
            v = fila.pop(0)
            for w in v.adjacencias.keys():
                if distancia[w] == float("inf"):
                    distancia[w] = distancia[v] + 1
                    fila.append(w)

    def grau_separacao(self, valor_vertice_origem) -> Dict[Vertice, int] or None:
        distancia = {}
        vertice_inicial = self.obtem_vertice(valor_vertice_origem)
        if not vertice_inicial:
            return None
        self._inicializa_distancias(distancia)
        self._calcula_grau_separacao(distancia, vertice_inicial)
        return distancia


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
    print(list(map(lambda key: {dict_materias[key]: list(map(lambda tup: (dict_materias[tup[0].valor], tup[1]), list(grafo.grau_separacao(key).items())))}, dict_materias.keys())))
