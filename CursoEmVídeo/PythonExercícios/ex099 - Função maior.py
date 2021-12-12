from time import sleep


def maior(*n):
    sleep(1)
    print('-=' * 15)
    print('List:', end=' ')

    m = 0
    for c in n:
        print(c, end=' ')
        if c > m:
            m = c

    print('\nAnalyzing the values entered...')
    sleep(0.5)
    print(f'{len(n)} values were entered')
    sleep(0.5)
    print(f'The biggest value is {m}')
    sleep(0.5)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
