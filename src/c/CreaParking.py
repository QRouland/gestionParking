from PyQt4 import QtGui, QtCore
from src.m.Parking import Parking
from src.m.Place import ListeTypePlace
from src.v.MyQWidget import MyQWidget
from src.v.Ui_CreaParking import Ui_CreaParking

__author__ = 'sidya'


class CreaParking:
    def __init__(self, main):
        self.__main = main
        self.__main.activity("Debut Creation Parking", self.__main.lvl.INFO)

        self.__row = 0

        self.__w = MyQWidget(self.__main)
        self.__ui = Ui_CreaParking()
        self.__ui.setupUi(self.__w)

        #connect
        self.__ui.btn_addRow.clicked.connect(self.addRow)
        self.__ui.btn_rmRow.clicked.connect(self.rmRow)
        self.__ui.btn_valider.clicked.connect(self.valider)
        self.__ui.btn_annuler.clicked.connect(self.annuler)

        #Validator
        self.__ui.lineEdit_nbNiv.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]*')))


        self.showWindow()


    def insererTable(self,hauteur,longueur,nombre) :
        self.__typePlacesparNiveau.add(hauteur,longueur,nombre)

    def addRow(self):
        self.__ui.tableWidget.insertRow(self.__row)
        self.__row += 1

    def rmRow(self):
        self.__ui.tableWidget.removeRow(self.__ui.tableWidget.rowCount()-1)
        self.__row -= 1

    def annuler(self):
        self.__main.activity("Annulation Creation Parking", self.__main.lvl.INFO)
        self.__w.hide()
        self.__main.showWindow()

    def valider(self):
        try:
            l = ListeTypePlace()
            for i in range(0,self.__ui.tableWidget.rowCount()):
                l.add(int(self.__ui.tableWidget.itemAt(i,0).text()), int(self.__ui.tableWidget.itemAt(i,1).text()),
                      int(self.__ui.tableWidget.itemAt(i,3).text()))
            self.__main.addParking(Parking(
                                   int(self.__ui.lineEdit_nbNiv.text()),
                                   l,
                                   self.__ui.lineEdit_nom.text()))
            self.__main.activity("Ajout Parking : detail", self.__main.lvl.INFO)
            self.__w.hide()
            self.__main.showWindow()
        except Exception as e :
            self.__main.activity("Erreur lors de la creations du Parking \n" + str(e), self.__main.lvl.FAIL)
            self.annuler()

    def showWindow(self):
        self.__w.show()
        self.__child = None #supprime l'eventuel widget enfant
        self.__w.focusWidget() # reprend le focus sur la fenetre