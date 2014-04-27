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
        "tuto_03_01",
        {
            LANGUAGE_FRENCH : (
                u"Ah T'es encore là ?",
                u"C'est bien, t'es un bon",
                u"petit soldat.",
            ),
            LANGUAGE_ENGLISH : (
                u"Hi. Still there ?",
                u"Fine. You are a good",
                u"little soldier.",
            )
        },
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        "tuto_03_02",
        {
            LANGUAGE_FRENCH : (
                u"Les 2 machins au milieu",
                u"de l'écran, ce sont",
                u"des cachets d'aspirine.",
                u"Il faut les coller ",
                u"ensemble.",
            ),
            LANGUAGE_ENGLISH : (
                u"The two white crappies,",
                u"in the middle of",
                u"the screen, are",
                u"half-aspirin pills.",
                u"You have to",
                u"assemble them.",
            )
        },
        (),
        False
    ),(
        STEP_COND_SELECT_TILES,
        ((4, 8), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (6, 5), (6, 6)),
        "tuto_03_03",
        {
            LANGUAGE_FRENCH : (
                u"Tu vas commencer par me",
                u"péter tout ça.",
            ),
            LANGUAGE_ENGLISH : (
                u"Begin by zapping",
                u"all that stuff.",
            )
        },
        ((4, 8), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (6, 5), (6, 6)),
        False
    ),(
        STEP_COND_STIM,
        (),
        "tuto_03_04",
        {
            LANGUAGE_FRENCH : (
                u"Ouaf ouaf, gruuiik",
                u"grruuuiiiikk ! Teuheu !",
                u"Pardon. Où on en étais ?",
                u"Oui euh... Cliquez sur",
                u"Suivant, comme d'hab'.",
            ),
            LANGUAGE_ENGLISH : (
                u"Woof woof, uuiirrk",
                u"uiiirrk ! Cough cough !",
                u"Sorry. What was I",
                u"saying ? Oh yes...",
                u"press the 'F' key,",
                u"as usual",
            )
        },
        (),
        False
    ),(
        STEP_COND_SELECT_TILES,
        ((5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9)),
        "tuto_03_05",
        {
            LANGUAGE_FRENCH : (
                u"Et maintenant, pète-moi",
                u"ça, histoire de vider la",
                u"colonne. Et tu regardes",
                u"bien ce que ça fait,",
                u"jeune boulawan.",
            ),
            LANGUAGE_ENGLISH : (
                u"Now, zap these tiles,",
                u"to empty the column.",
                u"And look carefully at",
                u"what will happen,",
                u"young Shitwalker.",
            )
        },
        ((5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 9), (7, 9)),
        False
    ),(
        STEP_COND_STIM,
        (),
        "tuto_03_06",
        {
            LANGUAGE_FRENCH : (
                u"Et hop. Ca s'est déplacé",
                u"vers la gauche.",
                u"C'est-y pas top foufoutre",
                u"au carré, ça ? Hmmm ?",
            ),
            LANGUAGE_ENGLISH : (
                u"Whoa ! It moved",
                u"to the left.",
                u"Isn't that squared",
                u"dibbly-didum-cool ? Hmm ?",
            )
        },
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        "tuto_03_07",
        {
            LANGUAGE_FRENCH : (
                u"Sauf que maintenant,",
                u"les aspirines ne sont",
                u"plus en face.",
            ),
            LANGUAGE_ENGLISH : (
                u"But now, the aspirins",
                u"are not on the",
                u"same line any more.",
            )
        },
        (),
        False
    ),(
        STEP_COND_SELECT_TILES,
        ((4, 7), (4, 8)),
        "tuto_03_08",
        {
            LANGUAGE_FRENCH : (
               u"Dégomme-moi ce bazar.",
            ),
            LANGUAGE_ENGLISH : (
                u"Zap that crap.",
            )
        },
        ((4, 7), (4, 8)),
        False
    ),(
        STEP_COND_INTERACTIVE_TOUCH_SUCCESSED,
        (),
        "tuto_03_09",
        {
            LANGUAGE_FRENCH : (
                u"Bien, petit stagiaire.",
                u"Maintenant, tu vas ",
                u"cliquer sur l'un des ",
                u"demi-cachets.",
            ),
            LANGUAGE_ENGLISH : (
                u"Weeell doooone, little",
                u"traineeeeee. Now,",
                u"click on one of the",
                u"half-pill.",
            )
        },
        (),
        False
    ),(
        STEP_COND_INTERACTIVE_TOUCH_SUCCESSED,
        (),
        "tuto_03_10",
        {
            LANGUAGE_FRENCH : (
                u"Et hop, ils se",
                u"réunissent.",
                u"Et pour finir, clique",
                u"sur le cachet entier.",
            ),
            LANGUAGE_ENGLISH : (
                u"Tadaaa ! They merged !",
                u"Click on the full pill",
                u"to finish it.",
            )
        },
        (),
        False
    ),(
        STEP_COND_STIM,
        (),
        "tuto_03_11",
        {
            LANGUAGE_FRENCH : (
                u"Voilà, c'était super.",
                u"J'espère que c'était",
                u"assez pour vous.",
            ),
            LANGUAGE_ENGLISH : (
                u"Well, that's it,",
                u"viewers. Was it",
                u"enough for you ?",
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
