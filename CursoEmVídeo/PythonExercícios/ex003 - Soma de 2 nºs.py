colors = {'clear': '\033[m',
          'blue': '\033[34m',
          'yellow': '\033[33m',
          'green': '\033[32m'}
n1 = float(input('Enter a number: '))
n2 = float(input('Enter another one: '))
print('The sum between {4}{0}{3} e {5}{1}{3} é {6}{2}{3}'.format(n1, n2, n1+n2,
                                                                 colors['clear'], colors['blue'],
                                                                 colors['yellow'], colors['green']))
