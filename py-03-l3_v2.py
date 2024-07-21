import random

zakres_liczb = list(range(1, 11))
strzal = None
max_ilosc_prob = 3
proba = 0
random.shuffle(zakres_liczb)
losowy_numer = random.choice(zakres_liczb)

print("Zgadnij liczbe calkowita od 1 do 10.")
while strzal != losowy_numer and proba < max_ilosc_prob:
    proba +=1
    strzal = int(input("Podaj liczbe calkowita: "))

    if strzal == losowy_numer:
        print(f"Gratulacje! Zgadles liczbe {losowy_numer}.")
    else:
        print(f"Nie udalo sie. Sprobuj ponownie. Pozostalo { max_ilosc_prob - proba } prob")

print(f"Poszukiwana liczba byla: {losowy_numer}")