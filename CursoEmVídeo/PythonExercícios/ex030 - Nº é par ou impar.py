num = int(input('Enter an integer: '))
if num % 2 == 0:
    print('Your number is {1}even{0}!'.format('\033[m', '\033[1;36m'))
else:
    print('Your number is {1}odd{0}!'.format('\033[m', '\033[1;35m'))
