n, a, b = list(map(int, input().split()))
namioty = []

for i in range(n):
    namioty.append(list(map(int, input().split())))

ziel_nam = sorted(namioty, key = lambda x: (x[0], x[1]))
zol_nam = sorted(namioty, key = lambda x: (x[1], x[0]))
posort = [ziel_nam, zol_nam]
najwiecej = 0

for i in range(2):
    yel, gre, l_nam, k = 0, 0, 0, 0
    while gre <= a and yel <= b:
        l_nam += 1
        gre += posort[i][k][0]
        yel += posort[i][k][1]
        k += 1
    if gre > a or yel > b:
        if l_nam - 1 > najwiecej:
            najwiecej = l_nam - 1
    else:
        if l_nam > najwiecej:
            najwiecej = l_nam
print(najwiecej)