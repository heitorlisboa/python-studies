l = float(input("What's the length of the wall? "))
a = float(input('And the weight? '))
ar = l * a
print('To paint {3}{0:.2f}{2} m² of wall, '
      'it will be necessary {3}{1:.2f}{2} liters of paint.'.format(ar, ar / 2, '\033[m', '\033[1;35m'))
