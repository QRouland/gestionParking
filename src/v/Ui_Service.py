# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'service.ui'
#
# Created: Mon Jan 12 17:07:46 2015
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

class Ui_Service(object):
    def setupUi(self, Service):
        Service.setObjectName(_fromUtf8("Service"))
        Service.resize(469, 221)
        self.btn_valider = QtGui.QPushButton(Service)
        self.btn_valider.setGeometry(QtCore.QRect(260, 180, 87, 27))
        self.btn_valider.setObjectName(_fromUtf8("btn_valider"))
        self.dateTimeEdit = QtGui.QDateTimeEdit(Service)
        self.dateTimeEdit.setGeometry(QtCore.QRect(330, 60, 121, 23))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.btn_annuler = QtGui.QPushButton(Service)
        self.btn_annuler.setGeometry(QtCore.QRect(120, 180, 87, 27))
        self.btn_annuler.setObjectName(_fromUtf8("btn_annuler"))
        self.formLayoutWidget = QtGui.QWidget(Service)
        self.formLayoutWidget.setGeometry(QtCore.QRect(160, 60, 160, 41))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lieuLabel = QtGui.QLabel(self.formLayoutWidget)
        self.lieuLabel.setObjectName(_fromUtf8("lieuLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lieuLabel)
        self.lieuLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.lieuLineEdit.setObjectName(_fromUtf8("lieuLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lieuLineEdit)
        self.widget = QtGui.QWidget(Service)
        self.widget.setGeometry(QtCore.QRect(50, 50, 109, 121))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBox_Livraison = QtGui.QCheckBox(self.widget)
        self.checkBox_Livraison.setObjectName(_fromUtf8("checkBox_Livraison"))
        self.verticalLayout.addWidget(self.checkBox_Livraison)
        self.checkBox_Maintenance = QtGui.QCheckBox(self.widget)
        self.checkBox_Maintenance.setObjectName(_fromUtf8("checkBox_Maintenance"))
        self.verticalLayout.addWidget(self.checkBox_Maintenance)
        self.checkBox_Entretien = QtGui.QCheckBox(self.widget)
        self.checkBox_Entretien.setObjectName(_fromUtf8("checkBox_Entretien"))
        self.verticalLayout.addWidget(self.checkBox_Entretien)

        self.retranslateUi(Service)
        QtCore.QMetaObject.connectSlotsByName(Service)

    def retranslateUi(self, Service):
        Service.setWindowTitle(_translate("Service", "Form", None))
        self.btn_valider.setText(_translate("Service", "Valider", None))
        self.btn_annuler.setText(_translate("Service", "Annuler", None))
        self.lieuLabel.setText(_translate("Service", "Lieu", None))
        self.checkBox_Livraison.setText(_translate("Service", "Livraison", None))
        self.checkBox_Maintenance.setText(_translate("Service", "Maintenance", None))
        self.checkBox_Entretien.setText(_translate("Service", "Entretien", None))

