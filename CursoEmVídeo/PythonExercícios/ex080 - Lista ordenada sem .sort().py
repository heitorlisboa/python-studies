num_list = []
for c in range(0, 5):
    new_number = int(input('Enter a number: '))
    if c == 0:
        num_list.append(new_number)
        print('First number added! (position 0)')
    elif new_number >= max(num_list):
        num_list.append(new_number)
        print(f'Number added in the position {len(num_list) - 1} (last position)')
    else:
        pos = 0
        while pos < len(num_list):
            if new_number <= num_list[pos]:
                num_list.insert(pos, new_number)
                print(f'Number added in the position {pos}')
                break
            pos += 1
print(f'The numbers entered in ascending order: {num_list}')
