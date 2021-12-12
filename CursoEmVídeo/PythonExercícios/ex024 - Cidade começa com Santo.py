city = str(input('Enter the name of your city: ')).strip()
# print('The name of your city starts with "Santo": {}'.format('santo' in city.lower()[:5]))
color = '\033[1;31m'
answer = 'No'
if city.lower().split()[0] == 'santo':
    color = '\033[1;32m'
    answer = 'Yes!'
print('The name of your city starts with "Santo"? {1}{0}'.format(answer, color))
