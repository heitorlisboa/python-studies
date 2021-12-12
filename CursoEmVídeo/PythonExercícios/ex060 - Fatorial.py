# Utilizando FOR
"""fact = num = int(input('Enter a whole number to see its factorial: '))
if num > 0:
    for c in range(1, num):
        fact *= c
elif num < 0:  # Não existe fatorial de números negativos
    print('Invalid!')
    exit()
else:  # Fatorial de 0 é 1
    fact = 1
print('{} factorial = {}'.format(num, fact))"""

# Utilizando while
"""fact = num = int(input('Enter a whole number to see its factorial: '))
multiplier = fact - 1
if num > 0:
    while multiplier != 0:
        fact *= multiplier
        multiplier -= 1
elif num < 0:  # Não existe fatorial de números negativos
    print('Invalid!')
    exit()
else:  # Fatorial de 0 é 1
    fact = 1
print('{} factorial = {}'.format(num, fact))"""

# Solução pythonística
from math import factorial
num = int(input('Enter a whole number to see its factorial: '))
if num < 0:  # Não existe fatorial de números negativos
    print('Invalid!')
    exit()
print('{} factorial = {}'.format(num, factorial(num)))
