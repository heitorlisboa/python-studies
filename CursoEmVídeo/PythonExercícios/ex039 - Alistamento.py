from datetime import date
year = int(input('Enter your year of birth: '))
age = date.today().year - year
if age == 18:
    print('You need to enlist this year!')
elif age < 18:
    print(f'You will need to enlist in {18 - age} year(s)!\n'
          f'Your enlistment will be in {year + 18}.')
else:
    print(f"You're {age - 18} year(s) delayed for enlistment!\n"
          f"Your enlistment was in {year + 18}.")
