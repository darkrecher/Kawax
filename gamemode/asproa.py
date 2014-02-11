#/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Kawax version 0.1

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

import pygame
import random
randRange = random.randrange

from common   import (pyRect, pyRectTuple, adjacenceType,
                      SELTYPE_NONE, SELTYPE_SUPPL, SELTYPE_PATH,
                      ZAP_PATH, ZAP_SUPPL, ZAP_ADJACENT, ZAP_INTERACTIVE,
                      UP, DOWN, LEFT, RIGHT)

from tile     import Tile

from coins    import (Chip, ChipNothing,
                      ChipAsproHalfLeft, ChipAsproHalfRight, ChipAsproFull,
                      CHIP_NOTHING, CHIP_COIN, CHIP_CLOPE, CHIP_SUGAR,
                      CHIP_ASPRO_HALF_LEFT, CHIP_ASPRO_HALF_RIGHT,
                      CHIP_ASPRO_FULL)

from crawler  import ArenaCrawler

from gravmov  import (GravityMovements,
                      IN_GRAVITY_NOT, IN_GRAVITY_PARTLY, IN_GRAVITY_YES)

from randchip import RandomChipGenerator

from arebasic import ArenaBasic


# TRODO : on devrait plus avoir besoin de ça ici. Car l'arena s'en branle de comment elle
# s'affiche.
ARENA_TILE_WIDTH  = 32
ARENA_TILE_HEIGHT = 32

(SKIP_NOT_FALLING_TILE,
 ADVANCE_NOTHING_TILE,
 ADVANCE_CONSEQUENT_TILE,
) = range(3)

# WIP
DEFAULT_LIST_CHIP_GENERATION = (
    ((CHIP_COIN,   0),  5),
    ((CHIP_COIN,   1),  7),
    ((CHIP_COIN,   2), 12),
    ((CHIP_COIN,   5), 12),
    ((CHIP_COIN,  10),  5),
    ((CHIP_SUGAR, ),   10),
)

