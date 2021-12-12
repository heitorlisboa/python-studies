def ficha(nome='<undefined>', gols=0):
    print(f'The player {nome} did {gols} goal(s).')


name = str(input('Player name: '))
numGoals = str(input('Number of goals: '))

while numGoals.strip() != '' and not numGoals.isnumeric():
    numGoals = str(input('INVALID! Number of goals: '))
if numGoals.isnumeric():
    numGoals = int(numGoals)
else:
    numGoals = 0
if name.strip() == '':
    ficha(gols=numGoals)
else:
    ficha(name, numGoals)
