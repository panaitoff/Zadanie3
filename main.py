from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import random
from UI import Ui_MainWindow
import sys


class Widget(QMainWindow, Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.kn = 1
        self.pushButton.clicked.connect(self.func)

    def paintEvent(self, event):
        if self.kn == 0:
            x, y = self.point
            # Рисовать будем на самом себе
            painter = QPainter(self)
            s = random.randint(10, 100)
            # Для рисования точки хватит setPen, но для других фигур (типо rect) понадобится setBrush
            painter.setPen(QPen(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), s))
            # Рисование точки
            painter.drawPoint(x, y)

        elif self.kn == 1:
            painter = QPainter(self)
            s = random.randint(10, 100)
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            painter.setPen(QPen(color, 8, Qt.SolidLine))
            painter.setBrush(QBrush(color, Qt.SolidPattern))

            painter.drawEllipse(100, 100, s, s)

        elif self.kn == 2:
            self.drawing.begin(self)
            s = random.randint(10, 150)
            r = a = s
            x, y = self.point
            self.drawing.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            coordss = [(x, y + r), (x + a, y - r), (x - a, y - r)]
            path = QPainterPath()
            path.moveTo(*coordss[0])
            path.lineTo(*coordss[1])
            path.lineTo(*coordss[2])
            self.drawing.drawPath(path)
            self.drawing.end()

    def func(self):
        self.update()

if __name__ == '__main__':
    app = QApplication([])

    w = Widget()
    w.show()

    app.exec()
    sys.exit(app.exec())
