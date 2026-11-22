import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QBrush, QColor, QPainter, QPen
from ui import Ui


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.ui = Ui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.a)

    def a(self):
        radius = random.randint(1, 100)
        x = random.randint(0, self.width())
        y = random.randint(0, self.height())
        center = QPointF(x, y)
        color = QColor(random.randint(0, 255),
                       random.randint(0, 255),
                       random.randint(0, 255))
        self.circles.append((center, radius, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        for i, j, color in self.circles:
            pen = QPen(color, 3)
            painter.setPen(pen)
            painter.setBrush(QBrush(color))
            painter.drawEllipse(i, j, j)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())