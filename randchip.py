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
import random

from common   import randWithListCoef
                  
from coins    import (Chip, ChipSugar, ChipCoin, ChipClope, ChipNothing,
                      ChipBigObject, 
                      ChipAsproFull, ChipAsproHalfLeft, ChipAsproHalfRight,
                      CHIP_NOTHING, CHIP_COIN, CHIP_SUGAR, CHIP_CLOPE, 
                      CHIP_BIG_OBJECT,
                      CHIP_ASPRO_FULL, CHIP_ASPRO_HALF_LEFT, 
                      CHIP_ASPRO_HALF_RIGHT)


#TRODO : tuple useless ?
DICT_CHIP_CREATION_INFO_FROM_CHIP_TYPE = {
    CHIP_NOTHING : (ChipNothing, ),
    CHIP_COIN : (ChipCoin, ),
    CHIP_SUGAR : (ChipSugar, ),
    CHIP_CLOPE : (ChipClope, ),
    CHIP_BIG_OBJECT : (ChipBigObject, ),
    CHIP_ASPRO_FULL : (ChipAsproFull, ),
    CHIP_ASPRO_HALF_LEFT : (CHIP_ASPRO_HALF_LEFT, ),
    CHIP_ASPRO_HALF_RIGHT : (CHIP_ASPRO_HALF_RIGHT, ),
}

class RandomChipGenerator():
    """
    classe qui crée des Chip au hasard, selon la distribution qu'on veut
    type MVC : Modèle
    """

    def __init__(self, listRandDistribution):
        """
        constructeur. (thx captain obvious)

        entrée :
            dictRandDistribution : blah
        """
        self.listRandDistribution = tuple(listRandDistribution)
        self.listGenInfo = [ elem[0] for elem in self.listRandDistribution ]
        self.listGenCoef = [ elem[1] for elem in self.listRandDistribution ]
        self.listGenCoef = tuple(self.listGenCoef)
        self.listGenInfo = tuple(self.listGenInfo)
    
        
    def _chooseGenInfo(self):
        """ zob """
        indexGenInfoChosen = randWithListCoef(self.listGenCoef)
        genInfo = self.listGenInfo[indexGenInfoChosen]
        return genInfo
    
    
    def chipFromGenInfo(self, genInfo):
        """ zob """
        chipType = genInfo[0]
        chipGenParam = genInfo[1:]
        chipClass = DICT_CHIP_CREATION_INFO_FROM_CHIP_TYPE[chipType][0]
        return chipClass(*chipGenParam)
    
    
    def chooseChip(self):
        """ zob """
        genInfo = self._chooseGenInfo()
        return self.chipFromGenInfo(genInfo)
        
        