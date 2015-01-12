# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'borne.ui'
#
# Created: Mon Jan 12 14:40:36 2015
# by: PyQt4 UI code generator 4.11.3
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


class Ui_Borne(object):
    def setupUi(self, Borne):
        Borne.setObjectName(_fromUtf8("Borne"))
        Borne.resize(669, 579)
        self.btn_Voiture = QtGui.QPushButton(Borne)
        self.btn_Voiture.setGeometry(QtCore.QRect(140, 40, 211, 27))
        self.btn_Voiture.setObjectName(_fromUtf8("btn_Voiture"))
        self.nomParking = QtGui.QLabel(Borne)
        self.nomParking.setGeometry(QtCore.QRect(300, 10, 151, 20))
        self.nomParking.setObjectName(_fromUtf8("nomParking"))
        self.box_id = QtGui.QGroupBox(Borne)
        self.box_id.setGeometry(QtCore.QRect(20, 150, 331, 171))
        self.box_id.setObjectName(_fromUtf8("box_id"))
        self.layoutWidget = QtGui.QWidget(self.box_id)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 60, 272, 85))
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
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.labIdClient = QtGui.QLabel(self.box_id)
        self.labIdClient.setGeometry(QtCore.QRect(130, 31, 91, 16))
        self.labIdClient.setObjectName(_fromUtf8("labIdClient"))
        self.box_abo = QtGui.QGroupBox(Borne)
        self.box_abo.setGeometry(QtCore.QRect(20, 350, 331, 201))
        self.box_abo.setObjectName(_fromUtf8("box_abo"))
        self.formLayoutWidget = QtGui.QWidget(self.box_abo)
        self.formLayoutWidget.setGeometry(QtCore.QRect(-1, 40, 291, 91))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.nomLabel = QtGui.QLabel(self.formLayoutWidget)
        self.nomLabel.setObjectName(_fromUtf8("nomLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.nomLabel)
        self.nomLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.nomLineEdit.setObjectName(_fromUtf8("nomLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nomLineEdit)
        self.prenomLabel = QtGui.QLabel(self.formLayoutWidget)
        self.prenomLabel.setObjectName(_fromUtf8("prenomLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.prenomLabel)
        self.numeroCarteLabel = QtGui.QLabel(self.formLayoutWidget)
        self.numeroCarteLabel.setObjectName(_fromUtf8("numeroCarteLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.numeroCarteLabel)
        self.numeroCarteLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.numeroCarteLineEdit.setObjectName(_fromUtf8("numeroCarteLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.numeroCarteLineEdit)
        self.prenomLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.prenomLineEdit.setObjectName(_fromUtf8("prenomLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.prenomLineEdit)
        self.checkBox = QtGui.QCheckBox(self.box_abo)
        self.checkBox.setGeometry(QtCore.QRect(0, 140, 121, 20))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.btn_valider_abo = QtGui.QPushButton(self.box_abo)
        self.btn_valider_abo.setGeometry(QtCore.QRect(210, 160, 87, 27))
        self.btn_valider_abo.setObjectName(_fromUtf8("btn_valider_abo"))
        self.btn_desabo = QtGui.QPushButton(self.box_abo)
        self.btn_desabo.setGeometry(QtCore.QRect(120, 160, 87, 27))
        self.btn_desabo.setObjectName(_fromUtf8("btn_desabo"))
        self.box_recup = QtGui.QGroupBox(Borne)
        self.box_recup.setGeometry(QtCore.QRect(380, 350, 271, 121))
        self.box_recup.setObjectName(_fromUtf8("box_recup"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.box_recup)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 40, 261, 80))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.numeroTicketLabel = QtGui.QLabel(self.formLayoutWidget_2)
        self.numeroTicketLabel.setObjectName(_fromUtf8("numeroTicketLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.numeroTicketLabel)
        self.numeroTicketLineEdit = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.numeroTicketLineEdit.setObjectName(_fromUtf8("numeroTicketLineEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.numeroTicketLineEdit)
        self.btn_recuperer = QtGui.QPushButton(self.formLayoutWidget_2)
        self.btn_recuperer.setObjectName(_fromUtf8("btn_recuperer"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.btn_recuperer)
        self.label_aff = QtGui.QLabel(Borne)
        self.label_aff.setGeometry(QtCore.QRect(10, 90, 641, 31))
        self.label_aff.setObjectName(_fromUtf8("label_aff"))
        self.box_garer = QtGui.QGroupBox(Borne)
        self.box_garer.setGeometry(QtCore.QRect(390, 150, 231, 131))
        self.box_garer.setObjectName(_fromUtf8("box_garer"))
        self.btn_garer = QtGui.QPushButton(self.box_garer)
        self.btn_garer.setGeometry(QtCore.QRect(50, 60, 131, 27))
        self.btn_garer.setObjectName(_fromUtf8("btn_garer"))
        self.btn_annuler = QtGui.QPushButton(Borne)
        self.btn_annuler.setGeometry(QtCore.QRect(390, 40, 87, 27))
        self.btn_annuler.setObjectName(_fromUtf8("btn_annuler"))
        self.btn_quitter = QtGui.QPushButton(Borne)
        self.btn_quitter.setGeometry(QtCore.QRect(520, 540, 87, 27))
        self.btn_quitter.setObjectName(_fromUtf8("btn_quitter"))

        self.retranslateUi(Borne)
        QtCore.QMetaObject.connectSlotsByName(Borne)

    def retranslateUi(self, Borne):
        Borne.setWindowTitle(_translate("Borne", "Borne", None))
        self.btn_Voiture.setText(_translate("Borne", "Detection Arrivee Voiture", None))
        self.nomParking.setText(_translate("Borne", "NomParking", None))
        self.box_id.setTitle(_translate("Borne", "Identification", None))
        self.label.setText(_translate("Borne", "Carte Membre ID ", None))
        self.btn_validerID.setText(_translate("Borne", "Valider", None))
        self.labIdClient.setText(_translate("Borne", "Non identifier", None))
        self.box_abo.setTitle(_translate("Borne", "S\'abonner", None))
        self.nomLabel.setText(_translate("Borne", "Nom", None))
        self.prenomLabel.setText(_translate("Borne", "Prenom", None))
        self.numeroCarteLabel.setText(_translate("Borne", "Numero carte", None))
        self.checkBox.setText(_translate("Borne", "PackGarantie", None))
        self.btn_valider_abo.setText(_translate("Borne", "Valider", None))
        self.btn_desabo.setText(_translate("Borne", "Désabonner", None))
        self.box_recup.setTitle(_translate("Borne", "Récuperer", None))
        self.numeroTicketLabel.setText(_translate("Borne", "Numero Ticket :", None))
        self.btn_recuperer.setText(_translate("Borne", "Récupérer Véhicule", None))
        self.label_aff.setText(
            _translate("Borne", "<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.box_garer.setTitle(_translate("Borne", "Se garer", None))
        self.btn_garer.setText(_translate("Borne", "Garer Véhicule", None))
        self.btn_annuler.setText(_translate("Borne", "Annuler", None))
        self.btn_quitter.setText(_translate("Borne", "Quitter", None))

