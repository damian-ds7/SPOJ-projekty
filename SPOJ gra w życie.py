n = int(input())

for i in range(n):
    plansza = list()
    for j in range(5):
        plansza.append(input())
    nowa = list()

    for pokolenia in range(99):
        for i in range(len(plansza)):
            linia = plansza[i]
            poprzednia = plansza[(i - 1) % 5]
            nastepna = plansza[(i + 1) % 5]

            nowa_linia = list()

            for j in range(len(linia)):
                sasiedzi = 0
                if linia[(j - 1) % 5] == '1':
                    sasiedzi += 1
                if linia[(j + 1) % 5] == '1':
                    sasiedzi += 1
                if poprzednia[j] == '1':
                    sasiedzi += 1
                if poprzednia[(j - 1) % 5] == '1':
                    sasiedzi += 1
                if poprzednia[(j + 1) % 5] == '1':
                    sasiedzi += 1
                if nastepna[j] == '1':
                    sasiedzi += 1
                if nastepna[(j - 1) % 5] == '1':
                    sasiedzi += 1
                if nastepna[(j + 1) % 5] == '1':
                    sasiedzi += 1

                if linia[j] == '0' and sasiedzi == 3:
                    nowa_linia.append('1')
                elif linia[j] == '1' and (sasiedzi == 2 or sasiedzi == 3):
                    nowa_linia.append('1')
                else:
                    nowa_linia.append('0')

            nowa.append(nowa_linia)

        plansza = nowa.copy()
        nowa = list()

    if any('1' in x for x in plansza):
        print('yes')
    else: print('no')