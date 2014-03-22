# Document de conception de Kawax #

Ce document décrit le code du jeu vidéo Kawax. 


## Avertissements ##

J'ai abandonné le développement de ce jeu. Le code n'est pas terminé, et contient beaucoup de parties non factorisée.

Vous constaterez également que le PEP8 a été foulé aux pieds, écartelé, équarri, et humilié en place publique par des petits enfants jetant des cailloux. C'est la faute à l'entreprise dans laquelle je bossais à l'époque, qui m'a appris à coder en python avec les conventions de nommage du C++. Il va falloir faire avec !

Une fois, au lycée, il y a eu un contrôle de Sciences Nat' (SVT pour les plus jeunes). J'avais énormément détaillé ma réponse à l'un des exercices, en expliquant pourquoi il fallait choisir cette solution là, quelle conditions il fallait respecter dans le choix de la solution, comment ça se justifiait, etc. Lorsque le prof a corrigé le contrôle, il a dit que "certains d'entre nous en avaient mis une tartine et qu'on n'y comprenait rien".

Ceci est ma vengeance.

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

Instanciaton de la classe GameXXX correspondant au mode de jeu choisi. Il s'agit, soit de la classe `GameBasic`, soit d'une classe héritée de `GameBasic`. Elles commencent toutes par "Game".

### Initialisation des trucs dans GameXXX ###

fonction `GameXXX.__init__` :

On va considérer que le mode de jeu choisi est sans tutoriel. (Les détails concernant les tutoriaux seront expliqués plus loin).

Les actions d'init sont réalisés par la fonction `__init__` elle-même, et par la fonction interne `initCommonStuff`

 - Récupération de la surface (objet pygame représentant une zone de dessin) dans laquelle doit se dessiner le jeu. Cette surface correspond à la fenêtre affichée à l'écran.

 - Création d'un objet `Console` : affichage de texte sur le côté droit de l'écran.

 - Premier dessin de la console à l'écran.

 - Création d'un objet `ManualnGame` : affichage des touches de jeu, en bas à gauche de l'écran.

 - Premier (et unique) dessin du manuel à l'écran.

 - Création d'un objet `StimuliStockerForGame` : récupération de tous les événements souris et clavier, traduction en "stimulis" de jeu.

 - Créaton d'un objet `pygame.time.Clock` : objet de la librairie pygame, permet de contrôler le nombre de FPS

 - Configuration de la gravité (dans quelle direction les objets du jeu tombent) et de la regénération (comment les pièces du jeu se regénèrent). On utilise pour cela des objets "crawler". Voir plus loin.

 - Création d'un objet `ArenaXXX` : à partir de la classe `ArenaBasic`, ou d'une classe héritée. Gère tout le bazar associé à l'aire de jeu : "game logic", affichage, déplacement des éléments lors de la gravité, ...

 - Création d'un objet Selector : gère les différents mode de sélection de tile : chemin principal, tuiles additionnelles, ... (une "tile" = une case dans l'aire de jeu).

 - Ajout des éléments dans l'arène, au hasard (pièces, sucres, aspirine, touillettes, ...).

 - Premier dessin de l'arène.

 - Premier rafraîchissement de l'écran (bien que ça n'ait pas grand-chose à foutre dans l'init, puisque ça sera fait en boucle après).

Retour à `main.py`

Exécution de la fonction `GameXXX.playOneGame()`.

Cette fonction commence par faire quelques bidouilleries d'init :

 - Création d'un objet `ZapValidatorBase`, afin de définir une première valeur de brouzouf et de sucre que le joueur doit obtenir.

 - Affichage de la première étape du tutoriel, si il y a un tutoriel,

 - ou sinon, affichage de l'objectif à atteindre, en terme de brouzouf et de nombre de sucres. (désolé pour le "en terme de", ici , il me semble réellement approprié). Le texte d'objectif à afficher est déterminé par le ZapValidator.

Puis, la fonction `GameXXX.playOneGame()` entre dans la game loop (boucle principale qui fait fonctionner le jeu).

