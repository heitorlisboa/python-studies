num_list = []
even_list = []
odd_list = []

while True:
    num_list.append(int(input('Enter a number: ')))
    answer = str(input('Do you wanna continue? [Y/N] ')).upper()
    while answer != 'Y' and answer != 'N':
        answer = str(input('INVALID! Do you wanna continue? [Y/N] ')).upper()
    if answer == 'N':
        break

for p, v in enumerate(num_list):
    if v % 2 == 0:
        even_list.append(v)
    else:
        odd_list.append(v)

print(f'List of all the numbers entered: {num_list}\n'
      f'List of all even numbers entered: {even_list}\n'
      f'List of all odd numbers entered: {odd_list}')
