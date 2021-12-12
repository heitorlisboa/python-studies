def increase(n, p=0):
    if p >= 0:
        res = n + n * p/100
    else:
        res = decrease(n, p)
    return res


def decrease(n, p):
    if p < 0:
        p *= -1
    res = n - n * p/100
    return res


def double(n):
    res = n * 2
    return res


def half(n):
    res = n / 2
    return res
