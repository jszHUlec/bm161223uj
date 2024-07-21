
with open("log.txt") as plik:
    with open("nowy.log","a") as nowy_plik:
        for linijka in plik.readlines():
            podzielona_linijka = linijka.split()
            if podzielona_linijka[2] in ["ERROR","FATAL"]:
                if "NetJournalDevApp" in linijka:
                    print(podzielona_linijka[:4])
                    nowy_plik.write(""+str(podzielona_linijka[:4])+"\n")


