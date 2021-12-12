from random import randint
wins = 0
print('Let\'s play Odds and Evens!')
while True:
    play = str(input('Odd or even [O/E]? ')).lower()
    while play != 'e' and play != 'o':
        play = str(input('Invalid! Odd or even [O/E]? ')).lower()

    num = int(input('Enter a number from 0 to 5: '))
    while num > 5 or num < 0:
        num = int(input('Enter a number from 0 to 5: '))

    pc = randint(0, 5)
    if (num + pc) % 2 == 0:
        oe = 'even'
    else:
        oe = 'odd'
    if play == oe[0]:
        result = 'won'
        wins += 1
    else:
        result = 'lost'

    print(f'You {result}! You played {num} and the computer {pc}\n'
          f'{num} + {pc} = {num + pc} ({oe})\n')
    if result == 'lost':
        break
print(f'You won {wins} consecutive times!')
