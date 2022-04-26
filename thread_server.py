from socket import socket
from threading import Thread
from datetime import datetime


def main():

    class MulStream(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            self.cclient.send(str(datetime.now()).encode('utf-8'))
            self.cclient.close()

    server = socket()
    server.bind(('192.168.2.238', 6788))
    server.listen(512)
    print('服务器启动开始监听...')
    while True:
        client, addr = server.accept()
        MulStream(client).start()


if __name__ == '__main__':
    main()