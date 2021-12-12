from ex115.lib.menu import *
from ex115.lib.file import *
from time import sleep

file = 'cursoemvideo.txt'

if not fileExist(file):
    createFile(file)

while True:
    answer = menu('See registered persons', 'Register a person', 'Quit system')
    if answer == 1:
        betweenLines('PERSONS REGISTERED')
        readFile(file)
    elif answer == 2:
        betweenLines('REGISTER')
        name = str(input('Name: '))
        age = inputWhole('Age: ')
        register(file, name, age)
    elif answer == 3:
        betweenLines('Exiting system... Goodbye!')
        sleep(1)
        break
    else:
        print(betweenColors('ERROR: Enter a valid option.', colors['red']))
    sleep(1)
