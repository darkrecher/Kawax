#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax
"""

import random
import pygame

from common   import (securedPrint, pyRect,
                           UP, DOWN, LEFT, RIGHT)

from gambasic import GameBasic

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
            listBla = (u"BRAVO ! ",
                       u"Vous avez gagné!",
                       u"Vous pouvez",
                       u"continuer de",
                       u"jouer si vous",
                       u"trouvez ça cool")
            self.console.addListTextAndDisplay(listBla, COLOR_WIN)
        else:
            strBla = u"%d/%d" % (self.nbZapDone, self.nbZapToDo)
            self.console.addListTextAndDisplay((u"yeah !!", strBla, ))
