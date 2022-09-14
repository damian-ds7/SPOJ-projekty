import itertools

t = int(input())


def podzbiory(zbior, k):
    return list(itertools.combinations(zbior, k))


for i in range(t):
    n, k = list(map(int, input().split()))
    zbior = []
    for j in range(1, n + 1):
        zbior.append(j)

    pz = podzbiory(zbior,k)

    for l in range(len(pz)):
        for m in range(len(pz[l])):
            print(pz[l][m], end = ' ')
        print()
    print()
