import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QLCDNumber
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, QTimer, QDateTime, QDate, QTime



class Example(QWidget):

    def initUI(self):
        self.resize(370,190)
        self.setWindowTitle('this is title')

        self.lcd = QLCDNumber(self)
        lb = QLabel("until to 2022 Olymbic winter",self)

        self.lcd.setDigitCount(12)
        self.lcd.setMode(QLCDNumber.Dec)
        # self.lcd.setSegmentStyle(QLCDNumber.Flat)#Mac系统需要加上，否则下面的color不生效。
        # self.lcd.setStyleSheet("border: 2px solid black; color: red; background: silver;")
        
        # setup  timer and set interval

        time = QTimer(self)
        time.setInterval(1000)
        # timeout is a signal and trigger a function to update the LCD number
        time.timeout.connect(self.refresh)

        # start the timer
        time.start()

    def refresh(self):
        # get the current sec sine epoch
        startDate = QDateTime.currentMSecsSinceEpoch()

        # set Date
        endDate = QDateTime(QDate(2020, 2, 4), QTime(0, 0, 0)).toMSecsSinceEpoch()
        interval = endDate - startDate
        if interval > 0:
            days = interval // (24 * 60 * 60 * 1000)
            hour = (interval - days * 24 * 60 * 60 * 1000) // (60 * 60 * 1000)
            min = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000) // (60 * 1000)
            sec = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000 - min * 60 * 1000) // 1000
            intervals = str(days) + ':' + str(hour) + ':' + str(min) + ':' + str(sec)
            self.lcd.display(intervals)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec_())
