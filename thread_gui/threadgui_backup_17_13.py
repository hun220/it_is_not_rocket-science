import sys
import socket
from PyQt5 import QtCore, QtWidgets, QtGui, Qt
from PyQt5.QtCore import QThread

IP = "192.168.137.211"
PORT = 333
DATA = []

class Ui_MainWindow(object):    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.connect_button = QtWidgets.QPushButton(MainWindow)
        self.connect_button.setGeometry(QtCore.QRect(150, 10, 91, 23))
        self.connect_button.setObjectName("connect_button")
        self.IPinput = QtWidgets.QLineEdit(MainWindow)
        self.IPinput.setGeometry(QtCore.QRect(10, 10, 131, 20))
        self.IPinput.setObjectName("IPinput")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Client"))
        self.connect_button.setText(_translate("MainWindow", "Connect to host"))

        
class guiManager(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.connect_button.clicked.connect(self.backgroundWorkerManager)

    def backgroundWorkerManager(self):
        self.bgw = backgroundWorker()
        self.bgw.start()

class backgroundWorker(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((IP, PORT))
        MESSAGE = "HELLO I\'M CONNECTED"
        self.sock.send(MESSAGE.encode())
        while True:
            DATA.append(int(self.sock.recv(2048)))
            print(DATA)

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = guiManager()
    gui.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
