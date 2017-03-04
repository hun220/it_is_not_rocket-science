import pyqtgraph as pg
import socket
from pyqtgraph.Qt import QtGui, QtCore


DATA = [0]

def update():
    #pw.plot(DATA, clear=True)
    DATA.append(int(sock.recv(BUFFER)))
    pw.plot(DATA, clear=True)


print("Add meg a szerver ip-jét!")
IP = input()
print("Add meg a portot a csatlakozáshoz!")
PORT = int(input())
BUFFER = 1024
MESSAGE = "HELLO! I\'m connected!"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((IP,PORT))
sock.send(MESSAGE.encode())

pw = pg.plot()
timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(16)