### Game Loop ###

Le déroulement global de la game loop est le suivant :

 - Auto-ralentissage de la game loop pour qu'elle ne s'exécute au maximum que 60 frames par secondes.

 - Récupération des appuis de touches, mouvements de souris, appui/relâchage de bouton de souris par le `stimuliStocker` (instance de `StimuliStockerForGame`). Conversion de ces événements en "stimulis". ("Un stimuli", "des stimulis", et que les latinistes distingués ne viennent pas me faire chier).

 - Récupération de ces stimulis par la game loop, action sur divers membres de la classe `GameXXX` selon ces stimulis (cette étape sera détaillée plus loin).

 - Application de la gravité (certains éléments de l'aire de jeu descendront d'une case), et regénération de tiles (ajout de nouvelles pièces/sucres/autres dans les espaces laissés vides par la gravité). Cette action n'est exécutée qui s'il y a de la gravité à appliquer. De plus, elle n'est exécutée que toutes les 18 frames, afin de laisser le temps au joueur de voir ce qu'il se passe.

 - Exécution de la fonction `periodicAction`. Elle ne fait rien dans le mode GameBasic. Les autres modes de jeu peuvent y rajouter des choses.

 - Mises à jour du clignotement des tiles, si il y en a à faire clignoter. Cela n'arrive que durant les tutoriels, ce sera expliqué plus loin.

 - Redessin complet de l'aire de jeu, même si rien n'a changé. Oui c'est bourrin, oui j'avais prévu de faire un peu plus subtil, non je l'ai pas fait.

 - Rafraîchissement complet de l'écran. C'est bourrin aussi.

### Sélection des tiles ###

L'information "quelle tile est sélectionnée, et de quelle manière", est stockée un peu bizarrement. C'est parce que je voulais prévoir la possibilité d'avoir plusieurs joueurs sur la même aire de jeu, qui ferait chacun leurs sélections respectives.

Donc, cette info de sélection est stockée dans la classe Tile. (une arène contient un tableau en deux dimensions d'instances de Tile).

La classe Tile contient une liste appelée `dicPlayerSel` (on me dit dans l'oreillette que c'est confusionnant). Chaque élément de la liste correspond à la sélection d'un joueur. Concrètement, dans tout le code que j'ai fait, il n'y a qu'un joueur, et `dicPlayerSel` ne contient toujours qu'un et un seul élément.

Cet élément peut prendre l'une des trois valeurs suivantes :

 - SELTYPE_PATH : La tile est sélectionnée dans le chemin principal. Elle apparaît à l'écran encadrée en rouge.
 - SELTYPE_SUPPL : La tile est sélectionnée par une sélection additionnelle. Elle apparaît à l'écran encadrée en orange.
 - SELTYPE_NONE : La tile n'est pas sélectionnée. Elle apparaît à l'écran sans cadre.

Tout le blabla de ce chapitre a pour but de décrire de quelle manière la valeur de `dicPlayerSel` est modifiée, en fonction des actions effectuées par le joueur.  

À l'initialisation de ArenaXXX, On indique le nombre de joueur (c'est toujours 1). Le tableau de tile est créé. chaque Tile est donc initialisée avec son `dicPlayerSel` de un seul élément, valant SELTYPE_NONE.   

#### Lorsque le joueur clique sur la fenêtre du jeu : ####

L'objet `GameXXX.stimuliStocker` le détecte (événement `pygame.locals.MOUSEBUTTONDOWN`).

Le stimuliStocker détermine, à partir des coordonnées du curseur de la souris, si le clic s'est fait sur l'aire de jeu, et si oui, sur quelle tile. (fonction `determinePosArenaMouse`).

Si c'est oui, le stimuliStocker place les coordonnées de la tile dans la variable interne `posArenaMouse`.

Puis il ajoute les coordonnées de cette tile dans la liste `listPosArenaToActivate`. (fonction `activateTileWithMouse`). Dans ce cas, `listPosArenaToActivate` ne contient qu'un seul élément. 

