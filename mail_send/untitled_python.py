# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/jesus/OneDrive/Masaüstü/PyQt5/PROJELER/DERS PRO/DENEME/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600,400 )
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/tolbar_icos/email.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#MainWindow{\n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"#toolBar{\n"
"    background-color: rgb(85, 170, 127);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 38, 258, 220))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/tolbar_icos/draft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(120, 61))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/tolbar_icos/send-mail.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(120, 10, 251, 19))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit.setObjectName("lineEdit")
        self.pbt_ara = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_ara.setGeometry(QtCore.QRect(400, 230, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbt_ara.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/tolbar_icos/Mail-search-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbt_ara.setIcon(icon3)
        self.pbt_ara.setIconSize(QtCore.QSize(20, 24))
        self.pbt_ara.setObjectName("pbt_ara")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 22))
        self.menubar.setObjectName("menubar")
        self.menuYard_m = QtWidgets.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionHakkinda = QtWidgets.QAction(MainWindow)
        self.actionHakkinda.setObjectName("actionHakkinda")
        self.action_Kaydet = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/tolbar_icos/save-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Kaydet.setIcon(icon4)
        self.action_Kaydet.setObjectName("action_Kaydet")
        self.action_Ac = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/tolbar_icos/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Ac.setIcon(icon5)
        self.action_Ac.setObjectName("action_Ac")
        self.menuYard_m.addAction(self.actionHakkinda)
        self.menubar.addAction(self.menuYard_m.menuAction())
        self.toolBar.addAction(self.action_Kaydet)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Ac)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "F - MAİL"))
        self.pushButton.setText(_translate("MainWindow", "Taslak Olarak Kaydet"))
        self.pushButton_2.setText(_translate("MainWindow", "Gönder"))
        self.label.setText(_translate("MainWindow", "Alıcı"))
        self.pbt_ara.setText(_translate("MainWindow", "Mail Ara"))
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionHakkinda.setText(_translate("MainWindow", "Hakkinda"))
        self.action_Kaydet.setText(_translate("MainWindow", "Kaydet"))
        self.action_Kaydet.setToolTip(_translate("MainWindow", "Kaydet"))
        self.action_Ac.setText(_translate("MainWindow", "Aç"))
        self.action_Ac.setToolTip(_translate("MainWindow", "Aç"))

import tolBar_rc
