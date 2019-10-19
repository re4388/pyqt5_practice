
from findfiles import Window
from PyQt5 import QtCore
from time import sleep

# qtbot as fixture
# pytest’s standard "tmpdir" that we use to create some files that will be used during our test
def test_basic_search(qtbot, tmpdir):
    '''
    test to ensure basic find files functionality is working.
    '''
    tmpdir.join('video1.avi').ensure()
    tmpdir.join('video1.srt').ensure()

    tmpdir.join('video2.avi').ensure()
    tmpdir.join('video2.srt').ensure()

    # we create the widget to test and register it
    window = Window()
    window.show()
    qtbot.addWidget(window)
    # qtbot.waitForWindowShown(window)
    # sleep(3)



    window.fileComboBox.clear()
    # use qtbot methods to simulate user interaction with the dialog
    qtbot.keyClicks(window.fileComboBox, '*.avi')

    window.directoryComboBox.clear()
    qtbot.keyClicks(window.directoryComboBox, str(tmpdir))

    qtbot.mouseClick(window.findButton, QtCore.Qt.LeftButton)

    assert window.filesTable.rowCount() == 2
    assert window.filesTable.item(0, 0).text() == 'video1.avi'
    assert window.filesTable.item(1, 0).text() == 'video2.avi'
