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
import random

from common import   (pyRect, isAdjacent, indexInList, isAdjacentList,
                      SELTYPE_PATH, SELTYPE_SUPPL, SELTYPE_NONE)

from arebasic import ArenaBasic


(SELMODE_PATH,
 SELMODE_SUPPL_ADD,
 SELMODE_SUPPL_REMOVE,
 SELMODE_STANDBY,
 SELMODE_FORBIDDEN,
) = range(5)



class Selector():
    """
    zob
    """
    def __init__(self, arena, idPlayer):
        """
        zob
        """
        self.arena = arena
        self.idPlayer = idPlayer
        self.stimuliLocked = False

        #C'est la somme des cases selPath et selSuppl qui fait toute la s�lection.
        #ces deux trucs sont des listes de rect. (listes de pos)
        self.selPath = []
        self.selSuppl = []

        self.selMode = SELMODE_STANDBY


    def setStimuliLock(self, stimuliLock):
        """
        zob
        """
        self.stimuliLocked = stimuliLock


    def selectionChange(self, posArena, selectionType):
        """
        zob
        """
        self.arena.selectionChange(posArena, self.idPlayer, selectionType)


    def getSelType(self, posArena):
        """
        zob
        useless
        """
        return self.arena.getTile(posArena).dicPlayerSel[self.idPlayer]


    def cancelAllSelection(self):
        """
        zob
        """
        for posPath in self.selPath:
            self.selectionChange(posPath, SELTYPE_NONE)

        for posBlock in self.selSuppl:
            self.selectionChange(posBlock, SELTYPE_NONE)

        self.selPath = []
        self.selSuppl = []

        self.selMode = SELMODE_STANDBY


    def isAdjacentSelection(self, posArena):
        """
        zob
        """
        if isAdjacentList(posArena, self.selPath):
            return True

        if isAdjacentList(posArena, self.selSuppl):
            return True

        return False

    def tryToActivatePath(self, posArena):
        """
        zob
        """

        indexPosPath = indexInList(posArena, self.selPath)

        if indexPosPath != -1:

            for posPath in self.selPath[indexPosPath+1:]:
                self.selectionChange(posPath, SELTYPE_NONE)

            self.selPath = self.selPath[:indexPosPath+1]

            if self.selSuppl != []:
                self.unselectTileSupplAlone()

            return True


        elif self.selPath == [] or isAdjacent(posArena, self.selPath[-1]):

            self.selPath.append(posArena)
            self.selectionChange(posArena, SELTYPE_PATH)
            if posArena in self.selSuppl:
                self.selSuppl.remove(posArena)
            return True

        elif isAdjacent(posArena, self.selPath[0]):

            self.selPath.insert(0, posArena)
            self.selectionChange(posArena, SELTYPE_PATH)
            if posArena in self.selSuppl:
                self.selSuppl.remove(posArena)
            return True

        else:

            return False


    def unselectTileSupplAlone(self):
        """
        zob
        """

        #on fait le premier. On le vire de listPosToBeRemoved. On le met dans une liste interm

        #on prend le premier de la liste interm, on fait les adjacents :
        #On les met dans la liste interm�diaire aufuramesure,
        #� condition que : ils soient s�lectionn�s, ils soient pas d�j� dans la liste interm,
        #et pas dans la liste des "totalement termin�s", et ils doivent �tre dans la liste des
        #ToBeRemoved (et on les y vire).

        #quand c'est fait, on vire le premier de la liste interm, et on le met dans les
        #"totalement termin�s"

        #etc jusqu'� ce que plus rien dans liste interm.

        listPosToTreat = list(self.selPath)
        listPosTreated = []
        listPosToBeRemoved = list(self.selSuppl)

        #choper les suppl adjacents au tile courant (qui est suppl ou path, osef)
        #les adjacents sont � traiter. on les enl�ve direct de listToRemove. On sait qu'ils sont
        #connect�s.
        #plus loin dans la boucle, on traitera ces adjacents. On chopera leurs adjacents, qui
        #sont peut �tre encore dans listToRemove.

        #j'esp�re que �a marche. D'apr�s mes tests, oui. Mais on sait jamais.
        while len(listPosToTreat) > 0:

            posCurrent = listPosToTreat.pop(0)

            listCoordAdjacent = ((-1, 0), (+1, 0), (0, -1), (0, +1))

            for coordAdjacent in listCoordAdjacent:
                posAdjacent = posCurrent.move(coordAdjacent)

                #TRODO : s'assurer que les suivants ne sont pas �valu� si y'a un False
                mustBeTreated = all((posAdjacent not in listPosToTreat,
                                     posAdjacent not in listPosTreated,
                                     posAdjacent in listPosToBeRemoved,
                                   ))

                if mustBeTreated:
                    listPosToTreat.append(posAdjacent)
                    listPosToBeRemoved.remove(posAdjacent)

            listPosTreated.append(posCurrent)

        #print "___________ paf"
        #print listPosToBeRemoved
        #print "___________ pif"

        for posToBeRemoved in listPosToBeRemoved:
            self.selectionChange(posToBeRemoved, SELTYPE_NONE)
            self.selSuppl.remove(posToBeRemoved)



    def takeStimuliActivateTile(self, posArena):
        """
        zob
        """

        if self.stimuliLocked:
            return

        tile = self.arena.getTile(posArena)

        #ah faut faire �a autrement peut �tre ?
        #y'a des chip ou des tiles qui r�pondent � des interactives clics.
        if not tile.isSelectable():
            return

        selType = tile.dicPlayerSel[self.idPlayer]

        if self.selMode == SELMODE_STANDBY:

            #print "--", selectionType

            if self.tryToActivatePath(posArena):

                self.selMode = SELMODE_PATH

            elif selType == SELTYPE_SUPPL:

                self.selSuppl.remove(posArena)
                self.selectionChange(posArena, SELTYPE_NONE)
                self.unselectTileSupplAlone()
                self.selMode = SELMODE_SUPPL_REMOVE

            elif self.isAdjacentSelection(posArena):

                self.selSuppl.append(posArena)
                self.selectionChange(posArena, SELTYPE_SUPPL)
                self.selMode = SELMODE_SUPPL_ADD

            else:

                self.cancelAllSelection()

                self.selPath.append(posArena)
                self.selectionChange(posArena, SELTYPE_PATH)
                self.selMode = SELMODE_PATH
                #WIP : l� on r�pond qu'on est revenu � zero. Et donc �a peut
                #faire un interactive clic. (qui peut �ventuellement
                #annuler la s�lection qu'on vient de faire, si c'est un clic
                #qui fait ceci ou cela. oui mais non.

        elif self.selMode == SELMODE_PATH:

            self.tryToActivatePath(posArena)

        elif self.selMode == SELMODE_SUPPL_REMOVE:

            if selType == SELTYPE_SUPPL:
                self.selSuppl.remove(posArena)
                self.selectionChange(posArena, SELTYPE_NONE)
                self.unselectTileSupplAlone()

        elif self.selMode == SELMODE_SUPPL_ADD:

            if selType == SELTYPE_NONE and self.isAdjacentSelection(posArena):
                self.selSuppl.append(posArena)
                self.selectionChange(posArena, SELTYPE_SUPPL)


        #StandBY :

            #si y'a rien dans le Path, (et donc � priori rien dans le suppl non plus)
            #on ajoute au selPath. Et on devient SELMODE_PATH

            #sinon, on essaye le tryToActivatePath.
            #Ca va ajouter ou couper du Path. On devient SELMODE_PATH

            #Sinon, on regarde si on a pris une tile d�j� s�lectionn� dans Suppl.
            #On la d�selectionne. Ca peut provoquer une separation.
            #On devient SELMODE_SUPPL_REMOVE

            #Sinon, on regarde si on a pris une tile adjacente au Path, ou au Suppl.
            #On la s�lectionne. On devient SELMODE_SUPPL_ADD

            #Sinon, on fout tout � la poubelle, on ajoute au SELPATH, et on devient SELMODE_PATH.

        #SELMODE_PATH

            #tryToActivatePath, et c'est tout.

        #SELMODE_SUPPL_REMOVE

            #on d�selectionne si il fait partie du Suppl.
            #Ca peut provoquer une separation.
            #Sinon on ne fait rien.

        #SELMODE_SUPPL_ADD

            #on s�lectionne si pas d�j� s�lectionn�, et adjacente � du Path ou du Suppl.
            #Sinon rien.

        #SELMODE_FORBIDDEN je sais pas encore. On verra plus tard.
        #(en fait ce sera PATH_FORBIDDEN. L'interdiction en mode Suppl n'a pas de cons�quence.)
        #quoi que si. Peut �tre.


    def takeStimuliStandBy(self):
        """
        zob
        """
        if self.stimuliLocked:
            return

        self.selMode = SELMODE_STANDBY

