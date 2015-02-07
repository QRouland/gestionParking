from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QTableWidgetItem
from src.m.Parking import TypePlace, Parking
from src.v.MyQt import MyQWidget
from src.v.Ui_Admin import Ui_CreaParking


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
        self._ui.lineEdit_nom.setValidator(
            QtGui.QRegExpValidator(QtCore.QRegExp('^([0-9a-zA-Z\'àâéèêôùûçñãõÀÂÉÈÔÙÛÑÃÕÇ\s-]{2,30})$')))

        self._ui.tableWidget.insertRow(self._ui.tableWidget.rowCount())
        self.showWindow()

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
        if self._ui.lineEdit_nom.text() == "":
            self._main.activity("Erreur lors de la creations du Parking. Nom Invalide.\n", self._main.lvl.FAIL)
            self.error("Nom Invalide!")
        else:
            try:
                l = []
                for i in range(0, self._ui.tableWidget.rowCount()):
                    l.append(TypePlace(None, int(self._ui.tableWidget.item(i, 0).text()),
                                       int(self._ui.tableWidget.item(i, 1).text()),
                                       int(self._ui.tableWidget.item(i, 2).text()),
                                       float(self._ui.tableWidget.item(i, 4).text()),
                                       int(self._ui.tableWidget.item(i, 3).text())))
                p = Parking(None, self._ui.lineEdit_nom.text(), l)
                self._main.activity("Ajout:" + str(p), self._main.lvl.INFO)
                self._w.hide()
                self._main.showWindow()
            except Exception as e:
                self._main.activity("Erreur lors de la creations du Parking \n" + str(e), self._main.lvl.FAIL)
                self.error("Verifiez que votre saisie est valide !")

    def showWindow(self):
        """
        Gestion affichage vue Creation de Parking
        :return:
        """
        self._w.show()

    def error(self, msg):
        """
        Qdialog message erreur
        :return:
        """
        QtGui.QMessageBox.warning(self._w,
                                  "Erreur ...",
                                  "Erreur lors de la création du parking ...\n" +
                                  msg
        )


class DetailsPlaces(CreaParking):
    def __init__(self, main, parking):
        self.__parking = parking
        super(DetailsPlaces, self).__init__(main)

        self._ui.lineEdit_nom.setText(parking.nom)
        for p in parking.typePlaces :
            row = self._ui.tableWidget.rowCount() - 1
            if row != 0:
                self._ui.tableWidget.insertRow(row)
            self._ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(p.hauteur)))
            self._ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(p.longueur)))
            self._ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(p.nb)))

        self._ui.lineEdit_nom.setDisabled(True)
        self._ui.tableWidget.setDisabled(True)
        self._ui.btn_annuler.setVisible(False)
        self._ui.btn_addRow.setVisible(False)
        self._ui.btn_rmRow.setVisible(False)

    def valider(self):
        self._w.hide()
        self._main.showWindow()