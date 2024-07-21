import os

def wyswietl_strukture(sciezka, poziom=0):
  """
  Funkcja rekurencyjna wyświetlająca strukturę katalogów i plików w podanym folderze z wcięciami.

  Argumenty:
    sciezka (str): Ścieżka do folderu, którego strukturę chcemy wyświetlić.
    poziom (int, domyślnie 0): Poziom zagnieżdżenia katalogu.
  """
  pliki = os.listdir(sciezka)

  for plik in pliki:
    pelna_sciezka = os.path.join(sciezka, plik)
    if os.path.isdir(pelna_sciezka):
      print(f"{poziom * '  '}{plik} (katalog)")
      wyswietl_strukture(pelna_sciezka, poziom + 1)
    else:
      print(f"{poziom * '  '}{plik}")

# Pobierz ścieżkę od użytkownika
sciezka = input("Podaj ścieżkę do folderu: ")

# Wyświetl strukturę katalogów i plików
wyswietl_strukture(sciezka)