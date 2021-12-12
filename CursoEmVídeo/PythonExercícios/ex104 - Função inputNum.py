def inputNum(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            break
        print('\033[1;31mERROR! Enter a valid integer.\033[m')
    return num


n = inputNum('Enter an integer: ')
print(f'You just entered the number {n}')
