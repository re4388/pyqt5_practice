# http://enki-editor.org/2014/08/23/Pyqt_mem_mgmt.html

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



# class MyObject(QObject):
#     def __init__(self):
#         super().__init__()
#         self.field = 7

# obj = MyObject()
# print(obj.field)
# obj.setObjectName("New object")


###################


# def createLabel():
#     label = QLabel("Hello, world!")
#     label.show()
#     return label


# app = QApplication([])
# createLabel()

# app.exec_()



######################

app = QApplication([])

widget = QWidget()
widget.setWindowTitle("Dead widget")
widget.deleteLater()

# Make the application quit just after start
QTimer.singleShot(0, app.quit) 

# Execute the application to call deleteLater()
app.exec_() 
