#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax
"""

import pygame

from common   import (securedPrint, pyRect,
                           UP, DOWN, LEFT, RIGHT)
from gambasic import GameBasic
import language

COLOR_WIN = (0, 255, 255)

class GameZapCounter(GameBasic):
    """
    classe qui gère tout le jeu. Non. haha !
    """

    def __init__(self, surfaceDest, gravityDir=DOWN, nbZapToDo=4):
        """
        constructeur. (thx captain obvious)

        entrée :
            surfaceDest : Surface principale de l'écran, sur laquelle s'affiche le jeu.
        """
        GameBasic.__init__(self, surfaceDest, gravityDir)
        self.nbZapToDo = nbZapToDo
        self.nbZapDone = 0


    def zapWin(self):
        """ à overrider """
        self.nbZapDone += 1
        if self.nbZapDone == self.nbZapToDo:
            listTextWin = language.LIST_TEXTS_WIN[language.languageCurrent]
            self.console.addListTextAndDisplay(listTextWin, COLOR_WIN)
        else:
            textYeah = language.TEXT_YEAH[language.languageCurrent]
            strBla = u"%d/%d" % (self.nbZapDone, self.nbZapToDo)
            self.console.addListTextAndDisplay((textYeah, strBla, ))
