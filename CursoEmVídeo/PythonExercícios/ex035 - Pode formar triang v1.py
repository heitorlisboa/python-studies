print('Enter 3 values to be sides of a triangle')
s1 = float(input('Side 1: '))
s2 = float(input('Side 2: '))
s3 = float(input('Side 3: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('You {1}can{0} form a triangle!'.format('\033[m', '\033[1;32m'))
else:
    print("You {1}can't{0} form a triangle".format('\033[m', '\033[1;31m'))
