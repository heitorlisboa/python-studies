import coin

price = float(input('Enter the price: R$'))
print(f'The half of {coin.coin(price)} is {coin.half(price, True)}')
print(f'The double of {coin.coin(price)} is {coin.double(price, True)}')
print(f'Increasing 10%, we have {coin.increase(price, 10, True)}')
print(f'Decreasing 13%, we have {coin.decrease(price, 13, True)}')
