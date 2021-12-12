print('Enter 3 numbers')
num1 = int(input('1st: '))
num2 = int(input('2nd: '))
num3 = int(input('3rd: '))
# Biggest number
big = num1
if num2 > num1 and num2 > num3:
    big = num2
if num3 > num1 and num3 > num2:
    big = num3
# Smallest number
small = num1
if num2 < num1 and num2 < num3:
    small = num2
if num3 < num1 and num3 < num2:
    small = num3
print('The {3}biggest{2} number is {3}{0}{2}\n'
      'And the {4}smallest{2} one is {4}{1}{2}'.format(big, small,
                                                       '\033[m', '\033[1;32m', '\033[1;31m'))