class ArenaAspirin(ArenaBasic):
    """
    classe qui gère une arène du jeu avec les Tile, les Chips,

    type MVC : Modèle
    TRODO : virer les fonctions d'affichage. Parce que pour l'instant c'est Modèle + Vue,
    et c'est pas bien
    """

    def __init__(self, surfaceDest, posPixelTopLeft, arenaSize, nbrPlayer,
                 listGenInit=DEFAULT_LIST_CHIP_GENERATION,
                 listGenAfterGravity=None):
        """
        constructeur. (thx captain obvious)

        entrée :
            surfaceDest : Surface principale de l'écran, sur laquelle s'affiche le jeu.
                          TRODO : a virer, of course
            posPixelTopLeft : Rect. Position, en pixel, du coin sup gauche de l'arena à l'écran.
            arenaSize : tuple de 2 elem (c'est pas un Rect). (longueur, largeur),
                        en nombre de tile. TRODO : faut un Rect. Plus pratique.
            nbrPlayer : nombre de joueur qui peuvent sélectionner les tiles.
                        (pas trop géré pour l'instant)
        """
        self.initCommonStuff(surfaceDest, posPixelTopLeft,
                             arenaSize, nbrPlayer)

        #rien à foutre là ce truc
        #self.crawlerGravityDefault = ArenaCrawler(self.arenaSize)
        #self.crawlerGravityDefault.config(RIGHT, UP)
        # TRODO : config de gravité à mettre dans un dict
        #self.gravityDir = DOWN
        #self.gravityMovements = GravityMovements()
        self.randomChipGenInit = RandomChipGenerator(listGenInit)
        if listGenAfterGravity is None:
            listGenAfterGravity = listGenInit
        self.randomChipGenAfterGrav = RandomChipGenerator(listGenAfterGravity)
        self.createMatrixTile()
        self.start()
        # TRODO : on pourrait déplacer ces limites durant la partie.
        self.xLimitAsproLeft = self.width/2
        self.xLimitAsproRight = self.width/2 + 1
        self.hasTakenAsproFull = False
        print "aspirin !!!"


    #def start(self):
    #    #degueu
    #    self.getTile(pyRect(7, 2)).chip = ChipAsproHalfLeft()
    #    self.getTile(pyRect(5, 5)).chip = ChipAsproHalfLeft()
    #    self.getTile(pyRect(2, 10)).chip = ChipAsproHalfLeft()
    #    self.getTile(pyRect(10, 1)).chip = ChipAsproHalfRight()
    #    self.getTile(pyRect(11, 3)).chip = ChipAsproHalfRight()
    #    self.getTile(pyRect(12, 1)).chip = ChipAsproHalfRight()


    # Pour ajouter des nouveaux aspirines :
    # gauche à gauche et droite à droite, comme ça, pas de risque de daubage.
    #  ou alors on décale la limite petit à petit. Ca ce sera pour le vrai mode.
    # proba = + 0.6 ou - 0.2 si déséquilibre
    # 0.5 de base. -0.2 pour chaque couple d'aspro en jeu. -O.3 pour un plein.
    # on teste pour left et right. Les 2 peuvent apparaître d'un coup. ou pas.

    # bon c'est donc de la merde. Autre chose :
    # les aspro gauches sont là dès le départ. les droits arrivent.
    # les positions potentielle, c'est du haut jusqu'au l'aspro gauche le plus
    # à droite. on fabrique un aspro droit si y'en a pas.
    # du coup, on crée les aspro un par un. Y'a pas le choix. Pas de pseudo-réaction
    # en chaîne. (Pas grave, on le fera pour autre chose).

    def _getPosPotentialAspro(self, crawlerRegen):
        """
        Sortie :
            tuple de 2 listes de coord X, indiquant où on pourrait poser une
            moitié gauche ou droite d'aspro.
        """
        listPosPotentialAsproLeft = []
        listPosPotentialAsproRight = []
        crawlerRegen.start()
        while crawlerRegen.coP == crawlerRegen.primStart:
            tile = self.getTile(crawlerRegen.posCur)
            if tile.chip.chipType == CHIP_NOTHING:
                coordXCurrent = crawlerRegen.posCur.x
                if coordXCurrent < self.xLimitAsproLeft:
                    listPosPotentialAsproLeft.append(coordXCurrent)
                if coordXCurrent > self.xLimitAsproRight:
                    listPosPotentialAsproRight.append(coordXCurrent)
            crawlerRegen.crawl()

        return (listPosPotentialAsproLeft, listPosPotentialAsproRight)


    def _countNbAspro(self):
        """
        Sortie :
            tuple de 3 elem. (nbre aspro left, right, full)
        """
        DICT_COUNT_FROM_CHIP_TYPE = {
            CHIP_ASPRO_HALF_LEFT : 0,
            CHIP_ASPRO_HALF_RIGHT : 1,
            CHIP_ASPRO_FULL : 2,
        }
        listNbAspro = [0, 0, 0]
        crawlerSimple = ArenaCrawler(self.arenaSize)
        crawlerSimple.config()
        crawlerSimple.start()
        while crawlerSimple.hasMoreToCrawl:
            chipType = self.getTile(crawlerSimple.posCur).chip.chipType
            indexCount = DICT_COUNT_FROM_CHIP_TYPE.get(chipType)
            if indexCount is not None:
                listNbAspro[indexCount] += 1
            crawlerSimple.crawl()
        return listNbAspro


    def _calculateProbaAspro(self, listNbAspro):
        """
        Sortie :
            renvoie un tuple de 2 entiers
        """
        probaAsproLeft = 50
        probaAsproRight = 50
        (nbAsproLeft, nbAsproRight, nbAsproFull) = listNbAspro
        if nbAsproLeft < nbAsproRight:
            probaAsproLeft += 60
            probaAsproRight -= 20
        elif nbAsproLeft > nbAsproRight:
            probaAsproLeft -= 20
            probaAsproRight += 60
        nbCoupleAspro = min(nbAsproLeft, nbAsproRight)
        probaAsproLeft -= nbCoupleAspro * 20
        probaAsproRight -= nbCoupleAspro * 20
        probaAsproLeft -= nbAsproFull * 30
        probaAsproRight -= nbAsproFull * 30
        return (probaAsproLeft, probaAsproRight)


    def _regenerateAsproHalf(self, probaAspro,
                             listPosPotentialAspro, classChipAsproHalf):
        """
        a
        """
        #TRODO : factorize WIP
        if probaAspro <= 0:
            return
        if not len(listPosPotentialAspro):
            return
        if randRange(100) >= probaAspro:
            print "proba fail"
            return
        coordXAspro = random.choice(listPosPotentialAspro)
        # pas très classe la coord Y = 0 en dur.
        tile = self.getTileCoordXY(coordXAspro, 0)
        tile.chip = classChipAsproHalf()
        print "regened aspro ", classChipAsproHalf, " on : ", coordXAspro


    def _regenerateAspro(self, crawlerRegen):
        """
        a
        """
        # calcul des probas avant le calcul des pos potentiels, car les probas peuvent être nulles
        # (voire négatives), alors que y'a très souvent au moins une position potentielle.
        # Pour l'instant, c'est même plus que "très souvent", c'est "toujours".
        listNbAspro = self._countNbAspro()
        print "listNbAspro :", listNbAspro
        tupleProbaAspro = self._calculateProbaAspro(listNbAspro)
        print "tupleProbaAspro : ", tupleProbaAspro
        (probaAsproLeft, probaAsproRight) = tupleProbaAspro
        if probaAsproLeft <= 0 and probaAsproRight <= 0:
            return
        listPosPotAspr = self._getPosPotentialAspro(crawlerRegen)
        listPosPotAsproLeft, listPosPotAsproRight = listPosPotAspr

        param = (probaAsproLeft, listPosPotAsproLeft, ChipAsproHalfLeft)
        self._regenerateAsproHalf(*param)

        param = (probaAsproRight, listPosPotAsproRight, ChipAsproHalfRight)
        self._regenerateAsproHalf(*param)


    def regenerateAllChipsAfterOneGravity(self, crawlerRegen=None):
        """
        warninge : le crawler ne doit pas être None. Même si c'est la val par défaut.
        zob """
        #self._regenerateAspro(crawlerRegen)
        ArenaBasic.regenerateAllChipsAfterOneGravity(self, crawlerRegen)


    def mergeAsproHalf(self, posArena):
        """ zob """
        tileOnPos = self.getTile(posArena)
        if isinstance(tileOnPos.chip, ChipAsproHalfLeft):
            print "thats' hwat !"

            posArenaAdjRight = posArena.move((+1, 0))
            if posArenaAdjRight.x >= self.width:
                return False

            chipOnPosAdjRight = self.getTile(posArenaAdjRight).chip

            if not isinstance(chipOnPosAdjRight, ChipAsproHalfRight):
                print "fail aspro right"
                return False

            print "aspro ok"
            self.zapOnePos(posArenaAdjRight, ZAP_INTERACTIVE, 1)
            tileOnPos.chip = ChipAsproFull()

            return True

        elif isinstance(tileOnPos.chip, ChipAsproHalfRight):

            posArenaAdjLeft = posArena.move((-1, 0))
            if posArenaAdjLeft.x < 0:
                return False

            chipOnPosAdjLeft = self.getTile(posArenaAdjLeft).chip

            if not isinstance(chipOnPosAdjLeft, ChipAsproHalfLeft):
                print "fail aspro left"
                return False

            print "aspro ok"
            self.zapOnePos(posArenaAdjLeft, ZAP_INTERACTIVE, 1)
            tileOnPos.chip = ChipAsproFull()

            return True

        else:

            return False


    def takeAsproFull(self, posArena):
        """ zob """
        chipOnPos = self.getTile(posArena).chip
        if isinstance(chipOnPos, ChipAsproFull):
            self.zapOnePos(posArena, ZAP_PATH, 1)
            self.hasTakenAsproFull = True
            return True
        else:
            return False

    #C'est vraiment le bordel ce code. Oh on s'en fiche. C'est pas grave.
    def getAndResetTakenAsproFull(self):
        """ zob """
        if self.hasTakenAsproFull:
            self.hasTakenAsproFull = False
            return True
        else:
            return False

    def stimuliInteractiveTouch(self, posArena):
        """ zob """
        print "interactive touch on : ", posArena
        #chipInteract = self.getTile(posArena).chip
        #if isinstance(chipInteract, ChipAsproHalfLeft):
        #    print "thats' hwat !"
        if self.mergeAsproHalf(posArena):
            return True
        elif self.takeAsproFull(posArena):
            return True
        else:
            return False


    def determineNbGravityRift(self, selPath, selSuppl):
        """
        zob adjacenceType
        """
        if len(selSuppl) > 0:
            return 0

        nbSelTilePerLine = [0, ] * self.height

        for pos in selPath:
            nbSelTilePerLine[pos.y] += 1

        print "min(nbSelTilePerLine)", min(nbSelTilePerLine)
        return min(nbSelTilePerLine)


    def regenerateAllChipsAfterOneGravity(self, crawlerRegen):
        """
        zob
        j'override, car va falloir ajouter des trucs là dedans.
        (Même si c'est dégueu.)
        """
        ArenaBasic.regenerateAllChipsAfterOneGravity(self, crawlerRegen)


    def removeHalfAsproBottom(self):
        """
        zob
        """
        crawlerBottom = ArenaCrawler(self.arenaSize)
        crawlerBottom.config(UP, RIGHT)
        crawlerBottom.start()
        #le crawler doit avoir un boolean à la con indiquant si on a changé
        #la prim coord ou pas (est-on encore dans la première ligne/col ou pas)

        while crawlerBottom.coP == crawlerBottom.primStart:
            print crawlerBottom.posCur
            tile = self.getTile(crawlerBottom.posCur)
            chipType = tile.chip.chipType
            if chipType in ( CHIP_ASPRO_HALF_LEFT, CHIP_ASPRO_HALF_RIGHT):
                tile.chip = ChipNothing()
            crawlerBottom.crawl()
