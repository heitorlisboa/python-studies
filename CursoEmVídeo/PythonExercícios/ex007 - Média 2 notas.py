print('Enter two grades to see their mean: ')
n1 = float(input('Grade 1: '))
n2 = float(input('Grade 2: '))
mean = (n1 + n2) / 2
color = '\033[1;31m'
if mean >= 6:
    color = '\033[1;32m'
print('The mean is {}{:.2f}'.format(color, mean))
