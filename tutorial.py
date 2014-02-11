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
"""

from common   import (pyRect, pyRectTuple)
import language

COLOR_TUTORIAL = (40, 255, 40)

(STEP_COND_NEVER,
 STEP_COND_STIM,
 STEP_COND_SELECT_TILES,
 STEP_COND_INTERACTIVE_TOUCH_SUCCESSED,
) = range(4)


class TutorialStep():
    """
    juste un step. WIP : ajouter un ensemble de bidule en param supp.
    les bidules incluant : TELL_OBJECTIVE. Et peut-�tre d'autres trucs apr�s.
    nan juste un boolean. Faites pas chier avec un rassemblage.
    """
    def __init__(self, conditionType, listPosCond, soundId,
                 listTextDescrip, listPosBlink, tellObjective):
        """
        """
        self.conditionType = conditionType
        self.listPosCond = listPosCond
        #osef du soundId pour l'instant.
        self.soundId = soundId
        self.listTextDescrip = listTextDescrip
        self.listPosBlink = listPosBlink
        self.tellObjective = tellObjective
        # et c'est tout � priori. La classe va stocker que �a.


class TutorialScheduler():
    """
    classe qui g�re un tutorial. Y'a des steps. Dans un step, on d�crit :
     - type de condition pour avancer au prochain step (stim, select) y'a pas de start.
       pas besoin.
     - liste des cases � s�lectionner pour l'avan�age (ou rien)
     - le texte � blablater pour le step actuel (ou rien)
     - le blink � blinker pour le step actuel (ou rien)
     - est-ce qu'il faut �crire l'objectif dans la console, ou pas.
    On fout tout �a dans un tuple, et basta.
    Si on veut que �a fasse rien au d�but, on met no text, no blink, et la condition qu'on veut.
    """

    def __init__(self, listTutStepsDescrip):
        """
        constructeur. (thx captain obvious)

        entr�e :
            surfaceDest : Surface principale de l'�cran, sur laquelle s'affiche le jeu.
        """
        self.listTutSteps = []
        #conversion coord->rect, et cr�ation de la liste des steps.
        for tutStepDescrip in listTutStepsDescrip:
            (conditionType, listCoordCond, soundId, blobTextDescrip,
             listCoordBlink, tellObjective) = tutStepDescrip
            listPosCond = [ pyRectTuple(coord) for coord in listCoordCond ]
            listPosBlink = [ pyRectTuple(coord) for coord in listCoordBlink ]

            if isinstance(blobTextDescrip, dict):
                textDescrip = blobTextDescrip[language.languageCurrent]
            else:
                textDescrip = blobTextDescrip
            param = (conditionType, listPosCond, soundId, textDescrip,
                     listPosBlink, tellObjective)
            tutStep = TutorialStep(*param)
            self.listTutSteps.append(tutStep)
        #self.listTutSteps = [ TutorialStep(*tutStepDescrip)
        #                      for tutStepDescrip
        #                      in listTutStepsDescrip ]
        self.listTutSteps = tuple(self.listTutSteps)
        self.indexStep = 0
        self.tutStepCurrent = self.listTutSteps[self.indexStep]
        self.justAdvanced = False # osef ??
        self.totallyFailed = False

    def getCurrentText(self):
        """
        """
        return self.tutStepCurrent.listTextDescrip

    def getCurrentBlink(self):
        """
        """
        return self.tutStepCurrent.listPosBlink

    def getCurrentTellObjective(self):
        return self.tutStepCurrent.tellObjective


    def takeStimTutoNext(self):
        """
        """
        if self.totallyFailed:
            return False
        if self.tutStepCurrent.conditionType != STEP_COND_STIM:
            return False
        self.indexStep += 1
        self.tutStepCurrent = self.listTutSteps[self.indexStep]
        return True

    def takeStimInteractiveTouch(self):
        """
        """
        # pas de condition ni rien. Faut que �a tombe juste.
        if self.totallyFailed:
            return False
        if self.tutStepCurrent.conditionType != STEP_COND_INTERACTIVE_TOUCH_SUCCESSED:
            return False
        print "success stim interactive sur le tuto"
        self.indexStep += 1
        self.tutStepCurrent = self.listTutSteps[self.indexStep]
        return True

    def takeStimTileSelected(self, selPath, selSuppl):
        """
        c'est des listes de pyRect � comparer � une liste de pyRect
        """
        if self.totallyFailed:
            return False
        if self.tutStepCurrent.conditionType != STEP_COND_SELECT_TILES:
            return False
        selAll = selPath + selSuppl
        listPosCond = self.tutStepCurrent.listPosCond
        if len(selAll) != len(listPosCond):
            self.totallyFail()
            return False
        while len(selAll):
            posSelected = selAll.pop(0)
            #comparaison de rect. Ca marche ?
            if posSelected not in listPosCond:
                self.totallyFail()
                return False
        #youpi ! La s�lection est bonne.
        self.indexStep += 1
        self.tutStepCurrent = self.listTutSteps[self.indexStep]
        return True

    def mustLockGameStimuli(self):
        """
        """
        # On aura peut �tre besoin de faire plus subtil que �a. Mais pour l'instant non.
        return (self.tutStepCurrent.conditionType == STEP_COND_STIM)

    def totallyFail(self):
        self.totallyFailed = True;

    def getFailText(self):
        return ("Vous n'avez pas s�lectionn� les bonnes cases.",
                "D�brouillez-vous tout seul maintenant !")

    # faut une classe externe, ou un overridage des classes actuelles ?
    # externe je dirais.
    # avec toutes les �tapes. Et ici, dans le Game (voir GameBasic), on appelle des
    # fonctions de cette classe externe, ici ou l�, comme il faut. Et �a fait avancer,
    # ou pas. C'est Game qui g�re tout. Mais il demande � la classe Tutorial comment
    # �a se passe pour lui. Si Tutorial demande de locker. Game va locker.
    # Y'a que 3 fa�ons d'avancer : start, le stimTutoNext, et choisir les bonnes chips
    # Et si on choisit pas les bonnes chips, �a fail direct. On peut plus du tout avancer.
    # Un avan�age provoque une �criture de texte dans la console, et du blink. C tout.

    # on met dans des propri�t�s "publiques" le texte et les blinks en cours.
    # La classe met � jour ses propri�t�s lorqu'elle doit avancer. (donc quand on
    # lui propose un avancement et qu'elle accepte).