Le code extérieur utilisera le contenu de `listPosArenaToActivate` pour en déduire ce qu'il doit faire.

D'autre part, le stimuliStocker retient les coordonnées de cette tile activée, dans la variable interne `posArenaPrevious`.

`listPosArenaToActivate` est remis à zéro à chaque appel à la fonction `resetStimuli`, c'est à dire à chaque itération de la game loop. (Donc, lorsque `listPosArenaToActivate` contient quelque chose, le code extérieur doit le prendre en compte tout de suite).

Si le joueur clique plusieur fois de suite sur la même tile, le stimuliStocker mettra plusieurs fois de suite la même coordonnée dans `listPosArenaToActivate`. Le code extérieur doit savoir s'en débrouiller.

#### Lorsque le joueur déplace la souris en maintenant le bouton appuyé : ####

Les actions décrites dans ce chapitre sont effectuées par la fonction `activateTileWithMouse`. C'est la même fonction qui gère les clics et les mouvements.

Le stimuliStocker détermine si les nouvelles coordonnées du curseur correspondent à une tile dans l'aire de jeu. Si ce n'est pas le cas, `posArenaPrevious` est réinitialisé à None, et `listPosArenaToActivate` reste vide.

Si les coordonnées du curseur correspondent à une tile, mais que c'est la même que `posArenaPrevious`, le stimuliStocker ne fait rien. `posArenaPrevious` conserve sa valeur. `listPosArenaToActivate` reste vide.

Mais si le curseur est sur une autre tile, alors le stimuliStocker effectue les actions suivantes :

 - Placement des coordonnées de la nouvelle tile dans la variable interne `posArenaMouse`.

 - Détermination de la liste de coordonnées effectuant un chemin de `posArenaPrevious` (exclue) jusqu'à `posArenaMouse` (inclue).

 - Enregistrement de cette liste dans `listPosArenaToActivate`.

 - Réactualisation de `posArenaPrevious`, qui devient `posArenaMouse`.

Si le joueur bouge la souris lentement, les coordonnées du curseur de souris ont peu changée depuis la dernière fois. `listPosArenaToActivate` ne contiendra qu'un seul élément : la nouvelle tile.

Si le joueur bouge la souris rapidement, `listPosArenaToActivate` peut contenir plusieurs éléments.

Si `posArenaPrevious` est très éloignée de `posArenaMouse`, il peut y avoir plusieurs chemins possible pour les relier. On décide arbitrairement de toujours prendre le chemin qui fait d'abord les déplacements en X, puis ceux en Y.

Si le joueur bouge très vite la souris, et que le curseur quitte l'aire de jeu, alors `posArenaPrevious` correspond à une tile qui n'est pas sur un bord, et `posArenaMouse` ne correspond pas à une position valide (None). Dans ce cas, on ne peut pas tracer de chemin, alors on réinitialise `posArenaPrevious` à None. Le joueur risque de voir un chemin de sélection qui ne semble pas être allé jusque là où il voulait. C'est de sa faute, il avait qu'à bouger la souris moins vite. 

Si le joueur maintient le curseur de souris appuyé, et revient vers l'aire de jeu mais par un autre endroit, alors `listPosArenaToActivate` contiendra une tile qui n'est pas forcément adjacente avec la dernière tile placée précédemment dans `listPosArenaToActivate`. Le code extérieur doit s'en débrouiller. 

#### Lorsque le joueur relâche le bouton de la souris ####

On réinitialise à None la variable `posArenaPrevious`.

On met à True la variable `mustStandBy`, qui sera utilisée par le code extérieur.

Comme pour `listPosArenaToActivate`, `mustStandBy` est réinitialisé à False à chaque itération de game loop. Donc si le code extérieur veut réagir à cette variable, il doit le faire tout de suite.

