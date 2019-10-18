from PyQt5 import QtCore
from exmaple_todo import MainWindow


def test_hello(qtbot):
    window = MainWindow()
    window.show()
    qtbot.addWidget(window)

    # click in the Greet button and make sure it updates the appropriate label
    qtbot.mouseClick(window.addButton, QtCore.Qt.LeftButton)

    assert window.greet_label.text() == 'Hello!'