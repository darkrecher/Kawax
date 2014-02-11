#/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Kawax version 1.0

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

from common import fontConsole, pyRect
import language

COLOR_DEFAULT = (255, 255, 255)



class ManualInGame():

    """
    classe qui affiche le manuel du jeu pendant le jeu.
    (Ça affiche la liste des touche)

    type MVC : osef.
    """

    def __init__(
        self, surfaceDest, rectManual, tutorialScheduler,
        fontManual=fontConsole
    ):
        """
        constructeur. (thx captain obvious)
        """
        self.surfaceDest = surfaceDest
        self.rectManual = rectManual
        self.tutorialScheduler = tutorialScheduler
        self.fontManual = fontManual
        self.imgManual = pygame.Surface(self.rectManual.size).convert()

    def refresh(self):
        """ zob """
        # Je convertis le tuple en une liste, parce que je vais faire des pop dessus.
        # Donc faut que je puisse le modifier. 
        manualTexts = list(language.MANUAL_TEXTS[language.languageCurrent])
        self.imgManual.fill((0, 0, 0))
        pygame.draw.rect(self.imgManual, COLOR_DEFAULT, pyRect(0, 0, 340, 127), 2)
        colorToWrite = COLOR_DEFAULT
        textToWrite = manualTexts.pop(0)
        imgText = self.fontManual.render(textToWrite, 0, colorToWrite)
        self.imgManual.blit(imgText, pyRect(10, 5))
        textToWrite = manualTexts.pop(0)
        imgText = self.fontManual.render(textToWrite, 0, colorToWrite)
        self.imgManual.blit(imgText, pyRect(10, 25))
        textToWrite = manualTexts.pop(0)
        imgText = self.fontManual.render(textToWrite, 0, colorToWrite)
        self.imgManual.blit(imgText, pyRect(10, 45))        
        if self.tutorialScheduler is not None:
            textToWrite = manualTexts.pop(0)
            imgText = self.fontManual.render(textToWrite, 0, colorToWrite)
            self.imgManual.blit(imgText, pyRect(10, 85))
            textToWrite = manualTexts.pop(0)
            imgText = self.fontManual.render(textToWrite, 0, colorToWrite)
            self.imgManual.blit(imgText, pyRect(10, 100))
                
        
    def display(self):
        self.surfaceDest.blit(self.imgManual, self.rectManual)
