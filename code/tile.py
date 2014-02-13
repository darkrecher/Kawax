#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax
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

        #poucrave. Mais c'est pas grave. Les clés vont peut-être changer.
        self.dicPlayerSel = {}

        for i in range(nbrPlayer):
            self.dicPlayerSel[i] = SELTYPE_NONE


    def draw(self):
        """
        zob
        """
        #ici le dessin de la tile.dans une img de réserve, ou pas.
        imgChipToDraw = self.chip.getImgToDraw()

        if imgChipToDraw is not None:
            self.surfaceDest.blit(imgChipToDraw, self.posPixel)

        #à l'arrache
        if self.dicPlayerSel[0] <> SELTYPE_NONE or self.tutoHighLight:

            #TRODO : dico selon la couleur du joueur. et arrêter les conneries avec le highlight
            if self.tutoHighLight:
                colorSelection = (0, 255, 255)
            elif self.dicPlayerSel[0] == SELTYPE_PATH:
                colorSelection = (255, 0, 0)
            else:
                colorSelection = (255, 150, 0)

            rectSelection = pyRectTuple(self.posPixel.topleft, (31, 31))

            param = (self.surfaceDest, colorSelection, rectSelection, 1)
            pygame.draw.rect(*param)

            #mega larrache (carré de clignotement plus épais que les autres.
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
        exécutée par le code extérieur
        """
        self.dicPlayerSel[idPlayer] = selectionType


    def zap(self, zapType, zapForce):
        """
        zob
        """
        return self.chip.zap(zapType, zapForce)