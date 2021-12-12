from random import randint
from time import sleep
from operator import itemgetter

allPlayers = dict()

for c in range(1, 5):
    allPlayers.update({f'Player {c}': randint(1, 6)})
for k, v in allPlayers.items():
    print(f'The {k} rolled {v}')
    sleep(1)

ranking = sorted(allPlayers.items(), key=itemgetter(1), reverse=True)
print(f'{" Ranking ":=^31}')
for i, t in enumerate(ranking):
    print(f'The {t[0]} is placed {i + 1} with {t[1]}')
    sleep(1)
