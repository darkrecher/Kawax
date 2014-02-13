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
        "jeu :",
        "   S : valider      D : annuler sélection",
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

# TODO : ça marche pas ce truc là. Comment on écrit dans une variable globale ?
def changeLanguage(languageNew):
    #language.languageCurrent = languageNew
    languageCurrent = languageNew




