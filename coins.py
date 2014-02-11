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

A priori, le coin est une d�finition "de haut niveau". Les tiles font r�f�rence � un coin.
Elles n'ont pas une copie d'un coin.
Donc y'a une seule instance de coin pour la pi�ce de 1, une seule pour la pi�ce de 2, etc...

Ou pas. Je sais pas encore.

"""

import pygame

from common import crappyFont, pyRect

#Virer �a, et utiliser des isinstance ? Non. Parce que impossible � exporter.
(CHIP_NOTHING,
 CHIP_COIN,
 CHIP_SUGAR,
 CHIP_CLOPE,
 CHIP_BIG_OBJECT,
 CHIP_ASPRO_FULL,
 CHIP_ASPRO_HALF_LEFT,
 CHIP_ASPRO_HALF_RIGHT,
) = range(8)


class Chip():

    """
    classe que c'est un truc.
    """

    def __init__(self, chipType=CHIP_NOTHING, selectable=True,
                 brouzouf=0, sugar=0, acceptGravityMove=True):
        """
        constructeur. (thx captain obvious)

        entr�e :
            Faut conna�tre le nombre de joueur, pour d�finir le dico de qui a s�lectionn�
            nan.
        """
        self.chipType = chipType
        self.selectable = selectable
        self.brouzouf = brouzouf
        self.sugar = sugar
        self.acceptGravityMove = acceptGravityMove


    def getImgToDraw(self):
        """
        zob
        faudra passer en param l'indice de rotation. Ou un truc de ce genre.
        C'est surtout que y'a pas besoin de ce truc ici. (MVC)
        """
        return None


    def isSelectable(self):
        """
        zob
        """
        return self.selectable


    def getChipType(self):
        """
        zob
        """
        return self.chipType


    def getBrouzouf(self):
        """
        zob
        """
        return self.brouzouf


    def getSugar(self):
        """
        zob
        """
        return self.sugar


    def zap(self, zapType, zapForce):
        """
        zob
        """
        #on peut dire None si le zap ne doit pas changer la chip.
        #ou si on a juste fait des changements internes.
        #TRODO : bizarre comme fa�on de faire, non ?
        return ChipNothing()


    def isAcceptGravityMove(self):
        """
        zob
        """
        return self.acceptGravityMove



class ChipCoin(Chip):

    def __init__(self, brouzouf):
        """
        constructeur. (thx captain obvious)

        entr�e :
        """

        Chip.__init__(self, chipType=CHIP_COIN, brouzouf=brouzouf)
        #self.brouzouf = brouzouf

        #tout � l'arrache. Osef.
        self.color = (240, 240, 240)
        self.coinImage = pygame.Surface((32, 32)).convert()

        param = (self.coinImage, self.color, (16, 16), 15, 1)
        pygame.draw.circle(*param)

        textBrouzouf = crappyFont.render(str(brouzouf), 0, self.color)
        posPixelBrouzouf = textBrouzouf.get_rect(center=(16, 16))
        self.coinImage.blit(textBrouzouf, posPixelBrouzouf)


    def getImgToDraw(self):
        """
        zob
        """
        return self.coinImage


class ChipSugar(Chip):

    def __init__(self):
        """
        constructeur. (thx captain obvious)

        entr�e :
        """

        Chip.__init__(self, chipType=CHIP_SUGAR, sugar=1)

        #tout � l'arrache. Osef.
        self.color = (240, 240, 240)
        self.coinImage = pygame.Surface((32, 32)).convert()

        #et �a s'appelle toujours coinImage alors que �a devrait p�. osef
        param = (self.coinImage, self.color, pyRect(4, 3, 24, 24), 1)
        pygame.draw.rect(*param)

        textSugar = crappyFont.render("S", 0, self.color)
        posPixelSugar = textSugar.get_rect(center=(16, 16))
        self.coinImage.blit(textSugar, posPixelSugar)


    def getImgToDraw(self):
        """
        posPixel en param, ou pas ? pour l'instant non.
        """
        return self.coinImage



#crappy name
class ChipClope(Chip):

    def __init__(self):
        """
        constructeur. (thx captain obvious)

        entr�e :
        """

        Chip.__init__(self, chipType=CHIP_CLOPE, selectable=False)

        #tout � l'arrache. Osef.
        self.color = (240, 240, 240)
        self.coinImage = pygame.Surface((32, 32)).convert()

        #et �a s'appelle toujours coinImage alors que �a devrait p�. osef
        param = (self.coinImage, self.color, pyRect(2, 5, 28, 20), 1)
        pygame.draw.rect(*param)

        textSugar = crappyFont.render("M", 0, self.color)
        posPixelSugar = textSugar.get_rect(center=(16, 16))
        self.coinImage.blit(textSugar, posPixelSugar)


    def getImgToDraw(self):
        """
        posPixel en param, ou pas ? pour l'instant non.
        """
        return self.coinImage



class ChipNothing(Chip):

    """
    classe que c'est un truc.
    """

    def __init__(self):
        """
        constructeur. (thx captain obvious)

        entr�e :
            Faut conna�tre le nombre de joueur, pour d�finir le dico de qui a s�lectionn�
            nan.
        """
        Chip.__init__(self, selectable=False)

        #osef aussi. En plus si y'a de la transparence �a marche plus cette affaire.
        self.coinImage = pygame.Surface((32, 32)).convert()


    def getImgToDraw(self):
        """
        zob
        faudra passer en param l'indice de rotation. Ou un truc de ce genre.
        """
        return self.coinImage



class ChipBigObject(Chip):

    """
    classe que c'est la partie d'un gros objay.
    """

    def __init__(self, bigObjectFather):
        """
        constructeur. (thx captain obvious)

        entr�e :
        """
        Chip.__init__(self, chipType=CHIP_BIG_OBJECT, selectable=False)
        self.bigObjectFather = bigObjectFather
        #osef aussi. En plus si y'a de la transparence �a marche plus cette affaire.
        self.coinImage = pygame.Surface((32, 32)).convert()


    def getImgToDraw(self):
        """
        zob
        faudra passer en param l'indice de rotation. Ou un truc de ce genre.
        """
        return self.coinImage


    def zap(self, zapType, zapForce):
        """
        zob
        """
        #on peut dire None si le zap ne doit pas changer la chip.
        return ChipNothing()



class ChipAsproFull(Chip):

    def __init__(self):
        """
        constructeur. (thx captain obvious)

        entr�e :
        """

        Chip.__init__(self, chipType=CHIP_ASPRO_FULL, selectable=False)

        #tout � l'arrache. Osef.
        self.color = (240, 240, 240)
        self.coinImage = pygame.Surface((32, 32)).convert()

        #et �a s'appelle toujours coinImage alors que �a devrait p�. osef
        param = (self.coinImage, self.color, (16, 16), 12, 1)
        pygame.draw.circle(*param)

        param = (self.coinImage, self.color, (16, 5), (16, 27))
        pygame.draw.line(*param)


    def getImgToDraw(self):
        """
        posPixel en param, ou pas ? pour l'instant non.
        """
        return self.coinImage


import math #youpi ! #TRODO a virer evidemment
class ChipAsproHalfLeft(Chip):

    def __init__(self):
        """
        constructeur. (thx captain obvious)

        entr�e :
        """

        Chip.__init__(self, chipType=CHIP_ASPRO_HALF_LEFT, selectable=False)

        #tout � l'arrache. Osef.
        self.color = (240, 240, 240)
        self.coinImage = pygame.Surface((32, 32)).convert()

        #et �a s'appelle toujours coinImage alors que �a devrait p�. osef
        param = (self.coinImage, self.color, pyRect(4, 4, 24, 24), math.pi/2, 3*math.pi/2, 1)
        pygame.draw.arc(*param)

        param = (self.coinImage, self.color, (16, 5), (16, 27))
        pygame.draw.line(*param)


    def getImgToDraw(self):
        """
        posPixel en param, ou pas ? pour l'instant non.
        """
        return self.coinImage


class ChipAsproHalfRight(Chip):

    def __init__(self):
        """
        constructeur. (thx captain obvious)

        entr�e :
        """

        Chip.__init__(self, chipType=CHIP_ASPRO_HALF_RIGHT, selectable=False)

        #tout � l'arrache. Osef.
        self.color = (240, 240, 240)
        self.coinImage = pygame.Surface((32, 32)).convert()

        #et �a s'appelle toujours coinImage alors que �a devrait p�. osef
        param = (self.coinImage, self.color, pyRect(4, 4, 24, 24), 3*math.pi/2, 5*math.pi/2, 1)
        pygame.draw.arc(*param)

        param = (self.coinImage, self.color, (16, 5), (16, 27))
        pygame.draw.line(*param)


    def getImgToDraw(self):
        """
        posPixel en param, ou pas ? pour l'instant non.
        """
        return self.coinImage
