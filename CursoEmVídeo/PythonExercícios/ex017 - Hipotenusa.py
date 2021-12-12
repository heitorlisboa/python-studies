from math import hypot
print('Enter the sides of the triangle rectangle: ')
adj = float(input('Adjacent = '))
opp = float(input('Opposite = '))
hyp = hypot(adj, opp)
print('The hypotenuse is {1}{0:.2f}'.format(hyp, '\033[1;32m'))
