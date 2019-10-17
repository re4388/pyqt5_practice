

# from os import listdir, rename
from os.path import join
import subprocess, traceback, sys, re, os


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox, QWidget, QLabel


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        `tuple` (exctype, value, traceback.format_exc() )

    result
        `object` data returned from processing, anything

    progress
        `int` indicating % progress 

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(str)


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
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            # Return the result of the processing
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()  # Done


class dropArea(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        # setup main window size
        self.setWindowTitle('epub -> mobi')
        self.resize(500, 500)

        # set whodpw accept drop
        self.setAcceptDrops(True)

        # show notice label
        self.showDropTextTitle = QLabel(
            '<p><span style="font-size: 20px;">please drop the epub file here</span></p>', self)
        self.showDropTextTitle.move(150, 10)
        self.showDropTextTitle.resize(250, 30)
        self.showDropTextTitle.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.showDropTextTitle.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.showDropTextTitle.setTextFormat(1)

        # show log label
        self.showDropText = QLabel('wait to process', self)
        self.showDropText.move(50, 40)
        self.showDropText.resize(400, 400)
        self.showDropText.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.showDropText.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.showDropText.setWordWrap(True)

        # setup threadpool
        self.threadpool = QThreadPool()
        print(f'We got {self.threadpool.maxThreadCount() } threads running')

        # show widow
        self.show()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()


    def get_final_path(self,filePath):
        file_name_pattern = re.compile(r'([^\/]+)(.epub)$')
        pattern_list = file_name_pattern.findall(filePath)
        source_file_name = pattern_list[0][0]
        dest_file_name = source_file_name + '.mobi'
        # new_path = "C:\\Users\\muen_infs\\Desktop\\" + dest_file_name
        new_path = os.getenv("HOME") + "\\" + dest_file_name
        print(new_path)
        return new_path

    def converFile(self, filepath, progress_callback):
        new_file = self.get_final_path(filepath)
        try:
            proc = subprocess.Popen(
                ['ebook-convert', filepath, new_file], stdout=subprocess.PIPE, shell=True)
            while True:
                line = proc.stdout.readline()
                if not line:
                    break
                # the real code does filtering here
                print(bytes.decode(line, "cp950", "ignore"))
                line_decode = bytes.decode(line, "cp950", "ignore")

                # emit signal to callback to show log in progress
                progress_callback.emit(line_decode)

        except Exception as e:
            print(e)
        # finally:
        #     self.showDropText.setText('<p><span style="font-size: 24px;">Done, see the file in the same dir</span></p>')

    def print_output(self, s):
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE!")

    # log out the stdout
    all_line = ""

    def progress_fn(self, line_decode):
        self.all_line += "\n" + line_decode
        if len(self.all_line) > 400:
            self.all_line = ""
            self.showDropText.setText(self.all_line)
        else:
            self.showDropText.setText(self.all_line)

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
                worker.signals.progress.connect(self.progress_fn)
                worker.signals.result.connect(self.print_output)
                worker.signals.finished.connect(self.thread_complete)

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
