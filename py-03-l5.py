"""
Mamy do dyspozycji budzet i owoce w sklepie
napisz program, ktory dodaje do koszyka produkty
jezeli mamy na nie pieniadze
wpisanie 'exit' konczy program i podsumowuje koszyk
"""

budzet = 20
owoce = { "jablko":5, "mandarynki":10, "pomarancza":8, "wisnia":15 }
koszyk = []

def podsumowanie():
    print("podsumowanie:")
    print("twoj koszyk:", koszyk)
    print("pozostaly budzet: ", budzet)

while True:
    wybor_uzytkownika = input("""
    1 - wybranie owocu do koszyka
    2 - podsumowanie koszyka
    3 - dostepne produkty
    wpisanie 'exit' konczy program i podsumowuje koszyk
    """).upper().strip()

    if wybor_uzytkownika == "1":
        print("dostepne sa:", owoce)
        podsumowanie()
        wybor = input("?: ").lower().strip()
        cena = owoce[wybor]
        if budzet - cena < 0:
            print("nie masz srodkow")
            continue
        budzet = budzet - cena
        koszyk.append(wybor)
    elif wybor_uzytkownika == "2":
        podsumowanie()
    elif wybor_uzytkownika == "3":
        print("dostepne sa:", owoce)
    elif wybor_uzytkownika == "EXIT":
        print("wychodze z programu")
        podsumowanie()
        break
    else:
        print("wybrales bledna opcje")