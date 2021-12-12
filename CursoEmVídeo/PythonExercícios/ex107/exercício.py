import coin

price = float(input('Enter the price: R$'))
print(f'The double of R${price:.2f} is R${coin.double(price):.2f}')
print(f'The half of R${price:.2f} is R${coin.half(price):.2f}')
print(f'Increasing in 10%, we have R${coin.increase(price, 10):.2f}')
print(f'Decreasing in 13%, we have R${coin.decrease(price, 13):.2f}')
