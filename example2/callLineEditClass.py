import sys
from PyQt5.QtWidgets import QDialog, QApplication
from Ui_LineEditClass import *


# a simple biz logic here
# just a Student class and have a methos to print name
class Student:
    name = ""
    def __init__(self, name):
        self.name = name

    def printName(self):
        return self.name


class MyForm(QDialog):

    def __init__(self):
        super().__init__()

        # initiate from UI desinger and use its method to setup UI part
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # begin to setup the logic
        self.ui.ButtonClickMe.clicked.connect(self.dispmessage)
        self.show()

    def dispmessage(self):
        studentObj = Student(self.ui.lineEditName.text())
        self.ui.LabelResponse.setText("Hello" + studentObj.printName())


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())