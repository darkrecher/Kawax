# Document de conception de Kawax #

Ce document décrit le code du jeu vidéo Kawax. Pour chaque fichier de code, son utilité, ainsi que son interaction avec les autres fichiers, est expliquée.


## Avertissement ##

J'ai abandonné le développement de ce jeu. Le code n'est pas terminé, et contient beaucoup de parties non factorisée.

Vous constaterez également que le PEP8 a été foulé aux pieds, écartelé, équarri, et humilié en place publique par des petits enfants qui lui jetaient des cailloux. C'est la faute à l'entreprise dans laquelle je bossais à l'époque, qui m'a appris à coder en python avec les conventions de nommage du C++. Il va falloir faire avec !


## Déroulement des actions lors d'une partie type ##

Début du code de `main.py`

Import de `common.py`

Initialisation de la librairie pygame au début du fichier common.py. `pygame.init()`

Import de `language.py`

Initialisation de la langue en cours. (français)

Retour à `main.py`

Création de la fenêtre du jeu. (640x480 pixels)

Affichage du menu principal

Attente d'un appui de touche correspondant au choix d'un mode de jeu

Instanciaton de la classe GameXXX correspondant au mode de jeu choisi.

Il s'agit, soit de la classe `GameBasic`, soit d'une classe héritée de `GameBasic`. Elles commencent toutes par "Game".

TODO : blabla instanciation

Exécution de la fonction GameXXX.playOneGame(), qui démarre et déroule le jeu.

On va considérer que le mode de jeu choisi est sans tutoriel. (Les détails concernant les tutoriaux seront expliqués plus loin).


