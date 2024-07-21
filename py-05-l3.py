"""
wyedytuj zmienna globalna z poziomu funkcji
"""
zmienna = 0

def podmien_wartosc(nowa_wartosc):
    global zmienna
    zmienna = nowa_wartosc

od_uzytkownika = input("podaj liczbe: ")
podmien_wartosc(od_uzytkownika)

print(zmienna)

