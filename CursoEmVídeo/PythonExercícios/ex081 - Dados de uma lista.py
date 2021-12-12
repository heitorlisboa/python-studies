num_list = []
cont = 0

while True:
    num_list.append(int(input('Enter a number: ')))
    cont += 1
    answer = str(input('Do you wanna continue? [Y/N] ')).upper()
    while answer != 'Y' and answer != 'N':
        answer = str(input('INVALID! Do you wanna continue? [Y/N] ')).upper()
    if answer == 'N':
        break

print(f'=' * 35,
      f'\nYou entered {len(num_list)} number(s)')

if 5 in num_list:
    print('The number 5 appeared in the positions', end=' ')
    for c in range(0, cont):
        if num_list[c] == 5:
            print(c, end=' ')
else:
    print('The number 5 is not on the list.', end='')

num_list.sort(reverse=True)
print(f'\nThe numbers in descending order: {num_list}')
