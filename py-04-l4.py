"""
Napisz program, ktory pobiera nazwe pliku i wyswietla go linijka po linijce w konsoli
"""

nazwa_pliku = input("Podaj nazwe pliku: ").strip()

with open(nazwa_pliku,'r') as plik:
    for linijka in plik.readlines():
        print(linijka, end="")