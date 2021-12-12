house = float(input('Enter the house price: R$'))
salary = float(input('Your salary: R$'))
years = int(input('How many years to pay off? '))
installment = house / (years * 12)
if installment <= (0.3 * salary):
    print(f'The monthly installment is R${installment:.2f}')
elif installment > (0.3 * salary):
    print("The installment (R${:.2f}) exceeds 30% of your salary (R${}), "
          "therefore you can't finance it.".format(installment, (0.3 * salary)))
