#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax
"""

from common   import (pyRect, pyRectTuple,
                      UP, DOWN, LEFT, RIGHT, NO_SOUND)
from language import LANGUAGE_FRENCH, LANGUAGE_ENGLISH

from console  import Console
from coins    import ChipCoin, ChipSugar
from gambasic import GameBasic
from touyettg import GameTouillette
from blinker  import Blinker
from zapvalid import ZapValidatorBase
from tutorial import (TutorialScheduler,
                      STEP_COND_NEVER, STEP_COND_STIM, STEP_COND_SELECT_TILES,
                      COLOR_TUTORIAL)
from bigobj   import Touillette

LIST_TUT_STEP_DESCRIP = (
    (
        STEP_COND_STIM,
        (),
        u"tuto_02_01",
        {
            LANGUAGE_FRENCH : (
                u"Bienvenue dans le second",
                u"tutoriel de Kawax. ",
                u"Dans ce mode, vous",
                u"devez faire tomber des",
                u"touillettes à café",
                u"en bas de l'aire de jeu.",
            ),
            LANGUAGE_ENGLISH : (
                u"Welcome to the second",
                u"Kawax tutorial.",
                u"In this mode, you have",
                u"to move some coffee",
                u"spoons to the bottom",
                u"of the screen.",
            )
        },
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        u"tuto_02_02",
        {
            LANGUAGE_FRENCH : (
                u"Bon ...",
                u"J'en ai marre de faire",
                u"ma voix pseudo-sexy.",
                u"Alors vous allez faire",
                u"ce que je dis,",
                u"sans pinailler. Ok ?",
            ),
            LANGUAGE_ENGLISH : (
                u"Well...",
                u"I'm fed up with",
                u"making my",
                u"pseudo-sexy voice.",
                u"So, you will just do",
                u"what I tell you, OK ?",
            )
        },
        (),
        False
    ),(
        STEP_COND_SELECT_TILES,
        ((5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (5, 8), (6, 8)),
        u"tuto_02_03",
        {
            LANGUAGE_FRENCH : (
                u"Les cases, là, ",
                u"vous les sélectionnez.",
            ),
            LANGUAGE_ENGLISH : (
                u"Select the",
                u"blink-blinking tiles.",
            )
        },
        ((5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (5, 8), (6, 8)),
        False
    ),(
        STEP_COND_STIM,
        (),
        u"tuto_02_04",
        {
            LANGUAGE_FRENCH : (
               (u"Wouhouuuu !",
                u"Regardez la touillette,",
                u"elle est descendue."),
            ),
            LANGUAGE_ENGLISH : (
                u"Woohooo !",
                u"Look at the spoon,",
                u"it went down.",
            )
        },
        (),
        False
    ),(
        STEP_COND_SELECT_TILES,
        ((7, 8), (8, 8), (9, 8), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9)),
        u"tuto_02_05",
        {
            LANGUAGE_FRENCH : (
               (u"Encore un petit effort,",
                u"feignasse de stagiaire."),
            ),
            LANGUAGE_ENGLISH : (
                u"One more effort,",
                u"you lazy trainee.",
            )
        },
        ((7, 8), (8, 8), (9, 8), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9)),
        False
    ),(
        STEP_COND_STIM,
        (),
        u"tuto_02_06",
        {
            LANGUAGE_FRENCH : (
               (u"Et crac ! La touillette ",
                u"a disparue.",
                u"C'est top foufoutre. "),
            ),
            LANGUAGE_ENGLISH : (
                u"Bing ! the spoon",
                u"disappeared. This is",
                u"so dibbly-didum-cool.",
            )
        },
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        u"tuto_02_07",
        {
            LANGUAGE_FRENCH : (
                u"C'est génial. Et sinon,",
                u"quand vous supprimez ",
                u"des gros tas de pièces,",
                u"d'autre touillettes",
                u"peuvent apparaitre",
                u"en haut de l'écran.",
            ),
            LANGUAGE_ENGLISH : (
                u"Yeah, fun. Oh, and",
                u"when you remove a",
                u"big bunch of coins,",
                u"other spoons can",
                u"appear at the top",
                u"of the screen.",
            )
        },
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        u"tuto_02_08",
        {
            LANGUAGE_FRENCH : (
               (u"Faut que j'y aille,",
                u"j'ai une réunion avec ",
                u"d'autres morceaux de ",
                u"mon cerveau.",
                u"Eclate-toi bien",
                u"jeune boulawan !"),
            ),
            LANGUAGE_ENGLISH : (
                u"I have to go, I got",
                u"a meeting with other",
                u"parts of my brain.",
                u"Have fun, young",
                u"Shitwalker !",
            )
        },
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
    (15, 2),
    (12, 1),
)

# premier elem : coordonnées
# 2eme elem. "C" ou "S" pour dire si c'est un coin ou un sugar.
#            Et ensuite la valeur en brouzouf du coin, si c'est un coin.
LIST_TILE_TO_HARDDEFINE = (
    # Pour la première sélection
    ((5, 7), ("C",10)),
    ((6, 7), ("C", 2)),
    ((7, 7), ("C", 0)),
    ((8, 7), ("S", 1)),
    ((9, 7), ("C", 1)),
    ((5, 8), ("C", 2)),
    ((6, 8), ("S", 1)),
    # pour la deuxième
    ((7, 8), ("C", 2)),
    ((8, 8), ("C", 0)),
    ((9, 8), ("C", 5)),
    ((5, 9), ("C", 2)),
    ((6, 9), ("C", 2)),
    ((7, 9), ("S", 1)),
    ((8, 9), ("C", 1)),
    ((9, 9), ("C", 0)),
)

class GameTouyetteTuto(GameTouillette):
    """
    classe qui gère tout le jeu. ou pas
    """

    def __init__(self, surfaceDest, gravityDir=DOWN, xyFirstTouillette=(5, 6)):
        """
        constructeur. (thx captain obvious)

        entrée :
            surfaceDest : Surface principale de l'écran, sur laquelle s'affiche le jeu.
        """
        tutorialScheduler = TutorialScheduler(LIST_TUT_STEP_DESCRIP)
        self.listTileToHardDefine = LIST_TILE_TO_HARDDEFINE
        param = (self, surfaceDest, gravityDir, tutorialScheduler, xyFirstTouillette)
        GameTouillette.__init__(*param)
        self.blinker = Blinker(self.arena)
        #self.refreshTutoInfo()
        #self.selectorPlayerOne.setStimuliLock(True)
        self.showObjectivesAtStart = False
        self.listZapConstraint = LIST_ZAP_CONSTRAINT
        self.nbZapMade = 0
        # truc spécifique au GameTouillette, que je sais même plus à quoi ça sert
        # bien joué le code dégueulasse.
        self.mustDisplayRemoving = False

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

    def respawnZapValidator(self):
        """ overrides
        redéfinit self.zapValidatorBase (qui n'est pas bien nommé, au passage) """
        if self.nbZapMade < len(self.listZapConstraint):
            tupleZapInfo = self.listZapConstraint[self.nbZapMade]
            brouzouf, sugar = tupleZapInfo
            param = (self.arena, brouzouf, sugar)
            self.zapValidatorBase = ZapValidatorBase(*param)
        else:
            GameBasic.respawnZapValidator(self)
        self.nbZapMade += 1

    def periodicAction(self):
        """ overrides """
        pass
