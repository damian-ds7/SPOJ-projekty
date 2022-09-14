d = int(input())

ruchy = {"L": {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)},
         "P": {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}}

for i in range(d):
        plansza = [['.'] * 6 for x in range(6)]
        # plansza[2][2] = 'x'
        n = int(input()) % 4592
        mrowka = [2, 2]
        r = (-1, 0)
        # for k in range(len(plansza)):
        #     print(''.join(plansza[k]))
        # print('__________' + str(1))
        # print()
        for j in range(n):
            if plansza[mrowka[0]][mrowka[1]] == '.':
                kier = "L"
                plansza[mrowka[0]][mrowka[1]] = 'x'
            else:
                kier = "P"
                plansza[mrowka[0]][mrowka[1]] = '.'
            r = ruchy[kier][r]
            mrowka[0] += r[0]
            mrowka[1] += r[1]
            if mrowka[0] > 5:
                mrowka[0] = 0
            elif mrowka[0] < 0:
                mrowka[0] = 5
            elif mrowka[1] > 5:
                mrowka[1] = 0
            elif mrowka[1] < 0:
                mrowka[1] = 5
        for k in range(len(plansza)):
            print(''.join(plansza[k]))