# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creationPlaces.ui'
#
# Created: Fri Dec 26 18:28:52 2014
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

class Ui_CreaPlaces(object):
    def setupUi(self, CreaPlaces):
        CreaPlaces.setObjectName(_fromUtf8("CreaPlaces"))
        CreaPlaces.resize(339, 202)
        self.formLayoutWidget = QtGui.QWidget(CreaPlaces)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 40, 241, 83))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_hauteur = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_hauteur.setObjectName(_fromUtf8("lineEdit_hauteur"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_hauteur)
        self.lineEdit_longueur = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_longueur.setObjectName(_fromUtf8("lineEdit_longueur"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_longueur)
        self.lineEdit_nombre = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_nombre.setObjectName(_fromUtf8("lineEdit_nombre"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_nombre)
        self.layoutWidget = QtGui.QWidget(CreaPlaces)
        self.layoutWidget.setGeometry(QtCore.QRect(81, 151, 171, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_annuler = QtGui.QPushButton(self.layoutWidget)
        self.btn_annuler.setObjectName(_fromUtf8("btn_annuler"))
        self.horizontalLayout.addWidget(self.btn_annuler)
        self.btn_valider = QtGui.QPushButton(self.layoutWidget)
        self.btn_valider.setObjectName(_fromUtf8("btn_valider"))
        self.horizontalLayout.addWidget(self.btn_valider)

        self.retranslateUi(CreaPlaces)
        QtCore.QMetaObject.connectSlotsByName(CreaPlaces)

    def retranslateUi(self, CreaPlaces):
        CreaPlaces.setWindowTitle(_translate("CreaPlaces", "Creation Type Place", None))
        self.label.setText(_translate("CreaPlaces", "Hauteur", None))
        self.label_2.setText(_translate("CreaPlaces", "Longueur", None))
        self.label_3.setText(_translate("CreaPlaces", "Nombre", None))
        self.btn_annuler.setText(_translate("CreaPlaces", "Annuler", None))
        self.btn_valider.setText(_translate("CreaPlaces", "Valider", None))

