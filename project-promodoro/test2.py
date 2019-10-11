import sys

# decorator need to have this import
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import QApplication, QWidget

from Ui_test2 import Ui_Dialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    # no need to use connect
    # just directly define the function with decorator
    # decorator need to have correct type

    # function need to follow the specific format
    # on_sender_signalName
    
    @pyqtSlot(int)
    def on_spinBox_valueChanged(self):
        self.ui.label_4.setText(str(self.ui.spinBox.value()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec_())



# import sys
# from PyQt5.QtCore import pyqtSlot
# from PyQt5.QtWidgets import QApplication, QWidget

# from Ui_test2 import Ui_Dialog



# # use connect  
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_Dialog()
#         self.ui.setupUi(self)

#         self.ui.spinBox.valueChanged.connect(self.show_text)

#     def show_text(self):
#         self.ui.label_4.setText(str(self.ui.spinBox.value()))


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     win = Example()
#     win.show()
#     sys.exit(app.exec_())
