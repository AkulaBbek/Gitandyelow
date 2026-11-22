import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QBrush, QColor, QPainter, QPen


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.a)

    def a(self):
        radius = random.randint(1, 100)
        x = random.randint(0, self.width())
        y = random.randint(0, self.height())
        center = QPointF(x, y)
        self.circles.append((center, radius))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor("yellow"), 3)
        painter.setPen(pen)
        painter.setBrush(QBrush(QColor("yellow")))

        for center, radius in self.circles:
            painter.drawEllipse(center, radius, radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())