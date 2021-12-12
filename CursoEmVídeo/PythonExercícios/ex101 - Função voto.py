def voto(year):
    from datetime import date
    age = date.today().year - year
    if age < 16:
        return f'Being {age} years old: DENIED'
    elif age < 18 or age > 69:
        return f'Being {age} years old: OPTIONAL'
    else:
        return f'Being {age} years old REQUIRED'


yearOfBirth = int(input('Enter your year of birth: '))
print(voto(yearOfBirth))
