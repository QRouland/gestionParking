from PyQt4 import QtGui
from src.v.MyQWidget import MyQWidget
from src.v.Ui_Service import Ui_Service


__author__ = 'sidya'


class SelectService:
    """
    Controleur de cretion de parking
    """
    def __init__(self, main):
        self.__main = main
        self.__main.activity("Choix Service", self.__main.lvl.INFO)

        self._w = MyQWidget(self.__main)
        self.__ui = Ui_Service()
        self.__ui.setupUi(self._w)

        # connect
        self.__ui.btn_valider.clicked.connect(self.valider)

        # Validator


        self.showWindow()

   
    def valider(self):
        """
        Gestion validation de formulaire de choix de service
        :return:
        """
    

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
                                  "Erreur lors du choix de service ...")
        self._w.hide()
        self.__main.showWindow()