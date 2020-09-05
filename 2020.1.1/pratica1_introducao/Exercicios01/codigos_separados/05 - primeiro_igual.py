def indice_prim_valor_igual(lista1: list, lista2: list):
    """
    @author: Pierre Vieira
    :param lista1: lista de valores.
    :param lista2: lista de valores.
    :return: Posição na lista1 do primeiro valor igual ao da lista2 ou None caso essa posição não exista.
    """
    for n in lista2:  # Para um número 'n' na lista 2
        try:  # Tente
            return lista1.index(n)  # Retorne a primeira posição de n em lista 1
        except ValueError:  # Exceto se ocorrer um ValueError
            pass  # Não faça nada
    return None  # Retorne None


if __name__ == '__main__':
    lista1 = [i // 4 for i in range(50)]
    lista2 = [(i + 8) // 5 for i in range(50)]
    posicao = indice_prim_valor_igual(lista1, lista2)
    print(f'Lista 1: \033[1;33m{lista1}\033[m')
    print(f'Lista 2: \033[1;33m{lista2}\033[m')
    if posicao is not None:
        print(f'A posição na lista 1 do primeiro valor igual à lista 2 é \033[1;31m{posicao}\033[m')
    else:
        print('A lista 1 e a lista 2 não tem valores iguais.')
