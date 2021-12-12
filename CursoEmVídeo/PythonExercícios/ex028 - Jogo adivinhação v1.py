from random import randint
from time import sleep
colors = {'clear': '\033[m',
          'cyan': '\033[1;36m',
          'blue': '\033[1;34m',
          'green': '\033[1;32m',
          'red': '\033[1;31m'}
rnum = randint(1, 10)
answer = int(input('{}Try to guess the whole number the computer generated from 1 to 10: '.format(colors['blue'])))
print('{}-'.format(colors['cyan']) * 14)
print('{1}Processing...{0}'.format(colors['clear'], colors['blue']))
print('{}-'.format(colors['cyan']) * 14)
sleep(3)
if answer == rnum:
    print('{1}Congratulations{0}, you guessed the number!'.format(colors['clear'], colors['green']))
else:
    print("{2}Wrong answer{1}. The correct number is {0}".format(rnum, colors['clear'], colors['red']))
