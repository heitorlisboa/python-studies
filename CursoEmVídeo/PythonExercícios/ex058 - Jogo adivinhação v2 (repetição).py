from random import randint
pc = randint(1, 10)
tries = 1
answer = int(input('Try to guess the whole number the computer generated from 1 and 10: '))
while pc != answer:
    if answer > pc:
        hint = 'Smaller'
    if answer < pc:
        hint = 'Bigger'
    answer = int(input(f'{hint}... Try again: '))
    tries += 1
print(f'''Correct answer! Congratulations!
Number of tries: {tries}''')
