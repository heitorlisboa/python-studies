def replaceComma(x):
    if ',' in str(x):
        x = x.replace(',', '.')
        x = float(x)
    return x


def increase(n, p=0, f=False):
    comma = False
    if n != replaceComma(n):
        n = replaceComma(n)
        comma = True
    if p >= 0:
        res = n + n * p/100
    else:
        res = decrease(n, p)
    if comma:
        res = str(res).replace('.', ',')
    return res if not f \
        else coin(res)


def decrease(n, p=0, f=False):
    comma = False
    if n != replaceComma(n):
        n = replaceComma(n)
        comma = True
    if p < 0:
        p *= -1
    res = n - n * p/100
    if comma:
        res = str(res).replace('.', ',')
    return res if not f \
        else coin(str(res))


def double(n, f=False):
    comma = False
    if n != replaceComma(n):
        n = replaceComma(n)
        comma = True
    res = n * 2
    if comma:
        res = str(res).replace('.', ',')
    return res if not f \
        else coin(str(res))


def half(n, f=False):
    comma = False
    if n != replaceComma(n):
        n = replaceComma(n)
        comma = True
    res = n / 2
    if comma:
        res = str(res).replace('.', ',')
    return res if not f \
        else coin(str(res))


def coin(n='0', style='R$'):
    if ',' not in str(n):
        res = str(f'{style}{float(n):.2f}')
    else:
        n = replaceComma(n)
        res = str(f'{style}{n:.2f}').replace('.', ',')
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
