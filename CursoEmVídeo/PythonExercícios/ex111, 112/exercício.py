from utilidadesCeV import coin, data

price = data.inputMoney('Enter the price: R$', auto=False)
coin.summary(price, 35, 22)
