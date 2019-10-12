# import python BIF
import sys

# import QT
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# from PyQt5.QtWidgets import QMainWindow, QApplication
# from PyQt5 import QtCore

# import UI
from Ui_main import Ui_MainWindow

# import other app
import Promodoro
import DragDrop



class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.TryPromodoro.triggered.connect(self.call_Promodoro)
        self.ui.actionChoose_Epub_File.triggered.connect(self.call_epub_converter)
        self.ui.actionChoose_Epub_File.triggered.connect(self.call_epub_converter)
        self.ui.actionHelp_Book.triggered.connect(self.call_qtAbout)


    def call_Promodoro(self):
        self.promo = Promodoro.MyTimer()


    def call_epub_converter(self):
        self.converter = DragDrop.dropArea()

    def call_qtAbout(self):
        print('about QT')
        app.aboutQt()



if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    app.setStyle("Fusion")
    # palette = QPalette()
    # palette.setColor(QPalette.Window, QColor(53, 53, 53))
    # palette.setColor(QPalette.WindowText, Qt.white)
    # app.setPalette(palette)

    w = AppWindow()
    w.show()
    sys.exit(app.exec_())