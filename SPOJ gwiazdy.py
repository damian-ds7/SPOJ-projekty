t = int(input())
gwiazdy = []

for i in range(t):
    linia = input().split()
    nazwa, x, y = linia[0], int(linia[1]), int(linia[2])
    gwiazdy.append([nazwa, x])

gwiazdy = sorted(gwiazdy, key = lambda l:(l[1], l[0]))

for i in range(len(gwiazdy)):
    print(gwiazdy[i][0])
