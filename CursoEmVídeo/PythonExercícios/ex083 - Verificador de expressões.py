# Meu método sem usar lista
"""expression = str(input('Enter a mathematical expression: '))
if expression.count('(') == expression.count(')'):
    print('Your expression is correct!')
else:
    print('Your expression is INCORRECT.')"""

# Método Guanabara usando lista (modificado por mim)
expression_list = []
expression = str(input('Enter a mathematical expression: ')).strip()
for p, v in range(0, len(expression)):
    if v == '(':
        expression_list.append(v)
    elif v == ')':
        if expression_list.count('(') > 0:
            expression_list.pop()
        else:
            expression_list.append(')')
if len(expression_list) == 0:
    print('Your expression is correct!')
else:
    print('Your expression is INCORRECT.')
