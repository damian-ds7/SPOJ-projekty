t = int(input())


def rek(n, dl):
    tab = []
    for i in range(dl):
        tab.append('_')
    s = ""
    for i in tab:
        s += i
    print(s)

    for i in range(1, n):
        temp = 0
        for j in range(dl):
            if tab[j] == " ":
                for k in range(temp // 3):
                    tab[j - 2 * temp // 3+k] = ' '
                temp = 0
            else:
                temp += 1

        for k in range(temp // 3):
            tab[dl - 2 * temp // 3 + k] = " "

        s = ""
        for i in tab:
            s += i
        print(s)


for i in range(t):
    x = int(input())
    rek(x, 3**(x - 1))
    print()