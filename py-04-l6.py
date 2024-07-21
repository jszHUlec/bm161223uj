"""
Napisz program, ktory tworzy katalogi
i przechodzi pomiedzy nimi wykorzystujac modul OS
"""
import datetime
import os

while True:
    print("Jestes w katalogu", os.getcwd())
    directory = input("Podaj folder albo wpisz exit aby wyjsc z programu:")
    if directory.strip().lower() == "exit":
        break
    else:
        if directory in os.listdir():
            pass
        else:
            os.mkdir(directory)

        print(os.chdir(directory))

    filename = input("podaj nazwe pliku: ")
    if filename.strip().lower() == 'exit':
        break

    with open(filename,'w') as plik:
        plik.write(str(datetime.datetime.now()))