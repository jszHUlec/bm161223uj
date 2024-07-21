import requests

# Lista adresów URL do plików PDF
pdf_urls = [
    "https://archiwum.mz.gov.pl/ministerstwo/urzad/przeciwdzialanie-korupcji/dokumenty/badania-opinii-publicznej.zip",
    "https://archiwum.mz.gov.pl/ministerstwo/urzad/przeciwdzialanie-korupcji/dokumenty/miedzynarodowe-konferencje-antykorupcyjne.zip",
    "https://archiwum.mz.gov.pl/ministerstwo/urzad/przeciwdzialanie-korupcji/dokumenty/publikacje-centralnego-biura-antykorupcyjnego.zip",
    "https://archiwum.mz.gov.pl/ministerstwo/urzad/przeciwdzialanie-korupcji/dokumenty/rzadowy-indeks-antykorupcyjny-w-sektorze-obronnym-2015.zip",
    "https://archiwum.mz.gov.pl/ministerstwo/urzad/przeciwdzialanie-korupcji/dokumenty/konflikt-interesow-czym-jest-i-jak-go-unikac.pdf",
]

# Pobierz każdy plik PDF i zapisz go w bieżącym katalogu
for url in pdf_urls:
    response = requests.get(url)

    if response.status_code == 200:
        filename = url.split("/")[-1]
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Plik {filename} pobrany pomyślnie.")
    else:
        print(f"Błąd podczas pobierania pliku {url}: {response.status_code}")
