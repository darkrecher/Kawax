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
from blinker  import Blinker
from zapvalid import ZapValidatorBase
from tutorial import (TutorialScheduler,
                      STEP_COND_NEVER, STEP_COND_STIM, STEP_COND_SELECT_TILES,
                      COLOR_TUTORIAL)

LIST_TUT_STEP_DESCRIP = (
    (
        STEP_COND_STIM,
        (),
        u"tuto_01_01",
        {
            LANGUAGE_FRENCH : (
                u"Bienvenue dans le premier",
                u"tutoriel de Kawax.",
                u"Appuyez sur",
                u"la touche 'F'.",
            ),
            LANGUAGE_ENGLISH : (
                u"Welcome to the first",
                u"kawax tutorial.",
                u"Press the 'F' key.",
            )
        },
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        u"tuto_01_02",
        {
            LANGUAGE_FRENCH : (
                u"Vous êtes un stagiaire",
                u"d'une quelconque",
                u"grande entreprise.",
                u"Votre chef vous a confié",
                u"son stock de centimes de",
                u"brouzoufs, et vous devez",
                u"lui ramener du café."
            ),
            LANGUAGE_ENGLISH : (
                u"You are a random trainee",
                u"in a random big company.",
                u"Your boss gave you his",
                u"own buck-cent stock.",
                u"You must bring him some",
                u"coffee back.",
            )
        },
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        u"tuto_01_03",
        {
            LANGUAGE_FRENCH : (
                u"Le premier café coûte",
                u"13 centimes.",
                u"Vous devez sélectionner",
                u"un groupe de pièces",
                u"correspondant à cette",
                u"somme.",
            ),
            LANGUAGE_ENGLISH : (
                u"The first coffee costs",
                u"13 buck-cents. You must",
                u"select a group of coins",
                u"corresponding to",
                u"that price.",
            )
        },
        (),
        False
    ),(
        STEP_COND_SELECT_TILES,
        ((2, 3), (3, 3), (3, 4), (3, 5)),
        u"tuto_01_04",
        {
            LANGUAGE_FRENCH : (
                u"Cliquez sur toutes les",
                u"cases clignotantes,",
                u"puis appuyez sur",
                u"la touche 'S'."
            ),
            LANGUAGE_ENGLISH : (
                u"Click all the blinking",
                u"tiles, then press",
                u"the 'S' key.",
            )
        },
        ((2, 3), (3, 3), (3, 4), (3, 5)),
        False
    ),(
        STEP_COND_STIM,
        (),
        u"tuto_01_05",
        {
            LANGUAGE_FRENCH : (
                u"Bravo, vous avez fait",
                u"votre premier café."
            ),
            LANGUAGE_ENGLISH : (
                u"Congratulations, you",
                u"made your first coffee.",
            )
        },
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        u"tuto_01_06",
        {
            LANGUAGE_FRENCH : (
                u"Il existe 2 façons de",
                u"sélectionner les pièces.",
                u"Le chemin principal",
                u"(en rouge), et les",
                u"pièces additionnelles.",
                u"(en orange)"
            ),
            LANGUAGE_ENGLISH : (
                u"Coins can be selected",
                u"by two different ways.",
                u"The main path (red),",
                u"and the additionnal path",
                u"(orange).",
            )
        },

        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        u"tuto_01_07",
        {
            LANGUAGE_FRENCH : (
                u"Le chemin principal",
                u"est créé en premier.",
                u"Il se trace en",
                u"passant sur les pièces,",
                u"avec le bouton",
                u"de la souris appuyé."
            ),
            LANGUAGE_ENGLISH : (
                u"The main path is created",
                u"first, by hovering over",
                u"the coins, while the",
                u"mouse button is pressed.",
            )
        },
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        u"tuto_01_08",
        {
            LANGUAGE_FRENCH : (
                u"Les pièces additionnelles",
                u"s'ajoutent en cliquant",
                u"sur une pièce adjacente",
                u"au chemin principal.",
            ),
            LANGUAGE_ENGLISH : (
                u"The additionnal coins",
                u"are added by clicking",
                u"a coin adjacent to the",
                u"main path.",
            )
        },
        (),
        False
    ),(
        STEP_COND_SELECT_TILES,
        ((4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (7, 6)),
        u"tuto_01_09",
        {
            LANGUAGE_FRENCH : (
                u"Essayez de prendre",
                u"toutes ces pièces.",
            ),
            LANGUAGE_ENGLISH : (
                u"Try to take all",
                u"these coins.",
            )
        },
        ((4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (7, 6)),
        False
    ),(
        STEP_COND_STIM,
        (),
        u"tuto_01_10",
        {
            LANGUAGE_FRENCH : (
                u"Félicitations,",
                u"vous êtes un bon",
                u"petit stagiaire.",
            ),
            LANGUAGE_ENGLISH : (
                u"Congratulations,",
                u"you are a good",
                u"little trainee.",
            )
        },
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        u"tuto_01_11",
        {
            LANGUAGE_FRENCH : (
                u"Certains cafés ",
                u"nécessitent d'ajouter",
                u"du sucre. Vous devrez",
                u"sélectionner le nombre",
                u"de morceaux requis, ",
                u"en plus des pièces.",
            ),
            LANGUAGE_ENGLISH : (
                u"Some coffees need",
                u"also some sugar.",
                u"You must select the",
                u"appropriate number of",
                u"sugar lumps, besides.",
                u"the coins.",
            )
        },
        (),
        False
    ),(
        STEP_COND_SELECT_TILES,
        ((7, 7), (8, 7), (9, 7), (8, 8), (7, 9), (8, 9), (9, 9)),
        u"tuto_01_12",
        {
            LANGUAGE_FRENCH : (
                u"Le prochain café coûte",
                u"9 centimes de brouzoufs",
                u"et 2 sucres. Sélectionnez",
                u"les cases indiquées.",
            ),
            LANGUAGE_ENGLISH : (
                u"The next coffee costs",
                u"9 buck-cents, and 2",
                u"sugars. Select the",
                u"highlighted tiles.",
            )
        },
        ((7, 7), (8, 7), (9, 7), (8, 8), (7, 9), (8, 9), (9, 9)),
        False
    ),(
        STEP_COND_STIM,
        (),
        u"tuto_01_13",
        {
            LANGUAGE_FRENCH : (
                u"Bravo, vous avez ",
                u"successifié à votre",
                u"examen d'embauche.",
                u"Chaque fois que vous",
                u"réussirez un café,",
                u"l'objectif suivant",
                u"vous sera spécifié,",
                u"en terme de brouzoufs",
                u"et de nombre de sucres.",
            ),
            LANGUAGE_ENGLISH : (
                u"Awesome ! You succeeded",
                u"at your trainee entry",
                u"test. Each time you make",
                u"a coffee, you will be",
                u"specified the next",
                u"objective, in terms of",
                u"buck-cents and sugar",
                u"lumps.",
            )
        },
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        u"tuto_01_14",
        {
            LANGUAGE_FRENCH : (
                u"Vous pouvez continuer",
                u"à vous entraîner dans",
                u"ce tutoriel.",
                u"Lorsque vous vous",
                u"sentirez suffisament",
                u"monté en compétence,",
                u"essayez les autres",
                u"modes de jeu.",
            ),
            LANGUAGE_ENGLISH : (
                u"You can continue to",
                u"train with that tutorial.",
                u"When you feel",
                u"sufficiently competent,",
                u"quit the game,",
                u"and restart it in ",
                u"the next mode.",
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
    (13, 0),
    (18, 0),
    ( 9, 2),
)

# premier elem : coordonnées
# 2eme elem. "C" ou "S" pour dire si c'est un coin ou un sugar.
#            Et ensuite la valeur en brouzouf du coin, si c'est un coin.
LIST_TILE_TO_HARDDEFINE = (
    # Pour la première sélection
    ((2, 3), ("C", 5)),
    ((3, 3), ("C", 5)),
    ((3, 4), ("C", 2)),
    ((3, 5), ("C", 1)),
    # Pour la 2ème
    ((4, 5), ("C", 2)),
    ((5, 5), ("C", 1)),
    ((6, 5), ("C", 5)),
    ((7, 5), ("C", 1)),
    ((8, 5), ("C", 2)),
    ((9, 5), ("C", 5)),
    ((7, 6), ("C", 2)),
    # Pour la 3ème
    ((7, 7), ("C", 2)),
    ((8, 7), ("C", 2)),
    ((9, 7), ("S", 1)),
    ((8, 8), ("S", 1)),
    ((7, 9), ("C", 2)),
    ((8, 9), ("C", 1)),
    ((9, 9), ("C", 2)),
)

class GameBasicTuto(GameBasic):
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
        GameBasic.__init__(self, surfaceDest, gravityDir, tutorialScheduler)
        self.blinker = Blinker(self.arena)
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
