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