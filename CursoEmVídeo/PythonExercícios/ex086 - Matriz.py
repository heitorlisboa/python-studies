matrix = [[], [], []]

for row in range(0, 3):
    for column in range(0, 3):
        matrix[row].insert(column, int(input(f'Enter a value for [{row}, {column}]: ')))

print('-' * 30)
for row in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[row][column]:^5}]', end=' ')
    print()
