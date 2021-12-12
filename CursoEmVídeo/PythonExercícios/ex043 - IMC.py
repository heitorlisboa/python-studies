weight = float(input('Enter your weight (in kilograms): '))
height = float(input('Enter your height (in meters): '))
imc = weight / height**2
if imc <= 18.5:
    print("You're underweight!")
if 18.5 < imc <= 25:
    print("You're in your ideal weight!")
if 25 < imc <= 30:
    print("You're overweight!")
if 30 < imc <= 40:
    print("You're obese!")
if imc > 40:
    print("You have morbid obesity!")
print(f'Your IMC: {imc:.1f}')