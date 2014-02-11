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

vocab et nommage des variables :

    pos : pygame.Rect, avec les valeurs width et height � 0.
          position d'un truc. (coordonn�es)
    posArena : position d'une case dans l'aire de jeu
    posPixel : position d'un pixel � l'�cran ou dans une Surface
    Quand y'a pos tout seul, c'est par d�faut posArena, en g�n�ral.

    path : liste/tuple de posArena (� priori adjacente) formant un chemin.

    coP : coordonn�e primaire. int
    coS : coordonn�e secondaire. int
    Y'a l'une des coordonn�es qu'est x, l'autre y. Ca d�pend du contexte.
    En g�n�ral, quand on veut parcourir toute les cases d'une arena, pour une raison ou
    une autre, la coordonn�e primaire, c'est celle de la boucle principale,
    et la coordonn�e secondaire, c'est celle de la boucle d'en dessous.

je rentre pas dans les d�tails, parce que ce serait trop long et pas int�ressant pour vous :
Mais j'ai vraiment une vie de merde. Toute ma vie, en entier, c'est de la merde.
"""

import random
import pygame
import pygame.locals
pygl = pygame.locals

from common   import securedPrint
import language
from gambasic import GameBasic
from gamemode.zapcntg  import GameZapCounter
from gamemode.touyettg import GameTouillette
from gamemode.asprog   import GameAspirin
from gamemode.gambtuto import GameBasicTuto
from gamemode.touytuto import GameTouyetteTuto
from gamemode.asprtuto import GameAspirinTuto

from common import fontConsole, pyRect

LIST_INTRO_TEXT_FRENCH = (
    "Appuyez sur la touche correspondant au mode de jeu souhait�.",
    "1 : mode normal - tutoriel",
    "2 : mode normal - jeu",
    "3 : mode touillette - tutoriel",
    "4 : mode touillette - jeu",
    "5 : mode aspirine - tutoriel",
    "6 : mode aspirine - jeu",
    "",
    "E : english.   F : fran�ais",
)

LIST_INTRO_TEXT_ENGLISH = (
    "Press the key corresponding to the chosen game mode.",
    "1 : normal mode - tutorial",
    "2 : normal mode - game",
    "3 : coffee spoon - tutorial",
    "4 : coffee spoon - game",
    "5 : aspirin - tutorial",
    "6 : aspirin - game",
    "",
    "E : english.   F : fran�ais",
)

DICT_GAME_CLASS_FROM_KEY = {
    pygl.K_1 : GameBasicTuto,
    pygl.K_2 : GameZapCounter,
    pygl.K_3 : GameTouyetteTuto,
    pygl.K_4 : GameTouillette,
    pygl.K_5 : GameAspirinTuto,
    pygl.K_6 : GameAspirin,
    # TRIP : ha ha ha, you failed at teaching video game to your son. Blast !
    # TODO : ajouter des touches du pav� num�rique.
}


def displayMainMenu(screen):
    screen.fill((0, 0, 0))
    yposIntroText = 20
    xposIntroText = 20
    first = True
    dictIntroTextFromLanguage = {
        language.LANGUAGE_ENGLISH : LIST_INTRO_TEXT_ENGLISH,
        language.LANGUAGE_FRENCH : LIST_INTRO_TEXT_FRENCH,
    }
    listIntroText = dictIntroTextFromLanguage[language.languageCurrent]
    for introText in listIntroText:
        imgText = fontConsole.render(introText, 0, (255, 255, 255))
        screen.blit(imgText, pyRect(xposIntroText, yposIntroText))
        yposIntroText += 40
        if first:
            first = False
            xposIntroText += 40
            yposIntroText += 30
    pygame.display.flip()


def askGameModeToUser(screen):
    displayMainMenu(screen)
    classGame = None
    clock = pygame.time.Clock()
    while classGame is None:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygl.QUIT:
                raise SystemExit()
            elif event.type == pygl.KEYDOWN:
                classGame = DICT_GAME_CLASS_FROM_KEY.get(event.key)
                if event.key == pygl.K_e:
                    # enregistrement du language actuel dans une variable globale,
                    # � la bourrin. C'est d�gueux, mais je sais pas comment faire mieux.
                    language.languageCurrent = language.LANGUAGE_ENGLISH
                    print "english"
                    displayMainMenu(screen)
                if event.key == pygl.K_f:
                    # enregistrement du language actuel dans une variable globale,
                    # � la bourrin. C'est d�gueux, mais je sais pas comment faire mieux.
                    language.languageCurrent = language.LANGUAGE_FRENCH
                    print "frrrrench"
                    displayMainMenu(screen)
    screen.fill((0, 0, 0))
    return classGame


if __name__ == "__main__":

    securedPrint("coucou")

    #cr�ation de l'objet pygame.Surface, dans laquelle on affichera le jeu, les menus, tout.
    #(cette action cr�e la fen�tre, ou met en plein �cran, selon ce qui a �t� choisi)
    screen = pygame.display.set_mode((640, 480), 0)  #SCREEN_RECT.size, displayOption)

    classGame = askGameModeToUser(screen)
    print classGame

    #cr�ation de la putain de classe qui contient tout le putain de code, et les
    #putains d'initialisations.
    #theFuckingGame = GameBasic(screen)
    #theFuckingGame = GameZapCounter(screen)
    #theFuckingGame = GameTouillette(screen, xyFirstTouillette=(2, 5))
    #theFuckingGame = GameAspirin(screen)
    #theFuckingGame = GameBasicTuto(screen)
    #theFuckingGame = GameTouyetteTuto(screen, xyFirstTouillette=(5, 6))
    #theFuckingGame = GameAspirinTuto(screen)
    theFuckingGame = classGame(screen)
    theFuckingGame.playOneGame()

    pygame.quit()

    securedPrint("tchaw")
