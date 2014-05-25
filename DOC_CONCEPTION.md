# Document de conception de Kawax #

## Avertissements ##

J'ai abandonné le développement de ce jeu. Le code n'est pas terminé, et contient beaucoup de parties non factorisée.

Vous constaterez également que le PEP8 a été foulé aux pieds, écartelé, équarri, et humilié en place publique par des petits enfants jetant des cailloux. C'est la faute à l'entreprise dans laquelle je bossais à l'époque, qui m'a appris à coder en python avec les conventions de nommage du C++. Il va falloir faire avec !

Une fois, au lycée, il y a eu un contrôle de Sciences Nat' (SVT pour les plus jeunes). J'avais énormément détaillé la réponse d'un des exercices, en expliquant pourquoi il fallait choisir cette solution, quelles conditions génériques celle-ci devait respecter, etc. Lorsque le prof a corrigé le contrôle, il a dit que "certains d'entre nous en avaient mis une tartine et qu'on n'y comprenait rien".

Ceci est ma vengeance.

## Diagramme de classe ##

![diagramme classe kawax](https://raw.githubusercontent.com/darkrecher/Kawax/master/doc_diverses/diagramme_pas_UML.png)

Ce diagramme ne respecte pas la norme UML. La seule fois où j'ai eu à m'en servir, c'était à l'école, et ensuite j'ai tout oublié parce que j'étais bourré.

Les flèches vertes indiquent des liens d'héritage.

Les cadres bleus avec des lignes pointillés indiquent des zooms sur une partie spécifique.

Les deux flèches en rond indiquent que la classe `GravityMovements` est créé dans `GameBasic` puis envoyée à `ArenaBasic`, qui fait des modifs dedans, la renvoie, et ainsi de suite.

## Déroulement des actions lors d'une partie type ##

### Initialisation générale, choix du mode de jeu ###

 - Début du code de `main.py`

 - Import de `common.py`

 - Initialisation de la librairie pygame au début du fichier common.py. `pygame.init()`

 - Import de `language.py`

 - Initialisation de la langue en cours. (français)

 - Retour à `main.py`

 - Création de la fenêtre du jeu. (640x480 pixels)

 - Affichage du menu principal

 - Attente d'un appui de touche correspondant au choix d'un mode de jeu

 - Instanciation de la classe correspondant au mode choisi. Il s'agit, soit de la classe `GameBasic`, soit d'une classe héritée (leur nom commencent tous par "Game"). **Dans la suite de cette documentation, la classe `GameBasic` et les classes héritées seront désignées par le terme générique `GameXXX`.**

### Initialisation des trucs dans GameXXX ###

fonction `GameXXX.__init__` :

On va considérer que le mode de jeu actuel est sans tutoriel.  [Voir par ici pour les détails concernant les tutoriaux](https://github.com/darkrecher/Kawax/blob/master/DOC_CONCEPTION.md#tutoriel).

Les actions d'init sont réalisés par la fonction `__init__` elle-même, et par la fonction interne `initCommonStuff`

 - Récupération de la surface (objet pygame représentant une zone de dessin) dans laquelle doit se dessiner le jeu. Cette surface correspond à la fenêtre affichée à l'écran.

 - Création d'un objet `Console` : permet l'affichage de texte sur le côté droit de l'écran.

 - Premier dessin de la console à l'écran.

 - Création d'un `ManualnGame` : permet l'affichage des touches du jeu, en bas à gauche de l'écran.

 - Premier (et unique) dessin du manuel à l'écran.

 - Création d'un `StimuliStockerForGame` : effectue la récupération de tous les événements souris et clavier, et la traduction en "stimulis" de jeu.

 - Création d'un `pygame.time.Clock` : objet de la librairie pygame, permet de contrôler le nombre de FPS.

 - Configuration de la gravité (dans quelle direction les pièces du jeu tombent) et de la regénération (comment les pièces du jeu se regénèrent). On utilise pour cela des objets "crawler". [Voir plus loin](https://github.com/darkrecher/Kawax/blob/master/DOC_CONCEPTION.md#gravit%C3%A9-et-reg%C3%A9n%C3%A9ration).

 - Instanciation d'une classe `ArenaBasic`, ou d'une classe héritée. Gère tout le bazar associé à l'aire de jeu : "game logic", affichage, déplacement des éléments lors de la gravité, ... **Dans la suite de cette documentation, les classes `ArenaBasic` et toutes les classes héritées seront désignées par le terme générique `ArenaXXX`.**

 - Création d'un Selector : gère les différents mode de sélection des cases de l'aire de jeu (chemin principal, sélections additionnelles).

 - Remplissage plus ou moins au hasard de l'aire de jeu : pièces, sucres, aspirine, touillettes, ...

 - Premier dessin de l'aire de jeu.

 - Premier rafraîchissement de l'écran (bien que ça n'ait pas grand-chose à foutre dans l'init, puisque ça sera fait en boucle après).

Retour à `main.py`

Exécution de la fonction `GameXXX.playOneGame()`.

Cette fonction commence par faire quelques bidouilleries d'init :

 - Création d'un `ZapValidatorBase`, afin de définir une première valeur de brouzouf et de sucre que le joueur doit obtenir.

 - Affichage de la première étape du tutoriel, s'il y en a un,

 - ou sinon, affichage de l'objectif à atteindre, (brouzouf et nombre de sucres). Le texte d'objectif à afficher est déterminé par le `ZapValidatorBase`.

Pour finir, la fonction `GameXXX.playOneGame()` entre dans la Game Loop, c'est à dire la boucle principale qui fait fonctionner le jeu.

### Game Loop ###

Le déroulement global de la Game Loop est le suivant :

 - Auto-ralentissage pour qu'elle ne s'exécute au maximum que 60 frames par secondes.

 - Récupération des appuis de touches, mouvements de souris, et clics de boutons de souris par le `stimuliStocker` (instance de `StimuliStockerForGame`). Conversion de ces événements en "stimulis". (Je dis : "un stimuli, des stimulis", et que les latinistes distingués ne viennent pas me faire chier).

 - Récupération de ces stimulis par la Game Loop. En fonction de ceux qui sont activés : actions sur divers membres de la classe `GameXXX`.

 - Application de la gravité, si nécessaire. Certains éléments de l'aire de jeu descendent d'une case.

 - Regénération de tiles, si nécessaire. De nouvelles pièces/sucres/autres sont ajoutés dans les espaces laissés vides par la gravité.

 - Ces deux actions (gravité et regénération) ne sont éventuellement exécutées que toutes les 18 frames, afin de laisser le temps au joueur de voir ce qu'il se passe.

 - Exécution de `periodicAction`. Cette fonction ne fait rien dans le mode `GameBasic`, mais les autres modes de jeu peuvent y rajouter des choses.

 - Mises à jour du clignotement des tiles, si nécessaire. Cela n'arrive que durant les tutoriels. [Voir plus loin](https://github.com/darkrecher/Kawax/blob/master/DOC_CONCEPTION.md#tutoriel).

 - Redessin complet de l'aire de jeu, même si rien n'a changé. Oui c'est bourrin, oui j'avais prévu de faire un peu plus subtil, non je ne l'ai pas fait.

 - Rafraîchissement complet de l'écran. (Bourrin aussi).

## Description détaillée des aspects du jeu ##

### Initialisation des classes GameXXX et ArenaXXX ###

L'initialisation est organisée de manière un peu bordelique. Les classes `GameXXX` possèdent toutes une fonction `__init__` et une fonction `initCommonStuff`.

`initCommonStuff` est définie dans la classe de base `GameBasic`. Elle n'est jamais héritée.

`__init__` doit systématiquement appeler `initCommonStuff` dès le début. Le code qui vient ensuite peut varier d'un héritage à l'autre.

J'ai fait comme ça pour pouvoir factoriser du code. Sauf que ça n'a pas vraiment été efficace, puisqu'à la fin des fonctions `GameXXX.__init`, on retrouve très souvent ce même mini-bloc :

    self.populateArena()
    self.arena.draw()
    pygame.display.flip()

Mais pas toujours, et pas forcément exactement sous cette forme. Ça me tirlapine de voir des répétitions de code. Il faut que je dise à mon cerveau d'arrêter de vouloir systématiquement factoriser, ça finit par être dangereux.

Pour les classes `ArenaXXX`, j'ai utilisé la même idée.

Sauf qu'à un moment, je sais pas ce que j'ai foutu, j'ai dû oublié, ou fumer une bière de trop. J'ai créé une fonction vide `ArenaBasic.start`, qu'on peut overrider dans les `ArenaXXX` héritées. Ça fait double emploi avec l'overridage de `__init__`.

Bref, c'est le bazar, et je ne saurais pas justifier pourquoi. Désolé !

### Structure d'une Arena ###

Les classes `ArenaXXX` possèdent une variable membre `matrixTile`. Il s'agit d'un tableau en 2D contenant des instances de `Tile` (une classe définie dans le fichier `tile.py`).

Une `Tile` = une case de l'aire de jeu.

Chaque tile contient une instance d'une classe `Chip`.

Une `Chip` = un objet dans l'aire de jeu : pièce de monnaie, sucre, mégot de clope, ...

Les différents types de chip sont définis en héritant la classe `Chip`. Tout est placé dans le fichier `coins.py`. (Le nom est mal choisi, désolé).

Lorsqu'on déplace un objet dans l'aire de jeu (par exemple, pour appliquer la gravité), on déplace la chip, mais pas la tile. La tile ne change jamais, et on n'en crée pas de nouvelle durant une partie.

### Initialisation d'une Arena ###

Les actions suivantes sont effectuées :

 - Création de `ArenaXXX.randomChipGenInit`. (Instance de `RandomChipGenerator`).

 - Remplissage de `matrixTile` avec des chips, plus ou moins aléatoirement. Cette action est effectuée par l'imbrication d'appels de fonction suivant :

	 - `ArenaBasic.createMatrixTile`.
	 	- pour chaque tile de l'aire de jeu : `ArenaBasic.createChipAtStart`.
		 	- `ArenaBasic.randomChipGenInit.chooseChip`.
			 	- Choix d'une chip au hasard, selon des coefficients de probabilité spécifiques. Renvoi de la chip.
	    - Création de la tile, en plaçant la chip nouvellement créée dedans.

Les probabilités de choix de chips sont définies par `listRandDistribution`, paramètre transmis au `RandomChipGenerator` lors de son initialisation. Chaque élément de cette liste est un tuple de 2 éléments :

 - Information de génération d'une chip.
 - Coefficient de probabilité (nombre entier).

La somme des coefs de tous les éléments de la liste peut faire n'importe quelle valeur, on s'en fout.

Une information de génération de chip est un tuple de x éléments. Le premier est un identifiant qui détermine quelle classe il faut instancier (`ChipCoin`, `ChipSugar`, `ChipClope`, ...). Les éventuels éléments suivants sont les paramètres à envoyer lors de l'instanciation de la classe. Par exemple, `ChipCoin` nécessite qu'on lui passe la valeur de la pièce. 

Le fait de mettre tout ce bazar dans les infos de génération permet de donner les coefs qu'on veut pour la probabilité d'apparition de la pièce de 1, celle de la pièce de 2, etc...

La regénération des chip après un zap, est également effectuée selon le même principe. C'est une classe `RandomChipGenerator` qui s'en occupe. Mais pas la même. Il s'agit de `ArenaXXX.randomChipGenAfterGrav`.

Donc potentiellement, on peut avoir des probabilités différentes pour la génération initiale des chips, et pour la génération durant la partie. Même si concrètement, j'ai mis les mêmes proba, parce que euh... voilà... c'est plus simple comme ça. Et puis c'est compliqué à équilibrer tout ce bazar.

### Sélection des tiles ###

L'information "quelle tile est sélectionnée, et de quelle manière", est stockée un peu bizarrement. C'est parce que je voulais prévoir la possibilité d'avoir plusieurs joueurs sur la même aire de jeu, qui feraient chacun leurs sélections respectives.

Or donc, cette info de sélection est stockée dans les `Tile`.

La classe `Tile` contient une liste appelée `dicPlayerSel` (on me dit dans l'oreillette que c'est confusionnant). Chaque élément de cette liste correspond à la sélection d'un joueur. Concrètement, dans tout le code que j'ai fait, il n'y a qu'un joueur, et `dicPlayerSel` ne contient toujours qu'un et un seul élément.

Cet élément peut prendre l'une des trois valeurs suivantes :

 - SELTYPE_PATH : La tile est sélectionnée dans le chemin principal. À l'écran, elle est dessinée avec un cadre rouge.
 - SELTYPE_SUPPL : La tile est sélectionnée par une sélection additionnelle. Elle est dessinée avec un cadre orange.
 - SELTYPE_NONE : La tile n'est pas sélectionnée. Elle est dessinée sans cadre.

Tout le blabla de ce chapitre a pour but de décrire de quelle manière le contenu de `dicPlayerSel` est modifié, en fonction des actions effectuées par le joueur.

À l'initialisation de `ArenaXXX`, on indique le nombre de joueur (c'est toujours 1). `matrixTile` est créé. chaque `Tile` est donc initialisée avec son `dicPlayerSel` de un seul élément, valant SELTYPE_NONE.

#### Lorsque le joueur clique sur la fenêtre du jeu : ####

L'objet `GameXXX.stimuliStocker` le détecte (événement `pygame.locals.MOUSEBUTTONDOWN`).

Le stimuliStocker détermine, à partir des coordonnées du curseur de la souris, si le clic s'est fait sur l'aire de jeu, et si oui, sur quelle tile. (fonction `determinePosArenaMouse`).

Si c'est oui, le stimuliStocker place les coordonnées de la tile dans la variable interne `posArenaMouse`.

Puis il ajoute les coordonnées de cette tile dans la liste `listPosArenaToActivate`. (fonction `activateTileWithMouse`). Dans ce cas, `listPosArenaToActivate` ne contient qu'un seul élément.

Le code extérieur utilisera le contenu de `listPosArenaToActivate` pour en déduire ce qu'il doit faire.

D'autre part, le stimuliStocker retient les coordonnées de cette tile activée, dans la variable interne `posArenaPrevious`.

`listPosArenaToActivate` est remis à zéro à chaque appel à la fonction `resetStimuli`, c'est à dire à chaque itération de la game loop. Donc, lorsque `listPosArenaToActivate` contient quelque chose, le code extérieur doit le prendre en compte tout de suite.

Si le joueur clique plusieur fois de suite sur la même tile, le stimuliStocker mettra plusieurs fois de suite la même coordonnée dans `listPosArenaToActivate`. Le code extérieur doit savoir s'en débrouiller.

#### Lorsque le joueur déplace la souris en maintenant le bouton appuyé : ####

Les actions effectuées suite à cette événement sont dans la fonction `activateTileWithMouse`. C'est la même fonction qui gère les clics et les mouvements.

Le stimuliStocker détermine si les nouvelles coordonnées du curseur correspondent à une tile dans l'aire de jeu. Si ce n'est pas le cas, `posArenaPrevious` est réinitialisé à None, et `listPosArenaToActivate` reste vide.

Si les coordonnées du curseur correspondent à une tile, mais que c'est la même que `posArenaPrevious`, le stimuliStocker ne fait rien. `posArenaPrevious` conserve sa valeur. `listPosArenaToActivate` reste vide.

Si le curseur est sur une autre tile, alors le stimuliStocker effectue les actions suivantes :

 - Placement des coordonnées de la nouvelle tile dans la variable interne `posArenaMouse`.

 - Détermination de la liste de coordonnées effectuant un chemin de `posArenaPrevious` (exclue) jusqu'à `posArenaMouse` (inclue).

 - Enregistrement de cette liste dans `listPosArenaToActivate`.

 - Réactualisation de `posArenaPrevious`, qui devient `posArenaMouse`.

Si le joueur bouge la souris lentement, les coordonnées du curseur de souris ont peu changée depuis la dernière fois. `listPosArenaToActivate` ne contiendra qu'un seul élément : la nouvelle tile.

Si le joueur bouge la souris rapidement, `listPosArenaToActivate` peut contenir plusieurs éléments.

Si `posArenaPrevious` est très éloignée de `posArenaMouse`, il peut y avoir plusieurs chemins possible pour les relier. On décide arbitrairement de faire d'abord le déplacement en X, puis celui en Y.

Si le joueur bouge très vite la souris, et que le curseur quitte l'aire de jeu, alors `posArenaPrevious` correspond à une tile qui n'est pas sur un bord, et `posArenaMouse` ne correspond pas à une position valide (None). Dans ce cas, on ne peut pas tracer de chemin, alors on réinitialise `posArenaPrevious` à None. Le joueur risque de voir un chemin de sélection qui ne semble pas être allé jusque là où il voulait. C'est de sa faute, il avait qu'à bouger la souris moins vite.

Si le joueur maintient le curseur de souris appuyé, et revient vers l'aire de jeu mais par un autre endroit, alors `listPosArenaToActivate` contiendra une tile qui n'est pas forcément adjacente avec la dernière tile placée précédemment dans `listPosArenaToActivate`. Le code extérieur doit s'en débrouiller.

#### Lorsque le joueur relâche le bouton de la souris ####

On réinitialise à None la variable `posArenaPrevious`.

On met à True la variable `mustStandBy`, qui sera utilisée par le code extérieur.

Comme pour `listPosArenaToActivate`, `mustStandBy` est réinitialisé à False à chaque itération de game loop. Donc si le code extérieur veut réagir à cette variable, il doit le faire tout de suite.

#### Description globale du rôle du stimuliStocker dans la sélection des tiles ####

 - Renvoyer `listPosArenaToActivate` : une liste de coordonnées, contenant 0, 1 ou plusieurs éléments, correspondant aux tiles que le joueur veut activer. Les tiles dans cette liste ne sont pas forcément adjacentes, et peuvent parfois re-indiquer la même chose (par exemple lorsque le joueur déplace son curseur à gauche, puis à droite).

 - Renvoyer `mustStandBy == True` lorsque le joueur relâche le bouton de souris.

Le stimulistocker n'a aucune idée de ce qu'il faut faire avec les tiles activées (sélection en chemin principal, sélection additionnelle, déselection, ...). C'est le code extérieur qui s'en occupera.

#### Transmission des tiles qui ont été activées ####

Cette action est effectuée dans la Game Loop. Les tiles activées sont transmises à l'objet `selectorPlayerOne` (instance de `Selector`, contenu dans l'objet `GameXXX`).

En théorie, il pourrait y avoir plusieurs objets `Selector` dans `GameXXX`, qui prendraient leurs stimulis depuis différentes sources. En pratique, il n'y a toujours qu'un seul `Selector`, qui s'appelle `selectorPlayerOne`.

Les tiles activées sont transmises une par une, dans l'ordre de `listPosArenaToActivate`, au `selectorPlayerOne`, via la fonction `takeStimuliActivateTile(posSelected)`.

C'est important qu'elles soient transmises une par une: Ça simplifie les choses, car ça oblige à avoir le même comportement, que le joueur ait bougé son curseur doucement ou rapidement.

#### Traitement, par le selectorPlayerOne, d'une tile activée ####

le `Selector` possède une variable interne `selMode`, indiquant le mode de sélection en cours. Elle a 4 valeurs possibles :

 - SELMODE_PATH : le joueur est en train de tracer le chemin principal de sélection des tiles.
 - SELMODE\_SUPPL\_ADD : le joueur ajoute des tiles dans la sélection additionnelle.
 - SELMODE\_SUPPL\_REMOVE : le joueur retire des tiles dans la sélection additionnelle.
 - SELMODE\_STANDBY : le joueur ne fait rien.

Il reste un dernier mode : SELMODE\_FORBIDDEN, mais je m'en sers jamais. (Je sais plus ce que je voulais faire avec, donc osef).

Au départ, le mode est SELMODE\_STANDBY. Dès la première activation de tile, on détermine un mode de sélection "utile" (c'est à dire, différent de SELMODE\_STANDBY). On garde ce mode durant les activations ultérieures.

Lorsque le joueur relâche le bouton de la souris, on reçoit le stimuli "Stand by" (fonction `Selector.takeStimuliStandBy`) et on revient en SELMODE\_STANDBY.

#### Prise en compte de la première activation de tile, et détermination du mode de sélection ####

Ces actions sont réalisées par la fonction `takeStimuliActivateTile`, dans le bloc commençant par `if self.selMode == SELMODE_STANDBY:`, ainsi que par la fonction `tryToActivatePath`.

La détermination du mode de sélection dépend des tiles déjà sélectionnées, ainsi que de celle qui est activée. On teste les situations suivantes, dans cet ordre :

 - La tile activée est déjà sélectionnée dans le chemin principal. -> On déselectionne toutes les tiles du chemin principal, depuis la tile activée (exclue) jusqu'à la fin du chemin. Le mode devient SELMODE_PATH.

 - La tile activée est adjacente à la première tile du chemin principal. -> On ajoute cette tile au début du chemin. Le mode devient SELMODE_PATH.

 - La tile activée est adjacente à la dernière tile du chemin principal. -> On ajoute cette tile à la fin du chemin. Le mode devient SELMODE_PATH.

 - La tile activée est déjà sélectionnée dans la sélection additionnelle. -> On déselectionne cette tile. Le mode devient SELMODE\_SUPPL\_REMOVE.

 - La tile activée est ajacente à une tile sélectionnée (chemin principal ou sélection additionnelle). -> On sélectionne cette tile en sélection additionnelle. Le mode devient SELMODE\_SUPPL\_ADD.

 - Dans tous les autres cas. -> Déselection de toutes les tiles (chemin principal et sélection additionnelle). Création d'un début de path sur la tile activée. Le mode devient SELMODE_PATH.

#### Prise en compte des activations de tile qui viennent après ####

Cette action est réalisée par la fonction `takeStimuliActivateTile` (les autres blocs `if`), et également par `tryToActivatePath`.

C'est comme lors de la première activation, mais en plus simple, car on a moins de cas possibles.

 - en mode SELMODE_PATH : On reprend les 3 premiers cas du chapitre précédent. Si on n'est dans aucun de ces 3 cas, on ne fait rien. Ça arrive lorsque le joueur active une tile non-adjacente au chemin principal (par exemple, le joueur sort le curseur de souris de l'aire de jeu, et y revient, mais par un autre endroit).

 - en mode SELMODE\_SUPPL\_ADD : Si la tile activée n'est pas sélectionnée, on l'ajoute à la sélection additionnelle. Si elle est déjà sélectionnée, on ne fait rien.

 - en mode SELMODE\_SUPPL\_REMOVE :  Si la tile activée est dans la sélection additionnelle, on la déselectionne. Si elle est sélectionnée par le chemin principal, ou non sélectionnée, on ne fait rien.

#### Déselection en cascade ####

L'ensemble de la sélection doit toujours être constitué d'un seul bloc.

Lorsqu'une ou plusieurs tiles sont déselectionnées (quelle que soit les tiles, quel que soit la méthode de déselection), il y a un risque que des sélections additionnelles ne soient plus reliées au chemin principal. Dans ce cas, il faut automatiquement déselectionner toutes ces tiles non reliées.

Cette action est réalisée par la fonction `Selector.unselectTileSupplAlone`. Je ne sais plus comment l'algo fonctionne en détail. Il y a quelques commentaires pour aider. Je laisse le lecteur explorer ça comme il le veut.

#### Modification effective de la sélection d'une tile ####

Maintenant qu'on sait sur quelles tiles agir, et quel sélection/déselection appliquer dessus, il faut le faire. L'action est un peu alambiquée, et passe à travers plusieurs fonctions.

Le `Selector` a tout ce qu'il faut pour lancer cette action :

 - Le numéro du joueur (Concrètement, c'est toujours 0, car il n'y a qu'un joueur).
 - Une référence vers ArenaXXX.
 - La position de la tile.
 - Le type de sélection (PATH/SUPPL/NONE).

La modification de sélection est effectuée par l'imbrication d'exécution de fonction suivante :

 - `Selector.selectionChange`. En param : la position de la tile et le type de sélection.
 	- `ArenaXXX.selectionChange`. En param : le numéro du joueur, la position de la tile et le type de sélection.
 		- `Tile[position].selectionChange`.  En param : le numéro du joueur et le type de sélection.
 			- Modification de `Tile.dicPlayerSel`. index : numéro du joueur. valeur : type de sélection.

### "Zap" d'un ensemble d'éléments ###

Le "zap" représente l'action effectuée par le joueur, après qu'il ait sélectionné des tiles, pour tenter de les faire disparaître. Le zap ne fonctionne pas forcément, ça dépend de la contrainte actuelle, et des tiles sélectionnés.

#### La classe ZapValidator ####

Cette classe, et toutes celles qui en héritent, doivent contenir 3 fonctions :

 - `getListStrDescription` : Renvoie une liste de chaînes de caractères, décrivant la contrainte à respecter pour que le zap soit réalisé.
 - `getListStrLastTry` : Renvoie une liste de chaînes de caractères, décrivant la dernière tentative de zap du joueur, pourquoi ça a raté, etc.
 - `validateZap` : Prend en paramètre la sélection effectuée par le joueur (chemin principal + sélection additionnelle). Renvoie un booléen, indiquant si le zap a réussi ou pas.

Un `ZapValidator` a accès à l'`ArenaXXX`, ce qui lui permet d'inspecter les tiles et les chips de l'aire de jeu. 

Cette classe doit être utilisée comme un one-shot. Une fois que le joueur a réussi le zap, il faut recréer un nouveau `ZapValidator`.

Bon, euh... tout ça pour dire que concrètement, je n'ai fait hériter qu'une seule fois le `ZapValidator`, en une classe appelée `ZapValidatorBase`.

Le `ZapValidatorBase` s'initialise avec une valeur de brouzouf et une valeur de sucre à atteindre. Lors de l'appel à `validateZap`, on additionne les brouzoufs et les sucres des tiles sélectionnées. Si ça correspond, le zap est validé. Sinon, eh bien non.

`ZapValidatorBase.getListStrDescription()` indique le nombre de brouzouf et de sucre à sélectionner. `ZapValidatorBase.getListStrLastTry()` indique le nombre de brouzouf et de sucre que le joueur a dernièrement sélectionné.

#### Déroulement d'un zap ####

Lors de l'initialisation, le `GameXXX` a créé une instance héritant de `ZapValidatorBase`. 

Lorsque le joueur appuie sur la touche "S", le `stimuliStocker` met à True la variable `stimuliTryZap`. Le `GameXXX` voit cette variable changer, et exécute la fonction interne `tryToZap`. (Auparavant, il y a un check à la con sur le lock, [voir les tutoriels](https://github.com/darkrecher/Kawax/blob/master/DOC_CONCEPTION.md#tutoriel)).

La fonction `tryToZap` récupère la sélection de tile et l'envoie au `ZapValidatorBase`. Si celui-ci répond que le zap n'est pas valide, on affiche dans la console la description du zap échoué.

Si le zap est valide, la fonction `tryToZap` exécute les actions suivantes :

 - Envoi d'un message au tutoriel, pour prévenir qu'un zap a été fait. (Il en a besoin. Mais pour le zap en lui-même, on s'en fout).
 - Exécution de `GameXXX.zapWin` : fonction qui ne fait pas grand-chose, mais qui peut être overridée.
 - Refabrication d'un autre `ZapValidatorBase`, avec une autre contrainte sur les brouzoufs et les sucres.
 - Envoi du zap à toutes les tiles sélectionnées. Ce qui enchaîne l'exécution imbriquée des fonctions suivantes :
	 - `GameXXX.arena.zapSelection()`.
		 - Sur chaque position de la sélection : `GameXXX.arena.zapOnePos()`.
			 - `tile.zap()`
				 - sur la chip contenue dans la tile : `tile.chip.zap()`.
				 	- Cette fonction renvoie un nouvel objet Chip, correspondant au résultat du zap.
				 	- Dans les faits, toutes les chip renvoient `ChipNothing`, c'est à dire un emplacement vide.
			 - L'`arena` remplace la chip de la tile par le résultat du zap. C'est cette action qui réalise effectivement la suppression des pièces et des sucres.
 - (retour à `tryToZap`). Déselection de toutes les tiles précédemment sélectionnées. Fonction `selectorPlayerOne.cancelAllSelection()`.
 - Si le jeu a besoin de se "stabiliser" : déclenchement de la gravité et lock des stimulis. [Voir plus loin](https://github.com/darkrecher/Kawax/blob/master/DOC_CONCEPTION.md#gravit%C3%A9-et-reg%C3%A9n%C3%A9ration).
 - Affichage, dans la console, de la contrainte du prochain zap, en appelant la fonction `ZapValidatorBase.getListStrDescription`. Cet affichage n'est pas forcément effectué dans le cas des tutoriels. ([Voir les tutoriels, donc](https://github.com/darkrecher/Kawax/blob/master/DOC_CONCEPTION.md#tutoriel)).

#### Trucs qui auraient pu servir pour le zap, et en fait non ####

Durant l'exécution du zap sur chaque chip, on transmet deux paramètres :

 - `zapType` : correspond à la façon dont la tile a été sélectionnée. `ZAP_PATH` : chemin principal. `ZAP_SUPPL` : sélection additionnelle.
 - `zapForce` : force du zap. Concrètement, on met toujours 1.

Ces deux valeurs pourraient être utilisées par la méthode `Chip.zap()`, pour des cas spécifiques. Exemple :

 - Une chip avec des points de vie. Si le jeu permet, d'une manière ou d'une autre, de faire des zap de force supérieure à 1, on enlève plusieurs points de vie d'un coup.
 - Une chip qui ne disparaît que si elle est sélectionnée dans le chemin principal.

La fonction `Chip.zap()` renvoie toujours une instance de `ChipNothing`, mais elle pourrait faire d'autre chose. Par exemple : une chip qui se transforme en une autre.

La fonction peut également renvoyer `None`, pour signaler de ne pas faire de remplacement. Ça peut servir dans le cas des chips à points de vie. Le zap modifie une valeur interne de la chip, mais ne remplace pas la chip elle-même.

### Stimuli lock/delock ###

Il s'agit d'un truc pas très bien géré, et qui a provoqué plein de bugs de partout. Je pense les avoir tout corrigé, mais rien n'est sûr.

Objectif initial du lock/delock : empêcher le joueur de sélectionner des tiles, et de les zapper, durant les moments où le jeu est occupé à autre chose, ce qui aurait provoqué des risques de chambardements intempestifs.

Le jeu est "occupé à autre chose" dans les cas suivants :

 - En cours de stabilisation : la gravité est en cours, ou bien des chips sont en cours de regénération.
 - En mode tutoriel : du texte explicatif est affiché dans la console, et le joueur doit appuyer sur la touche "F" afin de passer à l'étape suivante.

Le lock a lieu dans la classe `Selector`, et non pas, contrairement à ce qu'on aurait pu croire, dans la classe `StimuliStockerForGame`. (Oui enfin vous croyez ce que vous voulez, moi je m'en fous en fait).

Pour effectuer un lock, il faut exécuter la fonction `GameXXX.selectorPlayerOne.setStimuliLock(True)`. Pour l'enlever, c'est pareil, avec le paramètre False.

Lorsque le lock est mis en place, les clics du joueur ne sont plus pris en compte pour la sélection des tiles. La fonction `Selector.takeStimuliActivateTile` ne fait plus rien.

Par contre, les clics "d'interactive touch" restent pris en compte, même lorsque le lock est activé. Ce n'est peut-être pas tout à fait logique. Euh... Hem... Passons.

Les moments d'activation/suppression du lock sont détaillés dans d'autre partie de cette documentation. Voir partie ["Gravité"](https://github.com/darkrecher/Kawax/blob/master/DOC_CONCEPTION.md#gravit%C3%A9-et-reg%C3%A9n%C3%A9ration) et ["Tutoriel"](https://github.com/darkrecher/Kawax/blob/master/DOC_CONCEPTION.md#tutoriel)).

### Gravité et regénération ###

Ces actions sont gérées par les fonctions et variables suivantes :

 - `GameXXX.needStabilization()`
 - `GameXXX.handleGravity()`
 - `GameXXX.applyGravity()`
 - `GameXXX.gravityCounter`
 - `GameXXX.gravityMovements`
 - `arenaXXX.determineGravity()`
 - `arenaXXX.applyGravity()`
 - `arenaXXX.regenerateAllChipsAfterOneGravity()`
 - `arenaXXX.hasChipToRegenerate()`
 - `ArenaCrawler` (classe définie dans `crawler.py`).

Lorsque l'aire de jeu nécessite qu'on lui applique une ou plusieurs fois la  gravité, ou lorsqu'il faut regénérer des chips, on dit qu'elle est dans un état "instable".

#### Première vérification de l'instabilité ####

Cette vérification est effectuée après un zap (dans la fonction `GameXXX.tryToZap()`, et également après un Interactive Touch qui a fonctionné (dans la fonction `GameXXX.playOneGame`, juste après l'appel à `stimuliInteractiveTouch`).

Les Interactive Touches peuvent modifier l'aire de jeu, c'est pour ça qu'on fait la vérif aussi à ce moment là. Par exemple : on clique sur un aspirine, ça le supprime, donc il faut appliquer la gravité, etc.

La vérification d'instabilité est effectuée par la fonction `GameXXX.needStabilization`. Si elle renvoie True, l'état est instable. Sinon, il est stable.

Cette fonction a également un autre rôle : définir la variable `GameXXX.gravityMovements`, décrivant les mouvements de chips à effectuer lors de la prochaine gravité. Cette variable est une instance de `GravityMovements`. [Voir plus loin pour une explication détaillée de son fonctionnement interne](https://github.com/darkrecher/Kawax/blob/master/DOC_CONCEPTION.md#fonctionnement-de-gravitymovements).

`GameXXX.gravityMovements` peut être None, ou définie avec une liste de mouvements vide. Dans les deux cas il n'y a pas de gravité à appliquer.

Lorsque `GameXXX.needStabilization` renvoie True, le code extérieur qui l'a appelée doit effectuer les deux actions suivantes :

 - Locker les stimulis.
 - Définir `gravityCounter` à `DELAY_GRAVITY`, ce qui permettra d'appliquer la gravité/regénération ultérieurement. (la gravité n'est pas appliquée tout de suite lors de la première vérification).

#### Application des gravités successives ####

Le fait de devoir continuer ou pas d'appliquer les gravités est déterminé par `GameXXX.gravityCounter`. À chaque cycle de jeu, la fonction `GameXXX.playOneGame` décrémente cette variable de 1. lorsqu'elle atteint 0, la fonction `GameXXX.handleGravity` est appelée. Celle-c effectue les actions suivantes :

 - Exécution de `GameXXX.applyGravity`
	 - Exécution de `ArenaXXX.applyGravity`, en lui passant en paramètre `GameXXX.gravityMovements`, qui a été défini précédemment.
		 - Application de la gravité. Déplacement effectif des chips dans l'aire de jeu, pour les faire tomber d'une case.
     - Exécution de `ArenaXXX.regenerateAllChipsAfterOneGravity`. Création de nouvelle chips, en haut de l'aire de jeu, dans les emplacements laissés vides.
 - Exécution de `GameXXX.needStabilization`. Si la fonction renvoie True, on redéfinit `gravityCounter` à `DELAY_GRAVITY`, pour réappliquer une prochaine gravité dans quelques cycles.
 - L'appel à `needStabilization` a remis à jour `GameXXX.gravityMovements`, avec de nouvelles valeurs correspondant aux mouvements de la prochaine gravité à appliquer.

#### Fin de gravité ####

Si `GameXXX.needStabilization` renvoie False, on laisse `GameXXX.gravityCounter` à 0. Les prochains cycles de jeu déduiront, de cette variable à 0, qu'il n'y a plus de gravité à gérer. `GameXXX.handleGravity` ne sera plus appelée.

En fin de gravité, il faut délocker les stimulis, puisqu'on les avait précédemment lockés. Enfin... Sauf si le `tutorialScheduler` veut conserver le lock. ["Voir plus loin"](https://github.com/darkrecher/Kawax/blob/master/DOC_CONCEPTION.md#tutoriel), car tout ce bazar est déjà assez compliqué et entrelacé comme ça.

D'autre part, lorsque `needStabilization` renvoie False, elle est censée avoir défini `GameXXX.gravityMovements` à None, ou n'avoir mis aucun mouvement dedans. (On s'en fout, on ne le contrôle pas, mais je tenais à le préciser).

#### Regénération sans gravité ####

Lorsqu'en exécute une gravité une fois, on regénère tout de suite après les chips aux emplacements laissés vides, dans la ligne du haut. Cette action est effectuée par la fonction `ArenaXXX.regenerateAllChipsAfterOneGravity`.

On pourrait donc penser qu'à aucun moment, on n'ait besoin de juste regénérer des chips. Si pas de gravité -> pas d'emplacements vides en haut de l'aire de jeu -> pas besoin de regénération.

Eh bien non. Car il y a également le cas où le joueur a zappé des chips uniquement dans la ligne du haut.

Cette situation se règle avec l'enchaînement d'actions suivants :

 - Il y a eu un zap ou un Interactive Touch.
 - Exécution de `GameXXX.needStabilization`.
	 - Détermination de `GameXXX.gravityMovements`. On s'aperçoit qu'il n'y a aucun mouvement à effectuer.
	 - Appel de la fonction `ArenaXXX.hasChipToRegenerate`. La fonction répond qu'il y a des chips à regénérer.
 - Du coup, `GameXXX.needStabilization` répond True. Il y a des choses à faire pour stabiliser l'aire de jeu, bien qu'il n'y ait pas de gravité à appliquer.
 - Le code extérieur fixe `gravityCounter` à `DELAY_GRAVITY`.
 - `playOneGame` décrémente `gravityCounter`, et quelques cycles plus tard, `handleGravity` est appelé.
	 - `GameXXX.applyGravity` est appelé.
		 - `ArenaXXX.applyGravity` est appelé, avec `gravityMovements` ne contenant aucun mouvement. La fonction ne fait rien.
		 - `arena.regenerateAllChipsAfterOneGravity` est appelé. Les chips de la ligne du haut sont regénérées.
		 - À nouveau, appel de `GameXXX.needStabilization`, qui devrait répondre False. On arrête les gravités et on délocke les stimulis.

#### Fonctionnement de gravityMovements ####

La classe `GravityMovements`, définie dans le fichier `gravmov.py`, a pour vocation d'être la plus générique possible. C'est à dire qu'elle gère des mouvements de gravité dans n'importe quelle direction (les chips pourraient tomber vers le haut, vers la gauche, ...).

Elle peut également gérer des mouvements de gravité avec des "gros objets" (par exemple, les touillettes).

Dans une aire de jeu à gros objets, il peut y avoir plusieurs mouvements de gravité indépendants, sur une même colonne. Exemple, avec un zap en forme de "C" :

    0 0 0 0 0
    0 0 0 0 0
    . . 0 0 0
    . 1 0 0 0
    . +++++++
    . 2 0 0 0
    . . 0 0 0
    0 5 0 0 0

    0, 1, 2, 5 = une pièce, un sucre ou n'importe quoi d'autre.
    . = une tile vide, car on vient tout juste de la zapper.
    + = une touillette.

Dans la deuxième colonne, Les deux 0 du haut vont tomber. Le 1 ne va pas tomber, car il est retenu par la touillette. Le 2 va tomber. Le 5 ne va pas tomber, car il est tout en bas.

La classe `GravityMovements` doit être capable de gérer ce genre de subtilité.

Les infos stockées par cette classe ne peuvent servir que pour l'application d'une seule gravité (chaque chip ne se déplacera que d'une seule case). Pour faire la gravité suivante il faut repartir d'une nouvelle instance de `GravityMovements` et remettre des infos dedans à partir du début.

Comme il faut gérer n'importe quelle direction, on ne raisonne pas en coordonnées X et Y, mais en coordonnés primaire (les lignes/colonnes le long desquelles s'appliquent la gravité) et en coordonnées secondaires (la coordonnée qui va augmenter ou diminuer de 1).

La classe `GravityMovements` contient la variable `dicMovement`. Il s'agit d'un dictionnaire contenant les infos suivantes :

 - clé : une coordonnée primaire.

 - valeur : une liste de tuple de deux éléments. Chaque tuple définit un "segment gravitant". Avec :
	 - premier élément : coordonnée secondaire du début du segment. Cela correspond toujours à l'emplacement vide qui permet de démarrer la gravité.
	 - second élément : coordonnée secondaire de fin du segment. (Non incluse dans la gravité, je fais comme pour les ranges et les slices python qui n'incluent pas le dernier élément).

Si on reprend l'exemple précédent, après analyse complète de l'aire de jeu, prise en compte de la touillette, et dans le cas d'une gravité vers le bas, on devrait avoir un `GravityMovements.dicMovement` comme suit :

    {
        0: [    # pour la colonne de gauche. X = 0

            (2,     # coord (X=0, Y=2) :
                    # emplacement vide juste en dessous des deux chip "0".

             -1     # coord (X=0, Y=-1) :
                    # Dernier élément du segment, non inclu. 
                    # C'est une case hypothétique, au dessus de l'aire de jeu.
            ),
        ],
        1: [    # pour la colonne suivante. X = 1

            (2,     # Pareil. Les deux chips "0" du haut vont tomber.
             -1),

            (6,     # Et en plus, la chip "2" va tomber,
             4),    # à cause du vide en (X=1, Y=6)
                    # Le dernier élément n'est pas inclus (coord Y = 4)
        ]
    }

Lorsque la gravité est vers le bas, le premier élément du tuple de chaque segment gravitant est toujours strictement supérieur au second élément. Lorsque la gravité est vers le haut, c'est le contraire.

Lorsque la gravité est vers la droite : premier élément > second élément.
Lorsque la gravité est vers la gauche : second élément > premier élément.

Pour gérer tout ça, la classe `GravityMovements` dispose des fonctions suivantes :

 - `__init__`, en précisant le type de gravité.

 - `cancelAllMoves` : vidage du dictionnaire `dicMovement`.
 
 - `addSegmentMove` : ajout d'un segment gravitant. Attention, la fonction ne fusionne pas les segments existants avec le nouveau. On peut donc se retrouver dans une situation de ce type : { 0 : [ (3, -1), (2, 1) ] }. Ce serait tout à fait incohérent et ce n'est jamais censé arriver. Donc il faut faire attention à ce qu'on envoie lors des appels successifs à `addSegmentMove`.

 - `cancelGravity` : annulation de la gravité pour une position spécifique. Cette fonction peut raccourcir un segment et/ou en supprimer d'autres. Elle n'est utilisée que dans les arènes contenant des gros objets. [Voir explication de `ArenaBigObject`](https://github.com/darkrecher/Kawax/blob/master/DOC_CONCEPTION.md#gestion-de-la-gravit%C3%A9).

 - `isInGravity` : indique, pour une position donnée, si elle se trouve dans un segment gravitant ou pas. (Renvoie True/False).

 - `isListInGravity` : indique, pour une liste de position donnée, si elles sont toutes dans un segment gravitant (`IN_GRAVITY_YES`), si certaines d'entre elles le sont (`IN_GRAVITY_PARTLY`), ou si aucune d'entre elles ne le sont (`IN_GRAVITY_NO`).

 - `removeEmptyListSegment` : fonction à appeler après avoir exécuté un ou plusieurs `cancelGravity`. Permet de supprimer les coordonnées primaires n'ayant plus aucun segment gravitant. Par exemple, si `dicMovement` vaut { 0 : [ (1, -1) ], 3 : [] }. Après exécution de `removeEmptyListSegment`, on aura : { 0 : [ (1, -1) ] }.

#### Détermination des mouvements de gravité ####

La détermination des chips subissant une gravité (donc, le remplissage d'un objet `GravityMovements`) est effectué par la fonction `arenaXXX.determineGravity()`

L'algorithme est le suivant (dans le cas d'une gravité vers le bas) :

Pour chaque colonne, on parcourt toutes les chips, en allant du bas vers le haut:

 - On passe les premières chips non vides. Elles ne tomberont pas. `currentState = SKIP_NOT_FALLING_TILE`
 - Dès qu'on rencontre une chip vide, on change d'état. `currentState = ADVANCE_NOTHING_TILE`. Et on continue d'avancer tant qu'on est dans les chips vides.
 - Si on rencontre une chip qui ne peut pas tomber (ça existe pas dans le jeu, mais ça pourrait). On oublie ce qu'on a fait, et on revient à `currentState = SKIP_NOT_FALLING_TILE`.
 - Si on rencontre une chip non vide, qui peut tomber, on retient la coordonnée de l'emplacement précédent (emplacement vide qui permet de démarrer la gravité). Et `currentState = ADVANCE_CONSEQUENT_TILE`.
 - On continue d'avancer tant qu'on rencontre des chips non vides acceptant de tomber.
 - Lorsqu'on rencontre autre chose, ou qu'on arrive tout en haut de l'aire de jeu, on a trouvé un segment gravitant. On l'enregistre dans un `GravityMovements`, avec :
 	- coord primaire = X de la colonne courante.
 	- coord secondaire de début du segment = Y de l'emplacement vide précédemment retenu.
 	- coord secondaire de fin du segment = Y actuel.
 - On revient à `currentState = SKIP_NOT_FALLING_TILE` ou `currentState = ADVANCE_NOTHING_TILE` selon qu'on est sur une chip vide ou une chip qui n'accepte pas la gravité.

Pour la gravité du mode aspro (gravity rift) : [voir plus loin](https://github.com/darkrecher/Kawax/blob/master/DOC_CONCEPTION.md#gravity-rift).

#### La classe ArenaCrawler ####

Cette classe est définie dans le fichier `crawler.py`. Elle permet de parcourir les positions d'une aire de jeu dans le sens qu'on veut, et de passer directement à la ligne/colonne suivante.

Un `ArenaCrawler` se contente de renvoyer des coordonnées (sous forme de classes `pygame.Rect`), correspondant à des positions successives. Il connaît la taille de l'aire de jeu, mais pas l'aire de jeu en elle-même, ni son contenu. Il n'analyse pas les tiles ou les chips. C'est au code extérieur de faire ça.

On utilise la notion de coordonnée primaire/secondaire. Lorsque la coordonnée primaire est X, les "gros" changements de coordonnées seront sur le X. C'est à dire que le crawler se déplacera le long des colonnes. Il parcourra tous les Y d'une colonne, puis modifiera son X et passera à la colonne suivante, et ainsi de suite.

Plus précisément, on ne spécifie pas des **coordonnées** primaire/secondaire, mais des **directions** primaire/secondaire.

Si la direction primaire est LEFT ou RIGHT, la coordonnée primaire est X. Si la direction primaire est UP ou DOWN, la coordonnée primaire est Y. Pareil pour le secondaire.

La coordonnée primaire et la coordonnée secondaire doivent être différente. Sinon c'est n'importe quoi.

Exemple d'ordre de parcours de l'aire de jeu, pour une taille de X=3, Y=5.

    direction primaire = DOWN. direction secondaire = RIGHT.

    Y    0   1   2
    |    3   4   5
         6   7   8
         9  10  11
        12  13  14

    X ->

    direction primaire = RIGHT. direction secondaire = UP
         4   9  14
         3   8  13
         2   7  12
         1   6  11
         0   5  10

    etc.

Pour utiliser un `ArenaCrawler`, il faut l'instancier, le configurer et le démarrer :

 - Instanciation : `__init__`, en spécifiant la taille de l'aire de jeu.
 - Configuration : `ArenaCrawler.config()`, en spécifiant la direction primaire et la secondaire.
 - Démarration : `ArenaCrawler.start()`

Le crawler est alors initialisé à sa première position.

Pour avancer, il faut utiliser les fonction suivantes :

 - `ArenaCrawler.crawl()` : avance d'une position. Passe automatiquement à la ligne/colonne suivante si on est arrivée au bout de la ligne/colonne en cours.
 - `ArenaCrawler.jumpOnPrimCoord()` : passe directement à la ligne/colonne suivante, même si on n'a pas fini celle en cours.

Exemple :

    a = ArenaCrawler( (3, 5) )  # taille X = 3, taille Y = 5
    a.config(DOWN, RIGHT)
    a.start()
    a.crawl()
    a.jumpOnPrimCoord()
    a.jumpOnPrimCoord()
    a.crawl()
    a.crawl()
    a.crawl()
    a.crawl()
    a.jumpOnPrimCoord()
    a.jumpOnPrimCoord()  # La fonction renvoie False. On doit s'arrêter là.

    Positions parcourues :
        0   1   .
        2   .   .
        3   4   5
        6   7   .
        8   .   .

Durant le crawling, on peut accéder à diverses variables, renseignant la position actuelle, ce qu'il vient de se passer, etc . Ces variables sont pertinentes dès l'appel à `start`, avant même d'avoir exécuté un premier `crawl` ou un premier `jumpOnPrimCoord`. Il s'agit des variables suivantes :

 - `posCur` : objet `pygame.Rect`. Position courante.
 - `posPrev` : objet `pygame.Rect`. Position précédente (si on a exécuté un `jumpOnPrimCoord`, `posPrev` se trouve sur la ligne/colonne précédente.
 - `coP` : entier. coordonnée primaire courante.
 - `coS` : entier. coordonnée secondaire courante.
 - `crawledOnPrimCoord` : booléen. Indique si on vient de changer de coordonnée primaire.
 - Les fonctions `crawl` et `jumpOnPrimCoord` renvoient un booléen. Si celui-ci est True, on est sur une position valide. Si il est False, la position courante est invalide, car on est arrivé au bout de l'aire de jeu. Dans ce cas, on ne devrait pas consulter les variables ci-dessus, elles contiennent des informations non utilisables.

Il est possible de rappeler `crawl` et `jumpOnPrimCoord` après que l'une d'elles ait renvoyé False. Mais les résultats récupérés sont inutilisables. (En fait, le crawler devrait s'arrêter, ou carrément balancer une exception).

#### Configuration de gravité par les crawlers ####

La détermination de la gravité, son application, et la regénération des chips après gravité sont toutes gérés avec des `ArenaCrawler`.

Selon le sens dans lequel on parcourt l'aire de jeu pour effectuer ces tâches, on peut appliquer la gravité dans la direction qu'on veut.

La configuration des crawlers en fonction de la direction de gravité souhaitée est effectuée dans `GameXXX.initCommonStuff`, (à la fin de la fonction). On se sert de `DICT_GRAVITY_CONFIG`, défini dans `gambasic.py`.

Tous les modes de jeu actuels utilisent une gravité vers le bas (sauf le mode aspro, mais sa gravité vers la gauche est gérée différemment). Tout ça pour dire que la super-généricité de code que j'ai mise en place n'est pas utilisée. Mais ça pourrait. J'avais testé d'autres direction de gravité, ça marchait. (Disons que ça a marché à un certain moment de la vie du programme).

Pour une explication détaillée de "comment ça marche dans des directions autres que vers le bas" : voir code. Si j'explique avec du texte, ça va être super long et compliqué. C'est presque plus simple de regarder le code.

"_Algorithme : voir code_". J'adore quand ce genre de grossiereté est écrite dans de la documentation. Et je viens de le faire. Tant pis !

### Interactive Touch ###

Les "Interactive Touches" ont pour but d'exécuter des actions spécifiques dans l'arène, lorsque le joueur clique sur l'une des chips. Ça peut permettre un tas de choses, en fonction d'un tas d'autres choses : téléportation de chips, augmentation de la valeur d'une pièce, bombes, ...

Les Interactive Touches sont totalement indépendants des zap. Le fonctionnement est implémenté dans `GameBasic` et `ArenaBasic`. Il faut overrider quelques fonctions pour définir ce qu'ils font. Il y en a un exemple dans le mode de jeu aspro. [Voir plus loin](https://github.com/darkrecher/Kawax/blob/master/DOC_CONCEPTION.md#interactive-touch-sur-les-aspirines).

Le fonctionnement général est le suivant :

 - L'utilisateur clique dans la fenêtre du jeu.
 - Le `stimuliStocker` détecte ce clic, en déduit la tile cliquée, et enregistre sa position dans la variable interne `posArenaToInteractTouch`. (Cette action est effectuée uniquement sur les clics, pas sur les mouvements de souris, ni sur le maintien du bouton appuyé)
 - dans la Game Loop : récupération de `stimuliStocker.posArenaToInteractTouch`.
 - Si la variable contient une position valide :
	 - exécution de la fonction `ArenaXXX.stimuliInteractiveTouch`, en transmettant cette position.
		 - Cette fonction a le droit de faire tout et n'importe quoi sur les tiles et les chips de l'aire de jeu. Si elle fait quelque chose, elle doit répondre True.
		 - Concrètement, `ArenaBasic.stimuliInteractiveTouch` ne fait rien et renvoie toujours False. Mais la fonction peut être overridée dans un mode de jeu spécifique.
	 - (Retour à la Game Loop). Si on a récupéré True, exécution des actions suivantes :
		 - Comme il s'est passé quelque chose dans l'aire de jeu, les tiles sélectionnées par le joueur ne correspondent peut-être plus à rien. Donc on efface la sélection.
		 - L'aire de jeu est peut-être dans un état "instable". On doit donc agir comme si il y avait eu un zap : vérification de gravité ou de regénération, lock des stimulis, définition de `gravityCounter`, etc.
		 - Gestion du tutoriel, s'il y en a un. [Voir plus loin](https://github.com/darkrecher/Kawax/blob/master/DOC_CONCEPTION.md#tutoriel).
	 - Comme pour un zap, plusieurs gravités pourront s'effectuer à la suite. Le délockage des stimulis sera effectué à la fin de la dernière gravité.
	 - Pour finir, exécution de `GameXXX.gameStimuliInteractiveTouch`. Comme pour `ArenaXXX.stimuliInteractiveTouch`, cette fonction peut faire un peu ce qu'on veut, mais au niveau du `Game`, et pas de `Arena`. Par contre, pas la peine de renvoyer un booléen pour signaler si on a fait quelque chose. Là, on s'en tape.
	 - Concrètement, `GameBasic.gameStimuliInteractiveTouch` ne fait rien. Faut l'overrider.

## Spécificités des modes de jeu spécifique (ha ha) ##

### Gestion des "gros objets" ###

Les "gros objets" sont des éléments présents dans l'aire de jeu, qui s'étendent sur plus d'une tile.

Ils sont gérés par les bouts de codes suivants :

 - `bigobj.py` : définition de la classe générique `BigObject`. Et définition de classes héritées de `BigObject`, dotées d'une forme spécifique dans l'aire de jeu.
 - `arebigob.py` : définition de la classe `ArenaBigObject`, héritée de `ArenaBasic`. Permet la gestion des gros objets.
 - `coins.py` : définition de la classe `ChipBigObject`, héritée de `Chip`. Il s'agit d'une Chip faisant partie d'un gros objet. Elle sert à faire du remplissage dans `matrixTile`, mais rien de plus. Toute la gestion des gros objets se passe dans les deux fichiers mentionnés ci-dessus.
 - Rien dans `GameBasic` ni dans aucune classe héritée de `GameBasic`. La gestion des gros objets n'a pas d'influence à ce niveau du code. (Ce qui est presque étonnant vu comme tout est plus ou moins spaghettifié).

La façon dont c'est géré permet d'avoir des gros objets de n'importe quelle forme, tant qu'ils rentrent dans l'arène : avec des trous dedans, en plusieurs morceaux séparés, etc.

J'avais testé tous ces cas, à une époque, et ça marchait. À priori, ça devrait toujours marcher maintenant.

Le seul cas concret de gros objets est le mode Touillette. [Voir plus loin](https://github.com/darkrecher/Kawax/blob/master/DOC_CONCEPTION.md#le-mode-touillette).

#### La classe BigObject ####

Définit le comportement générique des gros objets. Contient les membres suivants :

 - `posTopLeft` : objet `pygame.Rect`. Position, dans l'aire de jeu, du coin supérieur gauche du rectangle englobant dans lequel se trouve actuellement le gros objet.
 - `listPosRel` : liste d'objet `pygame.Rect`. Position relative à `posTopLeft` de chaque tile occupée par le gros objet. Chaque coordonnée X et Y de chaque élément de cette liste doit être positif ou nul.
 - `listPosArena` : position, dans l'aire de jeu, de chaque tile occupée par le gros objet.
 - `imgBigObj` : objet `pygame.Surface`. Image à afficher dans l'aire de jeu, représentant le gros objet.
 - `typeBigObj` : entier. Type du gros objet. Ne sert à rien dans tout le reste du code, grâce à la magie de l'héritage, du duck typing et toutes ces sortes de choses.

La classe contient plusieurs méthodes, permettant de mettre à jour `listPosArena` par rapport à `postTopLeft` et `listPosRel`. (Ces 3 variables membres doivent toujours être cohérentes entre elles).

La classe est indépendante, elle ne possède pas de lien vers l'aire de jeu qui la contient. Aucune vérification de cohérence n'est faite. Par exemple, `posTopLeft` peut être placé trop bas ou trop à droite. Le gros objet peut alors occuper des tiles hors de l'aire de jeu. C'est au code extérieur de s'occuper de ces contrôles.

#### La classe ArenaBigObject ####

Fonctionne comme la classe ArenaBasic, mais possède une fonction en plus, et quelques fonctions overridées.

##### Ajout d'un gros objet #####

Cette action est réalisée par la fonction `ArenaBigObject.addBigObject`. Elle nécessite deux paramètres :

 - Une classe héritée de `BigObject`, qui sera instanciée pour créer le gros objet à ajouter dans l'aire de jeu.
 - `posTopLeft` : un objet `pygame.Rect`, indiquant la coordonnée du coin supérieur gauche du gros objet.

La fonction effectue les actions suivantes :

 - Instanciation du `BigObject`.
 - Ajout de l'objet `BigObject` (haha) dans la liste `ArenaBigObject.listBigObj`. Cette liste a été créée par la classe mère `ArenaBasic`. (Ça devrait pas, elle ne devrait exister que dans `ArenaBigObject`, mais on n'est plus à ça près).
 - Création des `ChipBigObject` dans l'aire de jeu, sur toutes les tiles occupées par le gros objet. On écrase les chips qui étaient là avant, tel le gros bourrin.

##### Dessin #####

Cette action est réalisée par la fonction overridée `ArenaBigObject.draw`. Elle effectue les actions suivantes :

 - Dessin des tiles, comme dans `ArenaBasic.draw`.
 	- Les `ChipBigObject` sont dessinées comme les autres, sauf que leur image de dessin est totalement transparente.
 - Pour chaque `BigObject` de `self.listBigObj` :
	 -  Récupération de l'image correspondant au gros objet, et dessin au bon endroit, dans l'aire de jeu.

##### Gestion de la gravité #####

Cette action est réalisée par les fonction overridée `ArenaBigObject.determineGravity` et `ArenaBigObject.applyGravity`.

La fonction `determineGravity` effectue les actions suivantes :

 - Détermination de la gravité, par la fonction `ArenaBasic.determineGravity`. Comme si il n'y avait aucun gros objet dans l'aire de jeu.
 - On obtient donc un objet `gravityMovements`, décrivant toutes les positions à déplacer dans le cadre de la gravité.
 - Pour qu'un gros objet tombe, il faut que toutes les tiles qu'il occupe soient soumises à la gravité. Sinon, le gros objet ne tombe pas, et toutes les tiles qui reposent sur lui ne tomberont pas non plus. Le non-tombage d'un gros objet peut entraîner le non-tombage d'autres gros objets qui reposent sur lui, et ainsi de suite. Pour implémenter cela, on utilise l'algorithme suivant :
 - Placement de tous les gros objets de l'aire de jeu dans `listBigObjInGravity`.
 - Pour chaque gros objet de cette liste :
	 - On vérifie si les tiles occupée par le gros objet sont soumise à la gravité.
	 - S'il n'y en a aucune, on enlève le gros objet de `listBigObjInGravity`.
	 - Si elles y sont toutes, on laisse le gros objet dans `listBigObjInGravity`. On ne fait rien de plus.
	 - S'il y en a certaines, mais pas toutes, on effectue les actions suivantes :
		 - On enlève le gros objet de `listBigObjInGravity`.
		 - On annule la gravité pour toutes les tiles occupées par le gros objet. (fonction `gravityMovements.cancelGravity`). C'est à dire que les tiles du gros objet, et toutes les tiles au-dessus d'elles, ne sont plus soumises à la gravité.
		 - On retient qu'on a effectuée une modification dans la gravité, donc il faudra reprendre la boucle sur `listBigObjInGravity` depuis le début. (Mais `listBigObjInGravity` a un ou plusieurs élément de moins par rapport à la boucle précédente, donc au bout d'un moment, ça s'arrête forcément).
 - Lorsqu'on a terminé, les gros objets qui restent dans `listBigObjInGravity` sont ceux qui sont réellement soumis à la gravité. On garde cette liste en mémoire pour plus tard.

La fonction `applyGravity` effectue les actions suivantes :

 - Exécution de `ArenaBasic.applyGravity` : Application de la gravité sur les tiles qui y sont soumises.
 - Application de la gravité sur tous les gros objets restés dans `listBigObjInGravity` : on modifie `bigObject.posTopLeft`, ainsi que tous les éléments de `bigObject.listPosArena`.

### Le mode Touillette ###

Ce mode est implémenté par la classe `GameTouillette`, (fichier `touyettg.py`), ainsi que par la classe `ArenaTouillette`, (fichier `touyetta.py`). Il comporte les particularités suivantes :

 - Présence de touillettes : gros objet ayant pour forme une ligne horizontale de 5 tiles.
 - Une première touillette est créée dans l'aire de jeu, à un emplacement prédéfini.
 - D'autres touillettes peuvent être créées durant l'étape de regénération des chips.
 - Lorsqu'une touillette arrive en bas de l'aire de jeu, elle disparaît automatiquement.
 - Il faut faire disparaître 2 touillettes pour gagner.

#### Ajout des touillettes ####

La première touillette est créé à l'initialisation (`GameTouillette.__init__`), avec la fonction `ArenaBigObject.addBigObject`.

L'ajout des autres touillettes est réalisé par les fonctions suivantes :

 - `regenerateAllChipsAfterOneGravity` (overridée).
 - `regenerateTouillette`.

Les étapes suivantes sont effectuées :

 - Appel de `regenerateAllChipsAfterOneGravity` par le code extérieur, après l'application d'une gravité.
 - Parcours de la ligne du haut de l'aire de jeu, pour détecter la liste des positions potentielles pouvant accueillir une touillette. Il s'agit de tiles vides, dont les 4 tiles à droite sont vides aussi. (Oh surprise, ça fait pil poil la largeur d'une touillette). Les positions potentielles peuvent se chevaucher. Par exemple, une ligne de 6 tiles vide générera 2 positions potentielles.
 - Exécution de `regenerateTouillette`, en donnant la liste des positions potentielles en paramètre.
	 - Calcul de probabilité, en fonction du nombre de touillettes déjà présentes dans l'aire de jeu, et du nombre de positions potentielles, pour déterminer si on doit créer une touillette ou pas.
	 - Si oui, choix d'une position potentielle au hasard, et ajout de la touillette dans l'aire de jeu. (`addBigObject`).
 - (Retour à `regenerateAllChipsAfterOneGravity`)
 - Exécution de la fonction de base `ArenaBigObject.regenerateAllChipsAfterOneGravity`, afin de regénérer des chips sur les tiles qui sont restés vide.

#### Disparition des touillettes en bas de l'écran ####

Cette action est réalisée par les fonctions suivantes :

 - `GameTouillette.handleGravity` (overridée)
 - `ArenaTouillette.hasTouilletteInBottom`
 - `ArenaTouillette.removeBottomTouillette`

Les étapes suivantes sont effectuées :

 - Appel de `handleGravity` par le code extérieur.
 - Exécution de `removeBottomTouillette`.
	 - Vérification s'il y a une ou plusieurs touillettes dans la ligne du bas de l'aire de jeu.
	 - Si oui, suppression du/des `bigObject` correspondants, dans la liste `listBigObj`.
	 - Suppression des `ChipBigObject` correspondantes. Truc bizarre : la suppression se fait via des exécutions de `zapOnePos`. Je ne parviens pas à me souvenir pourquoi j'ai pas fait un remplacement direct des chips. Ce serait plus logique.
	 - renvoi de True si au moins une touillette a été supprimée.
 - (Retour à `handleGravity`)
 - Si on a supprimé une touillette, enregistrement de cette info dans la variable membre `mustDisplayRemoving` (ça servira plus tard).
 - Application d'une gravité normale (`GameBasic.applyGravity`)
 - Il faut ensuite déterminer si l'aire de jeu est "instable". Elle peut l'être dans l'une des 3 conditions suivantes :
	 - Instabilité normale d'un mode de jeu basique.
	 - On vient de supprimer une touillette.
	 - Il y a une touillette en bas de l'aire de jeu. On ne l'a pas supprimée, car elle vient d'arriver suite à la gravité. Il faudra l'enlever au prochain coup. 
 - Comme dans un mode normal : re-détermination de `gravityCounter`, ou délockage des stimulis, selon que l'aire de jeu soit instable ou pas.

#### Affichage du nombre de touillettes disparues ####

Cette action est réalisée par la fonction `GameTouillette.periodicAction`. C'est vraiment bizarre et salement bourrin d'avoir mis ce code ici, mais je ne savais pas où le mettre ailleurs. C'est du code qui doit être exécuté à la fin d'une suite de gravité, mais qui n'a rien à voir avec la gravité elle-même. Car on pourrait imaginer d'autres processus qui éliminent des touillettes dans l'aire de jeu, et qui provoquerait également cette action d'affichage.

Bref voilà, c'est dans `periodicAction`, et puis c'est tout.

Les étapes suivantes sont effectuées :

 - Appel de `periodicAction`, à chaque cycle du jeu.
 - Si `mustDisplayRemoving` vaut True, on effectue toutes les actions suivantes :
	 - On remet `mustDisplayRemoving` à False, pour ne pas effectuer cette action plusieurs fois de suite. (Ça me fait penser que si plusieurs touillettes sont supprimées par plusieurs zap différents, dans le même cycle de jeu, eh bien un seul affichage sera effectuée. Mais ce genre de cas bien débile n'arrive jamais. Ne serait-ce que parce qu'on ne peut pas faire 2 zap dans un même cycle).
	 - Affichage dans la console, du nombre de touillettes supprimées et du nombre total à supprimer.
	 - Si on a supprimé une quantité suffisante de touillettes : affichage du texte indiquant que le joueur a gagné.
	 - On ne fait rien de plus même si le joueur a gagné. Ça lui permet de continuer à jouer si il a envie. Et comme ça j'ai pas à me faire suer à gérer un événement de quittage du programme.

### Le mode Aspro ###

Ce mode est implémenté par la classe `GameAspirin`, (fichier `asprog.py`), ainsi que par la classe `ArenaAspirin`, (fichier `asproa.py`). Il comporte les particularités suivantes :

 - La gravité est vers le bas, comme d'habitude, mais les chips ne se regénèrent pas en haut.
 - Une seconde gravité est appliquée, après celle vers le bas. Il s'agit du "Gravity Rift" : lorsqu'il y a une colonne complètement vide, toutes les colonnes à droite sont déplacées vers la gauche. La colonne tout à droite devient donc vide, c'est là qu'on regénère des chips.
 - L'aire de jeu comporte des demi-cachets d'aspirine, placés initialement à des endroits définis en dur.
 - Lorsque deux demi-cachets gauche et droite sont l'un à côté de l'autre, le joueur peut cliquer sur l'un d'eux, pour les fusionner en un cachet entier.
 - Le joueur peut également cliquer sur un cachet entier pour le prendre.
 - Le but est de prendre 3 cachets d'aspirine.
 - Les demi-cachets d'aspirine qui atterrissent en bas de l'aire de jeu sont supprimés, et ne sont pas comptabilisés dans les cachets récupérés.

#### Gravity Rift ####

Cette action est réalisée par les fonctions et les classes suivantes :

 - `ArenaBasic.determineGravityFullSegment()`
 - `GameAspirin.crawlerGravRift`
 - `GameAspirin.gravityMovementsRift`
 - `GameAspirin.crawlerRegenRift`
 - `GameAspirin.crawlerGravRiftApply`
 - `GameAspirin.applyGravity()`
 - `GameAspirin._determineAnyGravity()`
 - `GameAspirin.needStabilization()`

La gravité du mode aspro s'effectue en deux temps. Le premier temps est normal, vers le bas. On utilise le même crawler pour déterminer les mouvements et les appliquer : `GameAspirin.crawlerGrav`. On utilise également une instance de `GravityMovements` :  `GameAspirin.gravityMovements`. Ces deux objets sont configurés et utilisés de la même manière que dans le mode normal (voir fonction `GameBasic.initCommonStuff`).

Par contre, on n'utilise jamais `GameAspirin.crawlerRegen` (bien qu'il soit créé par `GameBasic.initCommonStuff`). Dans `GameAspirin`, on appelle parfois la fonction `ArenaXXX.regenerateAllChipsAfterOneGravity`, mais jamais avec `GameAspirin.crawlerRegen` en paramètre.

Le second temps de la gravité est un "Rift", vers la gauche. Contrairement au premier temps, on a besoin de deux crawlers distincts : un pour déterminer les mouvements (`GameAspirin.gravityMovementsRift`) et un autre pour les appliquer (`GameAspirin.crawlerGravRiftApply`). On a également besoin d'une autre instance de `GravityMovements` :  `GameAspirin.gravityMovementsRift`.

Le second temps de la gravité provoque des regénérations. Pour cela, on utilise le crawler `GameAspirin.crawlerRegenRift`.

Pour déterminer les mouvements de Rift, on utilise la fonction `ArenaBasic.determineGravityFullSegment`, avec en paramètre le crawler `GameAspirin.gravityMovementsRift`. Ce crawler parcourt l'aire de jeu colonne par colonne, en allant de la gauche vers la droite. (Chaque colonne est parcourue de haut en bas, mais on s'en fout).

La fonction `ArenaBasic.determineGravityFullSegment` effectue les actions suivantes :

 - Parcours de l'aire de jeu avec le crawler, jusqu'à trouver une colonne entièrement vide. Lorsque ça arrive, on retient sa coordonnée X, et on passe tout de suite à l'étape suivante. Pas la peine de parcourir le reste de l'aire de jeu. S'il y a d'autres segments vides, ils seront détectés lors de gravité suivantes.
 - Ajout de plusieurs mouvements de gravité, dans l'objet `GravityMovements` à retourner. Alors là c'est fait de manière un peu bizarre, avec un fort risque de se mélanger les crayons entre les différentes coordonnées.
	 - Les coordonnées primaires des mouvements de gravité sont : Y = (de 0 à tout en bas de l'aire de jeu).
	 - La coordonnée secondaire de chaque début de mouvement de gravité est X = (position de la colonne vide)
	 - La coordonnée secondaire de chaque fin de mouvement de gravité est X = (tout à droite de l'aire de jeu).
 - Donc pour ajouter ces mouvements, on utilise toujours `GameAspirin.gravityMovementsRift`, mais on le refait partir du début, et on ne lui fait parcourir qu'une colonne. À chaque itération, la coordonnée primaire du mouvement de gravité est égale à la coordonnée secondaire du crawler.
 - Je vous laisse réfléchir à tout ça. Si c'était à refaire, j'essayerais de trouver une manière plus simple d'exprimer tous ces mouvements et ces parcours, tout en essayant de rester le plus générique possible.

Pour appliquer les mouvements de Rift, on utilise donc `GameAspirin.gravityMovementsRift`, dûment rempli par l'étape ci-dessus. On utilise aussi le crawler "qui va bien" pour appliquer une gravité vers la gauche. C'est à dire `GameAspirin.crawlerGravRiftApply`.

Pour appliquer une gravité, il faut un crawler dont le sens secondaire est inverse au sens de la gravité. (Le sens primaire peut être n'importe lequel, on s'en fout).

Or donc, pour récapituler l'ensemble du bazar, les actions suivantes sont effectuées :

 - Appel de la fonction `GameBasic.tryToZap`, lorsque l'utilisateur tente un zap, comme dans un mode de jeu normal.
 - Si le zap réussi, appel de la fonction overridée `GameAspirin.needStabilization`.
	 - Exécution de la fonction `GameAspirin._determineAnyGravity`
		 - Détermination de gravité normale.
		 - Si il y en a, l'objet `GameAspirin.gravityMovements` contient des mouvements à faire. La fonction _determineAnyGravity ne fait rien de plus, et renvoie True
		 - Sinon, détermination de gravité Rift.
		 - Si il y en a, l'objet `gravityMovementsRift` contient des mouvements à faire. La fonction `_determineAnyGravity` renvoie True.
		 - Sinon, la fonction renvoie False.
	 - (retour à `needStabilization`). Renvoi de True si `_determineAnyGravity` a renvoyé True.
	 - Sinon, recherche de demi-cachets d'aspirine en bas de l'aire de jeu. (Mais ça n'a aucun rapport avec les gravités. Voir plus loin : "Suppression des cachets en bas de l'aire de jeu").
	 - Si il y en a, on renvoie True.
	 - Sinon, tout va bien, l'aire de jeu est stable. On renvoie False

Et durant la Game Loop, les actions suivantes sont effectuées :

 - Appel de la fonction overridée `GameAspirin.handleGravity`. (Ça se fait au moment habituel : lorsque le jeu est dans un état instable et que `gravityCounter` arrive à 0).
	 - Appel de la fonction `GameAspirin.applyGravity`.
		 - Application de la gravité normale, s'il y a des choses dans `GameAspirin.gravityMovements`
		 - Sinon :
			 - application de la gravité Rift, s'il y a des choses dans `GameAspirin.gravityMovementsRift`.
			 - Regénération des chips de la colonne tout à droite, en appelant `GameAspirin.arena.regenerateAllChipsAfterOneGravity`, avec le crawler de regénération spécialement prévu pour : `crawlerRegenRift`.
		 - Sinon :
			 - Exécution de `removeHalfAsproBottom`. (voir chapitre suivant)
	 - (retour à `handleGravity`). Exécution des mêmes actions que dans le mode de jeu normal.
	 - Appel de `needStabilization`. Si la fonction renvoie True, il faudra refaire une autre gravité plus tard.
	 - Suppression du lock des stimulis, sauf si c'est le tutoriel qui les a lockés.

#### Suppression des demi-cachets en bas de l'aire de jeu ####

Cette action est réalisée par les fonctions suivantes :

 - `GameAspirin.needStabilization`
 - `GameAspirin.handleGravity`
 - `ArenaAspirin.removeHalfAsproBottom`
 - `ArenaAspirin.hasAnyEmptyChipInBottom`

Cette suppression a été mise en place pour deux raisons :

 - Augmenter un peu la difficulté, sinon on s'ennuie.
 - Donner au joueur la possibilité de vider complètement une colonne de l'aire de jeu, même si elle comporte un demi-cachet qui ne peut pas être fusionné avec un autre.

Mais du coup, dès qu'un demi-cachet est supprimé de cette manière, on ne peut plus gagner la partie. Car il y a juste assez de cachets créés au départ pour pouvoir gagner, et aucun autre n'est généré durant le jeu. C'est ballot mais c'est comme ça. J'avais prévu une génération durant le jeu, et ensuite je suis passé à autre chose.

Pour bien montrer au joueur ce qui se passe dans l'aire de jeu, la suppression est faite en deux temps :

 - Transformation des demi-cachets du bas en chips vides. (Le joueur a le temps de voir les cases vides).
 - Application d'une gravité pour faire descendre d'une case les chips situées du dessus.

Les actions suivantes sont effectuées :

 - Durant la Game Loop, appel de la fonction overridée `GameAspirin.handleGravity`.
	 - Appel de la fonction `GameAspirin.applyGravity`.
		 - Application de la gravité normale, ou de la gravité Rift, selon ce qu'il y a à faire.
		 - Si aucune gravité n'a eu besoin d'être appliquée, exécution de `ArenaAspirin.removeHalfAsproBottom`
			 - Utilisation d'un crawler qui parcourt la ligne du bas de l'aire de jeu, et remplace tous les demi-cachets d'aspirine (gauche ou droit) par une `ChipNothing`.
	 - (retour à `handleGravity`)
	 - Exécution de `GameAspirin.needStabilization` :
		 - Si un demi-cachet vient d'être supprimé, il y a un emplacement vide. `GameAspirin._determineAnyGravity` détectera forcément une gravité normale, ou une gravité rift à effectuer. Elle sera effectuée au prochain coup.
		 - Si il n'y a aucune gravité à appliquer, on appelle la fonction `ArenaAspirin.hasAnyHalfAsproInBottom`
			 - Utilisation d'un crawler qui parcourt la ligne du bas de l'aire de jeu. Si on trouve un demi-cachet (gauche ou droit), la fonction renvoie True, sinon, elle renvoie False. Ce demi-cachet sera supprimé au prochain appel de `handleGravity`.

Donc, la suppression d'un demi-cachet s'effectue sur plusieurs appels à handleGravity, durant plusieurs Game Loop.

 - Application de gravité normale, vers le bas, jusqu'à ce qu'un demi-cachet tombe en bas.
 - Aucun mouvement de gravité n'est à effectuer (ni normaux, ni rift). Mais `ArenaAspirin.hasAnyHalfAsproInBottom` renvoie True, donc le jeu reste instable.
 - On n'applique aucune gravité, mais la fonction `ArenaAspirin.removeHalfAsproBottom` effectue quelque chose. Elle supprime le demi-cachet.
 - Détection d'une gravité à effectuer, à l'endroit où il y avait le demi-cachet.
 - Application de ce mouvement de gravité.
 - Aucun mouvement de gravité n'est à effectuer (ni normaux, ni rift). `ArenaAspirin.hasAnyHalfAsproInBottom` renvoie False. Le jeu est redevenu stable.

Le but de tout ce bazar, c'est de bien décomposer les étapes, en les affichant à chaque fois, afin que le joueur comprenne bien ce qu'il se passe.

Je n'ai pas testé le cas où il y a à la fois une gravité Rift et un demi-cachet à supprimer en bas. Normalement, ça plante pas, et toutes les étapes sont bien décomposées.

#### Interactive Touch sur les aspirines ####

Cette action est réalisée par les fonctions suivantes :

 - `GameAspirin.gameStimuliInteractiveTouch`
 - `ArenaAspirin.stimuliInteractiveTouch`
 - `ArenaAspirin.mergeAsproHalf`
 - `ArenaAspirin.takeAsproFull`
 - `ArenaAspirin.getAndResetTakenAsproFull`

Les actions suivantes sont effectuées :

 - Le joueur clique sur une chip de l'aire de jeu. Cette action est enregistré dans `GameBasic.stimuliStocker.posArenaToInteractTouch`.
 - La Game Loop appelle la fonction overridée `ArenaAspirin.stimuliInteractiveTouch`
 	- Exécution de la fonction `ArenaAspirin.mergeAsproHalf`
	 	- Si la chip sur laquelle le joueur a cliqué est une `ChipAsproHalfLeft`, et que la chip à droite est une `ChipAsproHalfRight`, alors on effectue les actions suivantes :
		 	- Zap de la tile de droite, afin de remplacer la `ChipAsproHalfRight` par une `ChipNothing`
		 	- Remplacement de la chip sur laquelle le joueur a cliqué par une `ChipAsproFull`
		 	- `mergeAsproHalf` renvoie True
		- Sinon, on fait pareil, mais de l'autre côté : Si la chip sur laquelle le joueur a cliqué est une `ChipAsproHalfRight`, et que la chip à gauche est une `ChipAsproHalfLeft`, alors on effectue les actions suivantes :
		 	- Zap de la tile de gauche, afin de remplacer la `ChipAsproHalfLeft` par une `ChipNothing`
		 	- Remplacement de la chip sur laquelle le joueur a cliqué par une `ChipAsproFull`
		 	- `mergeAsproHalf` renvoie True
		- Sinon, il ne s'est rien passé d'intéressant. `mergeAsproHalf` renvoie False.
	- Si `mergeAsproHalf` n'a rien fait, exécution de la fonction `ArenaAspirin.takeAsproFull`.
		- Si la chip sur laquelle le joueur a cliqué est une `ChipAsproFull` :
			- Zap de la tile cliqué, afin de remplacer la `ChipAsproFull` par une `ChipNothing`
			- Définition de la variable membre `hasTakenAsproFull` à True. (Utilisée par le code extérieur).
			- `takeAsproFull` renvoie True.
		- Sinon, il ne s'est rien passé d'intéressant. `takeAsproFull` renvoie False.
	- Si `mergeAsproHalf` ou `takeAsproFull` a fait quelque chose, `stimuliInteractiveTouch` renvoie True pour le signaler au code extérieur. Sinon, elle renvoie False.
 - Si `stimuliInteractiveTouch` a renvoyé True, la Game Loop le prend en compte : vérification si l'aire de jeu est "instable", exécution de gravité, lock des stimulis, ... Comme d'habitude.
 - Ensuite, la Game Loop appelle la fonction overridée `GameAspirin.gameStimuliInteractiveTouch`
	 - Exécution de `ArenaAspirin.getAndResetTakenAsproFull`
		 - La fonction vérifie la valeur de `hasTakenAsproFull`.
		 	 - Si elle est True, `getAndResetTakenAsproFull` remet la valeur à False, et renvoie True.
		 	 - Sinon, il ne s'est rien passé de spécial précédemment. `getAndResetTakenAsproFull` renvoie False.
	 - Si `getAndResetTakenAsproFull` a renvoyé True, on effectue les actions suivantes :
		 - Augmentation de la variable membre `nbAspirinTaken`.
		 - Si `nbAspirinTaken` a atteint 3 : affichage d'un texte dans la console, indiquant que le joueur a gagné. (On ne fait rien de plus, ce qui permet au joueur de continuer à jouer).
		 - Sinon, affichage de texte dans la console indiquant que le joueur a pris un aspirine. Affichage du nombre d'aspirine pris, et du nombre total à prendre. (Sauf si y'a un `tutorialScheduler`, mais pour ça : "voir plus loin").

La gestion est donc presque simple. Il y a juste cette histoire de `hasTakenAsproFull` qui est bizarre. On le met à True, pour le remettre à False tout de suite après, à un autre niveau du code. C'est parce que je ne voulais pas mettre la gestion "combien d'aspirine pris" et "est-ce qu'on a gagné ou pas" dans l'arena. Je voulais que ça soit dans le game, parce qu'à mon avis, c'est là que c'est censé être. (L'arena n'a pas à se soucier de ces détails, qui concerne le fonctionnement du jeu en lui-même, et pas l'état de l'aire de jeu, les tiles, les chips, ...)

Et donc il faut voir ce `hasTakenAsproFull` comme un message envoyé de l'arena au game, pour prévenir qu'il s'est passé un truc. Le message doit être acquitté dès qu'il a été pris en compte. C'est pourquoi on le remet à False très peu de temps après l'avoir mis à True. C'est de la gestion d'événements. Et je m'aperçois que j'aurais dû beaucoup plus coder en pensant "événement" que "orienté objet". C'est pas grave, on fera mieux la prochaine fois !!

#### Création des demi-cachets au début du jeu ####

Cette action est réalisée par la fonction overridée `GameAspirin.populateArena`.

Elle est appelée dans `GameBasic.__init__`, après instanciation de l'arena, et remplissage avec des chips au hasard.

La fonction remplace certaines chips existantes par des demi-cachets droit et gauche. Les positions de remplacement sont en dur. Elles sont définies par les constantes `LIST_COORD_ASPRO_HALF_LEFT` et `LIST_COORD_ASPRO_HALF_RIGHT`, dans le fichier `asprog.py`.

#### Génération des demi-cachets (non implémenté) ####

J'avais commencé de coder cette fonctionnalité, mais je ne suis pas sûr de l'avoir fini, et je n'ai plus la motivation pour me replonger dedans.

J'ai conservé le code correspondant, mais il n'est utilisé nul part. Je ne me souviens plus comment il fonctionne, si il fonctionne réellement comme je l'avais imaginé, et si il a été testé.

Il est entièrement dans le fichier `asproa.py`, signalé entre deux commentaires `Section de code non utilisée` et `Fin de section de code non utilisée`.

Il s'agit des fonctions suivantes :

 - `ArenaAspirin._getPosPotentialAspro`
 - `ArenaAspirin._countNbAspro`
 - `ArenaAspirin._calculateProbaAspro`
 - `ArenaAspirin._regenerateAsproHalf`
 - `ArenaAspirin._regenerateAspro`

### Tutoriel ###

Je n'ais pas trop su comment l'implémenter. Le problème, c'est que le tutoriel doit agir à plein de moments différents (lorsque l'utilisateur veut passer au texte suivant, lorsqu'il fait un zap, un interactive touch, ...). Je n'ai pas trouvé de meilleure solution que d'injecter des petits bouts de code, à plein d'endroits différents de pleins de classes. Et comme ça suffisait pas, il a en plus fallu que j'hérite la classe GameXXX de chaque mode de jeu, pour faire le tutoriel correspondant. Ça a énormément spaghettifié le code. Pas mieux.

Si c'était à refaire, j'essayerais de le gérer avec des événements qui s'échangent ici et là, entre différents modules. Ou de la programmation orientée aspect (jamais vraiment su ce que c'était, ce truc). Ou encore, le fameux "entité-composant-système". Dans le cas présent, on se retrouve avec des objets monolithiques remplis de code spaghetti. Faut faire avec.

Je me permet également d'ajouter que je n'ai jamais su si on doit dire "tutoriels" ou "tutoriaux". Ce sera donc "tutoriels". Ne venez pas m'embêteriels.

Les tutoriels sont gérés par les fichiers de code suivants :
 - `tutorial.py`
 - `blinker.py`
 - `gamemode/gambtuto.py` (tutoriel du mode de jeu Basique)
 - `gamemode/touytuto.py` (tutoriel du mode de jeu Touillette)
 - `gamemode/asprtuto.py` (tutoriel du mode de jeu Aspro)

#### La classe TutorialStep ####

Elle est définie dans `tutorial.py`. C'est une classe uniquement destinée à stocker des données (comme une `struct`, en C++). Elle définit une seule étape d'un tutoriel.

L'info principale d'une étape est le type de condition pour passer à l'étape suivante. Cette info est définie par la variable membre `conditionType`. Elle peut prendre l'une des valeurs suivantes :

 - `STEP_COND_NEVER` : condition impossible. On ne peut pas passer à l'étape suivante. (En général, on met cette valeur pour la dernière étape).
 - `STEP_COND_STIM` : on passe à l'étape suivante sur le stimuli spécifique "next tutorial step". C'est à dire lorsque le joueur appuie sur la touche "F" pour afficher le texte suivant.
 - `STEP_COND_SELECT_TILES` : on passe à l'étape suivante si le joueur parvient à faire un zap sur une sélection de tiles spécifique. Lorsqu'on utilise cette condition, il faut définir la variable membre `listPosCond`. Elle doit contenir une liste de `pygame.Rect`, correspondant aux positions à zapper. Le joueur doit zapper exactement cette liste, ni plus ni moins. Mais il n'y a pas de distinction entre les sélections "chemin principal" et "sélection additionnelle".
 - `STEP_COND_INTERACTIVE_TOUCH_SUCCESSED` : on passe à l'étape suivante si le joueur effectue un Interactive Touch qui a une influence sur l'aire de jeu. Cet Interactive Touch peut être fait sur n'importe quelle chip. (D'ailleurs c'est pas top, j'aurais du ajouter une contrainte éventuelle sur la position).

En plus de `conditionType`, un `TutorialStep` contient également les variables membres suivantes :

 - `soundId` : None, ou objet `pygame.mixer.Sound`. Le son à jouer lorsque l'étape est atteinte.
 - `listTextDescrip` : liste de string. Texte à écrire dans la console lorsque l'étape est atteinte. Rappelons que la console est un peu pourrie, et qu'elle est artificiellement limitée à 10 caractères par ligne. `listTextDescrip` est donc une liste, et non pas une grande string unique. Ça permet d'indiquer manuellement où sont les sauts de ligne.
 - `listPosBlink` : None, ou liste de `pygame.Rect`. Liste de positions dans l'aire de jeu à faire blinker. Les tiles apparaissent entourées de bleus clignotant pendant quelques secondes.
 - `tellObjective` : booléen. Indique s'il faut afficher l'objectif courant (nombre de brouzoufs et de sucres) à cette étape de tutoriel.

#### La classe TutorialScheduler ####

Elle est définie dans `tutorial.py`. Elle contient une liste de `TutorialStep`, dans laquelle elle avance au fur et à mesure. Elle n'agit pas sur des objets externes par elle-même. Elle n'a pas de référence vers un `GameXXX`, ni une `ArenaXXX`, ni même la console.

Cette classe ne sait que renvoyer les informations du `TutorialStep` courant, et recevoir des stimuli externes, afin d'avancer d'une étape, ou pas.

Pour instancier un `TutorialScheduler`, il faut lui passer une `listTutStepsDescrip`. Chaque élément de cette liste est un tuple, contenant les informations nécessaires à la création d'un `TutorialStep`. Chaque tuple doit contenir, dans cet ordre, les informations suivantes :

 - `conditionType`
 - Une liste de coordonnées (tuple de 2 éléments) dans l'aire de jeu. Sera convertie en liste de `pygame.Rect` pour créer `listPosCond`.
 - None, ou une string. Doit correspondre à un fichier son existant, dont le nom complet est déterminé comme suit : `"sound/" + <string> + ".ogg"`. Permet de créer `soundId`.
 - Un dictionnaire, ou une liste de string. Si c'est une liste de string, elle correspond directement à `listTextDescrip`. Si c'est un dictionnaire, la clé doit être un identifiant de langage défini dans `language.py` (`LANGUAGE_FRENCH` ou `LANGUAGE_ENGLISH`). On utilise la langue courante, pour récupérer la valeur correspondante dans le dictionnaire, qui sera affectée à `listTextDescrip`.
 - Une liste, éventuellement vide, de coordonnées. Sera convertie en liste de `pygame.Rect` pour créer `listPosBlink`.
 - `tellObjective`

À la création, le `TutorialScheduler` se place à sa première étape.

Les fonctions suivantes permettent de récupérer les informations de l'étape courante :

 - getCurrentSound
 - getCurrentText
 - getCurrentBlink
 - getCurrentTellObjective

D'autres fonctions permettent d'envoyer un stimuli au `TutorialScheduler`. Leur nom commence tous par `takeStim`, parce qu'elles sont nommées du point de vue de la classe, et non du point de vue du code extérieur. (C'est complètement con, je sais). Ces fonctions renvoient toutes un booléen, indiquant si le `TutorialScheduler` a avancé d'une étape ou pas. Il s'agit des fonctions suivantes :

 - `takeStimTutoNext` : Le joueur a appuyé sur la touche "F". Le `TutorialScheduler` avance d'une étape si l'étape courante a `conditionType == STEP_COND_STIM`.
 - `takeStimInteractiveTouch` : Le joueur a effectué un Interactive Touch avec un impact sur l'aire de jeu. Avance d'une étape si `conditionType == STEP_COND_INTERACTIVE_TOUCH_SUCCESSED`.
 - `takeStimTileSelected` : Le joueur a effectué un zap. On passe en paramètre les positions des tiles sélectionnées. Avance d'une étape Si `conditionType == STEP_COND_SELECT_TILES` et que `listPosCond` est égal à la sélection du joueur. Mais si `listPosCond` ne correspond pas, non seulement on n'avance pas, mais en plus le `TutorialScheduler` se met dans l'état `totallyFailed`.

L'état `totallyFailed` ne permet plus du tout d'avancer dans les étapes. Le code extérieur est censé appeler la fonction `getFailText` et l'afficher dans la console, et ne plus rien faire d'autre concernant le tutoriel. Cette état correspond à une situation dans laquelle on a demandé au joueur de zapper certaines tiles en particulier, sauf qu'il a réussi à faire un zap différent. Dans ce cas, l'aire de jeu risque de ne plus correspondre à ce qui était prévu pour le tutoriel. Par sécurité, on bloque les étapes, et donc totally fail.

Il reste une dernière fonction : le fameux `mustLockGameStimuli`. Elle sert à indiquer au code extérieur si les stimulis du jeu (sélection des tiles et zap) devraient être momentanément bloqués, du fait de l'état actuel du `TutorialScheduler`.

Les stimulis doivent être bloqués lorsqu'on demande au joueur d'appuyer sur "F" pour avancer à la prochaine étape. Dans cette situation, on ne permet pas au joueur de faire quoi que ce soit sur le jeu.

#### La classe Blinker ####

La classe `Tile` possède une variable membre booléenne : `tutoHighLight`. Lorsque cette variable est à True, et qu'on appelle la fonction `Tile.draw`, un cadre turquoise épais est dessiné sur les bords. (D'ailleurs, la façon dont l'épaissisation de cadre est effectuée est particulièrement horrible. Je vous laisse regarder le code).

Le but de la classe `Blinker` est de mettre à jour `tutoHighLight` dans les différentes tiles, afin de faire clignoter le cadre.

Le fichier `blinker.py` définit la classe `Blinker`, ainsi que deux constantes :

 - `BLINK_PERIOD` : demi-période (en cycle de jeu) de clignotement des tiles. Les tiles sont allumées durant `BLINK_PERIOD` cycles, puis éteintes durant `BLINK_PERIOD` cycles, et ainsi de suite.
 - `BLINK_DURATION` : temps total du blink, en cycle de jeu. Le clignotement des tiles s'arrête automatiquement au bout d'un certain temps.

La classe `Blinker` s'utilise de la manière suivante :

 - Instanciation, en lui passant en paramètre l'aire de jeu dans laquelle se trouve les tiles qu'elle devra blinker.
 - Exécution de `startBlink`, en passant en paramètre la liste des positions à faire blinker.
 - Pour que le blink soit effectué, il faut exécuter périodiquement, une fois par cycle de jeu, la fonction `advanceTimerAndHandle`. C'est cette fonction qui met à jour les variables `tutoHighLight`. Elle est appelée par la classe `GameBasic`, dans la Game Loop. Après appel de cette fonction, il faut redessiner l'aire de jeu.
 - Ensuite, on peut soit ne rien faire, et laisser le blink s'arrête tout seul, soit appeler `stopBlink` pour l'arrêter immédiatement, soit rappeler `startBlink`, avec une nouvelle liste de positions. La variable `tutoHighLight` des anciennes positions est remise à False, pour être sûr de ne pas se retrouver avec des restes d'anciens blinks, qui laisseraient des cadres turquoise n'importe où.

#### Création d'un tutoriel à partir d'un mode de jeu ####

Les 3 tutoriels existants sont définis dans les 3 fichiers suivants :

 - `gambtuto.py` : tutoriel du mode de jeu basique.
 - `touytuto.py` : tutoriel du mode Touillette.
 - `asprtuto.py` : tutoriel du mode Aspro.

Avec ou sans tutoriel, un mode de jeu doit respecter les mêmes règles. Donc pour amener le joueur à effectuer des étapes prédéfines (en particulier les zaps), il faut définir en dur, et en cohérence entre elles, les infos suivantes :

 - Les positions à zapper
 - Les chips de ces positions
 - Les consignes de zap (quantités de brouzoufs et de sucre à atteindre).

Nous allons maintenant voir les morceaux de code à implémenter pour créer un mode tutoriel. (C'est nul de dire "nous allons voir", mais je sais pas comment le dire autrement).

##### Étapes du tutoriel #####

Définir la liste d'étape `listTutStepsDescrip`. Il s'agit d'une liste de tuple, telle que décrite dans le chapitre précédent. (voir avant).

Certaines étapes de `listTutStepsDescrip` définissent des zap à effectuer, sur des listes de positions définies en dur (`listPosCond`). La bienséance veut qu'on fasse blinker ces positions, pour les montrer au joueur. Il est donc intéressant de toujours avoir `listPosCond == listPosBlink`. Cependant, aucune contrainte n'est imposée à ce sujet. On peut faire ce qu'on veut si on a envie d'embrouiller le joueur.  

La dernière étape de `listTutStepsDescrip` doit avoir `conditionType == STEP_COND_NEVER`. Aucune contrainte réelle sur ce point. Mais je ne sais pas ce que ça fait si on ne la respecte pas, je n'ai pas testé.

##### Aire de jeu #####

Afin que le tutoriel soit réussissable, il faut que toutes les positions à zapper (définies dans les `listPosCond`) contiennent des chips prédéfinis. En tenant compte du fait que la gravité est appliquée entre chaque zap. Donc des fois, on définit une chip en dur qui va ensuite tomber un peu plus bas pour arriver pil poil sur une position définie dans `listPosCond`. Enfin vous voyez ce que je veux dire, n'est-ce pas. 

Bref, il est donc nécessaire de définir une liste de chips en dur (position dans l'aire de jeu, type et valeur en brouzoufs). Les chips non définies seront créées au hasard, comme d'habitude.

En général, les chips en dur sont définies par une liste de tuple de tuple : `LIST_TILE_TO_HARDDEFINE`. Chaque élément de cette liste contient les infos suivantes :
 - Tuple de deux int : positions (X, Y) dans l'aire de jeu.
 - Tuple d'une string et d'un int :
	 - "C" : pièce de monnaie. "S" : sucre.
	 - int : valeur de la pièce. (0 si c'est un sucre).

##### Liste des consignes de zap #####

Chaque zap de tutoriel doit avoir une contrainte définie en dur, correspondant à des chips définies en dur aussi. (Ça fait beaucoup de dur). On utilise généralement une variable `LIST_ZAP_CONSTRAINT`. Chaque élément de cette liste est un tuple de deux éléments :

 - int. Total de de brouzoufs à sélectionner.
 - int. Nombre de sucre à sélectionner.

##### Implémentation de tout ce bazar #####

Il faut créer une classe `GameXXXTuto`, héritée à partir du `GameXXX` que l'on veut tutorialiser. C'est ce qui est fait avec les 3 fichiers de code précédemment mentionnées.

La classe `GameXXXTuto` doit overrider les fonctions suivantes :

 - `__init__` :
	 - Récupération des variables `LIST_TUT_STEP_DESCRIP`, `LIST_TILE_TO_HARDDEFINE` et `LIST_ZAP_CONSTRAINT`, pour les stocker en interne.
	 - Créaton d'un `tutorialScheduler`, en lui passant `LIST_TUT_STEP_DESCRIP`.
	 - Exécution de l'`__init__` de base, en lui passant le `tutorialScheduler`.
	 - Création d'un `Blinker`
	 - Initialisation d'une variable qui comptera le nombre de zap effectués.

 - `populateArena` : 
	 - Placement des chips en dur, selon les infos définies au départ dans `LIST_TILE_TO_HARDDEFINE`.

 - `respawnZapValidator` : 
	 - Dans les versions sans tuto, cette fonction doit recréer, après chaque zap, un nouveau `zapValidatorBase` à partir de données choisies au hasard. Dans la version overridée, il faut créer des consignes de zap pas au hasard, selon les infos définies dans `LIST_ZAP_CONSTRAINT`. On utilise le compteur de zap. Lorsque toutes les consignes de zap définies en dur ont été passées, on peut faire ce qu'on veut. Pour ne pas s'embêter, on revient à des créations avec du hasard.

Le tutoriel du mode Touillette override une fonction supplémentaire : `periodicAction`. Dans la classe de base `GameTouillette`, la fonction `periodicAction` affiche un message lorsque le joueur récupère une touillette. Cependant, lorsqu'il y a un tutoriel, il ne faut pas polluer la console avec ce genre de message. (Il y a déjà suffisamment de blablabla). L'overridage de `periodicAction` supprime cet affichage de message. C'est à dire que `periodicAction` ne fait plus rien.

(C'est déjà bizarre d'avoir mis ce bout de code dans `periodicAction`, mais là, c'est encore plus bizarre de l'enlever de cette manière. J'ai vraiment eu du mal à coder tout ça bien comme il faut. J'en suis sincèrement désolé).

#### Intégration du tutoriel dans le reste du code ####

Le `TutorialScheduler` est principalement utilisé par `GameBasic`, mais pas que.

##### Fonction GameBasic.showCurrentTutoStep #####

Cette fonction doit être appelée lorsqu'on vient d'avancer d'une étape. Elle effectue toutes les actions relative à l'étape courante :

 - Affichage de `listTextDescrip` dans la console.
 - Émission du son, si il y en a (la plupart viennent de ma superbe voix qui raconte n'importe quoi).
 - Démarrage du blink, s'il y a des tiles à blinker.
 - Lock des stimulis, si nécessaire.

##### Réalisation d'un zap #####

Dans la Game Loop, on vérifie que le `TutorialScheduler` n'a pas locké les stimulis, avant d'exécuter la fonction `GameBasic.tryToZap`.

Dans la fonction `GameBasic.tryToZap`, après avoir vérifié que le zap a réussi, on exécute la fonction `TutorialScheduler.takeStimTileSelected`, afin d'envoyer le stimuli de réalisation d'un zap. Si ça fait avancer d'une étape, on exécute la fonction `showCurrentTutoStep`.

Si le `TutorialScheduler` est tombé dans l'état `totallyFailed`, on affiche le texte de fail.

Lorsqu'un zap est réussi, il faut afficher la description de la consigne du nouveau zap. Mais on ne le fait que si le `TutorialScheduler` l'autorise (le `tellObjective` de l'étape courante doit être à True).

##### Appui sur la touche "F" #####

Lorsque le joueur appuie sur "F", le `stimuliStocker` met à True sa variable `stimTutoNext`. Lorsque la Game Loop le détecte, elle exécute la fonction `GameBasic.execStimTutoNext`.

Le stimuli est directement transféré au tutoriel, par un appel à la fonction `tutorialScheduler.takeStimTutoNext`.

Si la fonction renvoie True, c'est qu'on a avancé d'une étape. Dans ce cas, on exécute la foncton `GameBasic.showCurrentTutoStep`. Puis, on affiche la consigne actuelle du zap, si le `TutorialScheduler` l'autorise.

Si la fonction renvoie False, on ne devrait rien avoir à faire. Mais comme on est gentil, on redémarre un blink de tile, si l'étape courante indique qu'il y en a à faire. Ça permet au joueur de revoir les blinks.

##### Interactive touch #####

Durant la Game Loop, lorsqu'un Interactive Touch est réussi, le stimuli correspondant est envoyé, via la fonction `tutorialScheduler.takeStimInteractiveTouch`. Si la fonction renvoie True, on a avancé d'une étape, donc on exécute `GameBasic.showCurrentTutoStep`. On ne réaffiche pas la description de consigne du zap. Elle n'est pas censée avoir changé suite à un Interactive Touch.

##### handleGravity #####

Lorsque la fonction `GameBasic.handleGravity` s'aperçoit que le jeu est devenu stable, elle est censée délocker les stimulis. Mais avant, elle vérifie (via un appel à `mustLockGameStimuli`) que le `tutorialScheduler` ne souhaite pas conserver du lock.

On retrouve ce même code dans `GameAspirin.handleGravity`. Une partie du code de `GameBasic` est vilainement copié-collé dans `GameAspirin`.

##### Début du jeu #####

Au début du jeu (début de la fonction `playOneGame`), on affiche la première étape du tutoriel.

Ensuite, il faut afficher la consigne de zap, à condition que le `TutorialScheduler` l'autorise.

##### Reblink #####

Fonctionnalité très peu documentée parce qu'on s'en fout. (Le reclignotement des tiles est déjà géré quand le joueur rappuie sur "F").

Quand le joueur appuie sur "G", le `stimuliStocker` active le stimuli `stimReblink`, la Game Loop récupère la liste de blinks courante auprès du `TutorialScheduler`, et elle redémarre le blink, en exécutant `blinker.startBlink`. 

##### ManualInGame #####

La classe `ManualInGame`, qui affiche les touches de fonction à l'écran, a besoin du `TutorialScheduler`. On lui passe en paramètre dans la fonction `__init__`.

En réalité, le manual n'appelle aucune fonction du `TutorialScheduler`. Il teste juste si celui-ci est défini (différent de None). Si oui, il affiche deux lignes d'info en plus. Il s'agit des textes suivants :

 - tutoriel :
 -    F : message suivant / refaire clignoter,

Ces textes ne sont donc affichés que si le mode de jeu est un mode à tutoriel.

##### GameAspirin.gameStimuliInteractiveTouch #####

Cette fonction est censée afficher du texte dans la console lorsqu'on parvient à récupérer un cachet d'aspirine. (nombre de cachet pris / nombre de cachet à prendre, ou bien une message de félicitations).

On ne l'affiche que s'il n'y a pas de tutoriel. Car le tutoriel squatte beaucoup la console, donc il ne faut pas la polluer davantage avec d'autres textes qui vont se mélanger avec le blabla du tutoriel.

# Au revoir #

Et à bientôt !! Je vous aime !!
