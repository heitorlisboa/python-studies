idades = [15, 87, 32, 65, 56, 32, 49, 37]

for valor in enumerate(idades):
    print(valor)

for i, idade in enumerate(idades):
    print(f'{i} x {idade}')

# Também é possível criar listas com o enumerate

i_idade = list(enumerate(idades))  # É necessário usar o 'list()' ao invés do '[]',
print(i_idade)                     # pois quando se utiliza o '[]', a lista recebe
                                   # o endereço do enumerate (já que é uma função lazy,
                                   # ou seja, que só faz algo quando é ordenada a fazê-lo).
