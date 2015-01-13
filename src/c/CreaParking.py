from PyQt4 import QtGui

from src.m.Parking import Parking, TypePlace
from src.v.MyQWidget import MyQWidget
from src.v.Ui_CreaParking import Ui_CreaParking


__author__ = 'sidya'


class CreaParking:
    """
    Controleur de cretion de parking
    """
    def __init__(self, main):
        self._main = main
        self._main.activity("Debut Creation Parking", self._main.lvl.INFO)

        self._w = MyQWidget(self._main)
        self._ui = Ui_CreaParking()
        self._ui.setupUi(self._w)

        # connect
        self._ui.btn_addRow.clicked.connect(self.addRow)
        self._ui.btn_rmRow.clicked.connect(self.rmRow)
        self._ui.btn_valider.clicked.connect(self.valider)
        self._ui.btn_annuler.clicked.connect(self.annuler)

        # Validator
        #self._ui.lineEdit_nbNiv.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]*')))

        self._ui.tableWidget.insertRow(self._ui.tableWidget.rowCount())
        self.showWindow()

    def majNbPlaceTotal(self):
        nb = 0
        for i in range(0, self._ui.tableWidget.rowCount()):
            nb += int(self._ui.tableWidget.itemAt(i, 3).text())
        self._ui.nbPlacesTotal.setText(str(nb))

    def addRow(self):
        """
        Ajoute une ligne de creation de place
        :return:
        """
        self._ui.tableWidget.insertRow(self._ui.tableWidget.rowCount())

    def rmRow(self):
        """
        Enleve une ligne de creation de place
        :return:
        """
        self._ui.tableWidget.removeRow(self._ui.tableWidget.rowCount() - 1)

    def annuler(self):
        """
        Gestion annulation creation parking
        :return:
        """
        result = QtGui.QMessageBox.question(self._w,
                                            "Confirmer Fermeture...",
                                            "Etes vous sur de vouloir abandonner ?\n"
                                            "(Toute modification non enregistrée seras perdu)",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if result == QtGui.QMessageBox.Yes:
            self._main.activity("Annulation Creation Parking", self._main.lvl.INFO)
            self._w.hide()
            self._main.showWindow()

    def valider(self):
        """
        Gestion validation de formulaire de creation de parking.
        :return:
        """
        # try:
        l = []
        for i in range(0, self._ui.tableWidget.rowCount()):
            l.append(TypePlace(None,int(self._ui.tableWidget.item(i, 0).text()), int(self._ui.tableWidget.item(i, 1).text()),
                               int(self._ui.tableWidget.item(i, 2).text())))
        p = Parking(self._ui.lineEdit_nom.text(),l)
        self._main.activity("Ajout:" + str(p), self._main.lvl.INFO)
        self._w.hide()
        self._main.showWindow()
        #except Exception as e:
        #    self._main.activity("Erreur lors de la creations du Parking \n" + str(e), self._main.lvl.FAIL)
        #    self.error()

    def showWindow(self):
        """
        Gestion affichage vue Creation de Parking
        :return:
        """
        self._w.show()
        self.__child = None  # supprime l'eventuel widget enfant
        self._w.focusWidget()  # reprend le focus sur la fenetre

    def error(self):
        """
        Qdialog message erreur
        :return:
        """
        QtGui.QMessageBox.warning(self._w,
                                  "Erreur ...",
                                  "Erreur lors de la création du parking ...")
        self._w.hide()
        self._main.showWindow()