#server:
# otwarcie polaczenia po stornie serwera:
import socket

new_socket = socket.socket()

new_socket.bind(("0.0.0.0", 50000))
new_socket.listen(4)

conn, addr = new_socket.accept()
buffor = 2

while True:
    data = conn.recv(buffor).decode()
    print(data)
    if (len(data) < buffor):
        break

new_socket.close()
new_socket.close()


#client:
import socket

new_socket = socket.socket()

try:
    new_socket.connect(("127.0.0.1",50000))
    new_socket.send(b"Hi Kali ")
    # data = new_socket.recv(2048).decode()
    # print(data)
except:
    print("Polaczenie odrzucone")
finally:
    new_socket.close()