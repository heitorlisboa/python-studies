from random import shuffle, random
print('Enter the name of the four students')
s1 = input('Student 1: ')
s2 = input('Student 2: ')
s3 = input('Student 3: ')
s4 = input('Student 4: ')
seq = [s1, s2, s3, s4]
shuffle(seq)
print('The {2}order{1} of presentation is {2}{0}{1}'.format(seq, '\033[m', '\033[1;35m'))
