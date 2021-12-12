d = float(input('How many reais do you have? R$'))  # 03/17 dollar price
print('You can buy up to {3}${2}{0:.2f} (dollars) or {3}€{2}{1:.2f} (euros)'.format(d / 5.65, d / 6.72,
                                                                                    '\033[m', '\033[1;32m'))
