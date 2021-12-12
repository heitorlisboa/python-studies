name = input('Enter your full name: ')
color = '\033[1;31m'
answer = 'No'
if 'silva' in name.lower():
    color = '\033[1;32m'
    answer = 'Yes!'
print('Your name has "Silva": {1}{0}'.format(answer, color))
