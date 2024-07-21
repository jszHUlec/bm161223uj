"""
Wykonaj ping i zapisz go do pliku
Odczytaj zapisany plik i sprawdz czy maszyna odpowiadam na PING
"""
import os
import datetime

ip = input("podaj ip: ").strip()

os.system("ping -c 2 "+ ip +" > ip.txt")

with open("ip.txt","r") as plik:
    if "icmp_seq" in plik.read():
        print("Host is UP at "+str(datetime.datetime.now()))
    else:
        print("Host is DOWN at "+str(datetime.datetime.now()))