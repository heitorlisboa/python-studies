sum_num = 0
for c in range(0, 6):
    num = int(input('Enter a whole number: '))
    if num % 2 != 0:  # Se for ímpar
        continue      # Desconsidere
    sum_num += num
print(f'The sum of the even numbers is {sum_num}')
