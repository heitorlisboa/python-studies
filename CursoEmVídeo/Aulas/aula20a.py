def entreLinhas(txt):
    tam = len(txt) + 8
    print('-' * tam)
    print(f'{txt:^{tam}}')
    print('-' * tam)
