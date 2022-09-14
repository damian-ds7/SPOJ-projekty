t = int(input())
# t = 1


def cantor(start, dl, linia):
    seg = dl // 3
    if seg == 0:
        return None
    for x in range(wys - linia):
        i = linia + x
        for y in range(seg):
            j = start + seg + y
            poz = i * szer + j
            linie[poz] = ' '
    cantor(start, seg, linia + 1)
    cantor(start + seg * 2, seg, linia + 1)
    return None


for i in range(t):
    wys = int(input())
    # wys = 4
    szer = 3 ** (wys - 1)
    linie = ['_'] * (szer * wys)
    cantor(0, szer, 1)

    for j in range(wys):
        pocz = szer * j
        print(''.join(linie[pocz: pocz + szer]))
    print()