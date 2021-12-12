from collections import defaultdict

dicionario = defaultdict(int)  # Deve-se passar uma função/classe sem parênteses
# A classe 'int' apresenta um valor padrão que é 0, então se
# não houver nenhum valor para a chave procurada, este será 0.

print(dicionario['guilherme'])

def return_none(valor=None):
    return valor
# Nessa função, se não houver nenhum valor para a chave procurada, este será None.


dicionario = defaultdict(return_none)

print(dicionario['guilherme'])
