#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax
"""

import pygame

from common   import UP, DOWN, LEFT, RIGHT

(IN_GRAVITY_NOT,
 IN_GRAVITY_PARTLY,
 IN_GRAVITY_YES,
) = range(3)



class GravityMovements():

    def __init__(self, direction=DOWN, primCoordIsX=True,
                 gravIncsCoord=True):
        """
        constructeur. (thx captain obvious)

        entrée :
            surfaceDest : Surface principale de l'écran, sur laquelle s'affiche le jeu.
        """
        self.direction = direction
        self.primCoordIsX = primCoordIsX
        self.gravIncsCoord = gravIncsCoord
        #clé : coord primaire. valeur : liste de tuple de 2 elem :
        #(coord secondaire de début du mouvement, coord secondaire de fin)
        #y'en a une qu'est plus petite que l'autre. Mais on sait pas laquelle.
        #Ca dépend de gravIncsCoord
        self.dicMovement = {}


    def cancelAllMoves(self):
        """niok
        """
        self.dicMovement = {}


    def addSegmentMove(self, primCoord, secCoordStart, secCoordEnd):
        """zob we stay...
        pas de verif de doublon ou de chevauchement. Y'a qu'à juste faire gaffe.
        secCoordEnd n'est pas incluse dans l'application de la gravité. "rangestyle"
        secCoordStart est inclus. Et c'est la chip Nothing sur laquelle va s'écraser l'autre.
        Donc y'a toujours au moins 2 éléments. Et secCoordEnd-secCoordStart >= 2 (osef)
        """
        self.primCoord = primCoord
        self.secCoordStart = secCoordStart
        self.secCoordEnd = secCoordEnd

        if primCoord in self.dicMovement:
            self.dicMovement[primCoord].append([secCoordStart, secCoordEnd])
        else:
            self.dicMovement[primCoord] = [ [secCoordStart, secCoordEnd] ]


    def isInGravity(self, posToTest):
        """
        zob
        """
        if self.primCoordIsX:
            primCoord = posToTest.x
            secCoord = posToTest.y
        else:
            primCoord = posToTest.y
            secCoord = posToTest.x

        listSegmentMove = self.dicMovement.get(primCoord)

        if listSegmentMove is None:
            return False

        if self.gravIncsCoord:
            for segment in listSegmentMove:
                if segment[0] >= secCoord > segment[1]:
                    return True
        else:
            for segment in listSegmentMove:
                if segment[0] <= secCoord < segment[1]:
                    return True

        return False


    def cancelGravity(self, posToCancel):
        """
        zob
        """

        #TRODO : faut factoriser ce bordel avec la fonction du dessus.
        if self.primCoordIsX:
            primCoord = posToCancel.x
            secCoord = posToCancel.y
        else:
            primCoord = posToCancel.y
            secCoord = posToCancel.x

        listSegmentMove = self.dicMovement.get(primCoord)

        if listSegmentMove is None:
            return

        changeOccurred = False
        indexSegment = 0
        lenList = len(listSegmentMove)

        #TRODO : faut factoriser ce bordayl.
        if self.gravIncsCoord:

            while indexSegment < lenList and not changeOccurred:
                segment = listSegmentMove[indexSegment]
                if segment[0] >= secCoord > segment[1]:
                    segment[1] = secCoord
                    changeOccurred = True
                else:
                    indexSegment += 1

            if changeOccurred:
                if segment[1] - segment[0] >= -1:
                    listSegmentMove.pop(indexSegment)

            self.dicMovement[primCoord] = listSegmentMove

        else:

            while indexSegment < lenList and not changeOccurred:
                segment = listSegmentMove[indexSegment]
                if segment[0] <= secCoord < segment[1]:
                    segment[1] = secCoord
                    changeOccurred = True
                else:
                    indexSegment += 1

            if changeOccurred:
                if segment[1] - segment[0] <= +1:
                    listSegmentMove.pop(indexSegment)

            self.dicMovement[primCoord] = listSegmentMove


    def isListInGravity(self, listPosToTest):
        """ zob
        il faut renvoyer une variable IN_GRAVITY, et la liste des tiles dans la grav
        """
        listPosInGravity = [ posToTest for posToTest in listPosToTest
                             if self.isInGravity(posToTest) ]

        if listPosInGravity == []:
            return IN_GRAVITY_NOT, listPosInGravity
        elif len(listPosInGravity) == len(listPosToTest):
            return IN_GRAVITY_YES, listPosInGravity
        else:
            return IN_GRAVITY_PARTLY, listPosInGravity


    def removeEmptyListSegment(self):
        """ d """
        listPrimCoordNoSegment = [ primCoord for primCoord, listSegment
                                   in self.dicMovement.items()
                                   if listSegment == [] ]

        for primCoord in listPrimCoordNoSegment:
            self.dicMovement.pop(primCoord)



#-------------------------------------------------------------------
#test unitaire de GravityMovements
if __name__ == "__main__":

    from common   import pyRect

    # Je devrais utiliser securedPrint, mais bon, c'est les tests unitaires,
    # osef. De plus, je ne print que des caractères ascii, alors tout va bien.
    print " ------- DIR = DOWN --------- "
    gv = GravityMovements()
    gv.addSegmentMove(3, 15, 10)
    gv.addSegmentMove(2, 17, 7)
    gv.addSegmentMove(3, 30, 20)
    gv.addSegmentMove(3, 7, 2)
    print gv.dicMovement
    assert gv.isInGravity(pyRect(2, 9)) == True
    assert gv.isInGravity(pyRect(2, 8)) == True
    assert gv.isInGravity(pyRect(2, 17)) == True
    assert gv.isInGravity(pyRect(2, 7)) == False
    assert gv.isInGravity(pyRect(2, 18)) == False
    assert gv.isInGravity(pyRect(3, 12)) == True
    assert gv.isInGravity(pyRect(3, 9)) == False
    assert gv.isInGravity(pyRect(3, 10)) == False
    assert gv.isInGravity(pyRect(4, 11)) == False

    gv.cancelGravity(pyRect(4, 11))
    assert len(gv.dicMovement.keys()) == 2
    assert gv.dicMovement[2] == [[17, 7]]
    assert gv.dicMovement[3] == [[15, 10], [30, 20], [7, 2]]
    gv.cancelGravity(pyRect(3, 10))
    assert len(gv.dicMovement.keys()) == 2
    assert gv.dicMovement[2] == [[17, 7]]
    assert gv.dicMovement[3] == [[15, 10], [30, 20], [7, 2]]
    gv.cancelGravity(pyRect(2, 7))
    assert len(gv.dicMovement.keys()) == 2
    assert gv.dicMovement[2] == [[17, 7]]
    assert gv.dicMovement[3] == [[15, 10], [30, 20], [7, 2]]
    gv.cancelGravity(pyRect(2, 8))
    print gv.dicMovement
    assert len(gv.dicMovement.keys()) == 2
    assert gv.dicMovement[2] == [[17, 8]]
    assert gv.dicMovement[3] == [[15, 10], [30, 20], [7, 2]]
    gv.cancelGravity(pyRect(2, 11))
    print gv.dicMovement
    assert len(gv.dicMovement.keys()) == 2
    assert gv.dicMovement[2] == [[17, 11]]
    assert gv.dicMovement[3] == [[15, 10], [30, 20], [7, 2]]
    gv.cancelGravity(pyRect(2, 16))
    print gv.dicMovement
    assert len(gv.dicMovement.keys()) == 2
    assert gv.dicMovement[2] == []
    assert gv.dicMovement[3] == [[15, 10], [30, 20], [7, 2]]
    gv.cancelGravity(pyRect(3, 30))
    print gv.dicMovement
    assert len(gv.dicMovement.keys()) == 2
    assert gv.dicMovement[2] == []
    assert gv.dicMovement[3] == [[15, 10], [7, 2]]
    gv.cancelGravity(pyRect(3, 6))
    print gv.dicMovement
    assert len(gv.dicMovement.keys()) == 2
    assert gv.dicMovement[2] == []
    assert gv.dicMovement[3] == [[15, 10]]
    gv.cancelGravity(pyRect(3, 13))
    print gv.dicMovement
    assert len(gv.dicMovement.keys()) == 2
    assert gv.dicMovement[2] == []
    assert gv.dicMovement[3] == [[15, 13]]
    gv.cancelGravity(pyRect(3, 14))
    print gv.dicMovement
    assert len(gv.dicMovement.keys()) == 2
    assert gv.dicMovement[2] == []
    assert gv.dicMovement[3] == []
    gv.removeEmptyListSegment()
    print gv.dicMovement
    assert len(gv.dicMovement.keys()) == 0

    print " ------- DIR = LEFT --------- "
    gv = GravityMovements(LEFT, False, False)
    gv.addSegmentMove(13, 110, 115)
    gv.addSegmentMove(12, 107, 117)
    gv.addSegmentMove(13, 120, 130)
    gv.addSegmentMove(13, 102, 107)
    print gv.dicMovement
    assert gv.isInGravity(pyRect(109, 12)) == True
    assert gv.isInGravity(pyRect(108, 12)) == True
    assert gv.isInGravity(pyRect(117, 12)) == False
    assert gv.isInGravity(pyRect(107, 12)) == True
    assert gv.isInGravity(pyRect(118, 12)) == False
    assert gv.isInGravity(pyRect(112, 13)) == True
    assert gv.isInGravity(pyRect(109, 13)) == False
    assert gv.isInGravity(pyRect(110, 13)) == True
    assert gv.isInGravity(pyRect(111, 14)) == False

    gv.cancelGravity(pyRect(116, 12))
    print gv.dicMovement
    assert len(gv.dicMovement.keys()) == 2
    assert gv.dicMovement[12] == [[107, 116]]
    assert gv.dicMovement[13] == [[110, 115], [120, 130], [102, 107]]
    gv.cancelGravity(pyRect(112, 12))
    print gv.dicMovement
    assert len(gv.dicMovement.keys()) == 2
    assert gv.dicMovement[12] == [[107, 112]]
    assert gv.dicMovement[13] == [[110, 115], [120, 130], [102, 107]]
    gv.cancelGravity(pyRect(108, 12))
    print gv.dicMovement
    assert len(gv.dicMovement.keys()) == 2
    assert gv.dicMovement[12] == []
    assert gv.dicMovement[13] == [[110, 115], [120, 130], [102, 107]]
    gv.cancelGravity(pyRect(120, 13))
    print gv.dicMovement
    assert len(gv.dicMovement.keys()) == 2
    assert gv.dicMovement[12] == []
    assert gv.dicMovement[13] == [[110, 115], [102, 107]]
    gv.cancelGravity(pyRect(112, 13))
    print gv.dicMovement
    assert len(gv.dicMovement.keys()) == 2
    assert gv.dicMovement[12] == []
    assert gv.dicMovement[13] == [[110, 112], [102, 107]]
    gv.cancelGravity(pyRect(111, 13))
    print gv.dicMovement
    assert len(gv.dicMovement.keys()) == 2
    assert gv.dicMovement[12] == []
    assert gv.dicMovement[13] == [[102, 107]]
    gv.removeEmptyListSegment()
    print gv.dicMovement
    assert len(gv.dicMovement.keys()) == 1
    assert gv.dicMovement[13] == [[102, 107]]

    print " ------------ TEST OK -------------- "
