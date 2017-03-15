import pyqtgraph as pg
import socket
import _thread as  tr
import time
import sys
from pyqtgraph.Qt import QtGui, QtCore

DATA = []

def dataReceiving(delay):
    while True:
        time.sleep(delay)
        DATA.append(int(sock.recv(BUFFER)))
        print(DATA)


def plotDrawing(delay):
    pw = pg.plot()
    while True:
        time.sleep(delay)
        pw.plot(DATA, clear=True)
        pg.QtGui.QApplication.processEvents()
        print(DATA)
        
def logInMessage():
    MESSAGE = "HELLO I\'M CONNECTED"
    sock.send(MESSAGE.encode())


print("Add meg a szerver IP-jét!! (xxx.xxx.xxx.xxx formában!!)")
IP = input()
print("Add meg a portot a csatlakozáshoz!")
PORT = int(input())
BUFFER = 2048
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP,PORT))

logInMessage()

tr.start_new_thread(dataReceiving, (2, ))
tr.start_new_thread(plotDrawing, (0.2, ))


