"""
pobierz od uzytkownika liczbe wierszy
Pobierz od uzytkowniak liczbe kolumn
"""
tablice = []
ilosc_wierszy = int(input("Podaj ilosc wierszy: "))
ilosc_kolumn = int(input("Podaj ilosc kolumn: "))

for x in range(ilosc_wierszy):
    tablice.append([])
    for y in range(ilosc_kolumn):
        tablice[x].append(y)

print(tablice)