#### Description globale du rôle du stimuliStocker dans la sélection des tiles ####

 - Renvoyer `listPosArenaToActivate` : une liste de coordonnées, contenant 0, 1 ou plusieurs éléments, correspondant aux tiles que le joueur veut activer. Les valeurs successives contenues dans `listPosArenaToActivate` ne sont pas forcément adjacentes, et peuvent parfois re-indiquer la même chose (par exemple lorsque le joueur déplace son curseur à gauche, puis à droite).

 - Renvoyer `mustStandBy == True` lorsque le joueur relâche le bouton de souris.

Le stimulistocker n'a aucune idée de ce qu'il faut faire avec les tiles activées (sélection en chemin principal, sélection additionnelle, déselection, ...). C'est le code extérieur qui s'en occupera. 

#### Transmission des tiles qui ont été activées ####

Cette action est effectuée dans la game loop. Les tiles activées sont transmises à l'objet `selectorPlayerOne` (instance de `Selector`, contenus dans l'objet `GameXXX`).

En théorie, il pourrait y avoir plusieurs objets `Selector` dans `GameXXX`, qui prendraient leurs stimulis depuis différentes sources (on sait pas exactement lesquelles mais osef). En pratique, il n'y a toujours qu'un seul `Selector`, qui s'appelle `selectorPlayerOne`.

Les tiles activées sont transmises une par une, dans l'ordre de `listPosArenaToActivate`, au `selectorPlayerOne`, via la fonction `takeStimuliActivateTile(posSelected)`.

C'est important qu'elles soient transmises une par une, car ça simplifie les choses. Cela oblige à avoir le même comportement, que le joueur ait bougé son curseur doucement ou rapidement.

#### Traitement, par le selectorPlayerOne, d'une tile activée ####

le `Selector` possède une variable interne `selMode`, indiquant le mode de sélection en cours. Elle a 4 valeurs possibles :

 - SELMODE_PATH : le joueur est en train de tracer le chemin principal de sélection des tiles.
 - SELMODE\_SUPPL\_ADD : le joueur ajoute des tiles dans la sélection additionnelle.
 - SELMODE\_SUPPL\_REMOVE : le joueur retire des tiles dans la sélection additionnelle.
 - SELMODE\_STANDBY : le joueur ne fait rien.

Il reste un dernier mode : SELMODE_FORBIDDEN, mais je m'en sers jamais. (Je sais plus ce que je voulais faire avec, donc osef).

Au départ, le mode est SELMODE\_STANDBY. Dès la première activation de tile, on détermine un mode de sélection "utile". On garde ce mode au fur et à mesure des activations ultérieures.

Lorsque le joueur relâche le bouton de la souris, on reçoit le stimuli "Stand by" (fonction `Selector.takeStimuliStandBy`) et on revient en SELMODE\_STANDBY. 

#### Prise en compte de la première activation de tile, et détermination du mode de sélection ####

Ces actions sont réalisées par la fonction `takeStimuliActivateTile`, dans le bloc commençant par `if self.selMode == SELMODE_STANDBY:`, ainsi que par la fonction `tryToActivatePath`.

La détermination du mode de sélection dépend des tiles déjà sélectionnées, ainsi que de celle qui est activée. On teste les situations suivantes, dans cet ordre :

 - La tile activée est déjà sélectionnée dans le chemin principal. -> On déselectionne toutes les tiles du chemin principal, depuis la tile activée (exclue) jusqu'à la fin du chemin. Le mode devient SELMODE_PATH.

 - La tile activée est adjacente à la première tile du chemin principal. -> On ajoute cette tile au début du chemin. Le mode devient SELMODE_PATH.

 - La tile activée est adjacente à la dernière tile du chemin principal. -> On ajoute cette tile à la fin du chemin. Le mode devient SELMODE_PATH.

 - La tile activée est déjà sélectionnée dans la sélection additionnelle. -> On déselectionne cette tile. Le mode devient SELMODE\_SUPPL\_REMOVE.

 - La tile activée est ajacente à une tile sélectionnée (chemin principal ou sélection additionnelle). -> On sélectionne cette tile en sélection additionnelle. Le mode devient SELMODE\_SUPPL\_ADD.

 - Dans tous les autres cas. -> Déselection de toutes les tiles (chemin principal et sélection additionnelle). Création d'un nouveau path sur la tile activée. Le mode devient SELMODE_PATH. 

