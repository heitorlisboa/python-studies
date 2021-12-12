from datetime import date
print('Enter the year of birth of seven people: ')

majority = 0  # Maioridade
minority = 0  # Menoridade
for c in range(1, 8):
    year = int(input(f'Year of birth {c}: '))
    if date.today().year - year >= 21:
        majority += 1
    elif date.today().year - year < 21:
        minority += 1

print('''{} person(s) have already reached the adulthood.
{} person(s) haven't reached it yet.'''.format(majority, minority))
