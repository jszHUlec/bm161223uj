#server:
import socket

mysocket = socket.socket()
mysocket.bind(("0.0.0.0",50001))
mysocket.listen(1)

print("waiting for connection...")

con, adr = mysocket.accept()
print(f"client connected - > {adr}")

while True:
    toSent=input("wiadomosc dla clienta:")
    con.send(toSent.encode())

    if toSent.strip().upper() == "EXIT":
        print("polaczenie bedzie zamkniete")
        con.close()
        break

    fromClient = con.recv(2048).decode()
    print(fromClient)
    if fromClient.strip().upper() == "EXIT":
        print("client zakonczyl polaczenie")
        con.close()
        break

mysocket.close()


#client:
import socket

new_socket = socket.socket()
new_socket.connect(("127.0.0.1", 50001))
print("connection established....")

while True:
    fromServer = new_socket.recv(2048).decode()
    print(fromServer)

    if fromServer.strip().upper() == "EXIT":
        print("server przerwal polaczenie")
        new_socket.close()
        break

    toServer = input("widomosc do Serwera:")
    new_socket.send(toServer.encode())
    if toServer.strip().upper() == "EXIT":
        new_socket.close()
        print("koncze program")
        break

new_socket.close()