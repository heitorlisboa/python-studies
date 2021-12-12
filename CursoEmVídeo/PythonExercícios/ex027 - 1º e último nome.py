colors = {'clear': '\033[m',
          'cyan': '\033[1;36m'}
name = input('Enter your name: ')
split_name = name.title().split()
print('Your {2}first name{1} is {2}{0}{1}'.format(split_name[0],
                                                  colors['clear'], colors['cyan']))
print('Your {2}last name{1} is {2}{0}{1}'.format(split_name[len(split_name) - 1],
                                                 colors['clear'], colors['cyan']))
