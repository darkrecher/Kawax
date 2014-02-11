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

import pygame

# en nombre de cycles
BLINK_PERIOD = 10
BLINK_DURATION = BLINK_PERIOD * 15


class Blinker():
    """
    classe pour faire clignoter des tiles. Pour le tutorial.
    on ne peut faire clignoter qu'un groupe de Tile. Si il en faut plusieurs,
    y'a qu'à faire plusieurs blinker. Et de toutes façons j'ai pas besoin de ça.
    """
    def __init__(self, arena):
        """
        zob
        """
        self.arena = arena
        self.blinkTimer = 0
        self.blinkValue = False
        self.listTileBlinking = []
        self.isBlinking = False


    def startBlink(self, listPosToBlink):
        """
        listPosToBlink : liste de pyRect.
        """
        # eteignage des blinks, si ils étaient alllumés
        if self.blinkValue:
            for tile in self.listTileBlinking:
                tile.tutoHighLight = False
        # remise à zéro de la liste de blink
        self.listTileBlinking = []
        self.blinkTimer = BLINK_DURATION
        self.blinkValue = True
        # construction de la nouvelle liste de blink.
        for posArenaToBlink in listPosToBlink:
            tile = self.arena.getTile(posArenaToBlink)
            self.listTileBlinking.append(tile)
            tile.tutoHighLight = self.blinkValue

        self.isBlinking = True


    def stopBlink(self):
        for tile in self.listTileBlinking:
            tile.tutoHighLight = False
        self.listTileBlinking = []
        self.isBlinking = False


    def advanceTimerAndHandle(self):
        """
        zob
        """
        if not self.isBlinking:
            return
        # decrementer le compteur.
        self.blinkTimer -= 1
        # stopBlink si compteur arrive à 0
        if self.blinkTimer == 0:
            self.stopBlink()
            return
        # inverser blinkValue si on tombe sur modulo la période.
        if self.blinkTimer % BLINK_PERIOD == 0:
            self.blinkValue = not self.blinkValue
            # réactualiser les highlight
            for tile in self.listTileBlinking:
                tile.tutoHighLight = self.blinkValue
