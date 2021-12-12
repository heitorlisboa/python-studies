from random import randint
from time import sleep

lista = list()


def sorteia(x):
    print(f'Randomizing 5 numbers to a list:', end=' ')
    for c in range(0, 5):
        num = randint(1, 10)
        x.append(num)
        print(num, end=' ')
        sleep(0.5)
    print('DONE!')


def somaPar(x):
    soma = 0
    for c in x:
        if c % 2 == 0:
            soma += c
    print(f'Adding the even numbers from {lista}, we have {soma}')


# Programa principal
sorteia(lista)
somaPar(lista)
