import copy

pola = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

z = int(input())
# z = 1

def pion(k, p, plansza):
    y, x = p[0], p[1]
    if y + 1 <= -1:
        if x + 1 <= 7:
            if (y + 1, x + 1) == k:
                return True
        if x - 1 >= 0:
            if (y + 1, x - 1) == k:
                return True
    return False


def skoczek(k, s, plansza):
    y, x = s[0], s[1]
    if y + 2 <= -1:
        if x - 1 >= 0:
            if (y + 2, x - 1) == k:
                return True
        if x + 1 <= 7:
            if (y + 2, x + 1) == k:
                return True
    if y - 2 >= -8:
        if x - 1 >= 0:
            if (y - 2, x - 1) == k:
                return True
        if x + 1 <= 7:
            if (y - 2, x + 1) == k:
                return True
    if x - 2 >= 0:
        if y + 1 <= -1:
            if (y + 1, x - 2) == k:
                return True
        if y - 1 >= -8:
            if (y - 1, x - 2) == k:
                return True
    if x + 2 >= 0:
        if y + 1 <= -1:
            if (y + 1, x + 2) == k:
                return True
        if y - 1 >= -8:
            if (y - 1, x + 2) == k:
                return True
    return False


def wieza(k, w, plansza):
    ruchy = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    y, x = w[0], w[1]
    for d in ruchy:
        czy_przeskok = False
        for j in range(1, 8):
            kol_kon = x + d[0] * j
            wier_kon = y + d[1] * j
            if 0 <= kol_kon < 8 and -1 >= wier_kon >= -8:
                if plansza[wier_kon][kol_kon] == '.' or plansza[wier_kon][kol_kon] == 'K':
                    if (wier_kon, kol_kon) == k:
                        return True
                else:
                    czy_przeskok = True
                    break
            else: break
        if czy_przeskok: continue
    return False


def goniec(k, g, plansza):
    ruchy = [(1, -1), (-1, -1), (-1, 1), (1, 1)]
    y, x = g[0], g[1]
    for d in ruchy:
        czy_przeskok = False
        for j in range(1, 8):
            kol_kon = x + d[0] * j
            wier_kon = y + d[1] * j
            if 0 <= kol_kon < 8 and -1 >= wier_kon > -9:
                if plansza[wier_kon][kol_kon] == '.' or plansza[wier_kon][kol_kon] == 'K':
                    if (wier_kon, kol_kon) == k:
                        return True
                else:
                    czy_przeskok = True
                    break
            else: break
        if czy_przeskok: continue
    return False


def hetman(k, h, plansza):
    if wieza(k, h, plansza) or goniec(k, h, plansza):
        return True
    return False


ruchy = {'P': pion, 'S': skoczek, 'W': wieza, 'G': goniec, 'H': hetman}

for i in range(z):
    piony = []
    wsp = []
    krol = tuple()
    plansza = [['.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.'],
               ['.', '.', '.', '.', '.', '.', '.', '.']]
    # asd = ['8 A H',
    #        '4 A W',
    #        '5 E K',
    #        '5 H W',
    #        '6 G P',
    #        '7 D P',
    #        '8 H G',
    #        '8 G S',
    #        '8 C S']
    s = int(input())
    # s = len(asd)
    for j in range(s):
        linia = input().split()
        # linia = asd[j].split()
        y, x, f = -int(linia[0]), pola[linia[1]], linia[2]
        plansza[y][x] = f
        if f == 'K':
            krol = (x, y)
        else:
            if f not in piony:
                piony.append(f)
                wsp.append([(y, x)])
            else:
                wsp[piony.index(f)].append((y, x))

    k_ruchy = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    szach = 0
    mozliwe_ruchy = 0

    for r in k_ruchy:
        wiersz = krol[1] + r[1]
        kol = krol[0] + r[0]
        kopia = copy.deepcopy(plansza)
        kopia[krol[1]][krol[0]] = '.'
        kopia[wiersz][kol] = 'K'
        if -1 >= wiersz >= -8 and 0 <= kol <= 7:
            mozliwe_ruchy += 1
            czy_szach = False
            for k in range(len(wsp)):
                for l in range(len(wsp[k])):
                    if ruchy[piony[k]]((wiersz, kol), wsp[k][l], kopia):
                        szach += 1
                        czy_szach = True
                        break
                if czy_szach: break

    if szach >= mozliwe_ruchy:
        print('MAT')
    else:
        print('SZACH')
