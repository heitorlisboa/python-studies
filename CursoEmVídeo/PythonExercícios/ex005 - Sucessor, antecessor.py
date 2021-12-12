colors = {'clear': '\033[m',
          'green': '\033[1;32m',
          'red': '\033[1;31m'}
n = int(input('Enter a whole number: '))
print('Its successor is {3}{0}{2}\n'
      'Its predecessor is {4}{1}{2}'.format(n + 1, n - 1, colors['clear'], colors['green'], colors['red']))
