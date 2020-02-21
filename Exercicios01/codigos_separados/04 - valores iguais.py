def valores_iguais(lista1, lista2):
    """
    @author: Pierre Vieira
    :param lista1: lista de valores.
    :param lista2: lista de valores.
    :return: Valores iguais da lista1 e da lista2 em formato de lista.
    """
    return list(set(filter(lambda x: x in lista2, lista1)))  # filtre apenas os valores da lista 1 que estão na lista
    # 2, elimine os repetidos e transforme isso em uma nova lista.


if __name__ == '__main__':
    lista1 = [i // 2 for i in range(50)]
    lista2 = [i // 4 for i in range(50)]
    print(f'Lista 1: {lista1}')
    print(f'Lista 2: {lista2}')
    print(f'Valores iguais entre as listas:\n{valores_iguais(lista1, lista2)}')
