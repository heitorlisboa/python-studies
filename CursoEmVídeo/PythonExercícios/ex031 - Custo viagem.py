dist = float(input('Enter the trip distance in km: '))
# Normal Version
'''if dist <= 200:
    print('The trip will cost R${:.2f}'.format(dist * 0.5))
else:
    print('The trip will cost R${:.2f}'.format(dist * 0.45))'''
# Simplified Version
print('The trip will cost \033[1;32mR${:.2f}'.format(dist * 0.5 if dist <= 200 else dist * 0.45))
