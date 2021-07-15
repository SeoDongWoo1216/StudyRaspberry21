# QT Designer 연동 소스
# 네이버 검색 API 활용
from PyQt5 import QtGui,QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from naverSearch import *  # 네이버에 있는 것을 가져오겠다는 뜻

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui/naverSearch.ui',self)

        #ui에 있는 위젯하고 연결하는 시그널 처리(컨트롤 이벤트처리)
        self.btnSearch.clicked.connect(self.btnSearch_Clicked)

    def btnSearch_Clicked(self):
        api = naverSearch()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())