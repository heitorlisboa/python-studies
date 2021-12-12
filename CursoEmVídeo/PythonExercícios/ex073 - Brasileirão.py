brasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athlético-PR',
               'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará',
               'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná')
print('{:=^50}'.format(' Brasileirão '))
print('Teams in order: {}'.format(brasileirao))
print('=' * 50)
print('The top five teams are {}'.format(brasileirao[0:5]))
print('=' * 50)
print('The last four placed are {}'.format(brasileirao[-4:]))
print('=' * 50)
print('List in alphabetic order: {}'.format(sorted(brasileirao)))
print('=' * 50)
print('The team "Chapecoense" is placed {}'.format(brasileirao.index('Chapecoense') + 1))
print('=' * 50)
