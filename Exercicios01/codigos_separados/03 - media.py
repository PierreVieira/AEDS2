from Exercicios01.ex01 import soma


def media(lista):
    """
    @author: Pierre Vieira
    :param lista: Lista de valores inteiros numéricos.
    :return: Média dos valores da lista.
    """
    s = soma(lista)  # Faz a soma dos elementos da lista
    qtde_termos = 0
    for c in lista:
        qtde_termos += 1
    return s/qtde_termos


if __name__ == '__main__':
    lista = [i + 1 for i in range(10)]
    print(f'Lista: {lista}')
    print(f'A media dos termos {lista} vale {media(lista)}')
