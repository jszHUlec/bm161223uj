import socket
import base64

my_sock = socket.socket()
my_sock.bind(("0.0.0.0",4441))
my_sock.listen(1)

con, adr = my_sock.accept()

con.send("Podaj login:".encode())
data = con.recv(2048).decode("UTF-8")
login = base64.b64decode(data)

con.send("Podaj haslo:".encode())
data = con.recv(2048).decode("UTF-8")
haslo = base64.b64decode(data)

print(login)
print(haslo)


con.send("ok".encode())

my_sock.close()
input("wcisnij enter")