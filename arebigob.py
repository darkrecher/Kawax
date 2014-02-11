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
        
    