while True:
    num = int(input('Enter an integer to see its multiplication table [negative number = exit]: '))
    if num < 0:
        break
    print('-' * 15)
    for c in range(1, 11):
        print(f'{num} * {c:>2} = {num * c}')
    print('-' * 15)
print('Come back often!')
