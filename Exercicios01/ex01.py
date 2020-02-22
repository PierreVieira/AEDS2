def maior(a, b):
    """
    Retorna o maior número entre 'a' e 'b'.
    @author: Pierre Vieira
    """
    if a > b:
        return a
    return b


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


def valores_iguais(lista1, lista2):
    """
    @author: Pierre Vieira
    :param lista1: lista de valores.
    :param lista2: lista de valores.
    :return: Valores iguais da lista1 e da lista2 em formato de lista.
    """
    return list(set(filter(lambda x: x in lista2, lista1)))  # filtre apenas os valores da lista 1 que estão na lista
    # 2, elimine os repetidos e transforme isso em uma nova lista.


def indice_prim_valor_igual(lista1: list, lista2: list):
    """
    @author: Pierre Vieira
    :param lista1: lista de valores.
    :param lista2: lista de valores.
    :return: Posição na lista1 do primeiro valor igual ao da lista2 ou None caso essa posição não exista.
    """
    for n in lista2:  # Para um número 'n' na lista 2
        try:  # tente
            return lista1.index(n)  # Retorne a primeira posição de n em lista 1
        except ValueError:  # Exceto se ocorrer um ValueError
            pass  # Não faça nada
    return None  # Retorne None


if __name__ == '__main__':
    lista1 = [i // 4 for i in range(50)]
    lista2 = [(i + 8) // 5 for i in range(50)]
    print(f'Lista 1: {lista1}\nLista 2: {lista2}')
    print(f'Soma dos elementos da lista 1: {soma(lista1)}')
    print(f'Soma dos elementos da lista 1 e o valor numérico 7.3: {soma(lista1, 7.3)}')
    print(f'Média dos elementos da lista 2: {media(lista2):.2f}')
    print(f'Valores iguais entre as listas 1 e 2: {valores_iguais(lista1, lista2)}')
    print(f'Posição na lista 1 do primeiro valor igual ao da lista 2: ')
    indice = indice_prim_valor_igual(lista1, lista2)
    if indice is not None:
        print(indice)
    else:
        print('Essa posição não existe!')
