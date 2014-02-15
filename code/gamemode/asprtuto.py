#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax
"""

from common   import (pyRect, pyRectTuple,
                      UP, DOWN, LEFT, RIGHT, NO_SOUND)

from console  import Console
from coins    import ChipCoin, ChipSugar, ChipAsproHalfLeft, ChipAsproHalfRight
from asprog   import GameAspirin
from blinker  import Blinker
from zapvalid import ZapValidatorBase
from tutorial import (TutorialScheduler,
                      STEP_COND_NEVER, STEP_COND_STIM, STEP_COND_SELECT_TILES,
                      STEP_COND_INTERACTIVE_TOUCH_SUCCESSED,
                      COLOR_TUTORIAL)

LIST_TUT_STEP_DESCRIP = (
    (
        STEP_COND_STIM,
        (),
        NO_SOUND,
        (u"Salut. T'es encore là ?",
         u"C'est bien, t'es un bon",
         u"petit soldat.",),
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        NO_SOUND,
        (u"Les 2 machins blancs ",
         u"au milieu de l'écran,",
         u"ce sont des demis-cachets",
         u"d'aspirine.",
         u"Faut les coller ensemble."),
        (),
        False
    ),(
        STEP_COND_SELECT_TILES,
        ((4, 8), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (6, 5), (6, 6)),
        NO_SOUND,
        (u"Tu vas commencer par me",
         u"péter tout ça."),
        ((4, 8), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (6, 5), (6, 6)),
        False
    ),(
        STEP_COND_STIM,
        (),
        NO_SOUND,
        (u"Ouaf ouaf, Meeeuuhh",
         u"gruuiik grruuuiiiikk !",
         u"Pardon. On en étais où ?",
         u"Ah oui. Cliquez sur",
         u"Suivant, comme d'hab'."),
        (),
        False
    ),(
        STEP_COND_SELECT_TILES,
        ((5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9)),
        NO_SOUND,
        (u"Et maintenant, pète-moi",
         u"ça, histoire de vider la",
         u"colonne. Et tu regarderas",
         u"bien ce que ça fait,",
         u"jeune boulawan."),
        ((5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9)),
        False
    ),(
        STEP_COND_STIM,
        (),
        NO_SOUND,
        (u"Et hop. Ca s'est déplacé",
         u"vers la gauche.",
         u"C'est-y pas top foufoutre",
         u"au carré, ça ? Hmmm ?"),
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        NO_SOUND,
        (u"Sauf que maintenant,",
         u"les aspirines ne sont",
         u"plus en face."),
        (),
        False
    ),(
        STEP_COND_SELECT_TILES,
        ((4, 7), (4, 8)),
        NO_SOUND,
        ((u"Dégomme-moi ce bazar.", )),
        ((4, 7), (4, 8)),
        False
    ),(
        STEP_COND_INTERACTIVE_TOUCH_SUCCESSED,
        (),
        NO_SOUND,
        (u"Bien, petit stagiaire.",
         u"Maintenant, tu vas ",
         u"cliquer sur l'un des ",
         u"demi-cachets."),
        (),
        False
    ),(
        STEP_COND_INTERACTIVE_TOUCH_SUCCESSED,
        (),
        NO_SOUND,
        (u"Hop, ils se réunissent.",
         u"Et pour finir, cliques sur",
         u"le cachet entier."),
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        NO_SOUND,
        (u"Bon ben voilà, c'était super.",
         u"Est-ce que c'était assez",
         u"pour vous ?"),
        (),
        False
    ),(
        STEP_COND_NEVER,
        (),
        NO_SOUND,
        (),
        (),
        True
    ),
)

LIST_ZAP_CONSTRAINT = (
    (16, 2),
    (17, 1),
    (15, 0),
)

# premier elem : coordonnées
# 2eme elem. "C" ou "S" pour dire si c'est un coin ou un sugar.
#            Et ensuite la valeur en brouzouf du coin, si c'est un coin.
LIST_TILE_TO_HARDDEFINE = (
    # Pour la première sélection
    ((4, 8), ("C", 5)),
    ((5, 4), ("C", 2)),
    ((5, 5), ("C", 1)),
    ((5, 6), ("S", 0)),
    ((5, 7), ("C", 5)),
    ((5, 8), ("C", 1)),
    ((6, 5), ("S", 0)),
    ((6, 6), ("C", 2)),
    # Pour la 2ème
    ((5, 0), ("C", 1)),
    ((5, 1), ("C", 2)),
    ((5, 2), ("C", 0)),
    ((5, 3), ("C", 2)),
    ((5, 9), ("C", 10)),
    ((6, 9), ("C", 2)),
    ((7, 9), ("S", 0)),
    # Pour la 3ème
    ((4, 6), ("C", 10)),
    ((4, 7), ("C", 5)),
)

class GameAspirinTuto(GameAspirin):
    """
    classe qui gère tout le jeu. ou pas
    """

    def __init__(self, surfaceDest, gravityDir=DOWN):
        """
        constructeur. (thx captain obvious)

        entrée :
            surfaceDest : Surface principale de l'écran, sur laquelle s'affiche le jeu.
        """
        tutorialScheduler = TutorialScheduler(LIST_TUT_STEP_DESCRIP)
        self.listTileToHardDefine = LIST_TILE_TO_HARDDEFINE
        GameAspirin.__init__(self, surfaceDest, gravityDir, tutorialScheduler)
        self.blinker = Blinker(self.arena)
        #self.refreshTutoInfo()
        #self.selectorPlayerOne.setStimuliLock(True)
        self.showObjectivesAtStart = False
        self.listZapConstraint = LIST_ZAP_CONSTRAINT
        self.nbZapMade = 0

    def populateArena(self):
        """ overrides """
        # on définit des tiles. C'est mignon et gentil.
        for hardData in self.listTileToHardDefine:
            coord = hardData[0]
            typeTile = hardData[1][0]
            tileToHardDefine = self.arena.getTile(pyRectTuple(coord))
            if typeTile == "C":
                brouzouf = hardData[1][1]
                tileToHardDefine.chip = ChipCoin(brouzouf)
            else:
                tileToHardDefine.chip = ChipSugar()

        tileToHardDefine = self.arena.getTile(pyRect(4, 3))
        tileToHardDefine.chip = ChipAsproHalfLeft()
        tileToHardDefine = self.arena.getTile(pyRect(6, 3))
        tileToHardDefine.chip = ChipAsproHalfRight()


    def respawnZapValidator(self):
        """ overrides
        redéfinit self.zapValidatorBase (qui n'est pas bien nommé, au passage) """
        if self.nbZapMade < len(self.listZapConstraint):
            tupleZapInfo = self.listZapConstraint[self.nbZapMade]
            brouzouf, sugar = tupleZapInfo
            param = (self.arena, brouzouf, sugar)
            self.zapValidatorBase = ZapValidatorBase(*param)
        else:
            GameAspirin.respawnZapValidator(self)
        self.nbZapMade += 1

    def zapWin(self):
        """ overrides """
        if self.nbZapMade > len(self.listZapConstraint):
            self.console.addListTextAndDisplay((u"bravooo !!", ))
