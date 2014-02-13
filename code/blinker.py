#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax
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
