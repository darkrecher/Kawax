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
import random

from common   import (pyRect, pyRectTuple, adjacenceType,
                      SELTYPE_NONE, SELTYPE_SUPPL, SELTYPE_PATH,
                      ZAP_PATH, ZAP_SUPPL, ZAP_ADJACENT, ZAP_INTERACTIVE,
                      UP, DOWN, LEFT, RIGHT)

from tile     import Tile

from coins    import (Chip, ChipNothing,
                      CHIP_NOTHING, CHIP_COIN, CHIP_CLOPE, CHIP_SUGAR)

from crawler  import ArenaCrawler

from gravmov  import (GravityMovements,
                      IN_GRAVITY_NOT, IN_GRAVITY_PARTLY, IN_GRAVITY_YES)

from randchip import RandomChipGenerator


# TRODO : on devrait plus avoir besoin de ça ici. Car l'arena s'en branle de comment elle
# s'affiche.
ARENA_TILE_WIDTH  = 32
ARENA_TILE_HEIGHT = 32

(SKIP_NOT_FALLING_TILE,
 ADVANCE_NOTHING_TILE,
 ADVANCE_CONSEQUENT_TILE,
) = range(3)

DEFAULT_LIST_CHIP_GENERATION = (
    ((CHIP_COIN,   0),  5),
    ((CHIP_COIN,   1),  7),
    ((CHIP_COIN,   2), 12),
    ((CHIP_COIN,   5), 12),
    ((CHIP_COIN,  10),  5),
    ((CHIP_SUGAR, ),   10),
    ((CHIP_CLOPE, ),    4),
)

