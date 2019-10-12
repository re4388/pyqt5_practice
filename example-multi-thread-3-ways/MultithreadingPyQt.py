# https://www.learnpyqt.com/courses/concurrent-execution/multithreading-pyqt-applications-qthreadpool/


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import time


class Worker(QRunnable):
    """ Worker Thread Class"""

    @pyqtSlot()
    def run(self):
        """ new thread setup in this func """
        print('thread start')
        time.sleep(5)
        print('thread complete')


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.counter = 0

        layout = QVBoxLayout()

        # setup label and button
        self.l = QLabel("Start")
        b = QPushButton("DANGER!")

        # connect to function
        b.pressed.connect(self.oh_no)

        # build up layout and widget
        layout.addWidget(self.l)
        layout.addWidget(b)
        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
        self.show()

        # setup timer to countdown
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

        # setup threadpool
        self.threadpool = QThreadPool()
        print(f'We got {self.threadpool.maxThreadCount() }threads running')


    def oh_no(self):
        # create a worker runnable and use threadpool to quene and exec
        worker = Worker()
        self.threadpool.start(worker)
        

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)


app = QApplication([])
window = MainWindow()
app.exec_()
