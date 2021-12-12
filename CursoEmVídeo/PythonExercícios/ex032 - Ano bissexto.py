from datetime import date
year = int(input("Enter any year (type 0 to use today's year): "))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('\033[1;32m{} is a leap year!'.format(year))
else:
    print('\033[1;31m{} is not a leap year'.format(year))
