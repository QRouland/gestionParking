from PyQt4 import QtGui


class MyQMainWindow(QtGui.QMainWindow):
    def closeEvent(self, event):
        result = QtGui.QMessageBox.question(self,
                                            "Confirmer Fermeture...",
                                            "Etes vous sur de vouloir quitter ?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        event.ignore()
        if result == QtGui.QMessageBox.Yes:
            event.accept()

    def error(self, msg):
        """
        Qdialog message erreur
        :return:
        """
        QtGui.QMessageBox.warning(self._w,
                                  "Erreur ...",
                                  msg
        )


class MyQWidget(QtGui.QWidget):
    def __init__(self, main):
        super(MyQWidget, self).__init__()
        self.__main = main

    def closeEvent(self, event):
        result = QtGui.QMessageBox.question(self,
                                            "Confirmer Fermeture...",
                                            "Etes vous sur de vouloir quitter ?\n",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        event.ignore()
        if result == QtGui.QMessageBox.Yes:
            event.accept()
            self.__main.showWindow()