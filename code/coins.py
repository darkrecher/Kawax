#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax

A priori, le coin est une définition "de haut niveau". Les tiles font référence à un coin.
Elles n'ont pas une copie d'un coin.
Donc y'a une seule instance de coin pour la pièce de 1, une seule pour la pièce de 2, etc...

Ou pas. Je sais pas encore.

"""

import pygame

from common import crappyFont, pyRect, loadImg

#Virer ça, et utiliser des isinstance ? Non. Parce que impossible à exporter.
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

        entrée :
            Faut connaître le nombre de joueur, pour définir le dico de qui a sélectionné
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
        #TRODO : bizarre comme façon de faire, non ?
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

        entrée :
        """

        Chip.__init__(self, chipType=CHIP_COIN, brouzouf=brouzouf)

        DICT_IMG_FILE_FROM_BROUZOUF = {
            0 : "coin_00.png",
            1 : "coin_01.png",
            2 : "coin_02.png",
            5 : "coin_05.png",
            10: "coin_10.png",
        }
        img_file = DICT_IMG_FILE_FROM_BROUZOUF.get(brouzouf)

        if img_file is not None:
            self.coinImage = loadImg(img_file, colorkey=None)
        else:
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

        entrée :
        """

        Chip.__init__(self, chipType=CHIP_SUGAR, sugar=1)
        # Et ça s'appelle toujours coinImage alors que ça devrait pô. osef
        self.coinImage = loadImg("sugar.png", colorkey=None)

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

        entrée :
        """

        Chip.__init__(self, chipType=CHIP_CLOPE, selectable=False)
        # Et ça s'appelle toujours coinImage alors que ça devrait pô. osef
        self.coinImage = loadImg("rock.png", colorkey=None)


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

        entrée :
            Faut connaître le nombre de joueur, pour définir le dico de qui a sélectionné
            nan.
        """
        Chip.__init__(self, selectable=False)

        #osef aussi. En plus si y'a de la transparence ça marche plus cette affaire.
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

        entrée :
        """
        Chip.__init__(self, chipType=CHIP_BIG_OBJECT, selectable=False)
        self.bigObjectFather = bigObjectFather
        #osef aussi. En plus si y'a de la transparence ça marche plus cette affaire.
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

        entrée :
        """

        Chip.__init__(self, chipType=CHIP_ASPRO_FULL, selectable=False)

        #tout à l'arrache. Osef.
        self.color = (240, 240, 240)
        self.coinImage = pygame.Surface((32, 32)).convert()

        #et ça s'appelle toujours coinImage alors que ça devrait pô. osef
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

        entrée :
        """

        Chip.__init__(self, chipType=CHIP_ASPRO_HALF_LEFT, selectable=False)

        #tout à l'arrache. Osef.
        self.color = (240, 240, 240)
        self.coinImage = pygame.Surface((32, 32)).convert()

        #et ça s'appelle toujours coinImage alors que ça devrait pô. osef
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

        entrée :
        """

        Chip.__init__(self, chipType=CHIP_ASPRO_HALF_RIGHT, selectable=False)

        #tout à l'arrache. Osef.
        self.color = (240, 240, 240)
        self.coinImage = pygame.Surface((32, 32)).convert()

        #et ça s'appelle toujours coinImage alors que ça devrait pô. osef
        param = (self.coinImage, self.color, pyRect(4, 4, 24, 24), 3*math.pi/2, 5*math.pi/2, 1)
        pygame.draw.arc(*param)

        param = (self.coinImage, self.color, (16, 5), (16, 27))
        pygame.draw.line(*param)


    def getImgToDraw(self):
        """
        posPixel en param, ou pas ? pour l'instant non.
        """
        return self.coinImage
