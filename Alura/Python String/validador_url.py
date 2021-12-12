import re

url = 'bytebank.com/cabio'

padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
# Ao contrário do [colchetes] que significa que O DÍGITO tem que ser UM dos valores dentro dele,
# o (parênteses) significa TUDO que está dentro dele tem que estar presente naquela posição.

match = padrao_url.match(url)

if not match:
    raise ValueError('A URL é inválida')

print('A URL é válida')