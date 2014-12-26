# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'borne.ui'
#
# Created: Fri Dec 26 17:32:17 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 412)
        self.btn_Voiture = QtGui.QPushButton(Form)
        self.btn_Voiture.setGeometry(QtCore.QRect(90, 40, 211, 27))
        self.btn_Voiture.setObjectName(_fromUtf8("btn_Voiture"))
        self.lcdNumber = QtGui.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 80, 351, 31))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(170, 10, 151, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 300, 272, 85))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit_id = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_id.setObjectName(_fromUtf8("lineEdit_id"))
        self.verticalLayout_2.addWidget(self.lineEdit_id)
        self.btn_validerID = QtGui.QPushButton(self.layoutWidget)
        self.btn_validerID.setObjectName(_fromUtf8("btn_validerID"))
        self.verticalLayout_2.addWidget(self.btn_validerID)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.btn_validerNonMembre = QtGui.QPushButton(self.layoutWidget)
        self.btn_validerNonMembre.setObjectName(_fromUtf8("btn_validerNonMembre"))
        self.verticalLayout.addWidget(self.btn_validerNonMembre)
        self.btn_cb = QtGui.QPushButton(self.layoutWidget)
        self.btn_cb.setObjectName(_fromUtf8("btn_cb"))
        self.verticalLayout.addWidget(self.btn_cb)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 130, 261, 91))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.btn_precedent = QtGui.QPushButton(self.layoutWidget1)
        self.btn_precedent.setObjectName(_fromUtf8("btn_precedent"))
        self.verticalLayout_5.addWidget(self.btn_precedent)
        self.btn_annuler = QtGui.QPushButton(self.layoutWidget1)
        self.btn_annuler.setObjectName(_fromUtf8("btn_annuler"))
        self.verticalLayout_5.addWidget(self.btn_annuler)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.btn_suivant = QtGui.QPushButton(self.layoutWidget1)
        self.btn_suivant.setObjectName(_fromUtf8("btn_suivant"))
        self.verticalLayout_4.addWidget(self.btn_suivant)
        self.btn_valider = QtGui.QPushButton(self.layoutWidget1)
        self.btn_valider.setObjectName(_fromUtf8("btn_valider"))
        self.verticalLayout_4.addWidget(self.btn_valider)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Borne", None))
        self.btn_Voiture.setText(_translate("Form", "Detection Arrivee Voiture", None))
        self.label_4.setText(_translate("Form", "NomParking", None))
        self.label.setText(_translate("Form", "Carte Membre ID ", None))
        self.btn_validerID.setText(_translate("Form", "Valider", None))
        self.label_2.setText(_translate("Form", "Non membre", None))
        self.btn_validerNonMembre.setText(_translate("Form", "Valider", None))
        self.btn_cb.setText(_translate("Form", "PayerAvecCarte", None))
        self.btn_precedent.setText(_translate("Form", "<", None))
        self.btn_annuler.setText(_translate("Form", "Annuler", None))
        self.btn_suivant.setText(_translate("Form", ">", None))
        self.btn_valider.setText(_translate("Form", "Valider", None))

