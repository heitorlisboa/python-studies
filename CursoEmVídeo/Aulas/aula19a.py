brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
for index in brasil:
    for key, value in index.items():
        print(f'{key} = {value}')
    print('-' * 20)
