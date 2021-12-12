colors = {'clear': '\033[m',
          'red': '\033[1;35m'}
name = input("What's your name? ")
print('Nice to meet you, {}{}{}!'.format(colors['red'], name, colors['clear']))
