#/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Blarg version 1.0

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

vocab et nommage des variables : 

    pos : pygame.Rect, avec les valeurs width et height à 0.
          position d'un truc. (coordonnées)
    posArena : position d'une case dans l'aire de jeu
    posPixel : position d'un pixel à l'écran ou dans une Surface
    Quand y'a pos tout seul, c'est par défaut posArena, en général.
    
    path : liste/tuple de posArena (à priori adjacente) formant un chemin.
    
    coP : coordonnée primaire. int
    coS : coordonnée secondaire. int
    Y'a l'une des coordonnées qu'est x, l'autre y. Ca dépend du contexte.
    En général, quand on veut parcourir toute les cases d'une arena, pour une raison ou 
    une autre, la coordonnée primaire, c'est celle de la boucle principale,
    et la coordonnée secondaire, c'est celle de la boucle d'en dessous.

je rentre pas dans les détails, parce que ce serait trop long et pas intéressant pour vous :
Mais j'ai vraiment une vie de merde. Toute ma vie, en entier, c'est de la merde.
"""

import random
import pygame

from common   import (securedPrint, pyRect, pyRectTuple,
                      FRAME_PER_SECOND, DELAY_GRAVITY,
                      ARENA_SIZE, TILE_PIXEL_SIZE,
                      UP, DOWN, LEFT, RIGHT)

from console  import Console
from manual   import ManualInGame
from arebasic import ArenaBasic
from selector import Selector
from zapvalid import ZapValidatorBase
from stimgame import StimuliStockerForGame
from crawler  import ArenaCrawler
from gravmov  import GravityMovements

from tutorial import (STEP_COND_NEVER, STEP_COND_STIM, STEP_COND_SELECT_TILES,
                      COLOR_TUTORIAL)

# clé : direction de la gravité
# valeur : tuple de 6 éléments.
#           - direction primaire du crawler permettant de déterminer quels 
#             chip sont soumises à la gravité.
#           - direction secondaire du crawler. Ca doit être la direction inverse de la gravité.
#           - Boolean indiquant si la coordonnée primaire de la gravité est la coord X, ou pas. 
#             Coord prim de gravité = coord qui n'est pas modifiée quand on applique la gravité.
#             Par ex : si ça tombe vers le bas, la coord prim c'est X.
#           - Boolean indiquant le sens de variation de la coord secondaire quand on applique
#             la gravité. True : la coord secondaire augmente. False : elle diminue.
#           - direction primaire du crawler permettant de remplir les cases vides
#             au fur et à mesure que la gravité s'applique.
#           - direction secondaire du crawler.
DICT_GRAVITY_CONFIG = {
    UP    : (LEFT, DOWN, True, False, UP, RIGHT),
    DOWN  : (LEFT, UP, True, True, DOWN, RIGHT),
    LEFT  : (UP, RIGHT, False, False, LEFT, DOWN),
    RIGHT : (UP, LEFT, False, True, RIGHT, DOWN),
}

COLOR_ZAP_OBJECTIVE = (255, 50, 50)

class GameBasic():
    """
    classe qui gère tout le jeu.
    """

    def __init__(self, surfaceDest, gravityDir=DOWN, tutorialScheduler=None):
        """
        constructeur. (thx captain obvious)

        entrée :
            surfaceDest : Surface principale de l'écran, sur laquelle s'affiche le jeu.
        """
        self.initCommonStuff(surfaceDest, gravityDir, tutorialScheduler)
        
        self.arena = ArenaBasic(surfaceDest, self.posPixelArena, ARENA_SIZE, 2,
                                tutorialScheduler=tutorialScheduler)
        self.selectorPlayerOne = Selector(self.arena, 0)
                
        self.populateArena()
        self.arena.draw()
        pygame.display.flip()

        
    def populateArena(self):
        """ à overrider. On initialise l'arena avec les chips que l'on veut, si on veut. """
        pass

    
    def execStimTutoNext(self):
        print "next tutorializazione"
        # TRODO : un tutorial qui ne fait rien ? Ce qui permettrait d'éviter 
        # ces tests de is None à chaque fois ?
        if self.tutorialScheduler is None:
            return
        if self.tutorialScheduler.takeStimTutoNext():
            self.showCurrentTutoStep()
            if self.tutorialScheduler.getCurrentTellObjective():
                zapValidatorDescrip = self.zapValidatorBase.getListStrDescription()
                param = (zapValidatorDescrip, COLOR_ZAP_OBJECTIVE)
                self.console.addListTextAndDisplay(*param)
        else:
            # re-blink, si le tuto n'avance pas, et que y'a des trucs à blinker.
            # comme ça le joueur revoit les blinks si il a pas eu le temps de les voir.
            # ATTENTION : code ajouté à l'arrache suite à reprise du projet à l'arrache.
            listPosBlink = self.tutorialScheduler.getCurrentBlink()
            if len(listPosBlink) and self.blinker is not None:
                self.blinker.startBlink(listPosBlink)

            
    def initCommonStuff(self, surfaceDest, gravityDir, tutorialScheduler=None):
        """ zob 
        TRODO : c'est un peu le bordel d'avoir foutu ça là.
        Du coup, quand on regarde dans l'init, on se rend pas compte que y'a
        toutes ces variables membres. donc, c'est mal de faire ça.
        """
        self.surfaceDest = surfaceDest
        self.blinker = None
        self.tutorialScheduler = tutorialScheduler
        self.console = Console(self.surfaceDest, pyRect(400, 10, 235, 460), nbCharMax=25)
        self.console.addText("bonjour !!")
        self.console.refresh()
        self.console.display()
        self.manual = ManualInGame(
            self.surfaceDest, 
            pyRect(10, 340, 400, 130),
            self.tutorialScheduler)
        self.manual.refresh()
        self.manual.display()
        
        self.posPixelArena = pyRect(10, 10)
        
        param = (self.posPixelArena, ARENA_SIZE, TILE_PIXEL_SIZE)
        self.stimuliStocker = StimuliStockerForGame(*param)
        
        #Ca c'est le putain d'objet qui permet de maîtriser le temps !!!
        #Talaaaa, je suis le maître du temps. et des frames par secondes aussi.
        self.clock = pygame.time.Clock()
        
        self.showObjectivesAtStart = True
        
        if gravityDir is None:
            self.crawlerGrav = None
            self.gravityMovements = None
            self.crawlerRegen = None
        else:
            (gravPrimDir, gravSecDir, primCoordIsX, gravIncsCoord,
             regenPrimDir, regenSecDir) = DICT_GRAVITY_CONFIG[gravityDir]            
            self.crawlerGrav = ArenaCrawler(ARENA_SIZE)
            self.crawlerGrav.config(gravPrimDir, gravSecDir)
            param = (gravityDir, primCoordIsX, gravIncsCoord)
            self.gravityMovements = GravityMovements(*param)
            self.crawlerRegen = ArenaCrawler(ARENA_SIZE)
            self.crawlerRegen.config(regenPrimDir, regenSecDir)
            print "self.crawlerRegen.secMove :", self.crawlerRegen.secMove
    
    
    def respawnZapValidator(self):
        """ redéfinit self.zapValidatorBase (qui n'est pas bien nommé, au passage) """
        param = (self.arena, random.randrange(7, 23), random.randrange(3))
        self.zapValidatorBase = ZapValidatorBase(*param)

        
    def tryToZap(self):
        """ zob """
        selPath = self.selectorPlayerOne.selPath
        selSuppl = self.selectorPlayerOne.selSuppl
        
        if self.zapValidatorBase.validateZap(selPath, selSuppl, []):
        
            # gestion du tutorial, si y'en a un.
            if self.tutorialScheduler is not None:
                param = (selPath, selSuppl)
                if self.tutorialScheduler.takeStimTileSelected(*param):
                    self.showCurrentTutoStep()
        
            self.zapWin()
            self.respawnZapValidator()
            
            self.arena.zapSelection(selPath, selSuppl)
            self.selectorPlayerOne.cancelAllSelection()
            self.selectorPlayerOne.setStimuliLock(True)

            if self.determineGravity():
                self.gravityCounter = DELAY_GRAVITY
            
            if ((self.tutorialScheduler is None) or 
               (self.tutorialScheduler.getCurrentTellObjective())):
                zapValidatorDescrip = self.zapValidatorBase.getListStrDescription()
                self.console.addListTextAndDisplay(zapValidatorDescrip, COLOR_ZAP_OBJECTIVE)
            
        else:
            lastTryDescrip = self.zapValidatorBase.getListStrLastTry()
            self.console.addListTextAndDisplay(lastTryDescrip + ("FAIL",))

            
    def zapWin(self):
        """ à overrider """
        self.console.addListTextAndDisplay(("yeah !!", ))
        
    def periodicAction(self):
        """ à overrider """
        pass

        
    def applyGravity(self):
        """ zonc """
        param = (self.crawlerGrav, self.gravityMovements, self.crawlerRegen)
        self.arena.applyGravity(*param)
    
    
    #TRODO : y'a 2 fonctions différentes. determineGravity handleGravity.
    # On y pige rien. Ca va pas du tout.
    def determineGravity(self):
        """ zob 
        """
        param = (self.crawlerGrav, self.gravityMovements)
        self.gravityMovements = self.arena.determineGravity(*param)
        
        return (self.gravityMovements is not None 
                and len(self.gravityMovements.dicMovement) > 0)

                
    def handleGravity(self):
        self.applyGravity()
        if self.determineGravity():                        
            self.gravityCounter = DELAY_GRAVITY
        else:
            #arrache un peu no ?
            if ((self.tutorialScheduler is not None)
               and (not self.tutorialScheduler.mustLockGameStimuli())):
                self.selectorPlayerOne.setStimuliLock(False)
        
    
    def gameStimuliInteractiveTouch(self):
        """ à overrider """
        pass
        
    
    def showCurrentTutoStep(self):
        """
        """
        if self.tutorialScheduler is None:
            return
        listTextDescrip = self.tutorialScheduler.getCurrentText()
        if len(listTextDescrip):
            print listTextDescrip
            param = (listTextDescrip, COLOR_TUTORIAL)
            self.console.addListTextAndDisplay(*param)
        #blink
        listPosBlink = self.tutorialScheduler.getCurrentBlink()
        if len(listPosBlink) and self.blinker is not None:
            self.blinker.startBlink(listPosBlink)
        #lock
        if self.tutorialScheduler.mustLockGameStimuli():
            print "locked !!!"
            self.selectorPlayerOne.setStimuliLock(True)
        else:
            # Euh... Faut délocker ou rien faire ? Bonne question.
            self.selectorPlayerOne.setStimuliLock(False)
        
    def playOneGame(self):
        """
        zob
        """        
        # TRODO : pourquoi y'a du code d'init ici ?
        self.gravityCounter = 0
        self.respawnZapValidator()
        self.showCurrentTutoStep()
        
        if ((self.tutorialScheduler is None) or 
           (self.tutorialScheduler.getCurrentTellObjective())):
            zapValidatorDescrip = self.zapValidatorBase.getListStrDescription()
            self.console.addListTextAndDisplay(zapValidatorDescrip, COLOR_ZAP_OBJECTIVE)
        
        while True: #ça, c'est la classe, déjà pour commencer.

            #Le jeu va s'auto-ralentir pour atteindre le nombre de FPS spécifié
            self.clock.tick(FRAME_PER_SECOND)
            
            self.stimuliStocker.resetStimuli()
            self.stimuliStocker.takeEventsFromMouseAndKeyboard()
            
            #TRODO : une sorte de mapping ?
            
            if self.stimuliStocker.stimuliQuitGame:
                return
            
            if self.stimuliStocker.mustStandBy:
                self.selectorPlayerOne.takeStimuliStandBy()
                
            for posSelected in self.stimuliStocker.listPosArenaToActivate:
                print posSelected
                self.selectorPlayerOne.takeStimuliActivateTile(posSelected)
            
            if self.stimuliStocker.stimuliTryZap:
                # TRODO condition foutue à l'arrache. 
                # Faut rendre le stimuliStocker configurable. On y locke/délocke des trucs
                if (self.tutorialScheduler is None
                   or not self.tutorialScheduler.mustLockGameStimuli()):
                    self.tryToZap()
            
            if self.stimuliStocker.stimuliEmptySelection:
                self.selectorPlayerOne.cancelAllSelection()
            
            if self.stimuliStocker.stimuliChangeZapConstraint:
                self.respawnZapValidator()
                zapValidatorDescrip = self.zapValidatorBase.getListStrDescription()
                self.console.addListTextAndDisplay(zapValidatorDescrip, COLOR_ZAP_OBJECTIVE)

            if self.stimuliStocker.stimuliConsoleScrollUp:
                self.console.moveCursorText(-1)
                self.console.refresh()
                self.console.display()
                
            if self.stimuliStocker.stimuliConsoleScrollDown:
                self.console.moveCursorText(+1)
                self.console.refresh()
                self.console.display()
                
            if self.stimuliStocker.stimTutoNext:
                self.execStimTutoNext()
            
            if self.stimuliStocker.stimReblink:
                listPosBlink = self.tutorialScheduler.getCurrentBlink()
                if len(listPosBlink) and self.blinker is not None:
                    self.blinker.startBlink(listPosBlink)
            
#                #si stand by : stand by
#                
#                #si activate. on chope la coord.
#                
#                #    si coord none. : stan by. Et previous = None
#                
#                #    sinon : 
#                
#                #        si previous = None. On active et c'est tout.
#                
#                #        sinon : on active tout le chemin entre previous et actuel
#                
#                #        previous = actuel

            posInteract = self.stimuliStocker.posArenaToInteractTouch
            if posInteract is not None:
                # ça faut le foutre dans la fonction qu'on override.
                # C'est peut être mieux non ?
                if self.arena.stimuliInteractiveTouch(posInteract):
                    self.selectorPlayerOne.cancelAllSelection()
                    self.selectorPlayerOne.setStimuliLock(True)
                    if self.determineGravity():                    
                        self.gravityCounter = DELAY_GRAVITY
                    if (self.tutorialScheduler is not None and
                        self.tutorialScheduler.takeStimInteractiveTouch()):
                        self.showCurrentTutoStep()
                # c'est de cette fonction là que je parle.
                self.gameStimuliInteractiveTouch()
                
            #TRODO : faudra une 'tite classe pour les compteurs. 
            if self.gravityCounter:
            
                self.gravityCounter -= 1
                
                if not self.gravityCounter:
                    self.handleGravity()
            
            self.periodicAction()
            if self.blinker is not None:
                self.blinker.advanceTimerAndHandle()
            
            #TRODO : optimiser ça. Pas de refresh géant à chaque frame.
            self.arena.draw()
            pygame.display.flip()

