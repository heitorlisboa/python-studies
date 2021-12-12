usuarios = {1, 3, 5, 76, 32}

usuarios.add(54)
# Método equivalente ao 'append' das listas, porém, como não
# adiciona ao final do conjunto, já que ele não tem ordem,
# é chamado de 'add'.

print(usuarios)

# É possível criar um frozen set, que é um set IMUTÁVEL
usuarios = frozenset(usuarios) 

print(usuarios)

usuarios.add(134)  # Dá erro pois não existe o método 'add' para frozen set
