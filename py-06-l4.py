#server:
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



#client:
import socket
import base64

new_socket = socket.socket()
new_socket.connect(("127.0.0.1",4441))

prosba_o_login = new_socket.recv(2048).decode()
login = input(prosba_o_login)
new_socket.send(base64.b64encode(login.encode("UTF-8")))

prosba_o_haslo = new_socket.recv(2048).decode()
haslo = input(prosba_o_haslo)
new_socket.send(base64.b64encode(haslo.encode("UTF-8")))


czy_ok = new_socket.recv(2048).decode()
if(czy_ok == "ok"):
    print("hura")

new_socket.close()