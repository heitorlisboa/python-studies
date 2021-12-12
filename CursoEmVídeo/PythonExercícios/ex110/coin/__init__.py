def increase(n, p=0, f=False):
    if p >= 0:
        res = n + n * p/100
    else:
        res = decrease(n, p)
    return res if not f \
        else coin(res)


def decrease(n, p=0, f=False):
    if p < 0:
        p *= -1
    res = n - n * p/100
    return res if not f \
        else coin(res)


def double(n, f=False):
    res = n * 2
    return res if not f \
        else coin(res)


def half(n, f=False):
    res = n / 2
    return res if not f \
        else coin(res)


def coin(n=0.0, style='R$'):
    res = str(f'{style}{n:.2f}')
    return res


def summary(n, i=0, d=0):
    print('-' * 30)
    print('VALUE SUMMARY'.center(30))
    print('-' * 30)
    print(f'{"Price analyzed:":<20}{coin(n)}\n'
          f'{"Double the price:":<20}{double(n, True)}\n'
          f'{"Half the price:":<20}{half(n, True)}\n'
          f'{f"{i}% increase:":<20}{increase(n, i, True)}\n'
          f'{f"{d}% decrease:":<20}{decrease(n, d, True)}')
    print('-' * 30)
