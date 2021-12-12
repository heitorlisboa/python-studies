age_sum = 0
greater_age = 0
oldest = ''
wu20 = 0
for c in range(1, 5):
    print(f'---- Person {c} ----')
    name = str(input('Name: '))
    age = int(input('Age: '))
    gender = str(input('Gender [M/F]: ')).strip().upper()
    age_sum += age
    if gender == 'M' and age > greater_age:
        greater_age = age
        oldest = name
    if gender == 'F' and age < 20:
        wu20 += 1
mean = age_sum / 4
print('''\nThe mean of the ages is {}
The oldest man is {}, who is {} years old
And there is(are) {} woman(s) under 20'''.format(mean, oldest.capitalize().strip(), greater_age, wu20))
