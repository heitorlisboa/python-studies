def area(x=1.0, y=1.0):
    print(f'The area of a terrain {length:.1f}x{width:.1f} is {x * y:.1f}m²')


def entreLinhas(txt):
    tam = len(txt) + 8
    print('-' * tam)
    print(f'{txt:^{tam}}')
    print('-' * tam)


entreLinhas('Terrain control')
length = float(input('Length: '))
width = float(input('Width: '))
area(length, width)
