colors = {'clear': '\033[m',
          'cyan': '\033[1;36m',
          'red': '\033[1;31m'}
num = int(input('Enter an integer: '))
print('''Choose the {1}base{0} to convert to
{1}1{0} convert to {1}binary{0}
{1}2{0} convert to {1}octal{0}
{1}3{0} convert to {1}hexadecimal{0}'''.format(colors['clear'], colors['cyan']))
chosen = int(input('Chosen: '))
if chosen == 1:
    base = 'binary'
    conv = bin(num)
elif chosen == 2:
    base = 'octal'
    conv = oct(num)
elif chosen == 3:
    base = 'hexadecimal'
    conv = hex(num)
else:
    print('{1}Invalid option!{0}'.format(colors['clear'], colors['red']))
    exit()
print('{4}{0}{3} converted to {4}{1}{3} is {4}{2}{3}'.format(num, base, conv[2:].upper(),
                                                             colors['clear'], colors['cyan']))
