"""
Stworz zagniezdzona liste i wyswietl jej zawartosc za pomoca funkcji rekurencyjnej
"""

lista = [1,2,"a",[3,4,[45,"c",87],"b",33],22]

def drukuj_liste(lista):
    for item in lista:
        if type(item) == list:
            drukuj_liste(item)
        elif type(item) == str :
            print(item)

drukuj_liste(lista)