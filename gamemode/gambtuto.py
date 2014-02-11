#/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Kawax version 1.0

    La page du jeu sur indieDB : http://www.indiedb.com/games/kawax
    Liens vers d'autres jeux sur mon blog : http://recher.wordpress.com/jeux
    Mon twitter : http://twitter.com/_Recher_

    Ce superbe jeu, son code source, ses images, et son euh... contenu sonore est disponible,
    au choix, sous la licence Art Libre ou la licence CC-BY-SA

    Copyright 2010 Réchèr
    Copyleft : cette oeuvre est libre, vous pouvez la redistribuer et/ou la modifier selon les
    termes de la Licence Art Libre. Vous trouverez un exemplaire de cette Licence sur le site
    Copyleft Attitude http://www.artlibre.org ainsi que sur d'autres sites.

    Creative Commons - Paternité - Partage des Conditions Initiales à l'Identique 2.0 France
    http://creativecommons.org/licenses/by-sa/2.0/fr/deed.fr

date de la dernière relecture-commentage : None
"""

from common   import (pyRect, pyRectTuple,
                      UP, DOWN, LEFT, RIGHT)
from language import LANGUAGE_FRENCH, LANGUAGE_ENGLISH

from console  import Console
from coins    import ChipCoin, ChipSugar
from gambasic import GameBasic
from blinker  import Blinker
from zapvalid import ZapValidatorBase
from tutorial import (TutorialScheduler,
                      STEP_COND_NEVER, STEP_COND_STIM, STEP_COND_SELECT_TILES,
                      COLOR_TUTORIAL)

#a l'arrache
NO_SOUND = 0

LIST_TUT_STEP_DESCRIP = (
    (
        STEP_COND_STIM,
        (),
        NO_SOUND,
        {
            LANGUAGE_FRENCH : (
                "Bienvenue dans le premier",
                "tutoriel de Kawax.",
                "Appuyez sur la touche 'F'",
            ),
            LANGUAGE_ENGLISH : (
                "Welcome to the first",
                "kawax tutorial.",
                "Press the 'F' key",
            )
        },
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        NO_SOUND,
#        {
#            LANGUAGE_FRENCH : (
#                "",
#            ),
#            LANGUAGE_ENGLISH : (
#                "",
#            )
#        },
        {
            LANGUAGE_FRENCH : (
                "Vous êtes un stagiaire",
                "dans une quelconque",
                "grande entreprise.",
                "Votre chef vous a confié",
                "son stock de centimes de",
                "brouzoufs, vous devez",
                "lui ramener du café."
            ),
            LANGUAGE_ENGLISH : (
                "You are a random trainee",
                "in a random big company.",
                "Your boss gave you his",
                "own buck-cent stock.",
                "You must bring him some",
                "coffee back.",
            )
        },
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        NO_SOUND,
        {
            LANGUAGE_FRENCH : (
                "Le premier café coûte",
                "13 centimes.",
                "Vous devez sélectionner",
                "un groupe de pièces",
                "correspondant à cette",
                "somme.",
            ),
            LANGUAGE_ENGLISH : (
                "The first coffee costs",
                "13 buck-cents. You must",
                "select a group of coins",
                "corresponding to",
                "that price.",
            )
        },
        (),
        False
    ),(
        STEP_COND_SELECT_TILES,
        ((2, 3), (3, 3), (3, 4), (3, 5)),
        NO_SOUND,
        {
            LANGUAGE_FRENCH : (
                "Cliquez sur toutes les",
                "cases clignotantes,",
                "puis appuyez sur",
                "la touche 'S'."
            ),
            LANGUAGE_ENGLISH : (
                "Click all the blinking",
                "tiles, then press",
                "the 'S' key.",
            )
        },
        ((2, 3), (3, 3), (3, 4), (3, 5)),
        False
    ),(
        STEP_COND_STIM,
        (),
        NO_SOUND,
        {
            LANGUAGE_FRENCH : (
                "Bravo, vous avez fait",
                "votre premier café."
            ),
            LANGUAGE_ENGLISH : (
                "Congratulation, you",
                "made your first coffee.",
            )
        },
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        NO_SOUND,
        {
            LANGUAGE_FRENCH : (
                "Il existe 2 façons de",
                "sélectionner les pièces.",
                "Le chemin principal",
                "(en rouge), et les",
                "pièces additionnelles.",
                "(en orange)"
            ),
            LANGUAGE_ENGLISH : (
                "Coins can be selected",
                "by two different ways.",
                "The main path (red),",
                "and the additionnal path",
                "(orange).",
            )
        },
        
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        NO_SOUND,
        {
            LANGUAGE_FRENCH : (
                "Le chemin principal",
                "est créé en premier.",
                "Il se trace en",
                "passant sur les pièces,",
                "avec le bouton",
                "de la souris appuyé."
            ),
            LANGUAGE_ENGLISH : (
                "The main path is created",
                "first, by hovering over",
                "the coins, with the mouse",
                "button pressed",
            )
        },        
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        NO_SOUND,
        ("Les pièces additionnelles",
         "s'ajoutent en cliquant",
         "sur une pièce adjacente",
         "au chemin principal."),
        (),
        False
    ),(
        STEP_COND_SELECT_TILES,
        ((4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (7, 6)),
        NO_SOUND,
        ("Essayez de prendre",
         "toutes ces pièces."),
        ((4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (7, 6)),
        False
    ),(
        STEP_COND_STIM,
        (),
        NO_SOUND,
        ("Félicitations,",
         "vous êtes un bon",
         "petit stagiaire."),
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        NO_SOUND,
        ("Certains cafés ",
         "nécessitent d'ajouter",
         "du sucre. Vous devrez",
         "sélectionner le nombre",
         "de morceaux requis, ",
         "en plus des pièces."),
        (),
        False
    ),(
        STEP_COND_SELECT_TILES,
        ((7, 7), (8, 7), (9, 7), (8, 8), (7, 9), (8, 9), (9, 9)),
        NO_SOUND,
        ("Le prochain café coûte",
         "9 centimes de brouzoufs",
         "et 2 sucres. Sélectionnez",
         "les cases indiquées."),
        ((7, 7), (8, 7), (9, 7), (8, 8), (7, 9), (8, 9), (9, 9)),
        False
    ),(
        STEP_COND_STIM,
        (),
        NO_SOUND,
        ("Bravo, vous avez ",
         "successifié à votre",
         "examen d'embauche.",
         "Chaque fois que vous",
         "réussirez un café,",
         "l'objectif suivant",
         "vous sera spécifié,",
         "en terme de brouzoufs",
         "et de nombre de sucres."),
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        NO_SOUND,
        ("Vous pouvez continuer",
         "à vous entraîner dans",
         "ce tutoriel.",
         "Lorsque vous vous",
         "sentirez suffisament",
         "monté en compétence,",
         "appuyez sur le bouton",
         "'Terminer' pour initier",
         "le premier niveau."),
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

    def zapWin(self):
        """ overrides """
        if self.nbZapMade > len(self.listZapConstraint):
            self.console.addListTextAndDisplay(("bravooo !!", ))
