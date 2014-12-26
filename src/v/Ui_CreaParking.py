# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creationParking.ui'
#
# Created: Fri Dec 26 17:33:19 2014
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

class Ui_CreaParking(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 110, 331, 101))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 10, 291, 89))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEdit_nom = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_nom.setObjectName(_fromUtf8("lineEdit_nom"))
        self.verticalLayout_2.addWidget(self.lineEdit_nom)
        self.lineEdit_nbNiv = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_nbNiv.setObjectName(_fromUtf8("lineEdit_nbNiv"))
        self.verticalLayout_2.addWidget(self.lineEdit_nbNiv)
        self.btn_ajouterPlaces = QtGui.QPushButton(self.layoutWidget)
        self.btn_ajouterPlaces.setObjectName(_fromUtf8("btn_ajouterPlaces"))
        self.verticalLayout_2.addWidget(self.btn_ajouterPlaces)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(90, 270, 201, 29))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.layoutWidget2 = QtGui.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(60, 230, 275, 25))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.layoutWidget2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.nbPlacesTotal = QtGui.QLabel(self.layoutWidget2)
        self.nbPlacesTotal.setObjectName(_fromUtf8("nbPlacesTotal"))
        self.horizontalLayout_3.addWidget(self.nbPlacesTotal)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Creation Parking", None))
        self.label.setText(_translate("Form", "Nom", None))
        self.label_2.setText(_translate("Form", "Nombre de niveaux :", None))
        self.label_3.setText(_translate("Form", "Places par niveau :", None))
        self.btn_ajouterPlaces.setText(_translate("Form", "Ajouter places", None))
        self.pushButton_2.setText(_translate("Form", "Annuler", None))
        self.pushButton.setText(_translate("Form", "Valider", None))
        self.label_4.setText(_translate("Form", "Nombre Places Total : ", None))
        self.nbPlacesTotal.setText(_translate("Form", "TextLabel", None))

