num = sum_num  = 0
while num != 999:
    sum_num += num
    num = int(input('Enter a number [999 = exit]: '))
print('The sum is {}'.format(sum_num))
