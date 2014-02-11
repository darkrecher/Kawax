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
"""

import pygame

from common import (pyRect, )

from coins  import CHIP_NOTHING, CHIP_COIN, CHIP_SUGAR, CHIP_CLOPE



class ZapValidator():
    """
    classe qui d�termine si on a le droit de zapper une s�lection ou pas.
    """

    def __init__(self, arena):
        """
        constructeur. (thx captain obvious)

        entr�e :
            surfaceDest : Surface principale de l'�cran, sur laquelle s'affiche le jeu.
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
    classe qui d�termine si on a le droit de zapper une s�lection ou pas.
    """

    def __init__(self, arena, brouzoufReq, sugarReq):
        """
        constructeur. (thx captain obvious)

        entr�e :
            surfaceDest : Surface principale de l'�cran, sur laquelle s'affiche le jeu.
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

