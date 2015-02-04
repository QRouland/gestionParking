from PyQt4.QtGui import QTableWidgetItem

from src.c.CreaParking import CreaParking


__author__ = 'sidya'


class DetailsPlaces(CreaParking):
    def __init__(self, main, parking):
        self.__parking = parking
        super(DetailsPlaces, self).__init__(main)

        self._ui.lineEdit_nom.setText(parking.nom)
        for p in parking.typePlacesParNiv.l:
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

