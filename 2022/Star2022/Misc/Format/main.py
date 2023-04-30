import socket
import threading
from secret import flag


class Dindon():
    def __init__(self):
        self.__glou = flag

    def __str__(self):
        return "glouglouglou"

    def __repr__(self):
        return self.__glou

    def dis_bonjour(self):
        return "Glouglouglouglouglou"

    def dis_padaccord(self):
        return "glouglouglouglou"

    def donne_la_pate(self):
        return "glouglou?"


class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        super().__init__()
        self.__clientsocket = clientsocket

    def run(self):
        dindon = Dindon()
        self.__clientsocket.send(dindon.dis_bonjour().encode() + b'\n')
        while True:
            self.__clientsocket.send(dindon.donne_la_pate().encode() + b'\n>> ')
            try:
                r = self.__clientsocket.recv(2048).decode('utf-8')
            except UnicodeDecodeError:
                self.__clientsocket.send(dindon.dis_padaccord().encode() + b'\n')
                print(1)
            try:
                # self.__clientsocket.send(('Toi : ' + r + 'Le dindon être comme : {dindon.dis_padaccord()} (il est pas d\'accord)\n').format(dindon).encode('utf-8'))
                # grrrr! Ça marhe pas! Fuck le responsive de toute façon un dindon pas d'accord ça dit toujours glouglouglouglou
                self.__clientsocket.send(('Toi : ' + r + 'Le dindon être comme : glouglouglouglou (il est pas d\'accord)\n').format(dindon).encode('utf-8'))
            except BrokenPipeError:
                return
            except Exception:
                print(2)
                self.__clientsocket.send(dindon.dis_padaccord().encode() + b'\n')


if __name__ == '__main__':
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock.bind(("", 2042))

    while True:
        tcpsock.listen(10)
        (clientsocket, (ip, port)) = tcpsock.accept()
        newthread = ClientThread(ip, port, clientsocket)
        newthread.start()
