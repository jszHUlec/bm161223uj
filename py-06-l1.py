# otwarcie polaczenia po stornie serwera:
import socket

new_socket = socket.socket()

new_socket.bind(("0.0.0.0",50000))
new_socket.listen(4)

conn, addr = new_socket.accept()


new_socket.close()

# a pozniej z terminala: nc 127.0.0.1 50000