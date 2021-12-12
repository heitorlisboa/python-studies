words = ('LEARN', 'PROGRAM', 'LANGUAGE', 'PYTHON', 'COURSE', 'FREE', 'STUDY', 'PRACTICE', 'WORK', 'MARKET',
         'PROGRAMMER', 'FUTURE')
for w in words:
    print(f'In the word {w} there is(are) the vowel(s)', end=' ')
    for letter in w:
        if letter in 'AEIOU':
            print(letter, end=' ')
    print('')
