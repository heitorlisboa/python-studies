colors = {'clear': '\033[m',
          'white': '\033[97m',
          'green': '\033[32m'}
print('{1}Hello{0}, {2}world{0}!'.format(colors['clear'], colors['white'], colors['green']))
