total = plus1k = 0
while True:
    print('---- Product ----')
    name = str(input('Enter the product\'s name: ')).strip().upper()

    price = float(input('Enter the product\'s price: R$'))
    while price < 0:
        price = float(input('Invalid!\nEnter the product\'s price: R$'))

    answer = str(input('Do you wanna continue? [Y/N] ')).upper().strip()
    while answer != 'Y' and answer != 'N':
        answer = str(input('Invalid!\nDo you wanna continue? [Y/N] ')).upper().strip()

    total += price
    if price > 1000:
        plus1k += 1
    # Se o total == preço, quer dizer que é o 1º produto, portanto, o menor preço
    if total == price or price < c_price:
        cheapest = name
        c_price = price
    if answer == 'N':
        break

print(f'''\nThe total price is R${total:.2f}
There is(are) {plus1k} product(s) that costs more than R$1000.00
The cheapest product is {cheapest} that costs R${c_price:.2f}''')
