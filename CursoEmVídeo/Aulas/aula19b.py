state = dict()
country = list()

while True:
    state['name'] = str(input('State: ')).title()
    state['postalCode'] = str(input('Postal Code: ')).upper()
    country.append(state.copy())
    answer = str(input('Do you wanna continue? [Y/N] ')).upper()
    while answer != 'Y' and answer != 'N':
        answer = str(input('INVALID! Do you wanna continue? [Y/N] ')).upper()
    if answer == 'N':
        break

# Usando uma repetição
"""for s in country:
    print(f'The state {s["name"]} has the postal code {s["postalCode"]}')"""

# Usando duas repetições
for s in country:
    for v in s.values():
        print(v, end=' ')
    print()
