num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
usuario = int(input('Escolha um número de 0 a 9 para saber a escrita de todos os números até ele: '))
print('Números pares')
for con in range(0, usuario+1, 2):
    print(f'[ {con} ]', num[con].capitalize())

print('\nNúmeros ímpares')
for con in range(1, usuario+1, 2):
    print(f'[ {con} ]', num[con].capitalize())
