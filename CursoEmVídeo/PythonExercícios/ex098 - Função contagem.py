from time import sleep


def contador(i, f, p):
    sleep(1)
    print('-=' * 15)

    if p == 0:
        print('INVALID! Common difference set to 1')
        p = 1
    if p < 0:
        p *= -1

    print(f'{i} to {f} count going {p} by {p}')
    if i < f:
        while i <= f:
            print(i, end=' ')
            i += p
            sleep(0.5)
    elif f < i:
        while i >= f:
            print(i, end=' ')
            i -= p
            sleep(0.5)
    print('END')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 15)
print('Now it\'s your time to customize the count')
start = int(input('Start: '))
end = int(input('End: '))
comDif = int(input('Common difference: '))

contador(start, end, comDif)
