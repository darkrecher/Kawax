#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax
"""


from common   import pyRect

from gravmov  import (GravityMovements,
                      IN_GRAVITY_NOT, IN_GRAVITY_PARTLY, IN_GRAVITY_YES)

from coins    import ChipBigObject
from arebasic import ArenaBasic



class ArenaBigObject(ArenaBasic):
    """
    classe qui gère une arène du jeu avec les Tile, les Chips,
    Mais on peut ajouter des big object. Et la gravité les gère correctement.

    type MVC : Modèle
    TRODO : virer les fonctions d'affichage. Parce que pour l'instant c'est Modèle + Vue,
    et c'est pas bien
    """

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


    def draw(self):
        """
        zob à virer
        """
        for lineTile in self.matrixTile:
            for tile in lineTile:
                tile.draw()

        for bigObject in self.listBigObj:
            posPixel = self.posPixelFromPosArena(bigObject.posTopLeft)
            self.surfaceDest.blit(bigObject.imgBigObj, posPixel)


    def determineGravity(self, crawlerGravity=None, gravityMovements=None):
        """
        zob
        """

        gravityMovements = ArenaBasic.determineGravity(self,
                                                       crawlerGravity,
                                                       gravityMovements)

        if gravityMovements is None:
            return None

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

        listBigObjInGravity = list(self.listBigObj)
        listBigObjInGravityNext = []
        cancelledBigObj = True
        isLiInGrav = gravityMovements.isListInGravity

        while cancelledBigObj:

            cancelledBigObj = False

            for bigObj in listBigObjInGravity:

                inGravType, listPosInGrav = isLiInGrav(bigObj.listPosArena)

                if inGravType == IN_GRAVITY_YES:
                    listBigObjInGravityNext.append(bigObj)
                elif inGravType == IN_GRAVITY_PARTLY:
                    cancelledBigObj = True
                    for pos in listPosInGrav:
                        gravityMovements.cancelGravity(pos)

            listBigObjInGravity = listBigObjInGravityNext
            listBigObjInGravityNext = []

        self.listBigObjInGravity = listBigObjInGravity
        gravityMovements.removeEmptyListSegment()

        return gravityMovements


    def applyGravity(self, crawlerGravity=None,
                     gravityMovements=None, crawlerRegen=None):
        """
        zob
        """

        ArenaBasic.applyGravity(self, crawlerGravity,
                                gravityMovements, crawlerRegen)

        if gravityMovements is None:
            return

        # un peu bizarre, parce qu'on bouge les gros objets alors qu'on a déjà "acquitté"
        # les mouvements de gravité, en appelant la super-fonction ArenaBasic.applyGravity.
        # (Y'a eu le cancelAllMoves, la régénarion des chip).
        # Ca fait un peu "oups, je bouge mes gros objets à l'arrache, après tout le reste".
        # Mais ça tient le coup, donc on laisse comme ça.
        gravityDir = gravityMovements.direction
        for bigObj in self.listBigObjInGravity:
            bigObj.moveDirDist(gravityDir)

