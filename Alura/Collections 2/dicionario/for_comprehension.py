aparicoes = {
    'Guilherme': 1,
    'cachorro': 2,
    'nome': 2,
    'vindo': 1
}

# .keys() retorna as CHAVES.
# .values() retorna os VALORES.
# .items() retorna os ITENS (duplas de CHAVE + VALOR) em forma de tuplas.

palavras = [f'palavra {chave}' for chave in aparicoes.keys()]

print(palavras)

ao_quadrado = {x: x**2 for x in range(1,4)}

print(ao_quadrado)
