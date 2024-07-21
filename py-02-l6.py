"""
stworz liste elementow. Manipuluj lista, zeby cos usunac i dodac dodatkowe elementy
"""

lista = ["Malopolskie", "Mazowieckie", "Slaskie"]
lista.append("Wielkoplskie")
lista.insert(0,'Lubuskie')
miasta = ["Krakow", "Warszawa", "Poznan"]
rzeki = ['Wisla', 'Odra']

lista.append(miasta)
miasta.append(rzeki)

print(lista)
print(lista[-1][-1][0])
