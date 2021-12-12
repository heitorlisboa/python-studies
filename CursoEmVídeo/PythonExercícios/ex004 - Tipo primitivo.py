colors = {'clear': '\033[m',
          'blue': '\033[1;34m',
          'green': '\033[1;32m',
          'red': '\033[1;31m'}

alpha = colors['red']
num = colors['red']
alnum = colors['red']
space = colors['red']
up = colors['red']
low = colors['red']
cap = colors['red']

st = input('Type something: ')

print('The primitive type is {}{}{}'.format(colors['blue'], type(st), colors['clear']))

print('Is alphabetic?', end=' ')
if st.isalpha():
    alpha = colors['green']
print('{}{}{}'.format(alpha, st.isalpha(), colors['clear']))

print('Is numeric?', end=' ')
if st.isnumeric():
    num = colors['green']
print('{}{}{}'.format(num, st.isnumeric(), colors['clear']))

print('Is alphanumeric?', end=' ')
if st.isalnum():
    alnum = colors['green']
print('{}{}{}'.format(alnum, st.isalnum(), colors['clear']))

print('Are just spaces?', end=' ')
if st.isspace():
    space = colors['green']
print('{}{}{}'.format(space, st.isspace(), colors['clear']))

print('Is in uppercase only?', end=' ')
if st.isupper():
    up = colors['green']
print('{}{}{}'.format(up, st.isupper(), colors['clear']))

print('Is in lowercase only?', end=' ')
if st.islower():
    low = colors['green']
print('{}{}{}'.format(low, st.islower(), colors['clear']))

print('Is capitalized?', end=' ')
if st.istitle():
    cap = colors['green']
print('{}{}{}'.format(cap, st.istitle(), colors['clear']))