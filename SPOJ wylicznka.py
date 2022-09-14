from math import ceil
from math import pow

while True:
    try:
        k = int(input())
        pot = 1
        dl = 0
        x = 0
        while x < k:
            x += pow(2, pot)
            pot += 1
            dl += 1
        pom = pow(2, dl) - (x - k)
        for i in reversed(range(1, dl + 1)):
            w = ceil(pom / pow(2, i - 1))
            if w % 2 == 0:
                print('6', end = '')
            else: print('5', end = '')
        print()
    except:
        break
