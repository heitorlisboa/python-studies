# Old version
# m = float(input('Enter a value in meters: '))
# print('The value in centimeters is {:.0f} and the value in millimeters is {:.0f}'.format(m * 100, m * 1000))

# New version: features measures in km, hm, dam, dm, cm and mm.
m = float(input('Enter a value in meters: '))
print('The value of {} m is \033[1;34mequivalent\033[m to {} km,'
      ' {} hm, {} dam, {:.0f} dm, {:.0f} cm and {:.0f} mm.'.format(m, m/1000, m/100, m/10, m*10, m*100, m*1000))
