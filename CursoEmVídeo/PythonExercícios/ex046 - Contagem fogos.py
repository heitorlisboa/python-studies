from time import sleep
from emoji import emojize
print('{:=^33}'.format('Count for the fireworks'))
for c in range(10, 0, -1):
    print(c, end=' ')
    sleep(1)
print(emojize('ZERO!!! :fireworks: :fireworks:'))
