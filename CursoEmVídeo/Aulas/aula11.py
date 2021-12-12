num1 = int(input('Enter an integer: '))
num2 = int(input('Enter another one: '))
# Less organized method
'''# print('The numbers are \033[1;97;40m{}\033[m and \033[1;30;107m{}\033[m'.format(num1, num2))'''

# More organized method
'''colors = {'clear': '\033[m',
          'red': '\033[31m',
          'green': '\033[32m',
          'blue': '\033[34m'}
print('The numbers are {}{}{} and {}{}{}'.format(colors['red'], num1, colors['clear'], colors['green'], num2,
                                                 colors['clear']))'''

# Another alternative of more organized method
clear = '\033[m'
red = '\033[31m'
green = '\033[32m'
blue = '\033[34m'
print('The numbers are {}{}{} and {}{}{}'.format(red, num1, clear, blue, num2, clear))
