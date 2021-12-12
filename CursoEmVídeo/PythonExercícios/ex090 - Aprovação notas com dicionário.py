student = dict()
student['name'] = str(input('Name: ')).title()
student['mean'] = float(input(f'{student["name"]}\'s mean: '))

if student['mean'] < 5:
    student['situation'] = 'DISAPPROVED'
elif 5 <= student['mean'] < 7:
    student['situation'] = 'NEED TO RETAKE THE EXAMS'
else:
    student['situation'] = 'APPROVED'

for k, v in student.items():
    print(f'The {k} is {v}')
