print('Enter your grades')
grade1 = float(input('Grade 1: '))
grade2 = float(input('Grade 2: '))
mean = (grade1 + grade2) / 2
if mean < 5:
    print('You failed and will need to repeat the grade.')
elif 5 <= mean < 7:
    print("You'll need to retake your exams.")
else:
    print('You are approved!')
print(f'Your mean is {mean:.1f}')
