from pratica2_arvore_binaria.tree import Node
lista_valores_nos = [i + 1 for i in range(8)]  # Cria uma lista que vai de 1 até 8 em intervalo fechado
raiz = Node(lista_valores_nos[0])  # A raiz pega o valor 1
for valor in lista_valores_nos[1:]:  # Para cada valor na lista de valores dos nós (começando do segundo)
    raiz.insert(valor)  # Insira esse novo nó na àrvore
achou, quantidade_de_chamadas = raiz.search(8, retornar_cont_search=True)
print('\033[1;36m' + '='*22 + ' PIOR CASO ' + '='*22+'\033[m')
if achou:
    print(f'\033[0;32mO valor foi encontrado após\033[m \033[1;31m{quantidade_de_chamadas}\033[m \033[0;32mchamadas '
          f'do método search\033[m')
else:
    print(f'\033[0;32mO valor pesquisado não foi enxontrado.\033[m\n\033[0;32mO método search foi executado\033[m '
          f'\033[1;31m{quantidade_de_chamadas}\033[m \033[0;32mvezes\033[m')
