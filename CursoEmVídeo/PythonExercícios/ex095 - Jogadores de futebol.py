allPlayers = list()
player = dict()
matches = list()

while True:
    totGoals = 0
    matches.clear()

    player['name'] = str(input('Player name: ')).title()

    for c in range(1, int(input('How many matches he/she played? ')) + 1):
        matchGoals = int(input(f'How many goals in match {c}? '))
        matches.append(matchGoals)
        totGoals += matchGoals

    player['matches'] = matches[:]
    player['total of goals'] = totGoals
    allPlayers.append(player.copy())

    answer = str(input('Do you wanna continue? [Y/N] ')).upper()
    while answer != 'Y' and answer != 'N':
        answer = str(input('INVALID! Do you wanna continue? [Y/N] ')).upper()
    if answer == 'N':
        break

print('-' * 50)
print(f'{"No.":<5}{"Name":<20}{"Goals":<20}{"Total":>5}')
print('-' * 50)
for n, p in enumerate(allPlayers):
    print('{:<5}{:<20}{:<20}{:>5}'.format(n + 1, p['name'], str(p['matches']), p['total of goals']))
print('-' * 50)

while True:
    playerPos = int(input('Show statistics from which player? [0 = stop] ')) - 1
    if playerPos < 0:
        break
    elif playerPos < len(allPlayers):
        print(f'==== {allPlayers[playerPos]["name"]}\'s statistics ====')
        for i, v in enumerate(allPlayers[playerPos]["matches"]):
            print(f'In the game {i + 1}, made {v} goals.')
        print('-' * 40)
    else:
        print(f'INVALID! Player {playerPos + 1} doesn\'t exist!')
        print('-' * 40)
