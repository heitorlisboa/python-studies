import coin

price = float(input('Enter the price: R$'))
print(f'The half of {coin.coin(price)} is {coin.coin(coin.double(price))}')
print(f'The double of {coin.coin(price)} is {coin.coin((coin.half(price)))}')
print(f'Increasing 10%, we have {coin.coin(coin.increase(price, 10))}')