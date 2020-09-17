from banco import *

banco = CaixaBanco('Banco Heap')
clientes = [
    Cliente('Pierre', 20, False),
    Cliente('Joaquim', 84, False),
    Cliente('Ana', 42, False),
    Cliente('Jonas', 56, True),
    Cliente('Alex', 24, False),
    Cliente('Fernando', 76, False),
    Cliente('Matt', 30, True)
]


def inserir_clientes():
    print('\n========== ORDEM DE ENTRADA ==========\n')
    for cliente in clientes:
        print(cliente)
        banco.adiciona_cliente(cliente)


def remover_clientes():
    print('\n========== ORDEM DE PRIORIDADE ==========\n')
    while banco.tem_cliente:
        print(' '.join(str(banco.proximo_cliente()).split()[1:]))


inserir_clientes()
remover_clientes()
