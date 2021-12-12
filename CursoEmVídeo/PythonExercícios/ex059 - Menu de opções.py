from time import sleep
print('Enter two numbers: ')
num1 = float(input('\033[1;36mNumber 1: '))
num2 = float(input('Number 2: \033[m'))
action = 0
while action != 5:
    print('''\n\033[m[ 1 ] Sum
[ 2 ] Multiply
[ 3 ] Biggest number
[ 4 ] Enter new numbers
[ 5 ] Exit program''')
    action = int(input('Option chosen: \033[1;36m'))
    if action == 1:
        print(f'The sum between {num1:.1f} and {num2:.1f} is {num1 + num2:.1f}')
    elif action == 2:
        print(f'The multiplication between {num1:.1f} and {num2:.1f} is {num1 * num2:.1f}')
    elif action == 3:
        if num1 != num2:
            if num1 > num2:
                big = num1
            elif num2 > num1:
                big = num2
            print(f'{big} is the biggest')
        else:
            print('The numbers are equal')
    elif action == 4:
        num1 = float(input('Number 1: '))
        num2 = float(input('Number 2: '))
    elif action == 5:
        print('\033[mExiting...')
        sleep(1)
    else:
        print('\033[1;31mInvalid!\033[m')
print('Come back often!')
