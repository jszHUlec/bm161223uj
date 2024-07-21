"""
Napisz program, ktory przyjmuje 2 liczby i wykonuje na nich mnozenie
Napisz obsluge beldu, tak, zeby po wprowadzeniu liter ponownie dokonac
mnozenia na nowych wartosciach
"""
for x in range(4):
    try:
        x = int(input("Podaj x: "))
        y = int(input("Podaj y: "))

        print("x*y = ",x * y)
    except:
        print("Oczekuje tylko liczb!!!")


