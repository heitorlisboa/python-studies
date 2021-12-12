sum_num = tot_num = 0
while True:
    num = int(input('Enter an integer [999 = exit]: '))
    if num == 999:
        break
    sum_num += num
    tot_num += 1
print(f'You entered {tot_num} number(s) and the sum is {sum_num}')
