import sys
from random import randrange
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Different-circles')

        self.btn = QPushButton('create', self)
        self.btn.setGeometry(350, 510, 75, 23)
        self.btn.setText('Create')
        self.btn.clicked.connect(self.pluser)
        self.indicator = 0
        self.coord = [150, 130]

    def pluser(self):
        self.indicator = 1
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.indicator == 1:
            self.draw(qp, 1)
        qp.end()

    def draw(self, qp, indicator):
        a = randrange(5, 100)
        r, g, b = randrange(0, 255), randrange(0, 255), randrange(0, 255)
        qp.setBrush(QColor(r, g, b))
        if indicator == 1:
            qp.drawEllipse(*self.coord, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
