import pyqtgraph as pg
import socket
import _thread as  tr
import time
import sys
from pyqtgraph.Qt import QtGui, QtCore

DATA = [0, 0]

def dataReceiving(delay):
    while True:
        time.sleep(delay)
        DATA.append(int(sock.recv(BUFFER)))
        print(DATA)


def plotDrawing(delay):
    while True:
        if sys.flags.interactive != 1 or not hasattr(QtCore, 'PYQT_VERSION'):
            pg.QtGui.QApplication.exec_()
        pg.plot(DATA, clear = True)
        #time.sleep(delay)

def logInMessage():
    MESSAGE = "HELLO I\'M CONNECTED"
    sock.send(MESSAGE.encode())


print("Add meg a szerver ip-jét!")
IP = input()
print("Add meg a portot a csatlakozáshoz!")
PORT = int(input())
BUFFER = 2048
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP,PORT))

logInMessage()

tr.start_new_thread(dataReceiving, (2, ))
tr.start_new_thread(plotDrawing, (2, ))


