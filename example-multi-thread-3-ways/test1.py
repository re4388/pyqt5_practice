# https://stackoverflow.com/questions/6783194/background-thread-with-qthread-in-pyqt

import sys
import time

from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                            QThreadPool, pyqtSignal)

# Order don't mean anything

# Way no.1
# Subclassing QThread
# http://qt-project.org/doc/latest/qthread.html
class AThread(QThread):

    def run(self):
        count = 0
        while count < 5:
            time.sleep(1)
            print("A Increasing")
            count += 1


# Way no.2
# Subclassing QObject and using moveToThread
# http://blog.qt.digia.com/blog/2007/07/05/qthreads-no-longer-abstract
class SomeObject(QObject):

    # define a signal first
    finished = pyqtSignal()

    def long_running(self):
        count = 0
        while count < 5:
            time.sleep(1)
            print("B Increasing")
            count += 1
        self.finished.emit()


# Way no.3
# Using a QRunnable
# http://qt-project.org/doc/latest/qthreadpool.html
# Note that a QRunnable isn't a subclass of QObject and therefore does
# not provide signals and slots.
class Runnable(QRunnable):

    def run(self):
        count = 0
        app = QCoreApplication.instance()
        while count < 5:
            print("C Increasing")
            time.sleep(1)
            count += 1
        app.quit()


def using_q_thread():
    app = QCoreApplication([])
    thread = AThread()
    thread.finished.connect(app.exit)
    thread.start()
    sys.exit(app.exec_())



def using_move_to_thread():
    app = QCoreApplication([])

    obj = SomeObject()
    objThread = QThread()
    
    obj.moveToThread(objThread)
    obj.finished.connect(objThread.quit)
    
    objThread.started.connect(obj.long_running)
    objThread.finished.connect(app.exit)

    objThread.start()
    sys.exit(app.exec_())



def using_q_runnable():
    app = QCoreApplication([])
    # create a runnable object from Runnable class, which is subclassing from QRunnable
    runnable = Runnable()

    # then use QThreadPool to mgmt runnable object
    QThreadPool.globalInstance().start(runnable)
    sys.exit(app.exec_())



if __name__ == "__main__":
    #using_q_thread()
    #using_move_to_thread()
    using_q_runnable()