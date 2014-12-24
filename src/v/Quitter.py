# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Wed Dec 10 16:47:28 2014
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(522, 412)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 561, 441))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 10, 61, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.log = QtGui.QListView(self.tab)
        self.log.setGeometry(QtCore.QRect(30, 40, 421, 241))
        self.log.setObjectName(_fromUtf8("log"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.formLayoutWidget = QtGui.QWidget(self.tab_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(100, 80, 311, 151))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout_3 = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_13 = QtGui.QLabel(self.formLayoutWidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtGui.QLabel(self.formLayoutWidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_11 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_11)
        self.lineEdit_12 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_12)
        self.label_15 = QtGui.QLabel(self.formLayoutWidget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_13 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_13)
        self.label_16 = QtGui.QLabel(self.formLayoutWidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_14 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_14)
        self.label_17 = QtGui.QLabel(self.formLayoutWidget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_17)
        self.lineEdit_15 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_15)
        self.pushButton_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 270, 101, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.comboBox = QtGui.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(100, 40, 321, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.pushButton = QtGui.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(290, 270, 81, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tableView = QtGui.QTableView(self.tab_5)
        self.tableView.setGeometry(QtCore.QRect(50, 40, 431, 201))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuBorne = QtGui.QMenu(self.menubar)
        self.menuBorne.setObjectName(_fromUtf8("menuBorne"))
        self.menuBornes = QtGui.QMenu(self.menubar)
        self.menuBornes.setObjectName(_fromUtf8("menuBornes"))
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
        self.menuBorne.addSeparator()
        self.menuBorne.addAction(self.actionCharger)
        self.menuBorne.addAction(self.actionSauvegarder)
        self.menubar.addAction(self.menuBorne.menuAction())
        self.menubar.addAction(self.menuBornes.menuAction())
        self.menubar.addAction(self.menuA_propos.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Activité :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Activite", None))
        self.label_13.setText(_translate("MainWindow", "Nom :", None))
        self.label_14.setText(_translate("MainWindow", "Niveau :", None))
        self.label_15.setText(_translate("MainWindow", "Place / niveau :", None))
        self.label_16.setText(_translate("MainWindow", "Place disponible :", None))
        self.label_17.setText(_translate("MainWindow", "Place Reserve Super Abo : ", None))
        self.pushButton_2.setText(_translate("MainWindow", "Creer/Modifier", None))
        self.pushButton.setText(_translate("MainWindow", "Supprimer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Parkings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Membres", None))
        self.menuBorne.setTitle(_translate("MainWindow", "Fichier", None))
        self.menuBornes.setTitle(_translate("MainWindow", "Quitter", None))
        self.menuA_propos.setTitle(_translate("MainWindow", "A propos", None))
        self.actionCharger.setText(_translate("MainWindow", "Charger", None))
        self.actionSauvegarder.setText(_translate("MainWindow", "Sauvegarder", None))
        self.actionAfficher.setText(_translate("MainWindow", "Afficher", None))
        self.actionNouveau.setText(_translate("MainWindow", "Nouveau", None))
        self.actionRechercher.setText(_translate("MainWindow", "Rechercher", None))
        self.actionListe.setText(_translate("MainWindow", "Liste", None))
        self.actionAjouter.setText(_translate("MainWindow", "Ajouter", None))

