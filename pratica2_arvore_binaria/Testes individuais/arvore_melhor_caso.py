from pratica2_arvore_binaria.tree import Node
lista_valores_nos = [i for i in range(8, -1, -1)]  # Cria uma lista que vai de 1 até 0 em intervalo fechado
raiz = Node(lista_valores_nos[0])  # A raiz pega o valor 8
for valor in lista_valores_nos[1:]:  # Para cada valor na lista de valores dos nós (começando do segundo)
    raiz.insert(valor)  # Insira esse novo nó na àrvore
encontrou_valor_8, quantidade_de_chamadas = raiz.search(8, retornar_cont_search=True)
if encontrou_valor_8:  # Verifica se o valor 8 foi encontrado na àrvore
    print(f'O valor 8 foi encontrado após {quantidade_de_chamadas} chamadas do método search')
else:  # Se não foi encontrado
    print(f'O valor 8 não existe na àrvore.')
