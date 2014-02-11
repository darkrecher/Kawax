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

LANGUAGE_FRENCH = 0
LANGUAGE_ENGLISH = 1

languageCurrent = LANGUAGE_FRENCH

MANUAL_TEXTS = {
    LANGUAGE_FRENCH : (
        "jeu :",
        "   S : valider      D : annuler s�lection",
        "   L : quitter",
        "tutoriel :",
        "   F : message suivant / refaire clignoter",
    ),
    LANGUAGE_ENGLISH : (
        "game :",
        "   S : validate      D : cancel selection",
        "   L : quit",
        "tutorial :",
        "   F : next message / reblink tiles",
    ),
}

# TODO : �a marche pas ce truc l�. Comment on �crit dans une variable globale ?
def changeLanguage(languageNew):
    #language.languageCurrent = languageNew
    languageCurrent = languageNew




