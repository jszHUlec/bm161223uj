"""
napisz klika funkcji zwracajacych rozne typy danych
i sprawdz jakiego typu dane sa zwracane
"""


x1 = "jeden"
x2 = "dwa"

def return_lista(x1,x2):
    return [x1,x2]

def return_tupla(x1,x2):
    return (x1,x2)

def return_dictionary(x1, x2):
    return {x1:x2}
def main():
    print(return_lista(x1,x2))
    print(return_tupla(x1,x2))
    print(return_dictionary(x1,x2))

main()
