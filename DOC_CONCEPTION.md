# Document de conception de Kawax #

Ce document décrit le code du jeu vidéo Kawax. Pour chaque fichier de code, son utilité, ainsi que son interaction avec les autres fichiers, est expliquée.


## Avertissement ##

J'ai abandonné le développement de ce jeu. Le code n'est pas terminé, et contient beaucoup de parties non factorisée.

Vous constaterez également que le PEP8 a été foulé aux pieds, écartelé, équarri, et humilié en place publique par des petits enfants qui lui jetaient des cailloux. C'est la faute à l'entreprise dans laquelle je bossais à l'époque, qui m'a appris à coder en python avec les conventions de nommage du C++. Il va falloir faire avec !


## Déroulement des actions lors d'une partie type ##

### Initialisation générale, choix du mode de jeu ###

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

### Initialisation des trucs dans GameXXX ###

fonction `GameXXX.__init__` :

On va considérer que le mode de jeu choisi est sans tutoriel. (Les détails concernant les tutoriaux seront expliqués plus loin).

Les actions d'init sont réalisés par la fonction `__init__` elle-même, et par la fonction interne `initCommonStuff`

 - Récupération de la surface (objet pygame représentant une zone de dessin) dans laquelle doit se dessiner le jeu. C'est à dire la fenêtre à l'écran de l'ordinateur.

 - Création d'un objet `Console` : affichage de texte sur le côté droit de l'écran.

 - Premier dessin de la console à l'écran.

 - Création d'un objet `ManualnGame` : affichage des touches de jeu, en bas à gauche de l'écran.

 - Premier (et unique) dessin du manuel à l'écran.

 - Création d'un objet `StimuliStockerForGame` : récupération de tous les événements souris et clavier, traduction en "stimulis" de jeu.

 - Créaton d'un objet `pygame.time.Clock` : objet de la librairie pygame, permet de contrôler le nombre de FPS

 - Configuration de la gravité (dans quelle direction les objets du jeu tombent) et de la regénération (comment les pièces du jeu se regénèrent). On utilise pour cela des objets "crawler". Voir plus loin.

 - Création d'un objet `ArenaXXX` : à partir de la classe `ArenaBasic`, ou d'une classe héritée. Gère tout le bazar associé à l'aire de jeu.

 - Création d'un objet Selector : TODO : je sais plus exactement à quoi sert ce truc.

 - Ajout des éléments dans l'arène, au hasard (pièces, sucres, aspirine, touillettes, ...).

 - Premier dessin de l'arène.

 - Premier rafraîchissement de l'écran (bien que ça n'ait pas grand-chose à foutre dans l'init, puisque ça sera fait en boucle après).

Retour à `main.py`

Exécution de la fonction `GameXXX.playOneGame()`.

Cette fonction commence par faire quelques bidouilleries d'init :

 - Création d'un objet `ZapValidatorBase`, afin de définir une première valeur de brouzouf et de sucre que le joueur doit obtenir.

 - Affichage de la première étape du tutoriel, si il y a un tutoriel,

 - ou sinon, affichage de l'objectif à atteindre, selon le ZapValidator (en terme de brouzouf et de nombre de sucres). (désolé pour le "en terme de", ici , il me semble réellement approprié).

Puis, la fonction `GameXXX.playOneGame()` entre dans la game loop (boucle principale qui fait fonctionner le jeu).

### Game Loop ###

### Sélection des tiles ###

### "Zap" d'un ensemble d'éléments ###

### Gravité et regénération ###

### Stimuli lock/delock ###

### Interactive Touch ###

## Actions effectuées lors des mode de jeu spécifique ##

### Gestion des "gros objets" ###

### periodicAction (dans le mode touillette) ###

### Gravity Rift (dans le mode aspro)

### Interactive Touch sur les aspirines ###

### Tutoriel ###

## Vrac à détailler ##

Le code d'init des fonctions GameXXX est pourri. Y'en a dans __init__, dans initCommonStuff, et dans les __init__ des classes héritées. On pige rien.