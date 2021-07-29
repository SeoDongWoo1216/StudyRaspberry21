## pyQt 디자이너 설치
```Pyhton
sudo apt-get install python3-pyqt5
```

```Pyhton
sudo apt-get install qttools5-dev-tools
```

<p align = "center">
<img src = "https://github.com/SeoDongWoo1216/StudyRaspberry21/blob/main/pyqt_ex/QT5%EC%84%A4%EC%B9%98.PNG">
</p>

<p align = "center">
설치가 완료됐다면 메뉴바의 Programming 안에 Qt Designer가 설치된 것을 확인할 수 있다.
</p>

<br><br>

## Naver API 검색 프로그램(with QT)

```python
# naverSearch.py

import urllib.request as urq
import urllib.parse as uparse
import datetime
import json

class naverSearch(object):

    # 생성자
    def __init__(self):
        print('Naver Search API 생성')

    # 네이버 API 요청함수
    def getRequestUrl(self, url):
        req = urq.Request(url)

        # 네이버 open API 요청하기위해 반드시 필요한 헤더 작성
        req.add_header('X-Naver-Client-Id', 'API ID')
        req.add_header('X-Naver-Client-Secret', 'API Password')

        try:
            res = urq.urlopen(req)
            if res.getcode() == 200:  # ok
                print('[{0}] URL Request succeed'.format(datetime.datetime.now()))
                return res.read().decode('utf-8')

        except Exception as e:
            print(e)
            return None

    # 네이버 검색 API 사용함수
    def getNaverSearchResult(self, sNode, search_word, page_start, display):
        base = 'https://openapi.naver.com/v1/search/'
        node = '{0}.json'.format(sNode)
        param = '?start={0}&display={1}&query={2}'.format(
            page_start, display, uparse.quote(search_word))
        url = base + node + param 
        # https://openapi.naver.com...nodeval.json?start=1&display=10&query=코로나   # 검색어

        retData = self.getRequestUrl(url)
        if retData == None:
            return None
        else:
            return json.loads(retData)


    # 데이터 처리
    def getPostData(self, post, jsonResult):
        title = post['title']
        desc = post['description']
        org_link = post['originallink']
        link = post['link']
        pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
        p_date = pDate.strftime('%Y-%m-%d %H:%M:%S')

        #jsonResult.append({})
```

```python
# QT Designer 연동 소스
# 네이버 검색 API 활용
# pyqt_ex05.py 소스파일

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
```



<p align = "center">
    <img src="https://github.com/SeoDongWoo1216/StudyRaspberry21/blob/main/result_image/%EB%84%A4%EC%9D%B4%EB%B2%84%EA%B2%80%EC%83%89API/Qt%ED%99%94%EB%A9%B4.PNG" width="50%" height="50%">
 </p>
 
<p align = "center">
네이버 서치 QT 디자인    
</p>

  <br><br>
  
<p align = "center">  
<img src="https://github.com/SeoDongWoo1216/StudyRaspberry21/blob/main/result_image/%EB%84%A4%EC%9D%B4%EB%B2%84%EA%B2%80%EC%83%89API/%EA%B2%80%EC%83%89%EA%B2%B0%EA%B3%BC.PNG" width="50%" height="50%">
</p>
  
<p align = "center">  
검색화면    
</p>
    
<br><br>
      
<p align = "center"> 
    <img src="https://github.com/SeoDongWoo1216/StudyRaspberry21/blob/main/result_image/%EB%84%A4%EC%9D%B4%EB%B2%84%EA%B2%80%EC%83%89API/url%EC%97%B0%EA%B2%B0.PNG" width="50%" height="50%">
    </p>
    
<p align = "center"> 
검색화면에서 그리드를 더블 클릭했을때 웹 화면
</p>
      
<br><br>
      
<p align = "center"> 
    <img src = "https://github.com/SeoDongWoo1216/StudyRaspberry21/blob/main/result_image/%EB%84%A4%EC%9D%B4%EB%B2%84%EA%B2%80%EC%83%89API/NaverSearchAPI%20%EC%8B%A4%ED%96%89%ED%99%94%EB%A9%B4.gif" >  
   </p>

<p align = "center">
    실행 영상
 </p>
