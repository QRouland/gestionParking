from PyQt4 import QtGui

__author__ = 'sidya'


class MyQMainWindow(QtGui.QMainWindow):
    def closeEvent(self, event):
        result = QtGui.QMessageBox.question(self,
                                            "Confirmer Fermeture...",
                                            "Etes vous sur de vouloir quitter ?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        event.ignore()
        if result == QtGui.QMessageBox.Yes:
            event.accept()