from random import randint
from time import sleep

colors = {'clear': '\033[m',
          'cyan': '\033[1;36m',
          'red': '\033[1;31m',
          'green': '\033[1;32m'}
print("Let's play {1}Rock Paper Scissors{0}!\n"
      "Choose between one of those:\n"
      "{1}[ 1 ]{0} for {1}Rock{0}\n"
      "{1}[ 2 ]{0} for {1}Paper{0}\n"
      "{1}[ 3 ]{0} for {1}Scissors{0}".format(colors['clear'], colors['cyan']))
chosen = int(input('Play: '))

pc = randint(1, 3)
plays = ('rock', 'paper', 'scissors')

print('JO', end=' ')
sleep(0.5)
print('KEN', end=' ')
sleep(0.5)
print('PO!')

if chosen == pc:
    print('{2}Draw!{1} The computer have chosen {2}{0}{1}.'.format(plays[pc-1], colors['clear'], colors['cyan']))
elif (chosen == 1 and pc == 2) or (chosen == 2 and pc == 3) or (chosen == 3 and pc == 1):
    print('{3}You lost!{1} The computer have chosen {2}{0}{1}.'.format(plays[pc-1], colors['clear'], colors['cyan'],
                                                                       colors['red']))
else:
    print('{3}You won!{1} The computer have chosen {2}{0}{1}.'.format(plays[pc-1], colors['clear'], colors['cyan'],
                                                                      colors['green']))
