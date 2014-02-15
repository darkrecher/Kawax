#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kawax version 0.1
Créé par Réchèr
Repo : https://github.com/darkrecher/Kawax
"""

LANGUAGE_FRENCH = 0
LANGUAGE_ENGLISH = 1

languageCurrent = LANGUAGE_FRENCH

MANUAL_TEXTS = {
    LANGUAGE_FRENCH : (
        u"jeu :",
        u"   S : valider      D : annuler sélection",
        u"   L : quitter",
        u"tutoriel :",
        u"   F : message suivant / refaire clignoter",
    ),
    LANGUAGE_ENGLISH : (
        u"game :",
        u"   S : validate      D : cancel selection",
        u"   L : quit",
        u"tutorial :",
        u"   F : next message / reblink tiles",
    ),
}

# TODO : ça marche pas ce truc là. Comment on écrit dans une variable globale ?
def changeLanguage(languageNew):
    #language.languageCurrent = languageNew
    languageCurrent = languageNew