#### Prise en compte des activations de tile qui viennent après ####

Cette action est réalisée par la fonction `takeStimuliActivateTile` (les autres blocs `if`), et également par `tryToActivatePath`.

C'est comme lors de la première activation, mais en plus simple, car on a moins de cas possibles.

 - en mode SELMODE_PATH : On reprend les 3 premiers cas du chapitre précédent. Si on n'est dans aucun de ces 3 cas, on ne fait rien. Ça arrive lorsque le joueur active une tile non-adjacente au chemin principal (par exemple, le joueur sort le curseur de souris de l'aire de jeu, et y revient, mais par un autre endroit).

 - en mode SELMODE\_SUPPL\_ADD : Si la tile activée n'est pas sélectionnée, on l'on ajoute à la sélection additionnelle. Si elle est déjà sélectionnée, on ne fait rien.

 - en mode SELMODE\_SUPPL\_REMOVE :  Si la tile activée est dans la sélection additionnelle, on la déselectionne. Si elle est sélectionnée par le chemin principal, ou non sélectionnée, on ne fait rien.

#### Déselection en cascade ####

L'ensemble de la sélection doit toujours être constitué d'un seul bloc.

Lorsqu'une ou plusieurs tiles sont déselectionnées (quelle que soit les tiles, quel que soit la méthode de déselection), il y a un risque que des sélections additionnelles ne soient plus reliées au chemin principal. Dans ce cas, il faut automatiquement déselectionner toutes ces tiles non reliées. 

Cette action est réalisée par la fonction `Selector.unselectTileSupplAlone`. Je ne sais plus comment l'algo fonctionne en détail. Il y a quelques commentaires pour aider. Je laisse le lecteur explorer ça comme il le veut. 

#### Modification effective de la sélection d'une tile ####

Maintenant qu'on sait sur quelles tiles agir, et quel sélection/déselection appliquer dessus, il faut le faire. La méthode est un peu alambiquée, et passe à travers plusieurs fonctions.

