def soma(lista, x=0.0):
    """
    @author: Pierre Vieira
    :param lista: Lista de valores numéricos.
    :param x: Parâmetro opcional que será somado ao valor da lista. Vale 0 se não for informado.
    :return: Soma dos valores da lista + x.
    """
    s = 0
    for numero in lista:
        s += numero
    return s + x


if __name__ == '__main__':
    lista = [i + 1 for i in range(10)]
    print(f'A soma dos termos de {lista} é {soma(lista)}')
    print(f'A soma dos termos de {lista} somado à 5 é {soma(lista, 5)}')
