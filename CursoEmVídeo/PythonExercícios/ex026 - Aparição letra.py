colors = {'clear': '\033[m',
          'cyan': '\033[1;36m'}
phrase = str(input('Type a phrase: ')).lower().strip()
normalized_phrase = ' '.join(phrase.split())
print('The letter A appears {2}{0}{1} times'.format(phrase.count('a'),
                                                    colors['clear'], colors['cyan']))
print('The letter A first appears in the digit {2}{0}{1}'.format(normalized_phrase.find('a') + 1,
                                                                 colors['clear'], colors['cyan']))
print('The letter A last appears in the digit {2}{0}{1}'.format(normalized_phrase.rfind('a') + 1,
                                                                colors['clear'], colors['cyan']))
