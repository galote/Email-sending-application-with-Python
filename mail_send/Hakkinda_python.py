# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/jesus/OneDrive/Masaüstü/PyQt5/PROJELER/DERS PRO/DENEME/Hakkinda.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(416, 319)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 80, 241, 171))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HAKKINDA"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "Bu uygulana Ferhat Çelik tarafında geliştirilmiştir. \n"
"\n"
"                     \n"
"                   Tüm hakları saklıdır. \n"
""))

