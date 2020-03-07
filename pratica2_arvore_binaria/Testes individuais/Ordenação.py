from pratica2_arvore_binaria.tree import Node

root = Node(5)
root.insert(6)
root.insert(4)
print(root.to_sorted_array())  # resultado esperado [4,5,6]
