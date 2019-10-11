import sys

# from os import listdir, rename
from os.path import join
import subprocess


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox, QWidget, QLabel


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. 
    Supplied args and kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)


class dropArea(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        # setup main window size
        self.setWindowTitle('epub -> mobi')
        self.resize(500, 500)

        # set whodpw accept drop
        self.setAcceptDrops(True)

        # show notice label
        self.showDropText = QLabel(
            '<p><span style="font-size: 32px;">please drop the epub file here</span></p>', self)
        self.showDropText.move(80, 180)
        self.showDropText.setTextFormat(1)

        # setup threadpool
        self.threadpool = QThreadPool()
        print(f'We got {self.threadpool.maxThreadCount() }threads running')

        # show widow
        self.show()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def get_final_filename(self, f):
        # slit up and get the part excluding extention
        f = f.split(".")
        filename = ".".join(f[0:-1])

        # add new extension
        processed_file_name = filename+".mobi"
        return processed_file_name

    def converFile(self, original_filename):
        new_file = self.get_final_filename(original_filename)
        try:
            subprocess.call(["ebook-convert", original_filename, new_file])
        except Exception as e:
            print(e)
        finally:
            self.showDropText.setText('<p><span style="font-size: 32px;">Done, see the file in the same dir</span></p>')

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            filepath = str(urls[0].path())[1:]
            # any file type here

            if filepath[-5:].upper() == ".epub".upper():
                print(filepath)
                # create worker thread
                worker = Worker(self.converFile, filepath)
                # use threadpool to queue and exec worker
                self.threadpool.start(worker)
            else:
                dialog = QMessageBox()
                dialog.setWindowTitle("Error: Invalid File")
                dialog.setText("Only .epub files are accepted")
                dialog.setIcon(QMessageBox.Warning)
                dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = dropArea()
    win.show()
    sys.exit(app.exec_())
