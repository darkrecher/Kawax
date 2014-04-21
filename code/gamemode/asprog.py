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

je rentre pas dans les détails, parce que ce serait trop long et pas intéressant pour vous :
Mais j'ai vraiment une vie de merde. Toute ma vie, en entier, c'est de la merde.
"""

import random
import pygame

from common   import (securedPrint, pyRect, pyRectTuple,
                      FRAME_PER_SECOND, DELAY_GRAVITY,
                      ARENA_SIZE, TILE_PIXEL_SIZE,
                      UP, DOWN, LEFT, RIGHT)

from console  import Console
from arebasic import ArenaBasic
from selector import Selector
from zapvalid import ZapValidatorBase
from stimgame import StimuliStockerForGame
from crawler  import ArenaCrawler
from gravmov  import GravityMovements

from gambasic import GameBasic, DICT_GRAVITY_CONFIG

from coins import ChipAsproHalfLeft, ChipAsproHalfRight
from asproa import ArenaAspirin
from blinker  import Blinker
import language

NB_ASPIRIN_TO_TAKE = 3
COLOR_WIN = (0, 255, 255)
COLOR_ZAP_OBJECTIVE = (255, 50, 50)

LIST_COORD_ASPRO_HALF_LEFT = ((7, 2), (5, 5), (1, 8))
LIST_COORD_ASPRO_HALF_RIGHT = ((9, 1), (10, 3), (11, 1))


class GameAspirin(GameBasic):
    """
    classe qui gère tout le jeu.
    """

    def __init__(self, surfaceDest, gravityDir=DOWN, tutorialScheduler=None):
        """
        constructeur. (thx captain obvious)

        entrée :
            surfaceDest : Surface principale de l'écran, sur laquelle s'affiche le jeu.
        """
        self.initCommonStuff(surfaceDest, gravityDir, tutorialScheduler)

        self.arena = ArenaAspirin(surfaceDest, self.posPixelArena, ARENA_SIZE, 2)
        self.selectorPlayerOne = Selector(self.arena, 0)

        self.crawlerGravRift = ArenaCrawler(ARENA_SIZE)
        self.crawlerGravRift.config(RIGHT, DOWN)
        self.gravityMovementsRift = GravityMovements(LEFT, False, False)
        self.crawlerRegenRift = ArenaCrawler(ARENA_SIZE)
        self.crawlerRegenRift.config(LEFT, UP)
        self.crawlerGravRiftApply = ArenaCrawler(ARENA_SIZE)
        self.crawlerGravRiftApply.config(UP, RIGHT)
        self.nbAspirinTaken = 0

        self.blinker = Blinker(self.arena)

        self.populateArena()
        self.arena.draw()
        pygame.display.flip()


    def populateArena(self):
        """ overriden """
        for (coordX, coordY) in LIST_COORD_ASPRO_HALF_LEFT:
            tileToHardDefine = self.arena.getTile(pyRect(coordX, coordY))
            tileToHardDefine.chip = ChipAsproHalfLeft()
        for (coordX, coordY) in LIST_COORD_ASPRO_HALF_RIGHT:
            tileToHardDefine = self.arena.getTile(pyRect(coordX, coordY))
            tileToHardDefine.chip = ChipAsproHalfRight()

    def applyGravity(self):
        """ zonc """
        securedPrint(u" applyGravity")
        #TRODO : une fonction/propriété, au lieu de ce len de merte.
        # TODO : pourquoi y'a du crawlerGravRiftApply et du crawlerGravRift ?
        if len(self.gravityMovements.dicMovement) > 0:
            param = (self.crawlerGrav, self.gravityMovements, None)
            self.arena.applyGravity(*param)
        elif len(self.gravityMovementsRift.dicMovement) > 0:
            param = (self.crawlerGravRiftApply, self.gravityMovementsRift, self.crawlerRegenRift)
            self.arena.applyGravity(*param)
            self.arena.regenerateAllChipsAfterOneGravity(self.crawlerRegenRift)

    def _determineAnyGravity(self):
        param = (self.crawlerGrav, self.gravityMovements)
        self.gravityMovements = self.arena.determineGravity(*param)

        #pas besoin de controler None ?
        gravNormalToDo = (self.gravityMovements is not None
                          and len(self.gravityMovements.dicMovement) > 0)


        if gravNormalToDo:
            self.gravityCounter = DELAY_GRAVITY
            return True

        param = (self.crawlerGravRift, self.gravityMovementsRift)
        self.gravityMovementsRift = self.arena.determineGravityFullSegment(*param)

        gravColumnToDo = (self.gravityMovementsRift is not None
                          and len(self.gravityMovementsRift.dicMovement) > 0)

        if gravColumnToDo:
            self.gravityCounter = DELAY_GRAVITY
            return True

        return False

    def needStabilization(self):
        """ overriden
        """
        securedPrint(u"needStabilization")
        anyGravToDo = self._determineAnyGravity();
        if anyGravToDo:
            securedPrint(u"needStabilization TRUE")
            return True
        if self.arena.hasAnyEmptyChipInBottom():
            securedPrint(u"needStabilization true")
            return True
        securedPrint(u"needStabilization false")
        return False

    def handleGravity(self):
        """ zob
        True : il reste encore de la gravité à faire
        False : y'en a plus.
        osef ???
        """
        #mal foutu ??
        securedPrint(u"handleGravity")
        self.applyGravity()
        self.arena.removeHalfAsproBottom()

        #copier-coller vilain
        if not self.needStabilization():
            #arrache un peu no ? Réponse : oui, double-arrache, et même : double-arrache copié deux fois.
            if self.tutorialScheduler is None:
                self.selectorPlayerOne.setStimuliLock(False)
            else:
                if not self.tutorialScheduler.mustLockGameStimuli():
                    self.selectorPlayerOne.setStimuliLock(False)


    def gameStimuliInteractiveTouch(self):
        """ overriden """
        #self.blinker.startBlink((pyRect(2, 2), pyRect(3, 2), pyRect(4, 2)))
        if self.arena.getAndResetTakenAsproFull():
            self.nbAspirinTaken += 1
            if self.nbAspirinTaken == NB_ASPIRIN_TO_TAKE:
                listTextWin = language.LIST_TEXTS_WIN[language.languageCurrent]
                self.console.addListTextAndDisplay(listTextWin, COLOR_WIN)
            else:
                textYeah = language.TEXT_YEAH[language.languageCurrent]
                self.console.addListTextAndDisplay((textYeah, ))
                if self.tutorialScheduler is None:
                    strBla = u"%d/%d" % (self.nbAspirinTaken, NB_ASPIRIN_TO_TAKE)
                    self.console.addListTextAndDisplay((strBla, ))


