from collections import Counter

dicionario = Counter()
# Diferentemente de se utiliza o defaultdict, quando se
# utiliza o Counter não é necessário colocar uma função/classe
# que determine um valor padrão, o Counter já tem seu próprio
# valor padrão (que é 0), além de que pode diretamente receber
# um iterável como parâmetro para fazer a contagem e retornar
# um dicionário (verificar 'contar_aparicoes.py' para exemplos).

print(dicionario['guilherme'])
