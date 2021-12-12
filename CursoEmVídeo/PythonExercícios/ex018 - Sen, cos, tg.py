from math import sin, cos, tan, radians
angle = float(input('Enter the angle to see its sine, cosine and tangent: '))
print('The {4}sine{3} is {4}{0:.2f}{3}\n'
      'The {5}cosine{3} is {5}{1:.2f}{3}\n'
      'The {6}tangent{3} is {6}{2:.2f}{3}'.format(sin(radians(angle)), cos(radians(angle)), tan(radians(angle)),
                                                  '\033[m', '\033[1;34m', '\033[1;35m', '\033[1;36m'))
