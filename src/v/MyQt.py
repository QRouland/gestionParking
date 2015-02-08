"""
    Module de Gestion personnalisée d'élément Qt
"""

from PyQt4 import QtGui

## QMainWindow personnalisé
class MyQMainWindow(QtGui.QMainWindow):
    ## Ajout d'une boite de dialogue a la fermeture de la fenetre
    def closeEvent(self, event):
        result = QtGui.QMessageBox.question(self,
                                            "Confirmer Fermeture...",
                                            "Etes vous sur de vouloir quitter ?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        event.ignore()
        if result == QtGui.QMessageBox.Yes:
            event.accept()


## QWydget personnalisé
class MyQWidget(QtGui.QWidget):
    ## Ajout d'un controleur parent en parametre lors de la creation d'un Qwidget
    def __init__(self, main):
        super(MyQWidget, self).__init__()
        self.__main = main

    ## Ajout d'une boite de dialogue a la fermeture de la fenetre
    def closeEvent(self, event):
        result = QtGui.QMessageBox.question(self,
                                            "Confirmer Fermeture...",
                                            "Etes vous sur de vouloir quitter ?\n",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        event.ignore()
        if result == QtGui.QMessageBox.Yes:
            event.accept()
            self.__main.showWindow()