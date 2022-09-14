def plecak(pojemnosc, rozmiary, wartosci, n):
    tab = [[0 for x in range(pojemnosc + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(pojemnosc + 1):
            if i == 0 or j == 0:
                tab[i][j] = 0
            elif rozmiary[i - 1] <= j:
                tab[i][j] = max(wartosci[i - 1] + tab[i - 1][j - rozmiary[i - 1]], tab[i - 1][j])
            else:
                tab[i][j] = tab[i - 1][j]

    return tab[n][pojemnosc]


def rek_plecak(pojemnosc, rozmiary, wartosci, n):
    if n == 0 or pojemnosc == 0:
        return 0
    if rozmiary[n - 1] > pojemnosc:
        return rek_plecak(pojemnosc, rozmiary, wartosci, n - 1)
    else:
        return max(wartosci[n - 1] + rek_plecak(pojemnosc - rozmiary[n - 1], rozmiary, wartosci, n - 1),
                                    rek_plecak(pojemnosc, rozmiary, wartosci, n - 1))


pojemnosc = 10
rozmiary = [5, 3, 3, 4, 5]
wartosci = [1, 2, 1, 4, 1]
n = len(wartosci)
print(plecak(pojemnosc, rozmiary, wartosci, n))
print(rek_plecak(pojemnosc, rozmiary, wartosci, n))