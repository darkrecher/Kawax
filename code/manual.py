#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax
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
