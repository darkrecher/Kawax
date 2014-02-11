#/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Blarg version 1.0

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
"""

import os
import random
import pygame
import pygame.locals
pygl = pygame.locals

#�a me fait chier de foutre �a ici. Mais bon. Pas trop le choix.
#C'est le premier module qui s'importe, et il a besoin de truc dedans. (Genre crappyFont)
pygame.init()


ARENA_SIZE = (12, 10)

TILE_PIXEL_WIDTH  = 32
TILE_PIXEL_HEIGHT = 32
TILE_PIXEL_SIZE = (TILE_PIXEL_WIDTH, TILE_PIXEL_HEIGHT)

FRAME_PER_SECOND = 60

#nom du r�pertoire avec les images dedans
IMG_DIRECTORY_NAME = "img"
FONT_DIRECTORY_NAME = "fontzy"

crappyFont = pygame.font.Font(None, 30)
strPathFontConsole = os.sep.join((FONT_DIRECTORY_NAME, "tempesta.ttf"))
fontConsole = pygame.font.Font(strPathFontConsole, 12)

(SELTYPE_NONE,
 SELTYPE_SUPPL,
 SELTYPE_PATH,
) = range(3)

(ZAP_PATH,
 ZAP_SUPPL,
 ZAP_ADJACENT,
 ZAP_INTERACTIVE,
) = range(4)

(UP,
 DOWN,
 LEFT,
 RIGHT,
) = range(4)

DELAY_GRAVITY = 18


def pyRect(top=0, left=0, width=0, height=0):
    """
    permet de g�n�rer un pygame.Rect, sans forc�ment donner la hauteur et la largeur.

    pourquoi ils ont pas mis eux-m�me des valeurs par d�faut bordel !!
    (ou alors c'est moi qui suis � la masse et j'ai loup� une astuce.)
    """
    return pygame.Rect(top, left, width, height)

    
def pyRectTuple(tuplePos=(0, 0), tupleSize=(0, 0)):
    """
    permet de g�n�rer un pygame.Rect � partir de tuples,
    sans forc�ment donner la hauteur et la largeur.
    """
    return pygame.Rect(tuplePos, tupleSize)
    
    
def securedPrint(stringToWrite):
    """
    fonction pour balancer sur la sortie standard une string unicode, avec des accents et tout.
    C'est pas garanti que les accents sortent correctement.
    Mais c'est garanti que �a fasse jamais planter le programme.

    entr�e :
        unicodeString : string (unicode ou pas) contenant le message � afficher.

    chui oblig� de faire comme �a parce que le terminal du Mac est tellement merdique
    qu'il peut pas afficher des accents aigus unicode.
    Il peut en afficher que si ils viennent de l'encodage 'mac-roman'. Quelle daubasse !!!
    """

    try:
        print stringToWrite
    except:
        #fail ecrivage du unicode. Donc on convertit en ascii.
        #Ca fait des caract�res pourri, mais l'ascii, �a marche partout.
        unicodeString = unicode(stringToWrite)
        print unicodeString.encode("ascii", "replace")

        
def loadImg(filename, colorkey=-1, doConversion=True):
    """
    fonction piqu�e au tutorial chimp de pygame. Permet de charger une image.
    Si l'image ne peut pas �tre charg�e, envoie une message sur stdout et balance une exception

    entr�es :
        filename : string indiquant le nom du fichier image � charger.
                   les images doivent toutes �tre dans le sous-r�pertoire
                   d�fini par IMG_DIRECTORY_NAME

        colorkey : d�finition de la key transparency de l'image
                   None :        pas de transparence
                   une couleur : la transparence est sur cette couleur
                   -1 :          on prend la couleur du pixel
                                 en haut � gauche de l'�cran

        doConversion : boolean. Indique si on doit faire la conversion de l'image dans le mode
                       graphique actuel. (Normalement, faut le faire tout le temps, pour
                       optimiser). Sauf que si le mode graphique actuel n'a pas encore �t�
                       d�termin�, eh ben on peut p� faire de convert. Donc faudra mettre False.
                                 
    plat-dessert :
        la Surface contenant l'image charg�e
    """

    pathname = os.path.join(IMG_DIRECTORY_NAME, filename)

    #tentative de chargement de l'image. On sort comme un voleur si �a fail
    try:
        image = pygame.image.load(pathname)
    except pygame.error, message:
        securedPrint(u"Fail. Impossible de charger l'image : " + pathname)
        #On peut mettre "raise" sans rien apr�s. Ca recrache la derni�re exception en cours.
        raise

    #conversion dans le mode graphique actuel. On le fait qu'une fois au d�but
    #et apr�s c'est plus rapide pour les blits. Enfin... normalement, parce que sur Mac...
    #Si on switche plein-ecran/windowed, je sais pas ce que �a donne.
    #Si �a se trouve faudrait refaire le convert sur toutes les images.
    #Bon, �a marce quand m�me. C'est pas un drame si c'est pas hyper optimis�.
    if doConversion:
        image = image.convert()

    #ajout de la transparence en fonction du param�tre colorkey
    if colorkey is not None:

        if colorkey == -1:
            #la couleur de transparence est celle du 1er pixel
            #en haut � gauche de l'image
            colorkey = image.get_at((0,0))

        #je sais pas ce que c'est que ce RLEACCEL, mais �a doit �tre cool.
        image.set_colorkey(colorkey, pygl.RLEACCEL)

    #on balance l'image
    return image


DICT_DEPL_FROM_DIR = {
 UP :    pyRect( 0, -1),
 DOWN :  pyRect( 0, +1),
 LEFT :  pyRect(-1,  0),
 RIGHT : pyRect(+1,  0),
}


def rectDeplFromDirDist(dir, dist=1):
    """ ddd """
    rectDepl = DICT_DEPL_FROM_DIR[dir]    
    if dist == 1:
        return pygame.Rect(rectDepl)
    else:
        return pyRect(rectDepl.x * dist, rectDepl.y * dist)
    

def pathLine(posStart, posEnd, indexCoordPrim, coordSecAtStart):
    """
    zob
    """
    
    if indexCoordPrim == 0:
    
        coordPrimStart = posStart.x
        coordPrimEnd = posEnd.x
        if coordSecAtStart == True:
            coordSec = posStart.y
        else:
            coordSec = posEnd.y

    else:
    
        coordPrimStart = posStart.y
        coordPrimEnd = posEnd.y
        if coordSecAtStart == True:
            coordSec = posStart.x
        else:
            coordSec = posEnd.x

    
    if coordPrimStart < coordPrimEnd:
        listCoordPrim = range(coordPrimStart, coordPrimEnd+1)
    elif coordPrimStart > coordPrimEnd:
        listCoordPrim = range(coordPrimStart, coordPrimEnd-1, -1)
    else:
        listCoordPrim = [coordPrimStart, ]
        
    if indexCoordPrim == 0:
        return [ pyRect(coordPrim, coordSec) for coordPrim in listCoordPrim ]
    else:
        return [ pyRect(coordSec, coordPrim) for coordPrim in listCoordPrim ]


# TRIP: aucun remord, aucun regret, aucune responsabilit�. Mes souvenirs ne sont que des fant�mes.
def findPathSimple(posStart, posEnd, orderXY=True, 
                   includeStart=False, includeEnd=True):
    """
    balance une liste de coordonn�es permettant d'aller de start � end.
    y'a les positions start et end incluses dans la liste, ou pas...
    """
            
    if orderXY:
        pathSimple = pathLine(posStart, posEnd, 0, True)
        pathSimple += pathLine(posStart, posEnd, 1, False)[1:]
    else:
        pathSimple = pathLine(posStart, posEnd, 1, True)
        pathSimple += pathLine(posStart, posEnd, 0, False)[1:]
    
    if not includeStart:
        pathSimple.pop(0)
    
    if len(pathSimple)>0 and not includeEnd:
        pathSimple.pop()
    
    return pathSimple

    
def isAdjacent(pos1, pos2):
    """
    zob
    Renvoie False si pos1=pos2, car c'est pas de l'adjacence, �a.
    """
    if (pos1.x == pos2.x) and abs(pos2.y - pos1.y) == 1:
        return True

    if (pos1.y == pos2.y) and abs(pos2.x - pos1.x) == 1:
        return True
        
    return False
    
    
def adjacenceType(pos1, pos2):
    """ zob """

    if pos1.x == pos2.x:
        dist = pos2.y - pos1.y
        return {+1 : DOWN, -1 : UP}.get(dist)

    if pos1.y == pos2.y:
        dist = pos2.x - pos1.x
        return {+1 : RIGHT, -1 : LEFT}.get(dist)

    return None


def indexInList(pos1, listPos):
    """
    zob
    Je crois que y'a une fonction indexof, dans un python plus r�cent.
    Mais je peux pas trop utiliser un python plus r�cent, sinon j'arrive pas � le py2exe.
    """
    for indexPos, pos2 in enumerate(listPos):
        if pos1 == pos2:
            return indexPos
            
    return -1
    

def isAdjacentList(pos1, listPos):
    """
    zob
    ne controle pas si pos1 est dans listPos. Faut l'avoir fait avant.
    """
    
    for pos2 in listPos:
        if isAdjacent(pos1, pos2):
            return True
    
    return False

def randWithListCoef(listCoef):
    """
    g�n�re un nombre au hasard, entre 0 et N,
    avec des coefficient de proba diff�rent pour chaque nombre

    entr�e :
        listCoef : liste de int (positif ou nul), indiquant les coefs pour chaque valeur
                   possible. On peut avoir des coef de 0. Dans ce cas, ce nombre ne sera
                   jamais choisi.
                   La somme des coefs peut valoir n'importe quoi, on fait avec.

    plat-dessert
        int. nombre al�atoire g�n�r�e, compris entre 0 et len(listCoef)-1
    """

    #d�termination de la plage de random ( = somme de tous les coefs,
    #et g�n�ration d'un nombre au hasard, dans cette plage.
    randMax = sum(listCoef)
    choiceValue = random.randrange(randMax)

    choiceIndex = 0

    #il faut trouver � quelle choix correspond le nombre qu'on a g�n�r� au hasard.
    #on avance dans la liste des coefs. A chaque fois, on retire le coef du choix
    #en cours. Quand on arrive � un choix, alors que le nombre est descendu en dessous
    #de son coef, alors c'est ce choix qui est le bon.
    #Et �a marche, bon c'est tout simple. Pas besoin de plus d'explication, bordel.
    while choiceValue >= listCoef[choiceIndex]:

        choiceValue -= listCoef[choiceIndex]
        choiceIndex += 1

    #voili voil�, on a trouv� le choix qu'a �t� fait.
    return choiceIndex


def severalRandWithListCoef(listCoef, nbrOfChoice):
    """ 
    g�n�re X nombre au hasard, tous diff�rent, entre 0 et N,
    avec des coefficient de proba diff�rent pour chaque nombre.
    X = nbrOfChoice
    faut que nbrOfChoice <= len(listCoef), sinon �a plante.
    La fonction ne le v�rifie pas
    """
    listChoice = []
    currentListCoef = list(listCoef)
    for _ in xrange(nbrOfChoice):
        choice = randWithListCoef(currentListCoef)
        listChoice.append(choice)
        currentListCoef[choice] = 0
        
    return tuple(listChoice)
        
    
#------------------------------------------------------------------- 
    
if __name__ == "__main__":
    #test unitaire pour pathLine et findPathSimple
    #bordel de merde, faut commenter la ligne avec crappyFont pour lancer ces tests.
    #Je dois vraiment arranger ce truc.
    securedPrint("test unitaire. Hell yeah !")
    
    #toutes les coords diff�rentes. X Y. start < end
    
    assert findPathSimple(pyRect(1, 20), pyRect(3, 25)) == [
        pyRect(2, 20, 0, 0), pyRect(3, 20, 0, 0), 
        pyRect(3, 21, 0, 0), pyRect(3, 22, 0, 0), pyRect(3, 23, 0, 0), 
        pyRect(3, 24, 0, 0), pyRect(3, 25, 0, 0)
    ]

    assert findPathSimple(pyRect(1, 20), pyRect(3, 25),
                          includeStart=True, includeEnd=True) == [
        pyRect(1, 20, 0, 0),
        pyRect(2, 20, 0, 0), pyRect(3, 20, 0, 0), 
        pyRect(3, 21, 0, 0), pyRect(3, 22, 0, 0), pyRect(3, 23, 0, 0), 
        pyRect(3, 24, 0, 0), pyRect(3, 25, 0, 0)
    ]

    #toutes les coords diff�rentes. X Y. start > end    

    assert findPathSimple(pyRect(3, 25), pyRect(1, 23)) == [
        pyRect(2, 25, 0, 0), pyRect(1, 25, 0, 0), 
        pyRect(1, 24, 0, 0), pyRect(1, 23, 0, 0),
    ]
    
    assert findPathSimple(pyRect(3, 25), pyRect(1, 23),
                          includeStart=False, includeEnd=False) == [    
        pyRect(2, 25, 0, 0), pyRect(1, 25, 0, 0), 
        pyRect(1, 24, 0, 0),
    ]

    assert findPathSimple(pyRect(3, 25), pyRect(1, 23),
                          includeStart=True, includeEnd=False) == [        
        pyRect(3, 25, 0, 0), 
        pyRect(2, 25, 0, 0), pyRect(1, 25, 0, 0), 
        pyRect(1, 24, 0, 0), 
    ]
    
    #toutes les coords diff�rentes. Y X. start < end

    assert findPathSimple(pyRect(1, 20), pyRect(3, 25),
                          False, True, True) == [
        pyRect(1, 20, 0, 0), pyRect(1, 21, 0, 0), pyRect(1, 22, 0, 0), 
        pyRect(1, 23, 0, 0), pyRect(1, 24, 0, 0), 
        pyRect(1, 25, 0, 0), 
        pyRect(2, 25, 0, 0), pyRect(3, 25, 0, 0), 
    ]
    
    #toutes les coords diff�rentes. Y X. start > end

    assert findPathSimple(pyRect(3, 25), pyRect(1, 20),
                          False, True, True) == [
        pyRect(3, 25, 0, 0), pyRect(3, 24, 0, 0), pyRect(3, 23, 0, 0), 
        pyRect(3, 22, 0, 0), pyRect(3, 21, 0, 0), pyRect(3, 20, 0, 0), 
        pyRect(2, 20, 0, 0), pyRect(1, 20, 0, 0) 
    ]
    
    #X pareil. (un seul test, osef)
    assert findPathSimple(pyRect(200, -4), pyRect(200, 1),
                          False, True, True) == [
        pyRect(200, -4, 0, 0), pyRect(200, -3, 0, 0), pyRect(200, -2, 0, 0), 
        pyRect(200, -1, 0, 0), pyRect(200,  0, 0, 0), pyRect(200,  1, 0, 0), 
    ]
    
    #Y pareil. (un seul test, osef)
    assert findPathSimple(pyRect(2, 1337), pyRect(-2, 1337),
                          False, True, True) == [
        pyRect( 2, 1337, 0, 0), pyRect( 1, 1337, 0, 0), pyRect( 0, 1337, 0, 0), 
        pyRect(-1, 1337, 0, 0), pyRect(-2, 1337, 0, 0), 
    ]
        
    #X et Y pareil. L� faut tout tester, car cas limite.
    assert findPathSimple(pyRect(1, 2), pyRect(1, 2), False, False, False
                         ) == []

    assert findPathSimple(pyRect(1, 2), pyRect(1, 2), False, False, True
                         ) == []

    assert findPathSimple(pyRect(1, 2), pyRect(1, 2), False, True,  False
                         ) == []                         
                         
    assert findPathSimple(pyRect(1, 2), pyRect(1, 2), False, True,  True
                         ) == [ pyRect(1, 2), ]

    assert findPathSimple(pyRect(1, 2), pyRect(1, 2), True,  False, False
                         ) == []                      
                                                      
    assert findPathSimple(pyRect(1, 2), pyRect(1, 2), True,  False, True
                         ) == []                      
                                                      
    assert findPathSimple(pyRect(1, 2), pyRect(1, 2), True,  True,  False
                         ) == []                       
                                                      
    assert findPathSimple(pyRect(1, 2), pyRect(1, 2), True,  True,  True
                         ) == [ pyRect(1, 2), ]
    
    #bon �a y est, fini de jouer ?
    securedPrint("fin test unitaire. Paradise no !")
    
    