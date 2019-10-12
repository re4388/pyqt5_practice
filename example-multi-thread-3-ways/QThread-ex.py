"""

https://tnlin.wordpress.com/2017/03/05/%E7%AC%AC%E4%B8%80%E6%AC%A1%E5%AF%ABpyqt5%E5%B0%B1%E4%B8%8A%E6%89%8B/

主要做了幾件事情，分別如下

繼承 QThread 並且創建一個 Worker
在 GUI Thread 呼叫此 Worker，讓他來管理 ThreadPoolExecutor
在 GUI Thread 內用pyqtSlot 來註冊進度條更新的 event
在 Worker 透過 pyqtSignal 來與 GUI Thread 溝通，更新進度條

"""
import sys
from pyqtwindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.submit)

    def submit(self):
        self.work = WorkerThread(self.var)
        self.work.progressUpdated.connect(self.progressbar_change)
        self.work.start()
    
    @pyqtSlot(int)
    def progressbar_change(self, val):
        self.progressBar.setValue(val)

class WorkerThread(QThread):
    progressUpdated = pyqtSignal(int)

    def __init__(self, var):
        QThread.__init__(self)
        self.moveToThread(self)
        self.value = 0
        self.var = var

    def run(self):
        start_time = time.time()
        n_workers = (os.cpu_count() or 1) * 10
        n_data = 65535
        with concurrent.futures.ThreadPoolExecutor(max_workers=n_workers) as executor:
            future_row = {executor.submit(self.myjob, v): v for i in range(n_data)}
            for future in concurrent.futures.as_completed(future_row):
                try:
                    data = future.result()
                except Exception as exc:
                    print('Generated an exception: %s' % exc)
                else:
                    if data:
                        self.value += 1
                        # 不要讓畫面更新太頻繁，將進度條mapping成 0 ~ 100
                        if int(self.value / n_data * 100) % 2 == 0:
                            self.progressUpdated.emit(self.value)
        self.progressUpdated.emit(self.value)
        print("Total Time: " + str(int(time.time() - start_time)) + " seconds")

    def myjob(self, v):
        # I/O Jobs here
        return True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())