Le `Selector` a tout ce qu'il faut pour lancer l'action : 
 - Le numéro du joueur (Concrètement, c'est toujours 0, car il n'y a qu'un joueur).
 - Une référence vers l'ArenaXXX
 - La position de la tile
 - Le type de sélection (PATH/SUPPL/NONE).

Une modification de sélection est effectuée par une imbrication d'exécution de fonction : 

 - `Selector.selectionChange`. En param : la position de la tile et le type de sélection.
 - `ArenaXXX.selectionChange`. En param : le numéro du joueur, la position de la tile et le type de sélection.
 - `Tile[position].selectionChange`.  En param : le numéro du joueur et le type de sélection.
 - Modification de `Tile.dicPlayerSel`. index : numéro du joueur. valeur : type de sélection.

### "Zap" d'un ensemble d'éléments ###

Le "zap" représente l'action effectuée par le joueur, après qu'il ait sélectionné des tiles, pour tenter de les faire disparaître. Le zap ne fonctionne pas forcément, ça dépend de la contrainte actuelle du zap, et des tiles sélectionnés.

#### La classe ZapValidator ####

Lors de l'initialisation, l'objet GameXXX a créé une instance héritant de `ZapValidator`. Cette classe, et toutes celles qui en héritent, doivent contenir 3 fonctions :

 - `getListStrDescription` : Renvoie une liste de chaînes de caractères, décrivant la contrainte à respecter pour que le zap soit réalisé. 
 - `getListStrLastTry` : Renvoie une liste de chaînes de caractères, décrivant la dernière tentative de zap du joueur, pourquoi ça a raté, etc.
 - `validateZap` : Prend en paramètre la sélection effectuée par le joueur (chemin principal + sélection additionnelle). Renvoie un booléen, indiquant si le zap a réussi ou pas.

Un `ZapValidator` doit être utilisé comme un one-shot. Une fois que le joueur a réussi le zap, il faut recréer un nouveau `ZapValidator`.

Bon, euh... tout ça pour dire que concrètement, je n'ai fait hériter qu'une seule fois le `ZapValidator`, en une classe appelée `ZapValidatorBase`.

Le `ZapValidatorBase` s'initialise avec une valeur de brouzouf et une valeur de sucre à atteindre. Lors de l'appel à `validateZap`, on additionne tous les brouzoufs et tous les sucres des tiles sélectionnées, si c'est égal, le zap est validé. Sinon, eh bien non.

`ZapValidatorBase.getListStrDescription()` indique le nombre de brouzouf et de sucre à sélectionner. `ZapValidatorBase.getListStrLastTry()` indique le nombre de brouzouf et de sucre que le joueur a dernièrement sélectionné.

#### Déroulement d'un zap ####

Lorsque le joueur appuie sur la touche "S", le `stimuliStocker` met à True la variable `stimuliTryZap`. L'objet GameXXX voit cette variable changer, et exécute la fonction interne `tryToZap`. (Auparavant, il y a un check à la con sur le lock, voir plus loin).

La fonction `tryToZap` récupère la sélection de tile et l'envoie au `ZapValidatorBase`. Si celui-ci répond que le zap n'est pas valide, on affiche dans la console 

Si le zap est valide, la fonction `tryToZap` exécute les actions suivantes :

 - Envoi d'un message au tutoriel, pour prévenir qu'un zap a été fait. (Le fonctionnement des tutoriels sera détaillé plus loin).
 - Exécution de `GameXXX.zapWin` : fonction qui ne fait pas grand-chose, mais qui peut être overridé dans d'autres classes GameXXX.
 - Refabrication d'un autre `ZapValidatorBase`, avec une autre contrainte sur les brouzoufs et les sucres (déterminées au hasard).
 - Envoi du zap à toutes les tiles sélectionnées. Ce qui enchaîne l'exécution imbriquée des fonctions suivantes :
	 - `GameXXX.arena.zapSelection()`. Cette fonction agit sur chaque position de la sélection :
		 - `GameXXX.arena.zapOnePos()`.
			 - `tile.zap()`
				 - `tile.chip.zap()`, sur la chip contenue dans la tile.
				 	- Cette fonction renvoie un nouvel objet Chip, correspondant au résultat du zap. 
				 	- Dans les faits, toutes les chip renvoient `ChipNothing`, c'est à dire un emplacement vide.
			 - L'objet arena remplace la chip de la tile par le résultat du zap. C'est cette action qui réalise effectivement la suppression des pièces et des sucres.   
 - (revenons à `tryToZap`). Déselection de toutes les tiles précédemment sélectionnées. (fonction `selectorPlayerOne.cancelAllSelection()`)
 - Si le jeu a besoin de se "stabiliser" : Déclenchement du délai de gravité et lock des stimulis. Cette action a pour but d'appliquer la gravité sur l'aire de jeu. (Voir plus loin).
 - Affichage, dans la console, de la contrainte du prochain zap, en appelant la fonction `ZapValidatorBase.getListStrDescription` Cet affichage n'est pas forcément effectué dans le cas des tutoriels. (Voir plus loin aussi). 

#### Trucs qui auraient pu servir pour le zap, et en fait non ####

(WIP)
force.
type.
chip renvoyée.

### Stimuli lock/delock ###

### Gravité et regénération ###

### Interactive Touch ###

## Actions effectuées lors des mode de jeu spécifique ##

### Gestion des "gros objets" ###

### periodicAction (dans le mode touillette) ###

### Gravity Rift (dans le mode aspro) ###

### Interactive Touch sur les aspirines ###

### Tutoriel ###

## Vrac à détailler ##

Le code d'init des fonctions GameXXX est pourri. Y'en a dans `__init__`, dans `initCommonStuff`, et dans les `__init__` des classes héritées. On pige rien.
