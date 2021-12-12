print('=' * 39)
print('{:^39}'.format('ATM'))  # Caixa eletrônico em inglês é ATM (automated teller machine)
print('=' * 39)

# Meu método (usando FOR)
"""withdraw = int(input('How much money do you wanna withdraw? R$'))
while withdraw <= 0:
    withdraw = int(input('Invalid! How much money do you wanna withdraw? R$'))

bn50 = withdraw // 50  # Notas de 50
for c in range(bn50, 0, -1):
    withdraw -= 50
if bn50 != 0:
    print(f'Total of {bn50} banknote(s) of R$50')

bn20 = withdraw // 20  # Notas de 20
for c in range(bn20, 0, -1):
    withdraw -= 20
if bn20 != 0:
    print(f'Total of {bn20} banknote(s) of R$20')

bn10 = withdraw // 10  # Notas de 10
for c in range(bn10, 0, -1):
    withdraw -= 10
if bn10 != 0:
    print(f'Total of {bn10} banknote(s) of R$10')

if withdraw != 0:  # O resto são as notas de R$1
    print(f'Total of {withdraw} banknote(s) of R$1')
print('=' * 39)"""

# Método Guanabara (usando WHILE e IF)
withdraw = int(input('How much money do you wanna withdraw? R$'))
bn = 50
tot_bn = 0
while True:
    if withdraw >= bn:
        withdraw -= bn
        tot_bn += 1
    else:
        if tot_bn > 0:
            print(f'Total of {tot_bn} banknote(s) of {bn}')
        if bn == 50:
            bn = 20
        elif bn == 20:
            bn = 10
        elif bn == 10:
            bn = 1
        tot_bn = 0
        if withdraw == 0:
            break
print('=' * 39)
