import os
import sys
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QTextEdit, QCheckBox, QRadioButton, QButtonGroup, QDateTimeEdit
from PyQt6.QtGui import QIcon
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, QDateTime
#paps loader
from paps_loader import get_paps

os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-web-security --disable-site-isolation-trials"

#include paps from json
data = get_paps()
paps = data["paps"]

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("window")
        self.setGeometry(0,0,1000,1200)
        self.setWindowTitle("Train Tracker")

        layout = QVBoxLayout()
        self.view = QWebEngineView()

        #dodaj na window

        layout.addWidget(self.view)


        #url from local files so it knows what to open
        base_dir = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(base_dir, "leaf.html")
        self.setWindowIcon(QIcon(os.path.join(base_dir, "train.png")))

        self.view.setUrl(QUrl.fromLocalFile(html_path))
        self.setLayout(layout)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())