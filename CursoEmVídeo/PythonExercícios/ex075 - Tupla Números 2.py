numbers = (int(input('Enter a number: ')),
           int(input('Enter another number: ')),
           int(input('Enter one more number: ')),
           int(input('Enter the last number: ')))

cont = 0
print(f'The number 9 appeared {numbers.count(9)} time(s)')

if 3 in numbers:
    print(f'The number 3 first appeared on space {numbers.index(3) + 1}')
else:
    print('The number 3 didn\'t appear')

print(f'The even number(s) is(are)', end=' ')
for c in numbers:
    if c % 2 == 0:
        print(c, end=' ')
        cont += 1
if cont == 0:
    print('NONE')
