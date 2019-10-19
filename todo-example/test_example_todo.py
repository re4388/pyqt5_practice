from exmaple_todo import MainWindow
from time import sleep


def test_myapp(qtbot):
    window = MainWindow()
    window.show()
    qtbot.addWidget(window)
    sleep(3)

    window.todoEdit.clear()
    qtbot.keyClicks(window.todoEdit, 'todo-Test')
    # qtbot.mouseClick(window.addButton, Qt.LeftButton)
    assert window.todoEdit.text() == 'todo-Test'
    # qtbot.stopForInteraction()