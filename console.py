#/usr/bin/env python
# -*- coding: utf-8 -*-
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

A priori, le coin est une définition "de haut niveau". Les tiles font référence à un coin.
Elles n'ont pas une copie d'un coin.
Donc y'a une seule instance de coin pour la pièce de 1, une seule pour la pièce de 2, etc...

Ou pas. Je sais pas encore.

"""

import pygame

from common import fontConsole, pyRect

COLOR_DEFAULT = (255, 255, 255)



class Console():

    """
    classe que c'est une console pour afficher du texte.

    type MVC : modèle et vue en même temps. Mais on a le droit, c'est un petit truc de debug
    """

    def __init__(self, surfaceDest, rectConsole, fontConsole=fontConsole,
                 verticalSpace=20, nbCharMax=-1, memory=50):
        """
        constructeur. (thx captain obvious)

        entrée :
            Faut connaître le nombre de joueur, pour définir le dico de qui a sélectionné
            nan.
        """
        self.surfaceDest = surfaceDest
        self.rectConsole = rectConsole
        self.fontConsole = fontConsole
        self.verticalSpace = verticalSpace
        self.nbCharMax = nbCharMax
        self.memory = memory
        self.verticalSpaceMove = (0, self.verticalSpace)
        #tuple : couleur, texte
        self.listColoredText = []
        self.imgConsole = pygame.Surface(self.rectConsole.size).convert()
        self.cursorText = 0
        self.nbMaxLine = self.rectConsole.height / self.verticalSpace


    def addText(self, strText, colorText=COLOR_DEFAULT):
        """ zob """
        if self.nbCharMax != -1:
            while len(strText) > self.nbCharMax:
                coloredText = (tuple(colorText), strText[:self.nbCharMax])
                self.listColoredText.append(coloredText)
                strText = strText[self.nbCharMax:]

        self.listColoredText.append((tuple(colorText), strText))

        #on chope les "self.memory" derniers éléments.
        if len(self.listColoredText) > self.memory:
            self.listColoredText = self.listColoredText[-self.memory:]

        if len(self.listColoredText) > self.nbMaxLine:
            self.cursorText = len(self.listColoredText) - self.nbMaxLine


    def refresh(self):
        """ zob """
        self.imgConsole.fill((0, 0, 0))
        posText = pyRect()

        indexTextEnd = min(len(self.listColoredText),
                           self.nbMaxLine+self.cursorText)

        for coloredText in self.listColoredText[self.cursorText:indexTextEnd]:
            colorToWrite = coloredText[0]
            textToWrite = coloredText[1]
            imgText = self.fontConsole.render(textToWrite, 0, colorToWrite)
            self.imgConsole.blit(imgText, posText)
            posText.move_ip(self.verticalSpaceMove)


    def display(self):
        self.surfaceDest.blit(self.imgConsole, self.rectConsole)


    def moveCursorText(self, dist):

        self.cursorText += dist
        nbTextLines = len(self.listColoredText)
        if nbTextLines > self.nbMaxLine:
            limitUp = nbTextLines - self.nbMaxLine
        else:
            limitUp = nbTextLines - 1

        if self.cursorText < 0:
            self.cursorText = 0
        if self.cursorText > limitUp:
            self.cursorText = limitUp


    def addListTextAndDisplay(self, listStr,
                              colorText=COLOR_DEFAULT, addSeparator=True):
        if addSeparator:
            #default color obligatoire
            self.addText("------")
        for strDescrip in listStr:
            self.addText(strDescrip, colorText)
        self.refresh()
        self.display()

    #alias :
    #self.log = self.addListTextAndDisplay