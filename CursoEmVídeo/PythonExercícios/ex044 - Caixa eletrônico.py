colors = {'clear': '\033[m',
          'cyan': '\033[1;36m'}

price = float(input('Enter the product price: R$'))
print('''Choose the payment method:
{1}[ 0 ]{0} to pay by {1}check or in cash{0}
{1}[ 1 ]{0} to pay {1}cash by credit card{0}
{1}[ 2 ]{0} to pay in {1}2 installments by credit card{0}
{1}[ 3 ]{0} to pay in {1}3 or more installments by credit card{0}'''.format(colors['clear'], colors['cyan']))
method = int(input('Chosen method: '))

if method == 0:
    price = price * 0.9
    print('With {2}10% discount{1}, the {2}price{1} is {2}R${0:.2f}{1}'.format(price,
                                                                               colors['clear'], colors['cyan']))
elif method == 1:
    price = price * 0.95
    print('With {2}5% discount{1}, the {2}price{1} is {2}R${0:.2f}{1}'.format(price,
                                                                              colors['clear'], colors['cyan']))
elif method == 2:
    installment = price / 2
    print('The {3}price{2} is {3}R${0:.2f}{2}, '
          'and each {3}installment{2} is {3}R${1:.2f}{2}'.format(price, installment,
                                                                 colors['clear'], colors['cyan']))
elif method == 3:
    price = price * 1.2
    installments = int(input('How many installments? '))
    installment = price / installments
    if installments < 3:
        print('\033[1;31mInvalid number! Only 3 or more installments are allowed in this payment method!\033[m')
        exit()
    else:
        print('With {3}20% interest rate{2}, the {3}price{2} is {3}R${0:.2f}{2}, '
              'and each {3}installment{2} is {3}R${1:.2f}{2}'.format(price, installment,
                                                                     colors['clear'], colors['cyan']))
else:
    print('\033[1;31mInvalid payment method!\033[m')
    exit()
