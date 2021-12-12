from math import hypot
print('Enter 3 values to be sides of a triangle')
side1 = float(input('Side 1: '))
side2 = float(input('Side 2: '))
side3 = float(input('Side 3: '))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 == side2 == side3:
        ttype = 'n equilateral'
    elif side1 == side2 or side1 == side3 or side2 == side3:
        ttype = 'n isosceles'
    elif hypot(side1, side2) == side3 or hypot(side1, side3) == side2 or hypot(side2, side3) == side1:
        ttype = ' right'
    else:
        ttype = ' scalene'
    print('You can form a{} triangle!'.format(ttype))
else:
    print("You can't form a triangle")
