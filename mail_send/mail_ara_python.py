# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/jesus/OneDrive/Masaüstü/PyQt5/PROJELER/DERS PRO/DENEME/mail_ara.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mail_ara(object):
    def setupUi(self, mail_ara):
        mail_ara.setObjectName("mail_ara")
        mail_ara.resize(540, 350)
        self.pbt_ara = QtWidgets.QPushButton(mail_ara)
        self.pbt_ara.setGeometry(QtCore.QRect(70, 80, 75, 23))
        self.pbt_ara.setObjectName("pbt_ara")
        self.splitter = QtWidgets.QSplitter(mail_ara)
        self.splitter.setGeometry(QtCore.QRect(80, 10, 411, 51))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.lab_mail_ara = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_mail_ara.setFont(font)
        self.lab_mail_ara.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lab_mail_ara.setTextFormat(QtCore.Qt.PlainText)
        self.lab_mail_ara.setObjectName("lab_mail_ara")
        self.lne_ara = QtWidgets.QLineEdit(self.splitter)
        self.lne_ara.setObjectName("lne_ara")

        self.retranslateUi(mail_ara)
        QtCore.QMetaObject.connectSlotsByName(mail_ara)

    def retranslateUi(self, mail_ara):
        _translate = QtCore.QCoreApplication.translate
        mail_ara.setWindowTitle(_translate("mail_ara", "Form"))
        self.pbt_ara.setText(_translate("mail_ara", "Ara"))
        self.lab_mail_ara.setText(_translate("mail_ara", "                                    Mail Ara"))

