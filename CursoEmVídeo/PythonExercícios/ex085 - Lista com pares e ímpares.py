num_list = [[], []]

for c in range(1, 8):
    if c == 1:
        ordinal = 'st'
    elif c == 2:
        ordinal = 'nd'
    elif c == 3:
        ordinal = 'rd'
    else:
        ordinal = 'th'
    temp = int(input(f'Enter {c}{ordinal} value: '))
    if temp % 2 == 0:
        num_list[0].append(temp)
    else:
        num_list[1].append(temp)
num_list[0].sort()
num_list[1].sort()
print('-' * 35)
print(f'The even numbers are {num_list[0]}\n'
      f'The odd numbers are {num_list[1]}')
