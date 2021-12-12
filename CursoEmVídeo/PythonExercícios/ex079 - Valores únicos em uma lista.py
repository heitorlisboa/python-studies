num_list = []
while True:
    new_number = int(input('Enter a number: '))
    if new_number not in num_list:
        num_list.append(new_number)
        print('Number saved...')
    else:
        print('Duplicate number! I won\'t save...')
    answer = str(input('Do you wanna continue? [Y/N] ')).upper()
    while answer != 'Y' and answer != 'N':
        answer = str(input('INVALID! Do you wanna continue? [Y/N] ')).upper()
    if answer == 'N':
        num_list.sort()
        print(f'The numbers entered in ascending order: {num_list}')
        break
