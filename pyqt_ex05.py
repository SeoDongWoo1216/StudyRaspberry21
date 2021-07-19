# QT Designer 연동 소스
# 네이버 검색 API 활용
from PyQt5 import QtGui,QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from naverSearch import *  # 네이버에 있는 것을 가져오겠다는 뜻
import webbrowser

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui/naverSearch.ui',self)

        #ui에 있는 위젯하고 연결하는 시그널 처리(컨트롤 이벤트처리)
        self.btnSearch.clicked.connect(self.btnSearch_Clicked)
        self.tblResult.itemSelectionChanged.connect(self.tblResult_Selected)
        self.txtSearchWord.returnPressed.connect(self.btnSearch_Clicked)  # 엔터 눌렀을때 검색 이벤트 발생

    def tblResult_Selected(self):
        selected = self.tblResult.currentRow()  # 현재 선택된 열의 인덱스
        url = self.tblResult.item(selected, 1).text()  # Url 불러오기
        #QMessageBox.about(self, 'URL', url)
        webbrowser.open(url)

    def makeTable(self, result):
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)  # 한줄만 선택하겠다는 코드
        self.tblResult.setColumnCount(2)
        self.tblResult.setRowCount(len(result))

        self.tblResult.setHorizontalHeaderLabels(['기사제목', '뉴스링크'])

        n = 0
        for post in result:
            # 기사제목의 html들을 전부 걸러주기(<br>, &quot 등을 파싱해주기)
            title = post['title'].replace('&lt;', '<').replace('&gt;', '>').replace('<b>', '').replace('</b>', '').replace('&quot;',"'")

            self.tblResult.setItem(n, 0, QTableWidgetItem(title))
            self.tblResult.setItem(n, 1, QTableWidgetItem(post['originallink']))
            n += 1

        self.tblResult.setColumnWidth(0, 300)  # 0번째 컬럼 사이즈
        self.tblResult.setColumnWidth(1, 200)  # 1번째 컬럼 사이즈
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers) # 컬럼 데이터 수정 못하게 막아줌(Readonly 처리)

    def btnSearch_Clicked(self): # 
        api = naverSearch()
        jsonResult = []
        sNode = 'news'
        search_word = self.txtSearchWord.text()  # 텍스트 박스에있는 데이터를 변수에 저장
        display = 100

        if len(search_word) == 0: # 검색어 입력안했을때 오류 처리
            QMessageBox.about(self, 'popup', '검색어를 입력하세요') 
            return

        # naver api search
        jsonSearch = api.getNaverSearchResult(sNode, search_word, 1, display)
        jsonResult = jsonSearch['items']  # items 리스트 분리
        print(len(jsonResult))
        self.stsResult.showMessage('검색결과 : {0}개'.format(len(jsonResult)))
        #print(jsonSearch)

        # model = QtGui.QStandardItemModel()
        # self.lsvResult.setModel(model)
        
        # for post in jsonResult:
        #     item = QtGui.QStandardItem(post['title'])
        #     model.appendRow(item)
        self.makeTable(jsonResult)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())