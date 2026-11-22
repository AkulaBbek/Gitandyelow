from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton


class Ui:
    def setupUi(self, MainWindow):
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("MainWindow")
        self.centralwidget = QWidget()
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton = QPushButton("push", self.centralwidget)
        self.pushButton.setGeometry(250, 60, 250, 125)