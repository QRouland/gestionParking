import sqlite3

from src.c.Main import Main
from src.m.connexionBDD import connexionBDD


__author__ = 'sidya'


if __name__ == "__main__":
    c = connexionBDD()
    c.initialisationBDD()
    c.seDeconnecter()
    # lancement du controleur principal
    main = Main()

