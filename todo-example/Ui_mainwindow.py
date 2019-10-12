# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\ben-code\python\pyqt5\todo-example\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 476)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 290, 181, 28))
        self.pushButton.setObjectName("pushButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(270, 290, 171, 28))
        self.deleteButton.setObjectName("deleteButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(20, 400, 431, 28))
        self.addButton.setObjectName("addButton")
        self.todoEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.todoEdit.setGeometry(QtCore.QRect(20, 340, 431, 41))
        self.todoEdit.setObjectName("todoEdit")
        self.todoView = QtWidgets.QListView(self.centralwidget)
        self.todoView.setGeometry(QtCore.QRect(10, 10, 441, 271))
        self.todoView.setObjectName("todoView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Todo"))
        self.pushButton.setText(_translate("MainWindow", "Complete"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.addButton.setText(_translate("MainWindow", "Add Todo"))
