shop = ('Pencil', 1.75, 'Eraser', 2, 'Notebook', 15.9, 'Pencil Case', 25, 'Protractor', 4.2, 'Compass', 9.99,
        'Backpack', 120.32, 'Pen', 22.3, 'Book', 34.9)
print('-' * 40)
print(f'{"List of prices":^40}')
print('-' * 40)
for c in range(0, len(shop), 2):
    print('{:.<30}R$'.format(shop[c]), end='')
    print('{:>7.2f}'.format(shop[c + 1]))
print('-' * 40)
