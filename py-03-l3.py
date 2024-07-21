"""
Popros uzytkownika o odgadniecie liczby
Uzytkownik ma 10 prob.
Jezeli odgadnie liczbe, to wystl komunikat 'hurra'
"""

import random
proby = 3
zakres_max = 100
zakres_min = 1

def gra():
    print(f"Witam, w grze 'Zgadnij liczbe' (zakres {zakres_min}-{zakres_max}). Masz {proby} prob na jej odgadniecie ")

    wylosowana_liczba = random.randint(zakres_min, zakres_max)

    for x in range(proby):
        print(f"to jest twoja {x + 1} proba")
        wybrana_lcizba = int(input("?: "))

        if wybrana_lcizba == wylosowana_liczba:
            print("Hurra! wygrales !!!!!")
            break

    if wybrana_lcizba != wylosowana_liczba:
        print("Sprobuj nastepnym razem")
        print("szukana liczba byla:", wylosowana_liczba)

# cwiczenie z menu na zagniezdzanie if-ow w petlach:
while True:
    wybor_uzytkownika = input("""
    1. zagraj!
    exit - wyjscie z programu
    """).upper().strip()

    if wybor_uzytkownika == "1":
         gra()
    elif 'EXIT' == wybor_uzytkownika:
        break
    else:
        print("wybrales bledna opcje")

print("Dzieki, ze zagrales! ")


