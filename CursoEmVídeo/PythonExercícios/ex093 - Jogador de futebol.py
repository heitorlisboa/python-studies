player = dict()
matches = list()
totGoals = 0

player['name'] = str(input('Player name: ')).title()
for c in range(1, int(input('How many matches he/she played? ')) + 1):
    matchGoals = int(input(f'How many goals in match {c}? '))
    matches.append(matchGoals)
    totGoals += matchGoals  # Também dá pra, ao invés de fazer isso, fazer player['total of goals'] = sum(matches)
player['goals'] = matches
player['total of goals'] = totGoals

print('-' * 35)
print(f'The player {player["name"]} played {len(player["matches"])} games.')
for m, g in enumerate(player['matches']):
    print(f'In the match {m + 1}, did {g} goals.')
print(f'A total of {player["total of goals"]} goals.')
