sum_3 = 0
cont_3 = 0
# Método que vê se o número é ímpar e depois vê se é múltiplo de 3
for c in range(1, 501, 2):
    if c % 3 == 0:
        sum_3 += c
        cont_3 += 1

# Método que vê se o número é múltiplo de 3 e depois vê se é impar
'''for c in range(3, 501, 3):
    if c % 2 != 0:
        sum_3 +=
        cont_3 += 1'''

print(f'The sum of all the {cont_3} odd numbers between 1 and 500 that are divisible by 3 is {sum_3}')
