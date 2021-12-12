p = float(input('Enter product price: R$'))
print('The product price with {2}5%{1} discount is {2}R${0:.2f}{1}'.format(p * 95 / 100, '\033[m', '\033[1;32m'))
