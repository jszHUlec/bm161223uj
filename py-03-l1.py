"""
Pobierz od uzytkownika liczbe i uzyj jej w petli for.
Wysweitl wartosci od 0 do wprowadzonej liczby, oddzielajac je przecinkiem
"""

ilosc_krokow = int(input("podaj ile krokow mam zrobic?:"))

for x in range(1, ilosc_krokow+1): # x = 32
    if x == ilosc_krokow: # True
        print(x) # wykona sie!
        print(" -- koniec --")
    else:
        print(x, end=",")