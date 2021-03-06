#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax

A priori, le coin est une définition "de haut niveau". Les tiles font référence à un coin.
Elles n'ont pas une copie d'un coin.
Donc y'a une seule instance de coin pour la pièce de 1, une seule pour la pièce de 2, etc...

Ou pas. Je sais pas encore.

"""

import pygame

from common import pyRect, pyRectTuple, loadImg, rectDeplFromDirDist

(BIG_OBJECT_GENERIC,
 BIG_OBJECT_MACHIN,
 BIG_OBJECT_TOUILLETTE,
) = range(3)

class BigObject():
    """
    classe que c'est un truc.
    TRIP:
    "soirée mennthé yo", comme dirait les espagnols dans les chansons.
    strip/ pas d'aveniiiiiiiiir !!!! J'ai pas d'aveniiiiiiiiir !!!!
    """

    def __init__(self, posTopLeft, listPosRel, imgBigObj, typeBigObj):
        """
        constructeur. (thx captain obvious)

        entrée :
        """
        self.posTopLeft = pygame.Rect(posTopLeft)
        self.listPosRel = listPosRel
        self.updatePosArenaWithPosTopLeft()
        self.imgBigObj = imgBigObj
        self.typeBigObj = typeBigObj


    def updatePosArenaWithPosTopLeft(self):
        """ dd """
        self.listPosArena = [ posRel.move(self.posTopLeft.topleft)
                              for posRel in self.listPosRel ]


    def moveCoord(self, coordDepl):
        """ ff """
        self.posTopLeft.move_ip(coordDepl.topleft)
        self.updatePosArenaWithPosTopLeft()


    def moveDirDist(self, dir, dist=1):
        """ ddd """
        rectDepl = rectDeplFromDirDist(dir, dist)
        self.moveCoord(rectDepl)


    def getImgToDraw():
        return self.imgBigObj



class BigMachin(BigObject):

    LIST_COORD_REL = ((0, 0), (1, 0), (2, 0), (1, 1), (2, 1))
    LIST_POS_REL = tuple([ pyRectTuple(coordRel)
                           for coordRel in LIST_COORD_REL ])

    def __init__(self, posTopLeft):
        """ hop """
        #TRODO : complètement à l'arrache
        imgBigMachin = loadImg("machin.png")

        BigObject.__init__(self, posTopLeft,  BigMachin.LIST_POS_REL,
                           imgBigMachin, BIG_OBJECT_MACHIN)



class Touillette(BigObject):

    LIST_COORD_REL = ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0))
    LIST_POS_REL = tuple([ pyRectTuple(coordRel)
                           for coordRel in LIST_COORD_REL ])

    def __init__(self, posTopLeft):
        """ hop """
        #TRODO : complètement à l'arrache
        img = loadImg("touyette.png")

        BigObject.__init__(self, posTopLeft, Touillette.LIST_POS_REL,
                           img, BIG_OBJECT_TOUILLETTE)
