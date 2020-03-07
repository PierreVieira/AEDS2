def maior(a, b):
    """
    Retorna o maior número entre 'a' e 'b'.
    @author: Pierre Vieira
    """
    if a > b:  # Se 'a' maior que 'b'
        return a  # Retorne 'a'
    return b  # Retorne 'b'


if __name__ == '__main__':
    print(f'\033[1;34m1º teste (a > b): \033[m{maior(5, 2)}')
    print(f'\033[1;34m2º teste (a < b): \033[m{maior(8, 5)}')
    print(f'\033[1;34m3º teste (a = b): \033[m{maior(3, 3)}')
