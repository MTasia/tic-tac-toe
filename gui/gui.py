from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

N = 3
O = 'O'
X = 'X'
NON = '-'


class PlayWindow(QMainWindow):
    def __init__(self, field):
        super(PlayWindow, self).__init__()

        self.setGeometry(100, 100, 450, 550)
        self.setWindowTitle('tic-toc-tae')

        self.init_UI()
        self.reset_UI(field)

    def init_UI(self):
        self.info_label = QLabel(self)
        self.info_label.setGeometry(200, 440, 100, 50)
        self.info_label.setText("text label")

        self.cell_11 = QLabel(self)
        self.cell_11.setGeometry(QtCore.QRect(10, 10, 141, 141))
        self.cell_12 = QLabel(self)
        self.cell_12.setGeometry(QtCore.QRect(151, 10, 141, 141))
        self.cell_13 = QLabel(self)
        self.cell_13.setGeometry(QtCore.QRect(292, 10, 141, 141))

        self.cell_21 = QLabel(self)
        self.cell_21.setGeometry(QtCore.QRect(10, 151, 141, 141))
        self.cell_22 = QLabel(self)
        self.cell_22.setGeometry(QtCore.QRect(151, 151, 141, 141))
        self.cell_23 = QLabel(self)
        self.cell_23.setGeometry(QtCore.QRect(292, 151, 141, 141))

        self.cell_31 = QLabel(self)
        self.cell_31.setGeometry(QtCore.QRect(10, 292, 141, 141))
        self.cell_32 = QLabel(self)
        self.cell_32.setGeometry(QtCore.QRect(151, 292, 141, 141))
        self.cell_33 = QLabel(self)
        self.cell_33.setGeometry(QtCore.QRect(292, 292, 141, 141))


    def reset_UI(self, field):
        img_in_filed = [["" for i in range(N)] for j in range(N)]
        for i in range(N):
            for j in range(N):
                if field[i][j] == X:
                    img_in_filed[i][j] = "crossTemp.png"
                elif field[i][j] == O:
                    img_in_filed[i][j] = "circlePlay.png"
                else:
                    img_in_filed[i][j] = "emptyPlay.png"

        # 11
        self.cell_11.setText("")
        self.cell_11.setPixmap(QtGui.QPixmap(img_in_filed[0][0]))

        # 12
        self.cell_12.setText("")
        self.cell_12.setPixmap(QtGui.QPixmap(img_in_filed[0][1]))


        # 13
        self.cell_13.setText("")
        self.cell_13.setPixmap(QtGui.QPixmap(img_in_filed[0][2]))

        # 21
        self.cell_21.setText("")
        self.cell_21.setPixmap(QtGui.QPixmap(img_in_filed[1][0]))

        # 22
        self.cell_22.setText("")
        self.cell_22.setPixmap(QtGui.QPixmap(img_in_filed[1][1]))

        # 23
        self.cell_23.setText("")
        self.cell_23.setPixmap(QtGui.QPixmap(img_in_filed[1][2]))

        self.cell_31.setText("")
        self.cell_31.setPixmap(QtGui.QPixmap(img_in_filed[2][0]))

        self.cell_32.setText("")
        self.cell_32.setPixmap(QtGui.QPixmap(img_in_filed[2][1]))

        self.cell_33.setText("")
        self.cell_33.setPixmap(QtGui.QPixmap(img_in_filed[2][2]))

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('start play')
        self.b1.setGeometry(10, 440, 100, 50)
        self.b1.clicked.connect(self.click_start_play)

    def click_start_play(self):
        self.info_label.setText('play starting ...')


def window(filed):
    app = QApplication(sys.argv)
    win = PlayWindow(filed)

    win.show()
    sys.exit(app.exec_())


field = [[X, NON, X], [O, NON, NON], [O, O, X]]
window(field)
