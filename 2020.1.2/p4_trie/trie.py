from typing import List


class NoTrie:
    def __init__(self, letra="", fim_palavra: bool = False):
        self.filhos = dict()
        self.fim_palavra = fim_palavra
        self.letra = letra

    def insere(self, letra: str, fim_palavra: bool):
        self.filhos[letra] = NoTrie(letra, fim_palavra)

    def existe_letra(self, letra: str) -> bool:
        return letra in self.filhos

    def obtem_no_filho(self, letra: str) -> "NoTrie":
        return self.filhos[letra]

    def nos_filhos(self):
        return self.filhos.keys()

    # Estou definindo o __str__ e __repr__ para facilitar no debug
    def __str__(self):
        return self.letra

    def __repr__(self):
        return self.__str__()


class Trie:
    def __init__(self, raiz=None):
        if not raiz:
            raiz = NoTrie()
        self.raiz = raiz

    def insere(self, palavra: str):
        no_atual = self.raiz
        tamanho_palavra = len(palavra)  # Não faz sentido chamar esse len dentro do 'for' pois perde performance
        for i, letra in enumerate(palavra):
            if not no_atual.existe_letra(letra):
                fim_palavra = i == tamanho_palavra - 1
                no_atual.insere(letra, fim_palavra)
            no_atual = no_atual.obtem_no_filho(letra)
        no_atual.fim_palavra = True

    def pesquisa(self, palavra: str) -> bool:
        no_atual = self.raiz
        for letra in palavra:
            if letra not in no_atual.filhos:
                return False
            no_atual = no_atual.obtem_no_filho(letra)
        return True

    def preditor(self, prefixo_palavra: str) -> List[str]:
        # obtem a ultima letra do prefixo
        no_ult_letra_prefixo = self.raiz
        for letra in prefixo_palavra:
            if not no_ult_letra_prefixo.existe_letra(letra):
                return []

            no_ult_letra_prefixo = no_ult_letra_prefixo.obtem_no_filho(letra)

        # por meio da ultima letra do prefixo, faz a predição das possiveis palavras
        # Para isso, você poderá precisar de fazer um método recursivo
        return self._lista_predicao(prefixo_palavra, no_ult_letra_prefixo)

    def _lista_predicao(self, prefixo_palavra, no_ult_letra_prefixo):
        """
        Esse método já leva em conta que o prefixo da palavra encontra-se na árvore
        :param prefixo_palavra: prefixo a ser preditado da árvore.
        :param no_ult_letra_prefixo: última letra da palavra
        :return: Lista com as palavras a serem previstas
        """
        if no_ult_letra_prefixo.filhos == {}:  # se o nó da última letra não tem filhos
            return [prefixo_palavra]  # a predição é a própria palavra
        return list(map(lambda word: prefixo_palavra + word, self._palavras_a_partir_de(no_ult_letra_prefixo)))

    def _palavras_a_partir_de(self, inicio_pesquisa: "NoTrie", lista_palavras=None, palavra_formada=''):
        """
        :param inicio_pesquisa: Nó em que irá começar a pesquisa de palavras
        :return: lista de todas as palavras a partir do nó de pesquisa
        """
        if lista_palavras is None:
            lista_palavras = []
        if not inicio_pesquisa.fim_palavra:
            for no_filho in inicio_pesquisa.filhos.values():
                self._palavras_a_partir_de(
                    inicio_pesquisa=no_filho,
                    lista_palavras=lista_palavras,
                    palavra_formada=palavra_formada + no_filho.letra)
                if no_filho.fim_palavra:
                    lista_palavras.append(palavra_formada+no_filho.letra)
        return lista_palavras


def main():
    # palavras criadas
    palavras = ["teste", "a", "texto", "aresta", "ano", "zebra", "trabalho"]

    # arvore Trie
    arvore = Trie()

    # insere palavras
    print("Insercao:")
    for palavra in palavras:
        arvore.insere(palavra)
        print(f"palavra -{palavra}- inserida")

    print("\n")
    # pesquisa
    print("Pesquisa:")
    print(f'-{"ano"}-: {arvore.pesquisa("ano")}')
    print(f'-{"ana"}-: {arvore.pesquisa("ana")}')
    print(f'-{"teste"}-: {arvore.pesquisa("teste")}')
    print(f'-{"testa"}-: {arvore.pesquisa("testa")}')
    print(f'-{"texto"}-: {arvore.pesquisa("texto")}')
    print(f'-{"trabalho"}-: {arvore.pesquisa("trabalho")}')


if __name__ == '__main__':
    main()
