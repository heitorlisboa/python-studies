speed = int(input('Enter the your car speed in km/h: '))
if speed <= 80:
    print("You're {1}within{0} the speed limit.".format('\033[m', '\033[1;32m'))
else:
    print("You're going {2}over{1} the speed limit of 80 km/h\n"
          "You will be {2}fined{1} for R${0:.2f}".format((speed - 80) * 7, '\033[m', '\033[1;31m'))
