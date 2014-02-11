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

import random

from common   import pyRect, ZAP_INTERACTIVE

from gravmov  import (GravityMovements,
                      IN_GRAVITY_NOT, IN_GRAVITY_PARTLY, IN_GRAVITY_YES)

from coins    import (ChipBigObject,
                      CHIP_NOTHING, CHIP_COIN, CHIP_SUGAR)

#TRODO peut être à virer
from arebasic import ArenaBasic

from arebigob import ArenaBigObject
from bigobj   import Touillette


LIST_CHIP_GENERATION = (
    ((CHIP_COIN,   0),  5),
    ((CHIP_COIN,   1),  7),
    ((CHIP_COIN,   2), 12),
    ((CHIP_COIN,   5), 12),
    ((CHIP_COIN,  10),  5),
    ((CHIP_SUGAR, ),   10),
)

PROBA_BASE = 45
PROBA_ADD_POS_POTENTIAL = 5
PROBA_ADD_ALREADY_PRESENT = -10



class ArenaTouillette(ArenaBigObject):
    """
    classe qui gère une arène du jeu avec les Tile, les Chips,
    Mais on peut ajouter des big object. Et la gravité les gère correctement.

    type MVC : Modèle
    TRODO : virer les fonctions d'affichage. Parce que pour l'instant c'est Modèle + Vue,
    et c'est pas bien
    """

    def start(self):
        #self.addBigObject(Touillette, pyRect(2, 5))
        self.nbTouilletteRemoved = 0


    def removeBottomTouillette(self):
        """
        zob
        """
        print "removeBottomTouillette"
        listBigObjectToRemove = []

        for bigObject in self.listBigObj:
            print bigObject.posTopLeft.y, " comp ", self.height-1
            if bigObject.posTopLeft.y == self.height-1:
                print "faut enlever une touillette"
                self.nbTouilletteRemoved += 1
                listBigObjectToRemove.append(bigObject)
                for posArena in bigObject.listPosArena:
                    self.zapOnePos(posArena, ZAP_INTERACTIVE, 1)

        if listBigObjectToRemove != []:
            for bigObjToRemove in listBigObjectToRemove:
                self.listBigObj.remove(bigObjToRemove)
            return True
        else:
            return False

    def hasTouilletteInBottom(self):
        for bigObject in self.listBigObj:
            if bigObject.posTopLeft.y == self.height-1:
                return True
        return False

    def regenerateTouillette(self, listPosPotential):
        """ zob """
        # faut déterminer la proba d'apparition d'une (ou plusieurs ?)
        # touillettes.  Ouais nan. Une seule. Ha !
        # proba basse si touillette déjà en jeu
        # proba haute si plusieurs emplacements possible de touillette
        # 0.45 de base. on monte de 0.05 pour chaque emplacement
        # on baisse de 0.1 pour chaque touillette présente

        if listPosPotential == []:
            return

        nbPosPotential = len(listPosPotential)
        nbTouPresent = len(self.listBigObj)

        probaTouillette = sum((PROBA_BASE,
                               PROBA_ADD_POS_POTENTIAL * nbPosPotential,
                               PROBA_ADD_ALREADY_PRESENT * nbTouPresent))

        print listPosPotential, "proba :", probaTouillette

        if random.randrange(100) < probaTouillette:
            posTouillette = random.choice(listPosPotential)
            print "creation a : ", posTouillette
            self.addBigObject(Touillette, posTouillette)


    def regenerateAllChipsAfterOneGravity(self, crawlerRegen=None):
        """ zob """

        if crawlerRegen is None:
            return

        crawlerRegen.start()

        listPosPotential = []
        nbContiguousChipNothing = 0
        T_WIDTH = 5

        while crawlerRegen.coP == crawlerRegen.primStart:
            tile = self.getTile(crawlerRegen.posCur)
            if tile.chip.chipType == CHIP_NOTHING:
                nbContiguousChipNothing += 1
            else:
                nbContiguousChipNothing = 0
            crawlerRegen.crawl()
            if nbContiguousChipNothing >= T_WIDTH:
                newPosPotential = crawlerRegen.posCur.move((-T_WIDTH, 0))
                listPosPotential.append(newPosPotential)

        self.regenerateTouillette(listPosPotential)

        ArenaBigObject.regenerateAllChipsAfterOneGravity(self, crawlerRegen)
