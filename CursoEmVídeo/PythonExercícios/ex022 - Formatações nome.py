colors = {'clear': '\033[m',
          'green': '\033[1;32m',
          'red': '\033[1;31m',
          'light green': '\033[1;92m',
          'blue': '\033[1;34m',
          'light blue': '\033[1;94m'}

name = str(input('Enter your full name: ')).strip()
normalized_name = ' '.join(name.split())

print('Only {2}upper{1}: {2}{0}{1}'.format(normalized_name.upper(), colors['clear'], colors['green']))
print('Only {2}lower{1}: {2}{0}{1}'.format(normalized_name.lower(), colors['clear'], colors['red']))
print('All {2}first letters{1} in {2}upper{1}: {2}{0}{1}'.format(normalized_name.title(), colors['clear'],
                                                                 colors['light green']))
print('Your {2}full name{1} has {2}{0}{1} letters'.format(len(name) - name.count(' '), colors['clear'], colors['blue']))
print('Your {2}first name{1} has {2}{0}{1} letters'.format(len(name.split()[0]), colors['clear'], colors['light blue']))
