usuarios = [
    ('Guilherme', 40, 1981),
    ('Daniela', 34, 1987),
    ('Paulo', 42, 1979)
]

# Quando há elementos que não serão utilizados no desempacotamento,
# é comum se utilizar um underline para nomeá-los. Entretanto, é
# uma boa prática nomeá-los explicitamente quando forem poucos elementos,
# assim não será necessário procurar em outro lugar para saber o que é cada um.
for nome, _, _ in usuarios:
    print(nome)
