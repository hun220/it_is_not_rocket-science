import sys
import socket
from queue import Queue
from threading import Thread
from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtWidgets, QtGui

IP = ""
PORT = 333

def TCPconnection(q):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP, PORT))
    MESSAGE = "HELLO I\'M CONNECTED"
    sock.send(MESSAGE.encode())
    while True:
        dataTemp = 0
        dataTemp = int(sock.recv(2048))
        if dataTemp != 0:
            q.put(dataTemp)

class Ui_applicationGUI(QtWidgets.QWidget):        
    def setupUi(self, applicationGUI):
        applicationGUI.setObjectName("applicationGUI")
        applicationGUI.resize(349, 295)
        self.IPinput = QtWidgets.QLineEdit(applicationGUI)
        self.IPinput.setGeometry(QtCore.QRect(12, 10, 131, 20))
        self.IPinput.setObjectName("IPinput")
        self.connectButton = QtWidgets.QPushButton(applicationGUI)
        self.connectButton.setGeometry(QtCore.QRect(150, 10, 100, 23))
        self.connectButton.setObjectName("connectButton")
        self.disconnectButton = QtWidgets.QPushButton(applicationGUI)
        self.disconnectButton.setGeometry(QtCore.QRect(260, 10, 81, 23))
        self.disconnectButton.setObjectName("disconnectButton")
        self.plotItem = PlotWidget(applicationGUI)
        self.plotItem.setGeometry(QtCore.QRect(10, 40, 331, 251))
        self.plotItem.setObjectName("plotItem")
        self.connectButton.setEnabled(False)
        self.disconnectButton.setEnabled(False)

        self.retranslateUi(applicationGUI)
        QtCore.QMetaObject.connectSlotsByName(applicationGUI)

    def retranslateUi(self, applicationGUI):
        _translate = QtCore.QCoreApplication.translate
        applicationGUI.setWindowTitle(_translate("applicationGUI", "Client"))
        self.connectButton.setText(_translate("applicationGUI", "Connect to host"))
        self.disconnectButton.setText(_translate("applicationGUI", "Disconnect"))

class guiManager(Ui_applicationGUI):
    def __init__(self):
        self.data = []
        Ui_applicationGUI.__init__(self)
        self.setupUi(self)
        self.IPinput.textChanged[str].connect(self.onChangedIP)
        self.connectButton.clicked.connect(self.startBWM)

    def onChangedIP(self, text):
        global IP
        IP = text
        if IP != "":
            self.connectButton.setEnabled(True)
        else:
            self.connectButton.setEnabled(False)

    def runFunc(self, q):
        while True:
            if q != 0:
                self.data.append(q.get())
                self.plotItem.plot(self.data)
                print(self.data)

    def startBWM(self):
        TCPthread = Thread(target=TCPconnection, args=(q,))
        TCPthread.start()
                

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    q = Queue(maxsize=0)

    gui = guiManager()

    GUIthread = Thread(target=gui.runFunc, args=(q, ))
    GUIthread.start()
    
    gui.show()

    sys.exit(app.exec())
