#/usr/bin/env python
# -*- coding: utf-8 -*-
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
                      UP, DOWN, LEFT, RIGHT,
                      LIST_COEF_RANDOM_CHIP, randWithListCoef)

from tile     import Tile

from coins    import (Chip, ChipSugar, ChipCoin, ChipClope, ChipNothing,
                      ChipBigObject,
                      ChipAsproFull, ChipAsproHalfLeft, ChipAsproHalfRight,
                      CHIP_NOTHING, CHIP_COIN, CHIP_SUGAR, CHIP_CLOPE)

from arecrawl import ArenaCrawler

from gravmov  import (GravityMovements,
                      IN_GRAVITY_NOT, IN_GRAVITY_PARTLY, IN_GRAVITY_YES)

# TRODO : on devrait plus avoir besoin de ça ici. Car l'arena s'en branle de comment elle
# s'affiche.
ARENA_TILE_WIDTH  = 32
ARENA_TILE_HEIGHT = 32

(SKIP_NOT_FALLING_TILE,
 ADVANCE_NOTHING_TILE,
 ADVANCE_CONSEQUENT_TILE,
) = range(3)



class Arena():
    """
    classe qui gère une arène du jeu avec les Tile, les Chips, les gros objets, ...

    type MVC : Modèle
    TRODO : virer les fonctions d'affichage. Parce que pour l'instant c'est Modèle + Vue,
    et c'est pas bien
    """

    def __init__(self, surfaceDest, posPixelTopLeft, arenaSize, nbrPlayer):
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
        self.surfaceDest = surfaceDest
        self.posPixelTopLeft = posPixelTopLeft
        self.arenaSize = arenaSize
        self.nbrPlayer = nbrPlayer

        # TRODO : on n'a peut être pas besoin de ça. (width et height)
        self.width = self.arenaSize[0]
        self.height = self.arenaSize[1]
        self.rectArenaSize = pyRectTuple((0, 0), self.arenaSize)
        self.crawlerGravityDefault = ArenaCrawler(self.arenaSize)
        # TRODO : config à mettre dans un dict
        self.gravityDir = DOWN
        self.crawlerGravityDefault.config(RIGHT, UP)
        self.gravityMovements = GravityMovements()
        #contiendra une liste de classe BigObjects
        self.crawlerGravityRift = ArenaCrawler(self.arenaSize)
        self.crawlerGravityRift.config(DOWN, RIGHT)
        self.listBigObj = []


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


    def addBigObject(self, classBigObject, posTopLeft):
        """
        crée et ajoute un gros objet dans l'Arène.
        (Ca écrase les Chip sur lesquelles il se pose)

        entrées : classBigObject. Classe héritée de BigObject. Type du gos objet.
                  posTopLeft. Rect. Position, dans l'arène, du coin sup gauche de l'objet.
        """
        bigObject = classBigObject(posTopLeft)
        #Ecrasement des Chip. On doit mettre, dans l'arène, des Chip de type BigObject
        #Sur toutes les Tiles occupée par le BigObject.
        for posTileBigObj in bigObject.listPosArena:
            self.getTile(posTileBigObj).chip = ChipBigObject(bigObject)

        self.listBigObj.append(bigObject)


    def createRandomChip(self):
        """
        crée une Chip au hasard, selon des coefs prédéterminés (à l'arrache)
        Sorties : objet héritée d'une classe Chip.
        """
        #Détermination au hasard de l'identifiant de la Chip.
        choiceChip = randWithListCoef(LIST_COEF_RANDOM_CHIP)
        #idChip = (-2, -1, 0, 1, 2, 5, 10)[choiceChip]
        idChip = (0, -1, 0, 1, 2, 5, 10)[choiceChip]

        #Création du bon objet Chip, selon l'identifiant.
        #Cas spécifique : le sucre et le mégot de clope.
        if idChip == -2:
            return ChipAsproHalfLeft()

        if idChip == -1:
            return ChipSugar()

        #Cas général : une pièce de monnaie, dont la valeur est égale à l'identifiant.
        brouzouf = idChip
        return ChipCoin(brouzouf)


    def fillRandom(self):
        """
        crée l'arène, avec la matrix des Tile. Et place une Chip dans chaque Tile.
        Les Chip sont déterminées au hasard.
        #TRODO : c'est dégueux. Il faut pas créer les Chipo. C'est un autre process qui le fait.
        """

        self.matrixTile = []

        #youpi. Bon, vaut mieux une boucle que des list comprehension imbriquées, à mon avis.
        for y in xrange(self.height):

            lineTile = []

            for x in xrange(self.width):

                posArenaTile = pyRect(x, y)
                posPixelTile = self.posPixelFromPosArena(posArenaTile)

                newChip = self.createRandomChip()

                param = (self.surfaceDest, posArenaTile, posPixelTile,
                         newChip, self.nbrPlayer)

                newTile = Tile(*param)

                lineTile.append(newTile)

            self.matrixTile.append(lineTile)

        self.getTile(pyRect(7, 3)).chip = ChipAsproHalfLeft()
        self.getTile(pyRect(8, 3)).chip = ChipAsproHalfRight()


    def regenerateRandomAll(self):
        """
        écrase toutes les Chip de l'arène avec des Chip au hasard.
        """
        #TRODO : crawler.
        for y in xrange(self.height):

            lineTile = self.matrixTile[y]

            for tile in lineTile:

                if tile.chip.getChipType() == CHIP_NOTHING:
                    tile.chip = self.createRandomChip()


    def regenerateRandomFromUp(self):
        """
        crée des Chip au hasard, pour toutes les tiles vides qui sont en haut de l'arène.
        TRODO : faut utiliser un crawler. Faut regénérer à chaque action de gravité,
                et pas tout à la fin. Et faut le génériquifier pour tous les types de gravité.
                Bref, pour l'instant il est très moche ce truc.
        """
        for x in xrange(self.width):

            y = 0
            continueColumn = True

            while y < self.height and continueColumn:

                tile = self.getTileCoordXY(x, y)
                if tile.chip.getChipType() == CHIP_NOTHING:
                    tile.chip = self.createRandomChip()
                else:
                    continueColumn = False

                y += 1


    def draw(self):
        """
        zob
        """
        for lineTile in self.matrixTile:
            for tile in lineTile:
                tile.draw()

        for bigObject in self.listBigObj:
            posPixel = self.posPixelFromPosArena(bigObject.posTopLeft)
            self.surfaceDest.blit(bigObject.imgBigObj, posPixel)


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


    def nbGravityRift(self, selPath, selSuppl):
        """
        zob adjacenceType
        """
        if len(selSuppl) > 0:
            return 0

        nbSelTilePerLine = [0, ] * self.height

        for pos in selPath:
            nbSelTilePerLine[pos.y] += 1

        print "min(nbSelTilePerLine)", min(nbSelTilePerLine)
        return min(nbSelTilePerLine)


    def determineGravity(self, crawlerGravity=None):
        """
        zob
        """

        if crawlerGravity is None:
            crawlerGravity = self.crawlerGravityDefault

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
                    self.gravityMovements.addSegmentMove(*param)
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
                self.gravityMovements.addSegmentMove(*param)
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

            #"Je ne sais pas ce qui me retient de ..." "Hi hi hi. Moi je sais." "Connard".

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

        #isListInGravity
        #self.listBigObj
        listBigObjInGravity = list(self.listBigObj)
        listBigObjInGravityNext = []
        cancelledBigObj = True
        aliasGravIsIn = self.gravityMovements.isListInGravity

        while cancelledBigObj:

            cancelledBigObj = False

            for bigObj in listBigObjInGravity:

                inGravType, listPosInGrav = aliasGravIsIn(bigObj.listPosArena)

                if inGravType == IN_GRAVITY_YES:
                    listBigObjInGravityNext.append(bigObj)
                elif inGravType == IN_GRAVITY_PARTLY:
                    cancelledBigObj = True
                    for pos in listPosInGrav:
                        self.gravityMovements.cancelGravity(pos)

            listBigObjInGravity = listBigObjInGravityNext
            listBigObjInGravityNext = []

        self.listBigObjInGravity = listBigObjInGravity
        self.gravityMovements.removeEmptyListSegment()

        return self.gravityMovements.dicMovement != {}


    def applyGravity(self, crawlerGravity=None):
        """
        zob
        """
        if crawlerGravity is None:
            crawlerGravity = self.crawlerGravityDefault

        for coP, listSegment in self.gravityMovements.dicMovement.items():

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

        for bigObj in self.listBigObjInGravity:
            bigObj.moveDirDist(self.gravityDir)

        self.gravityMovements.cancelAllMoves()


    def determineGravityRift(self):
        """ zob """
        return self.determineGravity(self.crawlerGravityRift)


    def applyGravityRift(self):
        """ zob """
        self.applyGravity(self.crawlerGravityRift)


    def mergeAsproHalf(self, posArena):
        """ zob """
        tileOnPos = self.getTile(posArena)
        if isinstance(tileOnPos.chip, ChipAsproHalfLeft):
            print "thats' hwat !"

            posArenaAdjRight = posArena.move((+1, 0))
            if posArenaAdjRight.x >= self.width:
                return False

            chipOnPosAdjRight = self.getTile(posArenaAdjRight).chip

            if not isinstance(chipOnPosAdjRight, ChipAsproHalfRight):
                print "fail aspro right"
                return False

            print "aspro ok"
            self.zapOnePos(posArenaAdjRight, ZAP_INTERACTIVE, 1)
            tileOnPos.chip = ChipAsproFull()

            return True

        elif isinstance(tileOnPos.chip, ChipAsproHalfRight):

            posArenaAdjLeft = posArena.move((-1, 0))
            if posArenaAdjLeft.x < 0:
                return False

            chipOnPosAdjLeft = self.getTile(posArenaAdjLeft).chip

            if not isinstance(chipOnPosAdjLeft, ChipAsproHalfLeft):
                print "fail aspro left"
                return False

            print "aspro ok"
            self.zapOnePos(posArenaAdjLeft, ZAP_INTERACTIVE, 1)
            tileOnPos.chip = ChipAsproFull()

            return True

        else:

            return False


    def takeAsproFull(self, posArena):
        """ zob """
        chipOnPos = self.getTile(posArena).chip
        if isinstance(chipOnPos, ChipAsproFull):
            self.zapOnePos(posArena, ZAP_PATH, 1)
            return True
        else:
            return False


    def stimuliInteractiveTouch(self, posArena):
        """ zob """
        print "interactive touch on : ", posArena
        #chipInteract = self.getTile(posArena).chip
        #if isinstance(chipInteract, ChipAsproHalfLeft):
        #    print "thats' hwat !"
        if self.mergeAsproHalf(posArena):
            return True
        elif self.takeAsproFull(posArena):
            return True
        else:
            return False

