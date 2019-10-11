from PyQt5.QtWidgets import QWidget, QMessageBox, QLineEdit, QApplication
from PyQt5.QtGui import QIcon
from Ui_conveter import Ui_Dialog

import sys
import os

class MyConverter(QWidget):
    def __init__(self):
        super().__init__()

        # call designer UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


        self.ui.lineEdit.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            filepath = str(urls[0].path())[1:]
            # any file type here
            if filepath[-4:].upper() == ".txt":
                self.setText(filepath)
            else:
                dialog = QMessageBox()
                dialog.setWindowTitle("Error: Invalid File")
                dialog.setText("Only .txt files are accepted")
                dialog.setIcon(QMessageBox.Warning)
                dialog.exec_()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyConverter()
    win.show()
    sys.exit(app.exec_())
