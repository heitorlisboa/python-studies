matrix = [[], [], []]
evens = third_column_sum = second_row_biggest = 0

for row in range(0, 3):
    for column in range(0, 3):
        matrix[row].insert(column, int(input(f'Enter a value for [{row}, {column}]: ')))
        if matrix[row][column] % 2 == 0:
            evens += matrix[row][column]
        if column == 2:
            third_column_sum += matrix[row][column]
        if row == 1 and matrix[row][column] > second_row_biggest:
            second_row_biggest = matrix[row][column]

print('-' * 30)
for row in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[row][column]:^5}]', end=' ')
    print()

print('-' * 30)
print(f'The sum of all even numbers is {evens}')
print(f'The sum of all values from the third column is {third_column_sum}')
print(f'The biggest value in the second row is {second_row_biggest}')
