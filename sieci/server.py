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