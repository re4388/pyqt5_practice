#!/usr/bin/env python

# DESIGN
# ------
# TODO: Explain the logic behind pomodoro_start()


# NOTES
# -----
# https://wiki.python.org/moin/PyQt/Tutorials
# http://stackoverflow.com/questions/27212026/how-to-separate-the-ui-and-implementation-in-pyqt
# http://thecodeinn.blogspot.com/2013/07/tutorial-pyqt-digital-clock.html
# https://srinikom.github.io/pyside-docs/PySide/QtCore/QTimer.html
# http://pyqt.sourceforge.net/Docs/PyQt5/class_reference.html

import time, sys, os
from pomodoro_ui import Ui_main_window
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QSound

###############
# Global vars #
###############
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
AUDIO1 = SCRIPT_DIR + "/../media/1.wav"
AUDIO2 = SCRIPT_DIR + "/../media/2.wav"
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

#############
# Functions #
#############
# Mode 0 = We are running after the "Start" button was clicked
# Mode 1 = We are running after being called from pom.count_down()
def pomodoro_start(mode = 0):
    if (mode == 0):
        # Reset the values of the pom vars
        pom.iter_j = 0
        pom.iter_i = 0
        pom.iter_ceiling = 0
        pom.timer = None
        myapp.update_buttons(False, True, True)
        # How many loops the user wants
        pom.iter_ceiling = myapp.ui.spinBox_repetitions.value() + 1
        # First iteration should start with the work timer
        mode = 2
    elif (mode == 1):
        # Work timer is divisible by 2
        if pom.iter_j % 2 == 0:
            mode = 2
        # Break timer is not divisible by 2
        else:
            mode = 3

    ##############
    # Work timer #
    ##############
    if (mode == 2):
        pom.iter_j += 1
        hours = myapp.ui.spinBox_work_hours.value()
        minutes = myapp.ui.spinBox_work_minutes.value()
        seconds = myapp.ui.spinBox_work_seconds.value()

        # Do nothing when we don't have input
        if hours == 0 and minutes == 0 and seconds == 0:
            myapp.update_buttons(True, False, False)
        else:
            # Convert hours:minutes:seconds to seconds
            pom.convert_to_seconds(hours, minutes, seconds)
            # Start the countdown by using QTimer
            pom.count_down()
            myapp.timer(True)
    ###############
    # Break timer #
    ###############
    elif (mode == 3):
        pom.iter_j += 1
        pom.iter_i += 1
        hours = myapp.ui.spinBox_break_hours.value()
        minutes = myapp.ui.spinBox_break_minutes.value()
        seconds = myapp.ui.spinBox_break_seconds.value()

        # Do nothing when we don't have input
        if hours == 0 and minutes == 0 and seconds == 0:
            myapp.update_buttons(True, False, False)
        else:
            # Convert hours:minutes:seconds to seconds
            pom.convert_to_seconds(hours, minutes, seconds)
            # Start the countdown by using QTimer
            pom.count_down()
            myapp.timer(True)

def pomodoro_pause():
    myapp.update_buttons(False, True, True)
    # Unpause
    if pom.paused == True:
        # Start QTimer
        myapp.timer(True)
        pom.paused = False
        myapp.ui.pushButton_pause.setText("Pause")
    # Pause
    elif pom.paused == False:
        # Stop QTimer
        myapp.timer(False)
        pom.paused = True
        myapp.ui.pushButton_pause.setText("Unpause")

def pomodoro_stop():
    myapp.update_buttons(True, False, False)
    # Stop QTimer
    myapp.timer(False)
    # Remove the previous value from SECONDS
    pom.seconds = 0
    myapp.ui.label_clock.setText("00:00:00")
    # If we try to stop the timer while we are on the paused state
    # then update this state to unpaused
    if pom.paused == True:
        pom.paused = False

#################
# Pomodoro code #
#################
class Pomodoro():
    def __init__(self):
        # For keeping track of remaining seconds in our countdown
        self.seconds = 0
        # Holds the QTime timer
        self.timer = None
        # For when the user clicks on the PAUSE button
        self.paused = False
        # For performing the iterations on pomodoro_start()
        # One j = Work or break mode have been executed one time
        self.iter_j = 0
        # One i = Work mode plus break mode consitute one iter_i
        self.iter_i = 0
        # How many iterations can iter_i perform
        self.iter_ceiling = 0

    # Convert from seconds to hours:minutes:seconds
    def convert_from_seconds(self):
        # On the first divmod the quotient will be the minutes and the remainder will be the seconds
        # On the second divmod the quotient will be the hours and the remainder will be the minutes
        m, s = divmod(self.seconds, 60)
        h, m = divmod(m, 60)
        time_format = '{:02d}:{:02d}:{:02d}'.format(h, m, s)
        return time_format

    # Convert from hours:minutes:seconds to seconds
    def convert_to_seconds(self, hours, minutes, seconds):
        self.seconds = 0;
        if hours != 0:
            self.seconds += (hours * SECONDS_IN_HOUR)
        if minutes != 0:
            self.seconds += (minutes * SECONDS_IN_MINUTE)
        if seconds != 0:
            self.seconds += seconds

    # Perform the countdown
    def count_down(self):
        # Get a new format string
        string = self.convert_from_seconds()
        myapp.ui.label_clock.setText(string)
        # Update the seconds
        self.seconds = self.seconds - 1
        if self.seconds < 0:
            # Stop QTimer
            myapp.timer(False)
            # Play a notification
            myapp.play()
            # We want to call pomodoro_start() ONLY if we are NOT done
            # with the iterations provided by spinBox_repetitions
            if self.iter_i < self.iter_ceiling:
                pomodoro_start(1)
            else:
                myapp.update_buttons(True, False, False)

#############
# GUI Code  #
#############
class StartQT5(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        # Connect signals to our slots
        self.ui.pushButton_start.clicked.connect(pomodoro_start)
        self.ui.pushButton_pause.clicked.connect(pomodoro_pause)
        self.ui.pushButton_stop.clicked.connect(pomodoro_stop)
        # Create audio media 1
        self.sound1 = QSound(AUDIO1)
        # Create audio media 2
        self.sound2 = QSound(AUDIO2)

    # Button state toggle: start, pause, stop
    def update_buttons(self, start, pause, stop):
        if start:
            self.ui.pushButton_start.setEnabled(True)
        else:
            self.ui.pushButton_start.setEnabled(False)
        if pause:
            self.ui.pushButton_pause.setEnabled(True)
        else:
            self.ui.pushButton_pause.setEnabled(False)
        if stop:
            self.ui.pushButton_stop.setEnabled(True)
        else:
            self.ui.pushButton_stop.setEnabled(False)

    # QtMultimedia
    def play(self):
        # We have to subtract 1 because in pomodo_start() we increment
        # it by 1 before calling this function
        if (pom.iter_j - 1) % 2 == 0:
            self.sound1.play()
        else:
            self.sound2.play()

    # QTimer
    def timer(self, state):
        if state:
            # Create a timer
            pom.timer = QTimer()
            # Connect the timer to the appropriate slot
            pom.timer.timeout.connect(pom.count_down)
            # Wait one second between slot calls
            pom.timer.start(1000)
        if not state:
            pom.timer.stop()

########
# Main #
########
if __name__ == "__main__":
    # Create a PyQT5 application object
    app = QApplication(sys.argv)
    # Start the GUI
    myapp = StartQT5()
    # Create a Pomodoro object
    pom = Pomodoro()
    # Show the widget on the screen
    myapp.show()
    # Ensure a clean exit
    sys.exit(app.exec_())