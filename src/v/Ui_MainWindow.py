# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Jan 22 09:11:44 2015
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(601, 596)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 40, 561, 501))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 10, 61, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidget = QtGui.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(60, 50, 431, 261))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_13)
        self.nom = QtGui.QLabel(self.tab_2)
        self.nom.setObjectName(_fromUtf8("nom"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.nom)
        self.label_15 = QtGui.QLabel(self.tab_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_15)
        self.placesParNiveau = QtGui.QLabel(self.tab_2)
        self.placesParNiveau.setObjectName(_fromUtf8("placesParNiveau"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.placesParNiveau)
        self.label_16 = QtGui.QLabel(self.tab_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_16)
        self.placesDispo = QtGui.QLabel(self.tab_2)
        self.placesDispo.setObjectName(_fromUtf8("placesDispo"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.placesDispo)
        self.label_17 = QtGui.QLabel(self.tab_2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_17)
        self.placesSuperAbo = QtGui.QLabel(self.tab_2)
        self.placesSuperAbo.setObjectName(_fromUtf8("placesSuperAbo"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.placesSuperAbo)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_details = QtGui.QPushButton(self.tab_2)
        self.btn_details.setObjectName(_fromUtf8("btn_details"))
        self.horizontalLayout.addWidget(self.btn_details)
        self.btn_borne = QtGui.QPushButton(self.tab_2)
        self.btn_borne.setObjectName(_fromUtf8("btn_borne"))
        self.horizontalLayout.addWidget(self.btn_borne)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.btn_creer = QtGui.QPushButton(self.tab_2)
        self.btn_creer.setObjectName(_fromUtf8("btn_creer"))
        self.verticalLayout.addWidget(self.btn_creer)
        self.btn_supprimer = QtGui.QPushButton(self.tab_2)
        self.btn_supprimer.setObjectName(_fromUtf8("btn_supprimer"))
        self.verticalLayout.addWidget(self.btn_supprimer)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox = QtGui.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(30, 60, 501, 111))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.comboBox_maintenance = QtGui.QComboBox(self.groupBox)
        self.comboBox_maintenance.setGeometry(QtCore.QRect(10, 20, 481, 27))
        self.comboBox_maintenance.setObjectName(_fromUtf8("comboBox_maintenance"))
        self.btn_effectuer_maintenance = QtGui.QPushButton(self.groupBox)
        self.btn_effectuer_maintenance.setGeometry(QtCore.QRect(326, 70, 161, 27))
        self.btn_effectuer_maintenance.setObjectName(_fromUtf8("btn_effectuer_maintenance"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 180, 501, 101))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.comboBox_entretien = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_entretien.setGeometry(QtCore.QRect(10, 20, 481, 27))
        self.comboBox_entretien.setObjectName(_fromUtf8("comboBox_entretien"))
        self.btn_effectuer_entretien = QtGui.QPushButton(self.groupBox_2)
        self.btn_effectuer_entretien.setGeometry(QtCore.QRect(326, 60, 161, 27))
        self.btn_effectuer_entretien.setObjectName(_fromUtf8("btn_effectuer_entretien"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 290, 511, 111))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.comboBox_livraison = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_livraison.setGeometry(QtCore.QRect(10, 20, 481, 27))
        self.comboBox_livraison.setObjectName(_fromUtf8("comboBox_livraison"))
        self.btn_effectuer_livraison = QtGui.QPushButton(self.groupBox_3)
        self.btn_effectuer_livraison.setGeometry(QtCore.QRect(326, 70, 161, 27))
        self.btn_effectuer_livraison.setObjectName(_fromUtf8("btn_effectuer_livraison"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.label_2 = QtGui.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 161, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 161, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(40, 140, 241, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 10, 539, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        self.menuA_propos = QtGui.QMenu(self.menubar)
        self.menuA_propos.setObjectName(_fromUtf8("menuA_propos"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionCharger = QtGui.QAction(MainWindow)
        self.actionCharger.setObjectName(_fromUtf8("actionCharger"))
        self.actionSauvegarder = QtGui.QAction(MainWindow)
        self.actionSauvegarder.setObjectName(_fromUtf8("actionSauvegarder"))
        self.actionAfficher = QtGui.QAction(MainWindow)
        self.actionAfficher.setObjectName(_fromUtf8("actionAfficher"))
        self.actionNouveau = QtGui.QAction(MainWindow)
        self.actionNouveau.setObjectName(_fromUtf8("actionNouveau"))
        self.actionRechercher = QtGui.QAction(MainWindow)
        self.actionRechercher.setObjectName(_fromUtf8("actionRechercher"))
        self.actionListe = QtGui.QAction(MainWindow)
        self.actionListe.setObjectName(_fromUtf8("actionListe"))
        self.actionAjouter = QtGui.QAction(MainWindow)
        self.actionAjouter.setObjectName(_fromUtf8("actionAjouter"))
        self.actionQuitter = QtGui.QAction(MainWindow)
        self.actionQuitter.setObjectName(_fromUtf8("actionQuitter"))
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.actionNouveau_2 = QtGui.QAction(MainWindow)
        self.actionNouveau_2.setObjectName(_fromUtf8("actionNouveau_2"))
        self.menuFichier.addAction(self.actionCharger)
        self.menuFichier.addAction(self.actionNouveau_2)
        self.menuFichier.addAction(self.actionSauvegarder)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuitter)
        self.menuA_propos.addAction(self.action)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuA_propos.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Administration", None))
        self.label.setText(_translate("MainWindow", "Activité :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Activite", None))
        self.label_13.setText(_translate("MainWindow", "Nom :", None))
        self.nom.setText(_translate("MainWindow", "TextLabel", None))
        self.label_15.setText(_translate("MainWindow", "Places total:", None))
        self.placesParNiveau.setText(_translate("MainWindow", "TextLabel", None))
        self.label_16.setText(_translate("MainWindow", "Places disponible :", None))
        self.placesDispo.setText(_translate("MainWindow", "TextLabel", None))
        self.label_17.setText(_translate("MainWindow", "Places Reserve Super Abo : ", None))
        self.placesSuperAbo.setText(_translate("MainWindow", "TextLabel", None))
        self.btn_details.setText(_translate("MainWindow", "Details Places", None))
        self.btn_borne.setText(_translate("MainWindow", "Borne", None))
        self.btn_creer.setText(_translate("MainWindow", "Créer", None))
        self.btn_supprimer.setText(_translate("MainWindow", "Supprimer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Parkings", None))
        self.groupBox.setTitle(_translate("MainWindow", "Maintenance", None))
        self.btn_effectuer_maintenance.setText(_translate("MainWindow", "Effectuer Maintenance", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Entretien", None))
        self.btn_effectuer_entretien.setText(_translate("MainWindow", "Effectuer Entretien", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Livraison", None))
        self.btn_effectuer_livraison.setText(_translate("MainWindow", "Effectuer Livraison", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Services", None))
        self.label_2.setText(_translate("MainWindow", "Frequentation par jour", None))
        self.label_3.setText(_translate("MainWindow", "Frequentation par mois", None))
        self.label_4.setText(_translate("MainWindow", "Duree moyenne de stationnement ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Stats", None))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.menuA_propos.setTitle(_translate("MainWindow", "A propos", None))
        self.actionCharger.setText(_translate("MainWindow", "Charger", None))
        self.actionSauvegarder.setText(_translate("MainWindow", "Sauvegarder", None))
        self.actionAfficher.setText(_translate("MainWindow", "Afficher", None))
        self.actionNouveau.setText(_translate("MainWindow", "Nouveau", None))
        self.actionRechercher.setText(_translate("MainWindow", "Rechercher", None))
        self.actionListe.setText(_translate("MainWindow", "Liste", None))
        self.actionAjouter.setText(_translate("MainWindow", "Ajouter", None))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter", None))
        self.action.setText(_translate("MainWindow", "?", None))
        self.actionNouveau_2.setText(_translate("MainWindow", "Nouveau", None))

