num = int(input('Enter a whole number from 0 to 9999: '))
print('\033[36m', end='')
print('Unit(s): {}'.format(num // 1 % 10))
print('Dozen(s): {}'.format(num // 10 % 10))
print('Hundred(s): {}'.format(num // 100 % 10))
print('Thousand(s): {}'.format(num // 1000 % 10))
