#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax
"""

import pygame

from common import (pyRect, )
from coins  import CHIP_NOTHING, CHIP_COIN, CHIP_SUGAR, CHIP_CLOPE
import language


class ZapValidator():
    """
    classe qui détermine si on a le droit de zapper une sélection ou pas.
    """

    def __init__(self, arena):
        """
        constructeur. (thx captain obvious)

        entrée :
            surfaceDest : Surface principale de l'écran, sur laquelle s'affiche le jeu.
        """
        self.arena = arena


    def getListStrDescription(self):
        """
        zob
        """
        return (u"contrainte qui fonctionne jamay", )

    def getListStrLastTry(self):
        return (u"je sais pas ce que le joueur a fait avant.")


    def validateZap(self, selPath, selSuppl, selAdj):
        """
        zob
        """
        return False


class ZapValidatorBase(ZapValidator):
    """
    classe qui détermine si on a le droit de zapper une sélection ou pas.
    """

    def __init__(self, arena, brouzoufReq, sugarReq):
        """
        constructeur. (thx captain obvious)

        entrée :
            surfaceDest : Surface principale de l'écran, sur laquelle s'affiche le jeu.
        """
        ZapValidator.__init__(self, arena)
        self.brouzoufReq = brouzoufReq
        self.sugarReq = sugarReq
        self.brouzoufTotal = 0
        self.sugarTotal = 0


    def getListStrDescription(self):
        """
        zob
        """
        if language.languageCurrent == language.LANGUAGE_ENGLISH:
            return (u"objective :",
                    u"buck-cent : %s" % self.brouzoufReq,
                    u"sugar : %s" % self.sugarReq)
        else:
            return (u"objectif :",
                    u"brouzouf : %s" % self.brouzoufReq,
                    u"sucre : %s" % self.sugarReq)


    def getListStrLastTry(self):
        if language.languageCurrent == language.LANGUAGE_ENGLISH:
            return (u"selection :",
                    u"buck-cent : %s" % self.brouzoufTotal,
                    u"sugar : %s" % self.sugarTotal)
        else:
            return (u"sélection de :",
                    u"brouzouf : %s" % self.brouzoufTotal,
                    u"sucre : %s" % self.sugarTotal)


    def validateZap(self, selPath, selSuppl, selAdj):
        """
        zob
        """
        self.brouzoufTotal = 0
        self.sugarTotal = 0

        for posPath in selPath + selSuppl:
            chip = self.arena.getTile(posPath).chip
            self.brouzoufTotal += chip.getBrouzouf()
            self.sugarTotal += chip.getSugar()

        return (self.brouzoufTotal == self.brouzoufReq
                and self.sugarTotal == self.sugarReq)

