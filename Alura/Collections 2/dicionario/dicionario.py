# Um dicionário pode ser instanciado de duas maneiras.
# A primeira é utilizando '{'chave': valor, 'chave': valor}':
aparicoes = {
    'Guilherme': 1,
    'cachorro': 2,
    'nome': 2,
    'vindo': 1
}

print(aparicoes)

# A segunda maneira é utilizando o construtor 'dict()',
# que também pode ser usado de duas maneiras.

# A primeira é utilizando 'dict(chave = valor, chave = valor)'
aparicoes = dict(
    Guilherme = 1,
    cachorro = 2,
    nome = 2,
    vindo = 1
)

print(aparicoes)

# A segunda é utilizando 'dict([('chave', valor), ('chave', valor)])'
aparicoes = [
    ('Guilherme', 1),
    ('cachorro', 2),
    ('nome', 2),
    ('vindo', 1)
    ]

print(aparicoes)
