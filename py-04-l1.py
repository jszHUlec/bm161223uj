"""
wykonaj obsluge dzielenia przez zero, tak,
zeby uzytkonik mogl poprawic wprowadzone przez siebie dane
"""
# ValueError, ZeroDivisionError
while True:
    try:
        x = int(input("podaj x: "))
        y = int(input("podaj y: "))
        print(x/y)
    except ValueError:
        print("Przyjmuje tylko liczby!!!")
    except ZeroDivisionError:
        print("Dzielenie przez zero jest zabronione!")
    except:
        print("Blad!!!")



