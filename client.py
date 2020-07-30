from PyQt5 import QtCore, QtGui, QtWidgets
import socket, threading

HEADER = 16
PORT = 8000
FORMAT = 'utf-8'
DISCONNECT = '$!#^'
SERVER = '192.168.100.58'
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

username = input("Username: ").strip() + ' >> '


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 450)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chat = QtWidgets.QListWidget(self.centralwidget)
        self.chat.setGeometry(QtCore.QRect(10, 10, 620, 380))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(12)
        self.chat.setFont(font)
        self.chat.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chat.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.chat.setObjectName("chat")
        self.type = QtWidgets.QLineEdit(self.centralwidget)
        self.type.setGeometry(QtCore.QRect(10, 400, 560, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.type.setFont(font)
        self.type.setFrame(True)
        self.type.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.type.setClearButtonEnabled(True)
        self.type.setObjectName("type")
        self.send = QtWidgets.QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(570, 399, 60, 27))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.send.setFont(font)
        self.send.setObjectName("send")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.type.returnPressed.connect(self.onSend)
        self.send.clicked.connect(self.onSend)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat Room by Faizan"))
        self.type.setPlaceholderText(_translate("MainWindow", "Type here"))
        self.send.setText(_translate("MainWindow", "SEND"))

    def onSend(self):
        msg = (username + self.type.text()).encode(FORMAT)
        self.type.clear()
        client.send(msg)

def check():
    while True:
        data = client.recv(1024).decode(FORMAT)
        data = data.replace(':)', '\U0001F600')
        data = data.replace(':(', '\U0001F62C')
        data = data.replace(';)', '\U0001F609')
        data = data.replace(':|', '\U0001F612')
        data = data.replace(':p', '\U0001F61C')
        ui.chat.addItem(data)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    thread = threading.Thread(target=check)
    thread.start()
    sys.exit(app.exec_())
