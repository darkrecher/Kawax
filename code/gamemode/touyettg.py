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

        if self.mustDisplayRemoving:
            securedPrint(u"blorp")

            nbTouRemoved = self.arena.nbTouilletteRemoved
            nbTouToRem = self.nbTouilletteToRemove
            self.mustDisplayRemoving = False

            if nbTouRemoved == nbTouToRem:
                listBla = (u"BRAVO ! ",
                           u"Vous avez gagné!",
                           u"Vous pouvez",
                           u"continuer de",
                           u"jouer si vous",
                           u"trouvez ça cool")
                self.console.addListTextAndDisplay(listBla)
            else:
                strBla = u"%d/%d" % (nbTouRemoved, nbTouToRem)
                listStrBla = (u"Touillettes :", strBla)
                self.console.addListTextAndDisplay(listStrBla)


    def handleGravity(self):
        # Les actions de contrôle et d'actions sont pas dans l'ordre.
        # Ca fait nimp.
        securedPrint(u"handleGravity")
        if self.arena.removeBottomTouillette():
            touilletteRemoved = True
            self.mustDisplayRemoving = True
        else:
            touilletteRemoved = False
        self.applyGravity()
        if self.determineGravity() or touilletteRemoved or self.arena.hasTouilletteInBottom():
            self.gravityCounter = DELAY_GRAVITY
        else:
            self.selectorPlayerOne.setStimuliLock(False)

