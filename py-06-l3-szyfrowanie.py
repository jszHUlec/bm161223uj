#client:
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


#serwer:
import socket
import base64

mysocket = socket.socket()
mysocket.bind(("0.0.0.0",50001))
mysocket.listen(1)

print("waiting for connection...")

con, adr = mysocket.accept()
print(f"client connected - > {adr}")

while True:
    toSent=input("wiadomosc dla clienta:")
    con.send(base64.b64encode(toSent.encode()))

    if toSent.strip().upper() == "EXIT":
        print("polaczenie bedzie zamkniete")
        con.close()
        break

    fromClient = base64.b64decode(con.recv(2048).decode()).decode("UTF-8")
    print(fromClient)
    if fromClient.strip().upper() == "EXIT":
        print("client zakonczyl polaczenie")
        con.close()
        break

mysocket.close()