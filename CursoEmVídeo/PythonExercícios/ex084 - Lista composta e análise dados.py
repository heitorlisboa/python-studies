people = []
temp = []

while True:
    temp.append(str(input('Name: ')))
    temp.append(int(input('Weight: ')))
    if len(people) == 0:
        heavy = light = temp[1]
    elif temp[1] > heavy:
        heavy = temp[1]
    elif temp[1] < light:
        light = temp[1]
    people.append(temp[:])
    temp.clear()
    answer = str(input('Do you wanna continue? [Y/N] ')).upper()
    while answer != 'N' and answer != 'Y':
        answer = str(input('INVALID! Do you wanna continue? [Y/N] ')).upper()
    if answer == 'N':
        break

print(f'{len(people)} person(s) was(were) registered')
print(f'The heaviest person(s) is(are)', end=' ')
for name, weight in people:
    if weight == heavy:
        print(name.upper(), end=' ')
print(f'with {heavy}kg')
print(f'The lightest person(s) is(are)', end=' ')
for name, weight in people:
    if weight == light:
        print(name.upper(), end=' ')
print(f'with {light}kg')
