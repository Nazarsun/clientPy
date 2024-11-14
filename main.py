import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 80))

while True:
    sock.send(bytes('hello, world!', encoding=' utf-8 '))
    data = sock.recv(1024)
    print("Current date & time: ", data.decode("utf-8"))
    while True:
        h = input()
        sock.send(bytes(h, encoding="utf-8"))
        if h == 'Y':
            break
        elif h == 'N':
            sock.shutdown(0)
            sock.close()
            exit(0)