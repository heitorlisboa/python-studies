colors = {'clear': '\033[m',
          'green': '\033[1;32m',
          'red': '\033[1;31m'}

print('{:=^40}'.format('Is it a palindrome?'))

# Solução com repetição
'''phrase = str(input('Enter a phrase or word to get the answer: ')).upper().split()
joined = ''.join(phrase)
inverse = ''
for letters in range(len(joined) - 1, -1, -1):
    inverse += joined[letters]

if inverse == joined:
    answer = 'IS'
    ac = colors['green']
else:
    answer = 'IS NOT'
    ac = colors['red']

print('You typed {4}{0}{3}, and the inverse is {5}{1}{3}.\n'
      'It {5}{2}{3} a palindrome!'.format(joined, inverse, answer,
                                          colors['clear'], colors['green'], ac))'''

# Solução pythonística
phrase = str(input('Enter a phrase or word get the answer: ')).upper().split()
joined = ''.join(phrase)
inverse = joined[::-1]

if joined == inverse:
    answer = 'IS'
    ac = colors['green']
else:
    answer = 'IS NOT'
    ac = colors['red']

print('You typed {4}{0}{3}, and the inverse is {5}{1}{3}.\n'
      'It {5}{2}{3} a palindrome!'.format(joined, inverse, answer,
                                          colors['clear'], colors['green'], ac))
