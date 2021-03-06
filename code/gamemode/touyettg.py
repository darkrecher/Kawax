#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax

vocab et nommage des variables :

    pos : pygame.Rect, avec les valeurs width et height à 0.
          position d'un truc. (coordonnées)
    posArena : position d'une case dans l'aire de jeu
    posPixel : position d'un pixel à l'écran ou dans une Surface
    Quand y'a pos tout seul, c'est par défaut posArena, en général.

    path : liste/tuple de posArena (à priori adjacente) formant un chemin.

    coP : coordonnée primaire. int
    coS : coordonnée secondaire. int
    Y'a l'une des coordonnées qu'est x, l'autre y. Ca dépend du contexte.
    En général, quand on veut parcourir toute les cases d'une arena, pour une raison ou
    une autre, la coordonnée primaire, c'est celle de la boucle principale,
    et la coordonnée secondaire, c'est celle de la boucle d'en dessous.
"""

import random
import pygame

from common   import (securedPrint, pyRect, pyRectTuple,
                      FRAME_PER_SECOND, DELAY_GRAVITY,
                      ARENA_SIZE, TILE_PIXEL_SIZE,
                      UP, DOWN, LEFT, RIGHT)

from console  import Console

#from arebasic import ArenaBasic
from touyetta import ArenaTouillette, LIST_CHIP_GENERATION
from gambasic import GameBasic

from selector import Selector
from zapvalid import ZapValidatorBase
from stimgame import StimuliStockerForGame
from crawler  import ArenaCrawler
from gravmov  import GravityMovements
from bigobj   import Touillette
import language

COLOR_WIN = (0, 255, 255)

class GameTouillette(GameBasic):
    """
    classe qui gère tout le jeu.
    """

    def __init__(self, surfaceDest, gravityDir=DOWN, tutorialScheduler=None,
                 xyFirstTouillette=(2, 5)):
        """
        constructeur. (thx captain obvious)

        entrée :
            surfaceDest : Surface principale de l'écran, sur laquelle s'affiche le jeu.
        """
        self.initCommonStuff(surfaceDest, gravityDir, tutorialScheduler)
        self.nbTouilletteToRemove = 2
        self.mustDisplayRemoving = False

        self.arena = ArenaTouillette(surfaceDest, self.posPixelArena,
                                     ARENA_SIZE, 2, LIST_CHIP_GENERATION)

        self.selectorPlayerOne = Selector(self.arena, 0)

        self.populateArena()
        self.arena.addBigObject(Touillette, pyRectTuple(xyFirstTouillette))
        self.arena.draw()
        pygame.display.flip()


    def periodicAction(self):
        """ à overrider """
        # À priori, ce genre de truc n'a rien à foutre dans une "periodicAction".
        # On n'a besoin de le tester uniquement quand une touillette
        # est arrivée en bas de l'écran.
        if self.mustDisplayRemoving:
            securedPrint(u"blorp")

            nbTouRemoved = self.arena.nbTouilletteRemoved
            nbTouToRem = self.nbTouilletteToRemove
            self.mustDisplayRemoving = False

            if nbTouRemoved == nbTouToRem:
                listTextWin = language.LIST_TEXTS_WIN[language.languageCurrent]
                self.console.addListTextAndDisplay(listTextWin, COLOR_WIN)
            else:
                strBla = u"%d/%d" % (nbTouRemoved, nbTouToRem)
                textTouy = language.TEXT_TOUY[language.languageCurrent]
                self.console.addListTextAndDisplay((textTouy, strBla))


    def handleGravity(self):
        securedPrint(u"handleGravity")
        if self.arena.removeBottomTouillette():
            touilletteRemoved = True
            self.mustDisplayRemoving = True
        else:
            touilletteRemoved = False
        self.applyGravity()
        if self.needStabilization() or touilletteRemoved or self.arena.hasTouilletteInBottom():
            securedPrint(u"there is still gravity.")
            self.gravityCounter = DELAY_GRAVITY
        else:
            securedPrint(u"lock set to false.")
            self.selectorPlayerOne.setStimuliLock(False)