class ArenaBasic():
    """
    classe qui gère une arène du jeu avec les Tile, les Chips,

    type MVC : Modèle
    TRODO : virer les fonctions d'affichage. Parce que pour l'instant c'est Modèle + Vue,
    et c'est pas bien
    """

    def __init__(self, surfaceDest, posPixelTopLeft, arenaSize, nbrPlayer,
                 listGenInit=DEFAULT_LIST_CHIP_GENERATION,
                 listGenAfterGravity=None,
                 tutorialScheduler=None):
        """
        constructeur. (thx captain obvious)

        entrée :
            surfaceDest : Surface principale de l'écran, sur laquelle s'affiche le jeu.
                          TRODO : a virer, of course
            posPixelTopLeft : Rect. Position, en pixel, du coin sup gauche de l'arena à l'écran.
            arenaSize : tuple de 2 elem (c'est pas un Rect). (longueur, largeur),
                        en nombre de tile. TRODO : faut un Rect. Plus pratique.
            nbrPlayer : nombre de joueur qui peuvent sélectionner les tiles.
                        (pas trop géré pour l'instant)
        """
        self.initCommonStuff(surfaceDest, posPixelTopLeft,
                             arenaSize, nbrPlayer)

        #rien à foutre là ce truc
        #self.crawlerGravityDefault = ArenaCrawler(self.arenaSize)
        #self.crawlerGravityDefault.config(RIGHT, UP)
        # TRODO : config de gravité à mettre dans un dict
        #self.gravityDir = DOWN
        #self.gravityMovements = GravityMovements()
        self.randomChipGenInit = RandomChipGenerator(listGenInit)
        if listGenAfterGravity is None:
            listGenAfterGravity = listGenInit
        self.randomChipGenAfterGrav = RandomChipGenerator(listGenAfterGravity)
        self.createMatrixTile()
        self.start()


    def initCommonStuff(self, surfaceDest, posPixelTopLeft, arenaSize, nbrPlayer):
        self.surfaceDest = surfaceDest
        self.posPixelTopLeft = posPixelTopLeft
        self.arenaSize = arenaSize
        self.nbrPlayer = nbrPlayer

        # TRODO : on n'a peut être pas besoin de ça. (width et height)
        self.width = self.arenaSize[0]
        self.height = self.arenaSize[1]
        self.rectArenaSize = pyRectTuple((0, 0), self.arenaSize)
        # TRODO : ne sert que pour des arena héritée. Du coup, à réfléchir.
        self.listBigObj = []


    def start(self):
        pass


    def posPixelFromPosArena(self, posArena):
        """
        conversion position d'une Tile dans l'Arène -> position en pixel à l'écran,
        Entrées : posArena. Rect. Position de la tile dans l'arène.
        Sorties : Rect. Position en pixel, à l'écran, du coin sup gauche de la Tile.
        La fonction ne vérifie pas si la position en param existe vraiment dans l'arène.
        Elle convertit et puis c'est tout.

        TRODO : A mettre dans la View ?? Oui jconfirme
        """
        return pyRect(posArena.x*ARENA_TILE_WIDTH + self.posPixelTopLeft.x,
                      posArena.y*ARENA_TILE_HEIGHT + self.posPixelTopLeft.y)


    def createChipAtStart(self):
        """
        crée une Chip au hasard, selon des coefs prédéterminés (à l'arrache)
        Sorties : objet héritée d'une classe Chip.
        """
        return self.randomChipGenInit.chooseChip()


    def createMatrixTile(self):
        """
        crée l'arène, avec la matrix des Tile. Et place une Chip dans chaque Tile.
        Les Chip sont déterminées au hasard.
        """

        self.matrixTile = []

        #youpi. Bon, vaut mieux une boucle que des list comprehension imbriquées, à mon avis.
        for y in xrange(self.height):

            lineTile = []

            for x in xrange(self.width):

                posArenaTile = pyRect(x, y)
                posPixelTile = self.posPixelFromPosArena(posArenaTile)

                newChip = self.createChipAtStart()

                param = (self.surfaceDest, posArenaTile, posPixelTile,
                         newChip, self.nbrPlayer)

                newTile = Tile(*param)

                lineTile.append(newTile)

            self.matrixTile.append(lineTile)


    def regenerateChipAfterOneGravity(self):
        return self.randomChipGenAfterGrav.chooseChip()


    def regenerateAllChipsAfterOneGravity(self, crawlerRegen=None):
        """ zob """

        if crawlerRegen is None:
            return

        crawlerRegen.start()

        while crawlerRegen.coP == crawlerRegen.primStart:
            tile = self.getTile(crawlerRegen.posCur)
            if tile.chip.chipType == CHIP_NOTHING:
                tile.chip = self.regenerateChipAfterOneGravity()
            crawlerRegen.crawl()


    #TRODO : une fonction générique qui s'appelle tout à la fin d'une gravité.


    def draw(self):
        """
        zob à virer
        """
        for lineTile in self.matrixTile:
            for tile in lineTile:
                tile.draw()


    def getTile(self, posArena):
        """
        zob
        """
        return self.matrixTile[posArena.y][posArena.x]


    def getTileCoordXY(self, coordX, coordY):
        """
        zob
        """
        #oui, c'est inversé, c'est normal !
        return self.matrixTile[coordY][coordX]


    def selectionChange(self, posArena, idPlayer, selectionType):
        """
        zob
        Y'a que les Selector qui auront le droit d'appeler cette fonction, sinon c'est le bordayl.
        """
        tile = self.getTile(posArena)
        tile.selectionChange(idPlayer, selectionType)


    def zapOnePos(self, posArena, zapType, zapForce):
        """ zob """
        tile = self.getTile(posArena)
        newChip = tile.zap(zapType, zapForce)

        if newChip is not None:
            tile.chip = newChip


    def zapSelection(self, selPath, selSuppl):
        """
        zob
        does this belong here ? good quaysteune
        """
        for posPath in selPath:
            self.zapOnePos(posPath, ZAP_PATH, 1)

        for posSuppl in selSuppl:
            self.zapOnePos(posSuppl, ZAP_SUPPL, 1)


    def determineGravity(self, crawlerGravity=None, gravityMovements=None):
        """
        zob
        """

        if crawlerGravity is None or gravityMovements is None:
            return None

        crawlerGravity.start()
        continueCrawl = True

        while continueCrawl:

            #print "start loop at : ", crawlerGravity.posCur

            if crawlerGravity.crawledOnPrimCoord:
                currentState = SKIP_NOT_FALLING_TILE

            #print "currentState start", currentState

            chip = self.getTile(crawlerGravity.posCur).chip
            isChipTypeNothing = chip.getChipType() == CHIP_NOTHING

            if currentState == SKIP_NOT_FALLING_TILE:
                if isChipTypeNothing:
                    currentState = ADVANCE_NOTHING_TILE

            elif currentState == ADVANCE_NOTHING_TILE:
                if not isChipTypeNothing:
                    if chip.isAcceptGravityMove():
                        currentState = ADVANCE_CONSEQUENT_TILE
                        #TRODO : prim and sec coordz
                        coSLastNothing = crawlerGravity.prevSec
                    else:
                        currentState = SKIP_NOT_FALLING_TILE

            else: #ADVANCE_CONSEQUENT_TILE
                if isChipTypeNothing or not chip.isAcceptGravityMove():
                    #TRODO : prim and sec coordz
                    #On chope pas le prev, mais le current.
                    #Car quand on indique un segment de move, le dernier
                    #élément n'est pas dans le move. "rangestyle"
                    coSLastConsequent = crawlerGravity.coordSec
                    coPCur = crawlerGravity.coordPrim
                    param = (coPCur, coSLastNothing, coSLastConsequent)
                    gravityMovements.addSegmentMove(*param)
                    #print "added inside loop: ", param

                    if isChipTypeNothing:
                        currentState = ADVANCE_NOTHING_TILE
                    else:
                        currentState = SKIP_NOT_FALLING_TILE

            continueCrawl = crawlerGravity.crawl()

            if (crawlerGravity.crawledOnPrimCoord
                and currentState == ADVANCE_CONSEQUENT_TILE):

                coSLastConsequent = crawlerGravity.secEnd
                coPCur = crawlerGravity.prevPrim
                param = (coPCur, coSLastNothing, coSLastConsequent)
                gravityMovements.addSegmentMove(*param)
                #print "added at end loop: ", param

            #print "currentState end", currentState

        #print self.gravityMovements.dicMovement

        #while 1:
        #    pass



            #quand on a vu une chipnothing :
            #on remonte de cette chip nothing, vers le haut. on signale à toute les tiles en passant
            #qu'elles subissent une gravité vers le bas. Elles répondent qu'elles acceptent ou pas.
            #On retient les tiles soumises à grav.
            #C'est un peu plus compliqué que ça. Il faut retenir des colonnes à grav, de Y1 à Y2.
            #Si y'a plusieurs vides dans une même colonne, on retient plusieurs colonnes.
            #Car c'est deux tombages différent, pour deux raisons différentes.
            #Donc on retient : X, Y1, Y2

            #TRIP: "Je ne sais pas ce qui me retient de ..." "Hi hi hi. Moi je sais." "Connard".

            #Ensuite, on prend chaque big object. On vérifie que toutes leurs tiles sont dans
            #l'une des colonne à grav. Si non, on coupe toutes les colonnes à grave comportant
            #des tiles du bigObjet. (On coupe de la tile jusqu'en haut de la colonne à grav.

            #Tant qu'on enlève des trucs de cette manière, on continue.

            #A la fin, on fait tomber les tiles, et les big objects qu'on sait qu'ils tombent.

            #on ne fera plus ça du coup. (les chipNothing du haut tomberont aussi.
            #C'est pas optimisé mais c'est plus sûr.) Ah bah non. C'est bon.

        #bon reprenons. boucle sur une liste des bigobject in gravity.
        #on verif si ils sont in_gravity. Si not, osef, on le vire de la liste.
        #si partly, on cancel les tiles. on le vire de la liste. on retient qu'on a cancelé
        #si yes, on le laisse dans la liste.
        #et on recommence jusqu'à ce que plus rien de cancelé.
        #et faut stocker une liste de bigobj soumis à la gravité.

        return gravityMovements


    def determineGravityFullSegment(self,
                                    crawlerGravity=None,
                                    gravityMovements=None):
        """
        zob
        testé que avec des full segment de colonne. Parce que le reste,
        je suis sûr de rien.
        """
        if crawlerGravity is None or gravityMovements is None:
            return None

        primCoordEmptySegment = None
        crawlerGravity.start()
        continueCrawl = True
        #allTileEmpty = true
        while continueCrawl:
            chip = self.getTile(crawlerGravity.posCur).chip
            if chip.getChipType() != CHIP_NOTHING:
                continueCrawl = crawlerGravity.jumpOnPrimCoord()
            else:
                crawlerGravity.crawl()
                if crawlerGravity.crawledOnPrimCoord:
                    print "segment vide à :", crawlerGravity.prevPrim
                    primCoordEmptySegment = crawlerGravity.prevPrim
                    continueCrawl = False

        if primCoordEmptySegment is None:
            return gravityMovements

        #weird
        secCoordGravStart = primCoordEmptySegment
        secCoordGravEnd = crawlerGravity.primEnd
        crawlerGravity.start()
        continueCrawl = True
        while continueCrawl:
            primCoordGrav = crawlerGravity.coS
            param = (primCoordGrav, secCoordGravStart, secCoordGravEnd)
            gravityMovements.addSegmentMove(*param)
            crawlerGravity.crawl()
            if crawlerGravity.crawledOnPrimCoord:
                continueCrawl = False

        print "gravityMovements.dicMovement : ", gravityMovements.dicMovement
        return gravityMovements

    def applyGravity(self, crawlerGravity=None,
                     gravityMovements=None, crawlerRegen=None):
        """
        zob
        """
        if crawlerGravity is None or gravityMovements is None:
            return

        for coP, listSegment in gravityMovements.dicMovement.items():

            crawlerGravity.setPrimCoord(coP)

            for coSStart, coSEnd in listSegment:

                crawlerGravity.setSecCoord(coSStart)
                crawlerGravity.crawl()

                #ça tombe pil poil, mais c'est un peu expérimental, quand même.
                while not (crawlerGravity.crawledOnPrimCoord
                           or crawlerGravity.coS == coSEnd):

                    chipSource = self.getTile(crawlerGravity.posCur).chip
                    tileDest = self.getTile(crawlerGravity.posPrev)
                    tileDest.chip = chipSource
                    crawlerGravity.crawl()

                self.getTile(crawlerGravity.posPrev).chip = ChipNothing()

        gravityMovements.cancelAllMoves()
        # TRODO : ça n'a rien à foutre là ça.
        self.regenerateAllChipsAfterOneGravity(crawlerRegen)


    def stimuliInteractiveTouch(self, posArena):
        """ zob """
        return False

