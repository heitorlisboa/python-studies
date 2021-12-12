s = float(input('Enter the value of your salary: R$'))
print('With a {2}15%{1} pay increase, your salary is now {2}R${0:.2f}{1}'.format(s * 115 / 100, '\033[m', '\033[1;32m'))
