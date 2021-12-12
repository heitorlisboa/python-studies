allPeople = list()
person = dict()
meanAge = 0
overMeanAge = list()

while True:
    person['name'] = str(input('Name: ')).title()

    while True:
        gender = str(input('Gender: [M/F] ')).upper()
        if gender == 'M' or gender == 'F':
            break
        print('INVALID! Only enter "M" or "F"!')
    person['gender'] = gender

    person['age'] = int(input('Age: '))
    meanAge += person['age']

    allPeople.append(person.copy())

    while True:
        answer = str(input('Do you wanna continue? [Y/N] ')).upper()
        if answer == 'Y' or answer == 'N':
            break
        print('INVALID! Only enter "Y" or "N"!')
    if answer == 'N':
        break

meanAge /= len(allPeople)
print('-=' * 15)
print(f'{len(allPeople)} person(s) were registered')
print(f'The mean age is {meanAge:.1f} years old')
print(f'A list with all women:', end=' ')
for p in allPeople:
    if p['gender'] == 'F':
        print(f'[{p["name"]}]', end=' ')
print(f'\nA list with all people over the mean age:')
for p in allPeople:
    if p['age'] > meanAge:
        for k, v in p.items():
            print(f'{k.capitalize()} = {v};', end=' ')
        print()
