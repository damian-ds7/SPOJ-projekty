import math


def czy_pierwsza(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True


t = int(input())
# t = 1
l_pierwsze = [x for x in range(2, int(math.sqrt(1000000000)) + 1) if czy_pierwsza(x)]


for i in range(t):
    licznik = 0
    linia = input().split()
    a, b = int(linia[0]), int(linia[1])
    # a, b = 1, 1000000000
    for j in range(len(l_pierwsze)):
        if a <= l_pierwsze[j] * l_pierwsze[j] <= b:
            licznik += 1
        if l_pierwsze[j] * l_pierwsze[j] > b:
            break
    print(licznik)
