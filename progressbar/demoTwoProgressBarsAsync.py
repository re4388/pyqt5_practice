import sys, time
import asyncio
from PyQt5.QtWidgets import QDialog, QApplication
from quamash import QEventLoop
from Ui_demoTwoProgressBarsAsync import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # click button to invoke aysnc func
        self.ui.pushButtonStart.clicked.connect(self.invokeAsync)
        self.show()

    # 2 asy proces here
    def invokeAsync(self):
        asyncio.ensure_future(self.updt(0.05, self.ui.progressBarFileDownload),loop=loop)
        asyncio.ensure_future(self.updt(0.025, self.ui.progressBar_2),loop=loop)
        
    # the implemenetation fo the async func
    # set progress bar value from 0 to 100
    # process1 delay 0.05 sec, p2 delay 0.025 sec 
    @staticmethod
    async def updt(delay, ProgressBar):
        for i in range(101):
            await asyncio.sleep(delay)
            ProgressBar.setValue(i)

        # def stopper(loop):
        #     loop.stop()


if __name__=="__main__":
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    w = MyForm()
    w.exec()

    with loop:
        loop.run_forever()
        # loop.close()
    
    sys.exit(app.exec_())