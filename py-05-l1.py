"""
napisz program, ktory pobiera od uzytkownika dwie wartosci
zamienia te wartosci na liczby
wykonuje na tych liczbach operacje +,-,*,/
"""
import moja_biblioteka as mb

def main():
    a = mb.podaj_liczbe("a")
    b = mb.podaj_liczbe("b")
    o = mb.pobierz_operator()
    mb.wykonaj_obliczenia(a,b,o)

print("jestem w programie glownym", __name__)
main()
