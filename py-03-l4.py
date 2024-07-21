"""
Napisz program,ktory buduje slownik uslug internetowy.
wprowadzamy nazwe uslugi i numer portu np. HTPP:80
budujemy menu do wprowadzania danych i ich wyswietlania
"""

slownik = {}

while True:
    wybor_uzytkownika = input("""
   1 - wprowadz nowa wartosc
   2 - wyswietl slownik
exit - wyjscie z programu 
""").upper().strip()

    if wybor_uzytkownika == "1":
        usluga = input("Podaj nazwe uslugi:").upper().strip()
        port = int(input("Podaj port uslugi").strip())
        slownik[usluga] = port
    elif wybor_uzytkownika == "2":
        print(slownik)
    elif wybor_uzytkownika == "EXIT":
        print("wychodze z programu")
        break
    else:
        print("wybrales bledna opcje")