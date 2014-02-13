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
        return ("contrainte qui fonctionne jamay", )


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
        return ("objectif :", "brouzouf : %s" % self.brouzoufReq,
                "sucre : %s" % self.sugarReq)


    def getListStrLastTry(self):
        return ("selection de :", "brouzouf : %s" % self.brouzoufTotal,
                "sucre : %s" % self.sugarTotal)


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

