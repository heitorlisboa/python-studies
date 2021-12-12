from collections import defaultdict, Counter

meu_texto = 'Eu fui ao mercado e fui ao cinema'.lower()


# Utilizando dicionário padrão
aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

for palavra in aparicoes.items():
    print(palavra)
print('FIM')


# Utilizando defaultdict
aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    aparicoes[palavra] += 1

for palavra in aparicoes.items():
    print(palavra)
print('FIM')


# Utilizando Counter
aparicoes = Counter(meu_texto.split())

for palavra in aparicoes.items():
    print(palavra)
