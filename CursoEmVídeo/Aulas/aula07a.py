n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
p = n1 ** n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
print('Do primeiro número pelo segundo, a soma vale {:.2f}'.format(s))
print('O produto vale {:.2f}\nA potência vale {:.2f}\nA divisão vale {:.2f}\nA divisão inteira vale {}\nE o resto da divisão vale {}'.format(m, p, d, di, r))
# print('Do primeiro número pelo segundo, a soma vale {:.2f}, o produto vale {:.2f},'.format(s, m), end=' ')
# print('a potência vale {:.2f}, a divisão vale {:.2f}, a divisão inteira vale {}'.format(p, d, di), end=' ')
# print('e o resto da divisão vale {}'.format(r))
