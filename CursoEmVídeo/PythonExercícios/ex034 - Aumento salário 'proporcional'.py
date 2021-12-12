pay = float(input('Enter the value of your current salary: R$'))
if pay > 1250:
    pay = pay * 110/100
    inc = 10
else:
    pay = pay * 115/100
    inc = 15
print('With a {3}{0}%{2} pay increase, your salary is now {3}R${1:.2f}{2}'.format(inc, pay, '\033[m', '\033[1;32m'))
