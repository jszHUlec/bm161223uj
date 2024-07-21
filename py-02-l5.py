"""
pobierz od uzytkownika IP 192.168.10.0
i wysweitl poszczegolne elementy w postaci binarnej
192 -> 11000000
168->  10101000
"""
ip = input("Podaj swoje IP (np. 192.168.8.1) : ")
elementy = ip.split('.')

for x in range(32):  # 0,1,2,3
    print(elementy[x], "=>", bin(int(elementy[x]))[2:])
