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

from common import (pyRectTuple,
                    SELTYPE_NONE, SELTYPE_PATH, SELTYPE_SUPPL)


class Tile():
    """
    zob
    """
    def __init__(self, surfaceDest, posArena, posPixel, chip, nbrPlayer):
        """
        zob
        """
        self.surfaceDest = surfaceDest
        self.posPixel = posPixel
        self.posArena = posArena
        self.chip = chip
        self.tutoHighLight = False

        #poucrave. Mais c'est pas grave. Les cl�s vont peut-�tre changer.
        self.dicPlayerSel = {}

        for i in range(nbrPlayer):
            self.dicPlayerSel[i] = SELTYPE_NONE


    def draw(self):
        """
        zob
        """
        #ici le dessin de la tile.dans une img de r�serve, ou pas.
        imgChipToDraw = self.chip.getImgToDraw()

        if imgChipToDraw is not None:
            self.surfaceDest.blit(imgChipToDraw, self.posPixel)

        #� l'arrache
        if self.dicPlayerSel[0] <> SELTYPE_NONE or self.tutoHighLight:

            #TRODO : dico selon la couleur du joueur. et arr�ter les conneries avec le highlight
            if self.tutoHighLight:
                colorSelection = (0, 255, 255)
            elif self.dicPlayerSel[0] == SELTYPE_PATH:
                colorSelection = (255, 0, 0)
            else:
                colorSelection = (255, 150, 0)

            rectSelection = pyRectTuple(self.posPixel.topleft, (31, 31))

            param = (self.surfaceDest, colorSelection, rectSelection, 1)
            pygame.draw.rect(*param)

            #mega larrache (carr� de clignotement plus �pais que les autres.
            if self.tutoHighLight:
                rectSelection.move_ip((1, 1))
                param = (self.surfaceDest, colorSelection, rectSelection, 1)
                pygame.draw.rect(*param)
                rectSelection.move_ip((-2, -2))
                param = (self.surfaceDest, colorSelection, rectSelection, 1)
                pygame.draw.rect(*param)

    def isSelectable(self):
        """
        zob
        """
        return self.chip.isSelectable()


    def selectionChange(self, idPlayer, selectionType):
        """
        ex�cut�e par le code ext�rieur
        """
        self.dicPlayerSel[idPlayer] = selectionType


    def zap(self, zapType, zapForce):
        """
        zob
        """
        return self.chip.zap(zapType, zapForce)