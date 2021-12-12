num_list = []
for c in range(0, 5):
    num_list.append(int(input(f'Enter a number for the position {c}: ')))
print(f'The biggest number is {max(num_list)} and it appeared in the position(s)', end=' ')
for c in range(0, 5):
    if num_list[c] == max(num_list):
        print(c, end=' ')
print(f'\nThe smallest number is {min(num_list)} and it appeared in the position(s)', end=' ')
for p, v in enumerate(num_list):
    if v == min(num_list):
        print(p, end=' ')
