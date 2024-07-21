"""
Napisz program, ktory pobiera od uzytkownika linijki tekstu
ktore musza byc zapisane do pliku
Po wpisaniu exit konczymy wprowadzanie danych i zamykamy plik
"""

i = 0
with open("py-04-l3.txt",'w') as plik:
    while 1==1 :
        i = i+1
        text = input(str(i)+": ")
        if text.strip().lower() == "exit":
            break
        plik.write(text+'\n')
        plik.flush()
