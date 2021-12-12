# Método "gambiarra" usando IN
'''gender = str(input("Enter you gender [M/F]: ")).upper().strip()
while gender not in 'MF':
    gender = str(input("Invalid! Enter you gender [M/F]: ")).upper().strip()
print(f'Your gender is {gender}. Thanks for submitting!')'''

# Método usando != 'M' AND != 'F'
gender = str(input("Enter you gender [M/F]: ")).upper().strip()
while gender != 'M' and gender != 'F':
    gender = str(input("Invalid! Enter you gender [M/F]: ")).upper().strip()
print(f'Your gender is {gender}. Thanks for submitting!')
