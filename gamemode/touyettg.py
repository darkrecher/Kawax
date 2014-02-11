#/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Kawax version 0.1

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

vocab et nommage des variables :

    pos : pygame.Rect, avec les valeurs width et height � 0.
          position d'un truc. (coordonn�es)
    posArena : position d'une case dans l'aire de jeu
    posPixel : position d'un pixel � l'�cran ou dans une Surface
    Quand y'a pos tout seul, c'est par d�faut posArena, en g�n�ral.

    path : liste/tuple de posArena (� priori adjacente) formant un chemin.

    coP : coordonn�e primaire. int
    coS : coordonn�e secondaire. int
    Y'a l'une des coordonn�es qu'est x, l'autre y. Ca d�pend du contexte.
    En g�n�ral, quand on veut parcourir toute les cases d'une arena, pour une raison ou
    une autre, la coordonn�e primaire, c'est celle de la boucle principale,
    et la coordonn�e secondaire, c'est celle de la boucle d'en dessous.
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
    classe qui g�re tout le jeu.
    """

    def __init__(self, surfaceDest, gravityDir=DOWN, tutorialScheduler=None,
                 xyFirstTouillette=(2, 5)):
        """
        constructeur. (thx captain obvious)

        entr�e :
            surfaceDest : Surface principale de l'�cran, sur laquelle s'affiche le jeu.
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
        """ � overrider """

        if self.mustDisplayRemoving:
            print "blorp"

            nbTouRemoved = self.arena.nbTouilletteRemoved
            nbTouToRem = self.nbTouilletteToRemove
            self.mustDisplayRemoving = False

            if nbTouRemoved == nbTouToRem:
                listBla = ("BRAVO ! ", "Vous avez gagn�!",
                           "Vous pouvez", "continuer de",
                           "jouer si vous", "trouvez �a cool")
                self.console.addListTextAndDisplay(listBla)
            else:
                strBla = "%d/%d" % (nbTouRemoved, nbTouToRem)
                listStrBla = ("Touillettes :", strBla)
                self.console.addListTextAndDisplay(listStrBla)


    def handleGravity(self):
        # Les actions de contr�le et d'actions sont pas dans l'ordre.
        # Ca fait nimp.
        print "handleGravity"
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

