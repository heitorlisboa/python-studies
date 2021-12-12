in_full = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
           'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
           'twenty')
while True:
    num = int(input('Enter a whole number from 1 to 20 see it written in full: '))
    if not 0 <= num <= 20:
        print('INVALID!', end=' ')
    else:
        print(f'{num} written in full is "{in_full[num]}"')
        while True:
            answer = str(input('Do you wanna continue? [Y/N] ')).upper()
            if answer == 'Y' or answer == 'N':
                break
            print('INVALID!', end=' ')
        if answer == 'N':
            break
