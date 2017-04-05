# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui3.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!
import sys
import socket
import time
from queue import Queue
from threading import Thread
from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtWidgets, QtGui, pyqtSignal

IP = "192.168.0.31"
PORT = 234

def TCPconnection(q):
    print("SOCKET THREAD RUNNING")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP, PORT))
    #MESSAGE = "HELLO I\'M CONNECTED"
    #sock.send(MESSAGE.encode())
    while True:
        dataTemp = ""
        while '\n' not in dataTemp:
            dataTemp += str(sock.recv(2048),"utf-8")
            #print(dataTemp)
        dataTemp = dataTemp.strip("\r\n").split(";")
        #print("FINAL:")
        #print(dataTemp)
        q.put(dataTemp)


class Ui_applicationGUI(QtWidgets.QWidget):
    plotsignal = pyqtSignal(list)
    def setupUi(self, applicationGUI):
        applicationGUI.setObjectName("applicationGUI")
        applicationGUI.resize(1045, 635)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        applicationGUI.setPalette(palette)
        applicationGUI.setAutoFillBackground(False)
        self.tabWidget = QtWidgets.QTabWidget(applicationGUI)
        self.tabWidget.setGeometry(QtCore.QRect(6, 60, 1031, 561))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(178, 223, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(178, 223, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(178, 223, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(178, 223, 219))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 341, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.groupBox_5.setPalette(palette)
        self.groupBox_5.setAutoFillBackground(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.IPinput = QtWidgets.QLineEdit(self.groupBox_5)
        self.IPinput.setGeometry(QtCore.QRect(10, 30, 131, 20))
        self.IPinput.setObjectName("IPinput")
        self.connectButton = QtWidgets.QPushButton(self.groupBox_5)
        self.connectButton.setGeometry(QtCore.QRect(150, 30, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.connectButton.setFont(font)
        self.connectButton.setObjectName("connectButton")
        self.disconnectButton = QtWidgets.QPushButton(self.groupBox_5)
        self.disconnectButton.setGeometry(QtCore.QRect(250, 30, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.disconnectButton.setFont(font)
        self.disconnectButton.setObjectName("disconnectButton")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(450, 40, 471, 441))
        self.label_2.setText.plotsignal.connect(self.get_plot)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 411, 311))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(26)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.plotItem = PlotWidget(self.groupBox)
        self.plotItem.setGeometry(QtCore.QRect(10, 40, 381, 261))
        self.plotItem.setObjectName("plotItem")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(760, 20, 221, 241))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(460, 20, 221, 241))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(460, 270, 221, 241))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(applicationGUI)
        self.label.setGeometry(QtCore.QRect(10, 10, 451, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(applicationGUI)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(applicationGUI)
        
        def get_plot(self):
            
            

    def retranslateUi(self, applicationGUI):
        _translate = QtCore.QCoreApplication.translate
        applicationGUI.setWindowTitle(_translate("applicationGUI", "Rakéta adatgyüjtő program"))
        self.groupBox_5.setTitle(_translate("applicationGUI", "Hálozati beállítások (IP CÍM)"))
        self.connectButton.setText(_translate("applicationGUI", "Kapcsolodás"))
        self.disconnectButton.setText(_translate("applicationGUI", "EXIT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("applicationGUI", "TCP-beállítások-datastream"))
        self.groupBox.setTitle(_translate("applicationGUI", "Z tengely Gyorsulása"))
        self.groupBox_2.setTitle(_translate("applicationGUI", "Max értékek"))
        self.groupBox_3.setTitle(_translate("applicationGUI", "Aktuális értékek"))
        self.groupBox_4.setTitle(_translate("applicationGUI", "Kalkulációk"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("applicationGUI", "Adatok - Grafikonok"))
        self.label.setText(_translate("applicationGUI", "Rakéta Adatgyüjtő Földi Állomás"))


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

    def runFunc(self, q):
        while True:
            print("RUNTHREADRUNNING")
            if q.get() != []:
                self.data.append(q.get())

                konstans = [0,1,2,3,4,5,6,7,8,9,10,11,13,60]
                self.plotsignal.emit(konstans)
               # sorszamok = []
                #for sorszam in self.data:
                 #   sorszamok.append(sorszam[0])
                #print(sorszamok)
                #self.label_2.setText('\n'.join(sorszamok))
                # self.plotItem.plot([0,1,2,3,4,5,6,7,8,9,10,11,13,60])


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
