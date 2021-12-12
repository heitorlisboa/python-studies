num = int(input('Enter a whole number: '))
sum_test = 0
for c in range(1, num+1):
    color = '\033[1;31m'
    if num % c == 0:
        sum_test += 1
        color = '\033[1;32m'
    print(f'{color}{c}\033[m', end=' ')
if sum_test == 2:
    prime = 'a prime number!'
else:
    prime = 'NOT a prime number!'
print('''\nThe number {} could be divided {} time(s)
And because of that, it IS {}'''.format(num, sum_test, prime))
