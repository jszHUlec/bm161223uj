"""
Napisz program, ktory tworzy slownik z uslugami sieciowymi i przypisanymi im portami
Popros uzytkownika o wskazanie nazwy uslugi
a program wyswietli przypisany numer portu
"""

serwisy = {"FTP":"21","SSH":"22", "HTTP":"80", "HTTPS":"443"}

usluga = input("Podaj nazwe uslugi").upper().strip()
print( serwisy[ usluga ] )

