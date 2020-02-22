def media(lista):
    """
    @author: Pierre Vieira
    :param lista: Lista de valores inteiros numéricos.
    :return: Média dos valores da lista.
    """
    s = 0
    qtde_termos = 0
    for num in lista:  # Para cada número na lista
        s += num  # Adicione esse número à soma
        qtde_termos += 1  # A quantidade de termos é incrementada
    return s/qtde_termos  # A média é a soma dividida pela quantidade de termos


if __name__ == '__main__':
    lista = [i + 1 for i in range(10)]
    print(f'Lista: {lista}')
    print(f'A media dos termos {lista} vale {media(lista)}')
