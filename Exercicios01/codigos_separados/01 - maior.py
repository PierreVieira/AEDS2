def maior(a, b):
    """
    Retorna o maior número entre 'a' e 'b'.
    @author: Pierre Vieira
    """
    if a > b:  # Se 'a' maior que 'b'
        return a  # Retorne 'a'
    return b  # Retorne 'b'


if __name__ == '__main__':
    a, b = map(int, input('Informe dois valores em sequência: ').split())
    print(f'O maior valor entre {a} e {b} é {maior(a, b)}')
