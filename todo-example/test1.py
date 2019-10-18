# from pytestqt.qt_compat import qWarning
# import test_example_todo

# from exmaple_todo import MainWindow

# import pytestqt.qt_compat


# def do_something():
#     qWarning("this is a WARNING message")


# def test_foo():
#     do_something()
#     assert 0


##################################### another example##########################################

from exmaple_todo import MainWindow
from time import sleep
from PyQt5.QtCore import *


def test_myapp(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    # qtbot.waitForWindowShown(window)
    sleep(1)


    window.todoEdit.clear()
    qtbot.keyClicks(window.todoEdit, 'todo1')
    # qtbot.mouseClick(window.addButton, Qt.LeftButton)
    assert window.todoEdit.text() == 'todo1'
    # qtbot.stopForInteraction()