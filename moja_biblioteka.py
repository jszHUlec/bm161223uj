def wykonaj_obliczenia(a, b, o):
    if o == "+":
        print(a,"+",b,"=", a + b)
    elif o == "-":
        print(a,"-",b,"=", a - b)
    elif o == "*":
        print(a,"*",b,"=", a * b)
    elif o == "/":
        print(a,"/",b,"=", a / b)
    else:
        print("zly operator. To jest blad")
        raise NotImplementedError

def podaj_liczbe(nazwa):
    while True:
        try:
            liczba = int(input("podaj "+nazwa+" : "))
            return liczba
        except:
            print("przyjmuje tylko liczby. Sprobuj ponownie")

def pobierz_operator():
    operatory = ["+","-","*","/"] # white lista
    print("wybirz operator z dostepnych: ",operatory)
    while True:
        operator = input("podaj operator:").strip()
        if operator in operatory:
            return operator
        else:
            print("zly wybor. Sprobuj ponownie")


if __name__ == "__main__":
    print("Jestem biblioteka. Musisz mnie gdzies zaimportowac, zeby zadzialal")

    x = podaj_liczbe("x")
    if isinstance(x, int) :
        print("ok")
