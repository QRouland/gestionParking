__author__ = 'sidya'

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'borne.ui'
#
# Created: Tue Dec 23 18:12:55 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Borne(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 412)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 40, 211, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lcdNumber = QtGui.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 80, 351, 31))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(170, 10, 151, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 300, 272, 85))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.widget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout.addWidget(self.pushButton_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget1 = QtGui.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(70, 130, 261, 91))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.pushButton_7 = QtGui.QPushButton(self.widget1)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.verticalLayout_5.addWidget(self.pushButton_7)
        self.pushButton_10 = QtGui.QPushButton(self.widget1)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.verticalLayout_5.addWidget(self.pushButton_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.pushButton_8 = QtGui.QPushButton(self.widget1)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.verticalLayout_4.addWidget(self.pushButton_8)
        self.pushButton_9 = QtGui.QPushButton(self.widget1)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.verticalLayout_4.addWidget(self.pushButton_9)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Detection Arrivee Voiture", None))
        self.label_4.setText(_translate("Form", "NomParking", None))
        self.label.setText(_translate("Form", "Carte Membre ID ", None))
        self.pushButton_2.setText(_translate("Form", "Valider", None))
        self.label_2.setText(_translate("Form", "Non membre", None))
        self.pushButton_3.setText(_translate("Form", "Valider", None))
        self.pushButton_4.setText(_translate("Form", "PayerAvecCarte", None))
        self.pushButton_7.setText(_translate("Form", "<", None))
        self.pushButton_10.setText(_translate("Form", "Annuler", None))
        self.pushButton_8.setText(_translate("Form", ">", None))
        self.pushButton_9.setText(_translate("Form", "Valider", None))



    def delivrerTicket(self, client):
        pass

    def proposerService(self):
        pass

    def proposerAbonnement(self):
        pass

    def recupererInfosCarte(self):
        pass

    def proposerTypePaiement(self):
        pass