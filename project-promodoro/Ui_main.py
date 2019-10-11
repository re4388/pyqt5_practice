# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\ben-code\python\pyqt5\project-promodoro\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menupromodoro = QtWidgets.QMenu(self.menubar)
        self.menupromodoro.setObjectName("menupromodoro")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHelo = QtWidgets.QMenu(self.menubar)
        self.menuHelo.setObjectName("menuHelo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.TryPromodoro = QtWidgets.QAction(MainWindow)
        self.TryPromodoro.setObjectName("TryPromodoro")
        self.actionHelp_Book = QtWidgets.QAction(MainWindow)
        self.actionHelp_Book.setObjectName("actionHelp_Book")
        self.actionChoose_Epub_File = QtWidgets.QAction(MainWindow)
        self.actionChoose_Epub_File.setObjectName("actionChoose_Epub_File")
        self.menupromodoro.addAction(self.TryPromodoro)
        self.menuHelp.addAction(self.actionChoose_Epub_File)
        self.menuHelo.addAction(self.actionHelp_Book)
        self.menubar.addAction(self.menupromodoro.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuHelo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menupromodoro.setTitle(_translate("MainWindow", "promodoro"))
        self.menuHelp.setTitle(_translate("MainWindow", "Epub_to_Mobi"))
        self.menuHelo.setTitle(_translate("MainWindow", "Help"))
        self.TryPromodoro.setText(_translate("MainWindow", "Try it!"))
        self.TryPromodoro.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionHelp_Book.setText(_translate("MainWindow", "Help Book"))
        self.actionHelp_Book.setShortcut(_translate("MainWindow", "F1"))
        self.actionChoose_Epub_File.setText(_translate("MainWindow", "to conver file!"))
        self.actionChoose_Epub_File.setShortcut(_translate("MainWindow", "Ctrl+E"))
