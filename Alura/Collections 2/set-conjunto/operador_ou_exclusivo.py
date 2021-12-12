usuarios_data_science = {13, 54, 23, 46}
usuarios_machine_learning = {13, 92, 23, 35}

assistiram = usuarios_data_science ^ usuarios_machine_learning
# Utilizando o símbolo '^' ("ou exclusivo"), se faz a UNIÃO de
# conjuntos, EXCETO dos elementos da INTERSECÇÃO,
# ou seja, une elementos únicos de cada conjunto.

print(assistiram)