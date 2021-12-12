from datetime import date
person = dict()

person['Name'] = str(input('Name: ')).title()
person['Age'] = date.today().year - int(input('Year of birth: '))
person['CTPS'] = str(input('Carteira de trabalho [0 = don\'t have]: ')).title()
if person['CTPS'] != '0':
    person['Retirement age'] = person['Age'] + 35 - (date.today().year - int(input('Year of hiring: ')))
    person['Salary'] = float(input('Salary: R$'))
print('-' * 35)
for k, v in person.items():
    if k == 'Salary':
        print(f'{k} is R${v:.2f}')
    else:
        print(f'{k} is {v}')
