#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax
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
    # TRODO : wtf. Pourquoi c'est pas des classes dans la valeur ?
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

