#/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Kawax version 1.0

    La page du jeu sur indieDB : http://www.indiedb.com/games/kawax
    Liens vers d'autres jeux sur mon blog : http://recher.wordpress.com/jeux
    Mon twitter : http://twitter.com/_Recher_

    Ce superbe jeu, son code source, ses images, et son euh... contenu sonore est disponible,
    au choix, sous la licence Art Libre ou la licence CC-BY-SA

    Copyright 2010 R�ch�r
    Copyleft : cette oeuvre est libre, vous pouvez la redistribuer et/ou la modifier selon les
    termes de la Licence Art Libre. Vous trouverez un exemplaire de cette Licence sur le site
    Copyleft Attitude http://www.artlibre.org ainsi que sur d'autres sites.

    Creative Commons - Paternit� - Partage des Conditions Initiales � l'Identique 2.0 France
    http://creativecommons.org/licenses/by-sa/2.0/fr/deed.fr

date de la derni�re relecture-commentage : None
"""

import random
import pygame

from common   import (securedPrint, pyRect,
                      UP, DOWN, LEFT, RIGHT)

from gambasic import GameBasic

COLOR_WIN = (0, 255, 255)

class GameZapCounter(GameBasic):
    """
    classe qui g�re tout le jeu. Non. haha !
    """

    def __init__(self, surfaceDest, gravityDir=DOWN, nbZapToDo=4):
        """
        constructeur. (thx captain obvious)

        entr�e :
            surfaceDest : Surface principale de l'�cran, sur laquelle s'affiche le jeu.
        """
        GameBasic.__init__(self, surfaceDest, gravityDir)
        self.nbZapToDo = nbZapToDo
        self.nbZapDone = 0

        
    def zapWin(self):
        """ � overrider """
        self.nbZapDone += 1
        if self.nbZapDone == self.nbZapToDo:
            listBla = ("BRAVO ! ", "Vous avez gagn�!", 
                       "Vous pouvez", "continuer de",
                       "jouer si vous", "trouvez �a cool")
            self.console.addListTextAndDisplay(listBla, COLOR_WIN)
        else:
            strBla = "%d/%d" % (self.nbZapDone, self.nbZapToDo)
            self.console.addListTextAndDisplay(("yeah !!", strBla, ))
            