"""
Podaj procentowy wynik testu 0 - 100%
91-100 -> 'A'
81-90 -> 'B'
71-80 -> 'C'
61-70 -> 'D'
ponizej -> 'E'
"""

def glowny():
    wynik = int(input("podaj wynik"))
    if wynik >=91 and wynik <= 100:
        ocena="A"
    elif wynik >= 81 and wynik <= 90:
        ocena="B"
    elif wynik >=71 and wynik <= 80:
        ocena="C"
    elif wynik >=61 and wynik <= 70:
        ocena="D"
    else:
        ocena = "E"
    print(ocena)

glowny()


