
# import and init the app
from PyQt5.QtWidgets import *
app = QApplication([])


# create button
button = QPushButton('click')

# define func


def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked me')
    alert.exec_()


# signal and slot
button.clicked.connect(on_button_clicked)

# show the button and let the app begin
button.show()
app.exec_()
