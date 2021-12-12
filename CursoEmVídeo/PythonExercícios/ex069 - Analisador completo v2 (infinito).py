over18 = men = wu20 = 0
while True:
    print('---- Sign up ----')
    age = int(input('Age: '))
    while age < 0:
        age = int(input('Invalid!\nAge: '))

    if age >= 18:
        over18 += 1

    gender = str(input('Gender [M/F]: ')).upper().strip()
    while gender != 'M' and gender != 'F':
        gender = str(input('Invalid!\nGender [M/F]: ')).upper().strip()

    if gender == 'M':
        men += 1

    if gender == 'F' and age < 20:
        wu20 += 1

    answer = str(input('Do you wanna continue? [Y/N] ')).upper().strip()
    while answer != 'Y' and answer != 'N':
        answer = str(input('Invalid!\nDo you wanna continue? [Y/N] ')).upper().strip()

    if answer == 'N':
        break

print(f'''There is(are) {over18} person(s) over 18 years old
There is(are) {men} man(men) signed up
There is(are) {wu20} woman(women) under 20 years old''')