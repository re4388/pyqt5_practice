# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\ben-code\python\pyqt5\LineEditClass.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 318)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 101, 16))
        self.label.setObjectName("label")

        self.LabelResponse = QtWidgets.QLabel(Dialog)
        self.LabelResponse.setGeometry(QtCore.QRect(50, 120, 58, 15))
        self.LabelResponse.setObjectName("LabelResponse")

        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(140, 40, 113, 22))
        self.lineEditName.setObjectName("lineEditName")

        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(270, 40, 93, 28))
        self.ButtonClickMe.setObjectName("ButtonClickMe")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter your name"))
        self.LabelResponse.setText(_translate("Dialog", "TextLabel"))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))
