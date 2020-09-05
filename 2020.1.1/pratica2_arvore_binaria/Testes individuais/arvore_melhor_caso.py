from pratica2_arvore_binaria.tree import Node
no = Node(5)
for value in range(1, 5):  # Vai de 1 até 4 em intervalo fechado
    no.insert(value)  # Insere o valor
for value in range(6, 9):  # Vai de 6 até 8 em intervalo fechado
    no.insert(value)  # Insere o valor
achou, qtde_execucoes = no.search(5, retornar_cont_search=True)  # Melhor caso da busca ocorre quando estamos
# pesquisando na raiz
print('\033[1;36m' + '='*21 + ' MELHOR CASO ' + '='*21+'\033[m')
if achou:
    print(f'\033[0;32mO valor foi encontrado após\033[m \033[1;31m{qtde_execucoes}\033[m \033[0;32mchamadas do método '
          f'search\033[m')
else:
    print(f'\033[0;32mO valor pesquisado não foi enxontrado.\033[m\n\033[0;32mO método search foi executado\033[m '
          f'\033[1;31m{qtde_execucoes}\033[m \033[0;32mvezes\033[m')
