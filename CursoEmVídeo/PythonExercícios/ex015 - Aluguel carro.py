days = int(input('How many days did you rent the car for? '))
km = float(input('How many km did you travel with it? '))
print('The price to pay is {2}R${0:.2f}{1}'.format(days * 60 + km * 0.15, '\033[m', '\033[1;32m'))
