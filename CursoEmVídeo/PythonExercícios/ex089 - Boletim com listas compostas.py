all_students = []

while True:
    name = str(input('Name: ')).title()
    grade1 = float(input('Grade 1: '))
    grade2 = float(input('Grade 2: '))
    mean = (grade1 + grade2) / 2
    all_students.append([name, [grade1, grade2], mean])
    answer = str(input('Do you wanna continue? [Y/N] ')).upper()
    while answer != 'Y' and answer != 'N':
        answer = str(input('INVALID! Do you wanna continue? [Y/N] ')).upper()
    if answer == 'N':
        all_students.sort()
        break

print('-' * 40)
print(f'{"No.":<4}{"Name":<12}{"Mean":>4}')
print('-' * 20)
for index, student in enumerate(all_students):
    print('{:<4}{:<12}{:>4.1f}'.format(index+1, student[0], student[2]))
print('-' * 40)

while True:
    student_pos = int(input('Show grades from which student? (0 = stop) ')) - 1
    while student_pos >= len(all_students):
        student_pos = int(input('INVALID! Show grades from which student? (0 = stop) ')) - 1
    if student_pos < 0:
        break
    print('The grades from {} are {}'.format(all_students[student_pos][0], all_students[student_pos][1]))
    print('-' * 40)
