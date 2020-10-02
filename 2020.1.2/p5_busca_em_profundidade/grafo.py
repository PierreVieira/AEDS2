from typing import List, Dict


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

    def e_um_dag_dfs(self, vertice: Vertice, visitados: Dict[Vertice, int]) -> bool:
        """
        vertice: vertice a ser eexplorado
        visitados: Dicionário que mapeia, cada vertice explorado.
                Se visitados[vertice]==1: o vértice ainda sendo explorado
                Se visitados[vertice]==2: o vértice já foi explorado totalmente
        """
        pass

    def ordenacao_topologica(self) -> List[Vertice]:
        pass


if __name__ == '__main__':
    grafo = Grafo()

    for i in range(7):
        grafo.adiciona_vertice(i)

    grafo.adiciona_aresta(0, 1)
    grafo.adiciona_aresta(1, 2)
    grafo.adiciona_aresta(1, 3)
    grafo.adiciona_aresta(2, 5)
    grafo.adiciona_aresta(3, 5)
    grafo.adiciona_aresta(4, 5)
    pass
