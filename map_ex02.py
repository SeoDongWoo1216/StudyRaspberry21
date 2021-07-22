import io 
import sys
import folium

# pip install PyQt5 || pip install PyQtWebEngine
from PyQt5 import QtWidgets, QtWebEngineWidgets # PyQtWebEngine 추가 설치 -> QtWebEngineWidgets

app = QtWidgets.QApplication(sys.argv)

m = folium.Map(location=[35.1175, 129.0903], zoom_start=12)
data = io.BytesIO()
m.save(data, close_file=False)

win = QtWebEngineWidgets.QWebEngineView()
win.setHtml(data.getvalue().decode())
win.resize(480, 320)
win.show()

sys.exit(app.exec_())