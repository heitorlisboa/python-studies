print('Enter as many whole numbers as you want to sum all of them')
answer = 'Y'
sum_num = tot_num = 0

while answer == 'Y':
    num = int(input('Enter a number: '))
    sum_num += num  # Soma os números
    tot_num += 1  # Total de números
    if tot_num == 1:  # Primeiro número sempre será o maior e o menor
        big = small = num
    elif num > big:  # Se for maior
        big = num
    elif num < small:  # Se for menor
        small = num
    answer = str(input('Do you wanna continue? [Y/N] ')).upper().strip()  # Se a resposta for Y o ciclo continua
    while answer != 'Y' and answer != 'N':  # Se a resposta não for Y nem N, dá erro
        answer = str(input('\033[1;31mERROR!\033[m Enter a valid option: ')).upper().strip()
mean = sum_num / tot_num

print('''\nThe mean is {:.1f}
The biggest number is {}
The smallest number is {}'''.format(mean, big, small))
