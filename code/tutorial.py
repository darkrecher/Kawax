#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax
"""

from common   import (securedPrint, pyRect, pyRectTuple)
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
    les bidules incluant : TELL_OBJECTIVE. Et peut-être d'autres trucs après.
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
        # et c'est tout à priori. La classe va stocker que ça.


class TutorialScheduler():
    """
    classe qui gère un tutorial. Y'a des steps. Dans un step, on décrit :
     - type de condition pour avancer au prochain step (stim, select) y'a pas de start.
       pas besoin.
     - liste des cases à sélectionner pour l'avançage (ou rien)
     - le texte à blablater pour le step actuel (ou rien)
     - le blink à blinker pour le step actuel (ou rien)
     - est-ce qu'il faut écrire l'objectif dans la console, ou pas.
    On fout tout ça dans un tuple, et basta.
    Si on veut que ça fasse rien au début, on met no text, no blink, et la condition qu'on veut.
    """

    def __init__(self, listTutStepsDescrip):
        """
        constructeur. (thx captain obvious)

        entrée :
            surfaceDest : Surface principale de l'écran, sur laquelle s'affiche le jeu.
        """
        self.listTutSteps = []
        #conversion coord->rect, et création de la liste des steps.
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
        # pas de condition ni rien. Faut que ça tombe juste.
        if self.totallyFailed:
            return False
        if self.tutStepCurrent.conditionType != STEP_COND_INTERACTIVE_TOUCH_SUCCESSED:
            return False
        securedPrint(u"success stim interactive sur le tuto")
        self.indexStep += 1
        self.tutStepCurrent = self.listTutSteps[self.indexStep]
        return True

    def takeStimTileSelected(self, selPath, selSuppl):
        """
        c'est des listes de pyRect à comparer à une liste de pyRect
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
        #youpi ! La sélection est bonne.
        self.indexStep += 1
        self.tutStepCurrent = self.listTutSteps[self.indexStep]
        return True

    def mustLockGameStimuli(self):
        """
        """
        # On aura peut être besoin de faire plus subtil que ça. Mais pour l'instant non.
        return (self.tutStepCurrent.conditionType == STEP_COND_STIM)

    def totallyFail(self):
        self.totallyFailed = True;

    def getFailText(self):
        return (u"Vous n'avez pas sélectionné les bonnes cases.",
                u"Débrouillez-vous tout seul maintenant !")

    # faut une classe externe, ou un overridage des classes actuelles ?
    # externe je dirais.
    # avec toutes les étapes. Et ici, dans le Game (voir GameBasic), on appelle des
    # fonctions de cette classe externe, ici ou là, comme il faut. Et ça fait avancer,
    # ou pas. C'est Game qui gère tout. Mais il demande à la classe Tutorial comment
    # ça se passe pour lui. Si Tutorial demande de locker. Game va locker.
    # Y'a que 3 façons d'avancer : start, le stimTutoNext, et choisir les bonnes chips
    # Et si on choisit pas les bonnes chips, ça fail direct. On peut plus du tout avancer.
    # Un avançage provoque une écriture de texte dans la console, et du blink. C tout.

    # on met dans des propriétés "publiques" le texte et les blinks en cours.
    # La classe met à jour ses propriétés lorqu'elle doit avancer. (donc quand on
    # lui propose un avancement et qu'elle accepte).


