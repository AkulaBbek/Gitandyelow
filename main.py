import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QBrush, QColor, QPainter, QPen


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tf = False
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.a)

    def a(self):
        self.tf = True
        self.update()

    def paintEvent(self, event):
        if self.tf == True:
            painter = QPainter(self)
            pen = QPen(QColor("yellow"), 3)
            painter.setPen(pen)
            painter.setBrush(QBrush(QColor("yellow")))
            center = QPointF(200, 200)
            radius = random.randint(10, 100)
            painter.drawEllipse(center, radius, radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())