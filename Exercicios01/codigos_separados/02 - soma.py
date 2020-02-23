def soma(lista, x=0.0):
    """
    @author: Pierre Vieira
    :param lista: Lista de valores numéricos.
    :param x: Parâmetro opcional que será somado ao valor da lista. Vale 0 se não for informado.
    :return: Soma dos valores da lista + x.
    """
    s = 0  # A soma começa inicialmente com 0
    for numero in lista:  # Para cada número na lista
        s += numero  # A soma é acrescentada pelo número
    return s + x  # A soma final é a soma calculada acrescentada do parâmetro opcional x


if __name__ == '__main__':
    lista = [i + 1 for i in range(10)]
    print(f'A soma dos termos de \033[1;33m{lista}\033[m é \033[1;31m{soma(lista)}\033[m')
    print(f'A soma dos termos de \033[1;33m{lista}\033[m somado à \033[1;34m5\033[m é \033[1;31m{soma(lista, 5)}\033[m')
