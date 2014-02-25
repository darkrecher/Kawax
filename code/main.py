#/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax

vocab et nommage des variables :

    pos : pygame.Rect, avec les valeurs width et height à 0.
          position d'un truc. (coordonnées)
    posArena : position d'une case dans l'aire de jeu
    posPixel : position d'un pixel à l'écran ou dans une Surface
    Quand y'a pos tout seul, c'est par défaut posArena, en général.

    path : liste/tuple de posArena (à priori adjacente) formant un chemin.

    coP : coordonnée primaire. int
    coS : coordonnée secondaire. int
    Y'a l'une des coordonnées qu'est x, l'autre y. Ca dépend du contexte.
    En général, quand on veut parcourir toute les cases d'une arena, pour une raison ou
    une autre, la coordonnée primaire, c'est celle de la boucle principale,
    et la coordonnée secondaire, c'est celle de la boucle d'en dessous.

TRIP : je rentre pas dans les détails, parce que ce serait trop long et pas intéressant pour vous :
Mais j'ai vraiment une vie de merde. Toute ma vie, en entier, c'est de la merde.
TRIP : non c'est bon, ça va un peu mieux.
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
    u"Appuyez sur la touche correspondant au mode de jeu souhaité.",
    u"1 : mode normal - tutoriel",
    u"2 : mode normal - jeu",
    u"3 : mode touillette - tutoriel",
    u"4 : mode touillette - jeu",
    u"5 : mode aspirine - tutoriel",
    u"6 : mode aspirine - jeu",
    u"",
    u"E : english.   F : français",
)

LIST_INTRO_TEXT_ENGLISH = (
    u"Press the key corresponding to the chosen game mode.",
    u"1 : normal mode - tutorial",
    u"2 : normal mode - game",
    u"3 : coffee spoon - tutorial",
    u"4 : coffee spoon - game",
    u"5 : aspirin - tutorial",
    u"6 : aspirin - game",
    u"",
    u"E : english.   F : français",
)

DICT_GAME_CLASS_FROM_KEY = {
    pygl.K_1 : GameBasicTuto,
    pygl.K_2 : GameZapCounter,
    pygl.K_3 : GameTouyetteTuto,
    pygl.K_4 : GameTouillette,
    pygl.K_5 : GameAspirinTuto,
    pygl.K_6 : GameAspirin,
    # TRIP : ha ha ha, you failed at teaching video game to your son. Blast !
    pygl.K_KP1 : GameBasicTuto,
    pygl.K_KP2 : GameZapCounter,
    pygl.K_KP3 : GameTouyetteTuto,
    pygl.K_KP4 : GameTouillette,
    pygl.K_KP5 : GameAspirinTuto,
    pygl.K_KP6 : GameAspirin,
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
                    # à la bourrin. C'est dégueux, mais je sais pas comment faire mieux.
                    language.languageCurrent = language.LANGUAGE_ENGLISH
                    displayMainMenu(screen)
                if event.key == pygl.K_f:
                    # enregistrement du language actuel dans une variable globale,
                    # à la bourrin. C'est dégueux, mais je sais pas comment faire mieux.
                    language.languageCurrent = language.LANGUAGE_FRENCH
                    displayMainMenu(screen)
    screen.fill((0, 0, 0))
    return classGame


if __name__ == "__main__":

    securedPrint("coucou")

    #création de l'objet pygame.Surface, dans laquelle on affichera le jeu, les menus, tout.
    #(cette action crée la fenêtre, ou met en plein écran, selon ce qui a été choisi)
    screen = pygame.display.set_mode((640, 480), 0)  #SCREEN_RECT.size, displayOption)

    classGame = askGameModeToUser(screen)

    #création de la putain de classe qui contient tout le putain de code, et les
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
