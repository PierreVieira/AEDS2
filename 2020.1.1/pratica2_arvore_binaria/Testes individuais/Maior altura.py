from pratica2_arvore_binaria.tree import Node

root = Node(5)
root.insert(6)
root.insert(4)
root.insert(3)
print(root.max_depth())  # resultado esperado: 3
