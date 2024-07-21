"""
pobierz pliki do skopiowania od uzytkownika i skopiuj plik!
"""
import os
zrodlo = input("Podaj plik do skopiowania")
cel = input("Podaj docelowa lokalizacje i nazwe")

os.system(f"cp {zrodlo} {cel}")

