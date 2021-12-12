aparicoes = {
    'Guilherme': 1,
    'cachorro': 2,
    'nome': 2,
    'vindo': 1
}

procura1 = aparicoes.get('xpto', 0)
# Significa: procure a chave 'xpto' e retorne seu valor,
# caso essa chave não exista, retorne 0 (você escolhe o valor
# retornado por parâmetro, como no código acima).

print(procura1)

print('xpto' in aparicoes)
# Retorna True ou False se o elemento está ou não no dicionário.

procura2 = aparicoes['xpto']
# Caso utilize dessa outra maneira, se a chave não existir,
# o programa simplesmente dá erro.

print(procura2)
