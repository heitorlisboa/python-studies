from random import randint
from time import sleep
all_games = []
game_n = []

print('-' * 40)
print('{:^40}'.format('MEGA SENA DRAWER'))
print('-' * 40)
many = int(input('How many games do you want to draw? '))

for tot_games in range(0, many):
    for numbers in range(0, 6):
        num = randint(1, 60)
        while num in game_n:
            num = randint(1, 60)
        game_n.append(num)
    game_n.sort()
    all_games.append(game_n[:])
    game_n.clear()

for n, numbers in enumerate(all_games):
    sleep(1)
    print(f'Game {n+1}: {numbers}')
print('{:-^40}'.format(' GOOD LUCK! '))
