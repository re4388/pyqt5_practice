# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\ben-code\python\pyqt5\progressbar\demoTwoProgressBarsAsync.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 80, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 180, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.progressBarFileDownload = QtWidgets.QProgressBar(Dialog)
        self.progressBarFileDownload.setGeometry(QtCore.QRect(100, 110, 118, 23))
        self.progressBarFileDownload.setProperty("value", 24)
        self.progressBarFileDownload.setObjectName("progressBarFileDownload")
        self.progressBar_2 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_2.setGeometry(QtCore.QRect(100, 210, 118, 23))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.pushButtonStart = QtWidgets.QPushButton(Dialog)
        self.pushButtonStart.setGeometry(QtCore.QRect(140, 20, 93, 28))
        self.pushButtonStart.setObjectName("pushButtonStart")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Downloading the file"))
        self.label_2.setText(_translate("Dialog", "Scannning for the Virus"))
        self.pushButtonStart.setText(_translate("Dialog", "START"))
