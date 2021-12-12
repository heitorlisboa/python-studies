celsius = float(input('Enter the temperature in ºC: '))
# The equation is 5 (F - 32) = 9 * C
fahrenheit = celsius * 9 / 5 + 32
print('The temperature of {3}{0:.1f}ºC{2} in Fahrenheit is {4}{1:.1f}ºF{2}'.format(celsius, fahrenheit,
                                                                                   '\033[m', '\033[1;34m',
                                                                                   '\033[1;35m'))
