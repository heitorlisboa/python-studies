from datetime import date
print('Insira sua data de nascimento')
day = int(input('Dia: '))
month = int(input('Mês: '))
year = int(input('Ano: '))
age = date.today().year - year if date.today().month >= month and date.today().day >= day \
    else date.today().year - year - 1
if age < 9:
    category = 'Mirim'
elif age <= 14:
    category = 'Infantil'
elif age <= 19:
    category = 'Junior'
elif age <= 25:
    category = 'Sênior'
else:
    category = 'Master'
print(f'Sua categoria de natação é {category}!')
