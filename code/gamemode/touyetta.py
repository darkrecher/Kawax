#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax
"""

import random

from common   import securedPrint, pyRect, pyRectTuple, ZAP_INTERACTIVE

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
        securedPrint(u"removeBottomTouillette")
        listBigObjectToRemove = []

        for bigObject in self.listBigObj:
            securedPrint(u"%s comp %s" % (
                         unicode(bigObject.posTopLeft.y),
                         unicode(self.height-1)))
            if bigObject.posTopLeft.y == self.height-1:
                securedPrint(u"faut enlever une touillette")
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

        securedPrint(u"%s proba : %s" % (
                     unicode(listPosPotential),
                     unicode(probaTouillette)))

        if random.randrange(100) < probaTouillette:
            posTouillette = random.choice(listPosPotential)
            securedPrint(u"creation a : %s" % posTouillette)
            self.addBigObject(Touillette, posTouillette)


    def regenerateAllChipsAfterOneGravity(self, crawlerRegen=None):
        """ zob """

        if crawlerRegen is None:
            return

        crawlerRegen.start()

        listPosPotential = []
        nbContiguousChipNothing = 0
        T_WIDTH = 5
        list_current_pos = []
        list_is_nothing = []

        # Remplissage initiale de list_current_pos et list_is_nothing.
        for _ in range(T_WIDTH-1):
            list_current_pos.append(pyRectTuple(crawlerRegen.posCur.topleft))
            tile = self.getTile(crawlerRegen.posCur)
            list_is_nothing.append( tile.chip.chipType == CHIP_NOTHING )
            crawlerRegen.crawl()

        while crawlerRegen.coP == crawlerRegen.primStart:

            # On prend. Donc il y a T_WIDTH elem dans les listes.
            list_current_pos.append(pyRectTuple(crawlerRegen.posCur.topleft))
            tile = self.getTile(crawlerRegen.posCur)
            list_is_nothing.append( tile.chip.chipType == CHIP_NOTHING )

            # On teste.
            if all(list_is_nothing):
                newPosPotential = list_current_pos[0]
                listPosPotential.append(newPosPotential)

            # On dépile. Il y a T_WIDTH-1 elem dans les listes.
            list_current_pos.pop(0)
            list_is_nothing.pop(0)

            # On avance. Si on est passé à la ligne suivante,
            # pas la peine de continuer.
            crawlerRegen.crawl()

        self.regenerateTouillette(listPosPotential)

        ArenaBigObject.regenerateAllChipsAfterOneGravity(self, crawlerRegen)
