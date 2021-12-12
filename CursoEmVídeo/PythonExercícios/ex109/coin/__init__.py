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
