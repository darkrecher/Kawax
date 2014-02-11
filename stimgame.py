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

# TRODO : a ranger
import random
import pygame
import pygame.locals
pygl = pygame.locals

from common   import (ARENA_SIZE, securedPrint, pyRect, pyRectTuple,
                      FRAME_PER_SECOND, DELAY_GRAVITY,
                      findPathSimple)



class StimuliStockerForGame():
    """
    classe qui chope les stimulis pour que la classe Game les r�cup�re
    type MVC : Vue. (Mais c'est une vue "input", pas une vue "output")
    """

    def __init__(self, posPixelArena, sizeArena, sizePixelTile):
        """
        constructeur. (thx captain obvious)

        entr�e :
        """
        self.posPixelArena = posPixelArena
        self.sizeArena = sizeArena
        self.widthArena, self.heightArena = self.sizeArena
        self.sizePixelTile = sizePixelTile
        self.widthPixelTile, self.heightPixelTile = self.sizePixelTile

        sizePixelArena = (self.widthArena * self.widthPixelTile,
                          self.heightArena * self.heightPixelTile)

        self.rectPixelArena = pyRectTuple(self.posPixelArena.topleft,
                                          sizePixelArena)

        self.posArenaPrevious = None
        self.resetStimuli()


    def resetStimuli(self):
        self.listPosArenaToActivate = []
        self.posArenaToInteractTouch = None
        #zarb ?
        self.stimuliEmptySelection = False
        self.stimuliChangeZapConstraint = False
        self.stimuliTryZap = False
        self.stimuliQuitGame = False
        self.stimuliConsoleScrollUp = False
        self.stimuliConsoleScrollDown = False
        self.mustStandBy = False
        self.stimTutoNext = False
        self.stimReblink = False


    def determinePosArenaMouse(self):
        """
        zob
        phrase � la con : il faudrait enrichir le document XXXX. "Enrichir" c'est nul comme mot.
        Et aussi : la valeur ajout�e du truc, elle est faible.
        trip : On a �vit� le massacre avec le ridal.
        """
        tupleXYposPixelMouse = pygame.mouse.get_pos()
        posPixelMouse = pyRectTuple(tupleXYposPixelMouse)
        self.posArenaMouse = self.posArenaFromPosPixel(posPixelMouse)


    def posArenaFromPosPixel(self, posPixel):
        """
        conversion position en pixel � l'�cran -> position d'une Tile dans l'Ar�ne
        Entr�es : posPixel. Rect. Position en pixel, � l'�cran, de n'importe quel point de la Tile
        Sorties : Soit un Rect : Position de la tile correspondante dans l'ar�ne.
                  Soit None : la position en pixel ne correspond � aucune Tile.
        Donc y'a une verif dans cette fonction. OKay ?

        A mettre dans la View, ou dans le controleur qui va taper dedans ??
        je sais pas si elle a quelque chose � foutre l� cette fonction
        """
        #TRODO : c'est tout pouillave car on fait les calculs avant la verif.
        # Faut inverser. (Et donc conna�tre le coin bas droite de l'Arena.
        #A faire quand on s�parera en MVC comme il faut.
        if self.rectPixelArena.contains(posPixel):

            posX = (posPixel.x - self.rectPixelArena.x) / self.widthPixelTile
            posY = (posPixel.y - self.rectPixelArena.y) / self.heightPixelTile
            posArena = pyRect(posX, posY)
            return posArena

        else:

            return None


    def activateTileWithMouse(self, mustInteractTouch):
        """
        zob
        """
        #TRODO : peut �tre �a, �a passe en param. Et pas chop� ici alarach.
        self.determinePosArenaMouse()

        if self.posArenaMouse is None:
            #pas de mise en stand by quand on quitte l'�cran. C'est chiant.
            #self.selectorPlayerOne.takeStimuliStandBy()
            self.posArenaPrevious = None
            return

        if mustInteractTouch:
            self.posArenaToInteractTouch = self.posArenaMouse

        if self.posArenaPrevious is None:
            self.listPosArenaToActivate.append(self.posArenaMouse)
            self.posArenaPrevious = self.posArenaMouse

        elif self.posArenaPrevious != self.posArenaMouse:

            param = (self.posArenaPrevious, self.posArenaMouse)
            pathSelection = findPathSimple(*param)

            for posSelected in pathSelection:
                self.listPosArenaToActivate.append(posSelected)

            self.posArenaPrevious = self.posArenaMouse

        # si le previous est �gal au current, on ne fait rien ??

        return


    def takeEventsFromMouseAndKeyboard(self):

        mustActivate = False
        mustInteractTouch = False

        for event in pygame.event.get():
            #on quitte la partie si le joueur fait un �v�nement de quittage (alt-F4, ...)
            #et il faudra carr�ment quitter le programme.
            if event.type == pygl.QUIT:
                self.stimuliQuitGame = True

            #Les events MOUSEBUTTONXX correspondent � n'importe quel bouton.
            #A chaque fois, on v�rifie que c'est du bouton gauche dont il s'agit

            elif event.type == pygl.MOUSEBUTTONUP:
                if not pygame.mouse.get_pressed()[0]:
                    self.mustStandBy = True
                    self.posArenaPrevious = None

            elif event.type == pygl.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mustActivate = True
                    mustInteractTouch = True

            elif event.type == pygl.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    mustActivate = True

            elif event.type == pygl.KEYDOWN:

                if event.key == pygl.K_s:
                    self.stimuliTryZap = True

                elif event.key == pygl.K_d:
                    self.stimuliEmptySelection = True

                # Supprim�, car c'est de la triche.
                # (C'�tait pour tester sans que je me fasse chier)
                #elif event.key == pygl.K_p:
                #    self.stimuliChangeZapConstraint = True

                elif event.key == pygl.K_UP:
                    self.stimuliConsoleScrollUp = True

                elif event.key == pygl.K_DOWN:
                    self.stimuliConsoleScrollDown = True

                elif event.key == pygl.K_f:
                    self.stimTutoNext = True

                elif event.key == pygl.K_g:
                    self.stimReblink = True

                elif event.key == pygl.K_l:
                    self.stimuliQuitGame = True

        if mustActivate:
            self.activateTileWithMouse(mustInteractTouch)
