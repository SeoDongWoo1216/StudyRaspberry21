## QT5 베이스 프레임 소스
import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
win = QWidget()
win.show()

app.exec_()