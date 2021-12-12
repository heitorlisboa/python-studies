colors = {'clear': '\033[m',
          'blue': '\033[1;34m',
          'magenta': '\033[1;35m',
          'red': '\033[1;31m'}
n = float(input('Enter a number: '))
print('The {4}double{3} is {4}{0:.2f}{3}\n'
      'The {5}triple{3} is {5}{1:.2f}{3}\n'
      'The {6}square root{3} is {6}{2:.2f}{3}'.format(n * 2, n * 3, n ** (1/2),
                                                colors['clear'], colors['blue'], colors['magenta'], colors['red']))
