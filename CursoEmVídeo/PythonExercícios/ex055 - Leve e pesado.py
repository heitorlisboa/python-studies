print('Enter the weight of five people (kg): ')

# Método com gambiarra (lightest = 999)
'''heaviest = 0
lightest = 999
for c in range(1, 6):
    weight = float(input(f'Weight {c}: '))
    if weight > heaviest:
        heaviest = weight
    if weight < lightest:
        lightest = weight'''

# Método infalível (primeira medida sempre vai ser o menor e o maior)
heaviest = 0
lightest = 0
for c in range(1, 8):
    weight = float(input(f'Weight {c}: '))
    if c == 1:
        lightest = weight
        heaviest = weight
    else:
        if weight > heaviest:
            heaviest = weight
        if weight < lightest:
            lightest = weight

print('''The heaviest is {:.1f} kg
And the lightest is {:.1f} kg'''.format(heaviest, lightest))
