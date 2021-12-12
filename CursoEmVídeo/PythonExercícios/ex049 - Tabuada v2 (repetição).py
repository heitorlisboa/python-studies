num = int(input('Enter a whole number to see its multiplication table: '))
for c in range(1, 11):
    print('{} * {:>2} = {}'.format(num, c, num * c))
