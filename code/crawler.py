#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax
"""

import pygame

from common import (pyRect, pyRectTuple, UP, DOWN, LEFT, RIGHT)

class ArenaCrawler():
    """
    classe qui parcourt une matrice en 2D, dans tous les sens qu'on veut. Yeah

    trip/ Je voulais contrebalancer le truc. Je sais pas si c'était une bonne idée.
    C'est bizarre cette histoire de poisson quand même. Toujours un problème d'équité.
    """

    def __init__(self, arenaSize):
        """
        constructeur. (thx captain obvious)
        L'aïle

        entrée :

        """
        self.arenaSize = arenaSize #tuple de 2 val. Not a rect
        self.width = self.arenaSize[0]
        self.height = self.arenaSize[1]

        self.DICT_DIR_CONF = {
            RIGHT : (0, self.width,     (+1, 0)),
            LEFT  : (self.width-1,  -1, (-1, 0)),
            DOWN  : (0, self.height,    (0, +1)),
            UP    : (self.height-1, -1, (0, -1)),
        }

        #On pige que d'alle. C'est pas grave.

        self.DICT_CRAWL_CONFIGURATION = {}

        LIST_DIR_ID_PRIM_Y = ((DOWN, RIGHT), (DOWN, LEFT),
                              (UP, RIGHT), (UP, LEFT))

        LIST_DIR_ID_PRIM_X = ((RIGHT, DOWN), (RIGHT, UP),
                              (LEFT, DOWN), (LEFT, UP))

        self._fillDictCrawlConfiguration(False, LIST_DIR_ID_PRIM_Y)
        self._fillDictCrawlConfiguration(True, LIST_DIR_ID_PRIM_X)
        # TRODO : init les trucs à None.
        self.hasMoreToCrawl = None


    def _fillDictCrawlConfiguration(self, isPrimX, listDirectionId):
        """ grab """
        for directionId in listDirectionId:
            primDir, secDir = directionId
            crawlConfigPrim = self.DICT_DIR_CONF[primDir]
            crawlConfigSec = self.DICT_DIR_CONF[secDir]
            crawlConfig = (isPrimX, ) + crawlConfigPrim + crawlConfigSec
            self.DICT_CRAWL_CONFIGURATION[directionId] = crawlConfig


    def config(self, primDir=LEFT, secDir=DOWN):
        """
        zob
        ça devrait pas être RIGHT la primDir par défaut
        """
        #Si la clé est pas bonne, ça pète. C'est ce qu'on veut.
        crawlConfig = self.DICT_CRAWL_CONFIGURATION[(primDir, secDir)]

        (self.isPrimX, self.primStart, self.primEnd, self.primMove,
         self.secStart, self.secEnd, self.secMove
        ) = crawlConfig

        if self.isPrimX:
            self.PrimSecFromPos = self.funcPrimSecFromPosPrimIsX
            self.PosFromPrimSec = self.funcPosFromPrimSecPrimIsX
            self.prevPrimSecFromPos = self.funcPrevPrimSecFromPosPrimIsX
        else:
            self.PrimSecFromPos = self.funcPrimSecFromPosPrimIsY
            self.PosFromPrimSec = self.funcPosFromPrimSecPrimIsY
            self.prevPrimSecFromPos = self.funcPrevPrimSecFromPosPrimIsY


    def setPrimCoord(self, primCoord):
        self.coP = primCoord
        self.coS = self.secStart
        self.PosFromPrimSec()

        self.coord = self.posCur.topleft
        self.posOnStartPrim = pyRectTuple(self.coord)
        self.posPrev = None
        self.crawledOnPrimCoord = True


    def setSecCoord(self, secCoord):
        self.coS = secCoord
        self.PosFromPrimSec()

        self.coord = self.posCur.topleft
        self.posPrev = None
        self.crawledOnPrimCoord = False


    def start(self):
        self.setPrimCoord(self.primStart)
        self.hasMoreToCrawl = True


    def funcPrimSecFromPosPrimIsX(self):
        """ zob """
        self.coP, self.coS = self.posCur.topleft
        self.coordPrim, self.coordSec = self.coP, self.coS

    def funcPrimSecFromPosPrimIsY(self):
        """ zob """
        self.coS, self.coP = self.posCur.topleft
        self.coordPrim, self.coordSec = self.coP, self.coS

    def funcPosFromPrimSecPrimIsX(self):
        """ azeddf"""
        self.posCur = pyRect(self.coP, self.coS)

    def funcPosFromPrimSecPrimIsY(self):
        """ azeddf"""
        self.posCur = pyRect(self.coS, self.coP)

    def funcPrevPrimSecFromPosPrimIsX(self):
        """ sdfsdf """
        self.prevPrim, self.prevSec = self.posPrev.topleft

    def funcPrevPrimSecFromPosPrimIsY(self):
        """ sdfsdf """
        self.prevSec, self.prevPrim = self.posPrev.topleft

    def _crawlOnPrimCoord(self):
        """
        zob
        """
        self.posOnStartPrim.move_ip(self.primMove)
        self.coord = self.posOnStartPrim.topleft
        self.posCur = pyRectTuple(self.coord)
        self.crawledOnPrimCoord = True
        self.PrimSecFromPos()
        self.hasMoreToCrawl = (self.coP != self.primEnd)


    def jumpOnPrimCoord(self):
        """
        zob
        """
        self.posPrev = pygame.Rect(self.posCur)
        self._crawlOnPrimCoord()
        return self.hasMoreToCrawl


    def crawl(self):
        """ zob """
        self.posPrev = pygame.Rect(self.posCur)
        self.prevPrimSecFromPos()
        self.posCur.move_ip(self.secMove)
        self.PrimSecFromPos()
        if self.coS == self.secEnd:
            self._crawlOnPrimCoord()
        else:
            self.crawledOnPrimCoord = False
        return self.hasMoreToCrawl

#-------------------------------------------------------------------

if __name__ == "__main__":

    print "--------------- POUR PIGER COMMENT CA MARCHE --------------"

    aC = ArenaCrawler( (3, 5) )  # X=3, Y=5
    aC.config(DOWN, RIGHT)
    aC.start()
    print "current :", aC.posCur, "previous :", aC.posPrev
    print "prim :", aC.coP, "sec : ", aC.coS,
    print "bigCrawl", aC.crawledOnPrimCoord

    aC.crawl()
    print "current :", aC.posCur, "previous :", aC.posPrev
    print "prim :", aC.coP, "sec : ", aC.coS,
    print "bigCrawl", aC.crawledOnPrimCoord

    aC.jumpOnPrimCoord()
    print "current :", aC.posCur, "previous :", aC.posPrev
    print "prim :", aC.coP, "sec : ", aC.coS,
    print "bigCrawl", aC.crawledOnPrimCoord

    aC.jumpOnPrimCoord()
    print "current :", aC.posCur, "previous :", aC.posPrev
    print "prim :", aC.coP, "sec : ", aC.coS,
    print "bigCrawl", aC.crawledOnPrimCoord

    aC.crawl()
    print "current :", aC.posCur, "previous :", aC.posPrev
    print "prim :", aC.coP, "sec : ", aC.coS,
    print "bigCrawl", aC.crawledOnPrimCoord

    aC.crawl()
    print "current :", aC.posCur, "previous :", aC.posPrev
    print "prim :", aC.coP, "sec : ", aC.coS,
    print "bigCrawl", aC.crawledOnPrimCoord

    aC.crawl()
    print "current :", aC.posCur, "previous :", aC.posPrev
    print "prim :", aC.coP, "sec : ", aC.coS,
    print "bigCrawl", aC.crawledOnPrimCoord

    aC.crawl()
    print "current :", aC.posCur, "previous :", aC.posPrev
    print "prim :", aC.coP, "sec : ", aC.coS,
    print "bigCrawl", aC.crawledOnPrimCoord

    aC.jumpOnPrimCoord()
    print "current :", aC.posCur, "previous :", aC.posPrev
    print "prim :", aC.coP, "sec : ", aC.coS,
    print "bigCrawl", aC.crawledOnPrimCoord

    res = aC.jumpOnPrimCoord()  # La fonction renvoie False. On doit s'arrêter là.
    print "res :", res
    # Les infos récupérées ici ne sont pas valides, et ne correspondent pas à de vraies positions.
    print "current :", aC.posCur, "previous :", aC.posPrev
    print "prim :", aC.coP, "sec : ", aC.coS,
    print "bigCrawl", aC.crawledOnPrimCoord

    print "--------------- TESTS --------------"

    # TRODO : faut inverser tout ces tests. Le crawl est à la fin.
    # Bien joué !!!
    aC = ArenaCrawler((3, 7))
    aC.config(RIGHT, UP)
    aC.start()

    verifX = (0, 1, 2)
    verifY = (6, 5, 4, 3, 2, 1, 0)
    verifXY = []

    for X in verifX:
        listSecMove = [ (X, Y) for Y in verifY ]
        verifXY += listSecMove

    # Je devrais utiliser securedPrint, mais bon, c'est les tests unitaires,
    # osef. De plus, je ne print que des caractères ascii, alors tout va bien.
    print verifXY
    listRectCur = [ pyRectTuple(tupleXY) for tupleXY in verifXY ]
    listRectPrev = [None, ] + listRectCur[:-1]

    indexVerif = 0

    print "current :", aC.posCur, "previous :", aC.posPrev
    print "prim :", aC.coP, "sec : ", aC.coS,
    print "bigCrawl", aC.crawledOnPrimCoord
    print "-" * 10
    assert aC.posCur == listRectCur[indexVerif]
    assert aC.posPrev == listRectPrev[indexVerif]
    assert aC.crawledOnPrimCoord == (aC.posCur.y == 6)
    assert aC.coP == aC.posCur.x
    assert aC.coS == aC.posCur.y

    while aC.crawl():
        print "current :", aC.posCur, "previous :", aC.posPrev
        print "prim :", aC.coP, "sec : ", aC.coS,
        print "bigCrawl", aC.crawledOnPrimCoord
        print "-" * 10
        indexVerif += 1
        assert aC.posCur == listRectCur[indexVerif]
        assert aC.posPrev == listRectPrev[indexVerif]
        assert aC.crawledOnPrimCoord == (aC.posCur.y == 6)
        assert aC.coP == aC.posCur.x
        assert aC.coS == aC.posCur.y


    print "current :", aC.posCur, "previous :", aC.posPrev
    print "prim :", aC.coP, "sec : ", aC.coS,
    print "bigCrawl", aC.crawledOnPrimCoord
    print "-" * 10
    assert indexVerif == len(verifXY)-1
    assert aC.posPrev == listRectCur[-1]
    assert aC.crawledOnPrimCoord == (aC.posCur.y == 6)
    assert aC.coP == aC.posCur.x
    assert aC.coS == aC.posCur.y

    print "--------------- YOUPLA --------------"

    aC = ArenaCrawler((12, 6))
    aC.config(DOWN, LEFT)
    aC.start()

    verifX = (11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
    verifY_1 = (0,)
    verifY_2 = (2, 3, )
    verifXY = []

    for Y in verifY_1:
        listSecMove = [ (X, Y) for X in verifX ]
        verifXY += listSecMove

    listSecMove = [ (X, 1) for X in (11, 10, 9, 8, 7, ) ]
    verifXY += listSecMove

    for Y in verifY_2:
        listSecMove = [ (X, Y) for X in verifX ]
        verifXY += listSecMove

    listSecMove = [ (X, 4) for X in (11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, ) ]
    verifXY += listSecMove

    listSecMove = [ (X, 5) for X in (11, ) ]
    verifXY += listSecMove

    print verifXY
    listRectCur = [ pyRectTuple(tupleXY) for tupleXY in verifXY ]
    listRectPrev = [None, ] + listRectCur[:-1]

    indexVerif = 0

    print "current :", aC.posCur, "previous :", aC.posPrev
    print "prim :", aC.coP, "sec : ", aC.coS,
    print "bigCrawl", aC.crawledOnPrimCoord
    print "-" * 10
    assert aC.posCur == listRectCur[indexVerif]
    assert aC.posPrev == listRectPrev[indexVerif]
    assert aC.crawledOnPrimCoord == (aC.posCur.x == 11)
    assert aC.coP == aC.posCur.y
    assert aC.coS == aC.posCur.x
    crawlContinue = True

    while crawlContinue and aC.crawl():
        print "current :", aC.posCur, "previous :", aC.posPrev
        print "prim :", aC.coP, "sec : ", aC.coS,
        print "bigCrawl", aC.crawledOnPrimCoord
        print "-" * 10
        indexVerif += 1
        assert aC.posCur == listRectCur[indexVerif]
        assert aC.posPrev == listRectPrev[indexVerif]
        assert aC.crawledOnPrimCoord == (aC.posCur.x == 11)
        assert aC.coP == aC.posCur.y
        assert aC.coS == aC.posCur.x
        while aC.posCur in (pyRect(7, 1), pyRect(1, 4), pyRect(11, 5)):
            print "JUMP !!"
            crawlContinue = aC.jumpOnPrimCoord()
            print "current :", aC.posCur, "previous :", aC.posPrev
            print "prim :", aC.coP, "sec :", aC.coS,
            print "bigCrawl :", aC.crawledOnPrimCoord, "cont :", crawlContinue
            print "-" * 10
            if crawlContinue:
                indexVerif += 1
                print listRectPrev[indexVerif]
                assert aC.posCur == listRectCur[indexVerif]
                assert aC.posPrev == listRectPrev[indexVerif]
                assert aC.crawledOnPrimCoord == (aC.posCur.x == 11)
                assert aC.coP == aC.posCur.y
                assert aC.coS == aC.posCur.x

    print "current :", aC.posCur, "previous :", aC.posPrev
    print "prim :", aC.coP, "sec : ", aC.coS,
    print "bigCrawl", aC.crawledOnPrimCoord
    print "-" * 10
    assert indexVerif == len(listRectCur)-1
    assert aC.posPrev == listRectCur[-1]
    assert aC.crawledOnPrimCoord == (aC.posCur.x == 11)
    assert aC.coP == aC.posCur.y
    assert aC.coS == aC.posCur.x

    print "---------- tests OK ------------"


