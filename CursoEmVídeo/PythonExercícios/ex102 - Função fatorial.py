def fatorial(num, show=False):
    """
    Calcula o fatorial
    :param num: Número cujo fatorial vai ser calculado.
    :param show: (opcional) Se True, mostra o cálculo; se False (ou vazio), não mostra.
    :return: O valor do Fatorial de num.
    """
    res = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('*', end=' ')
            else:
                print(f'=', end=' ')
        res *= c
    return res


print(fatorial(5, show=True))
help(fatorial)
