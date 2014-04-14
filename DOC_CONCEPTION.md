# Document de conception de Kawax #

## Avertissements ##

J'ai abandonné le développement de ce jeu. Le code n'est pas terminé, et contient beaucoup de parties non factorisée.

Vous constaterez également que le PEP8 a été foulé aux pieds, écartelé, équarri, et humilié en place publique par des petits enfants jetant des cailloux. C'est la faute à l'entreprise dans laquelle je bossais à l'époque, qui m'a appris à coder en python avec les conventions de nommage du C++. Il va falloir faire avec !

Une fois, au lycée, il y a eu un contrôle de Sciences Nat' (SVT pour les plus jeunes). J'avais énormément détaillé la réponse de l'un des exercices, en expliquant pourquoi il fallait choisir cette solution, quelles conditions génériques il fallait respecter dans ce choix, etc. Lorsque le prof a corrigé le contrôle, il a dit que "certains d'entre nous en avaient mis une tartine et qu'on n'y comprenait rien".

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

Instanciaton de la classe GameXXX correspondant au mode de jeu choisi. Il s'agit, soit de la classe `GameBasic`, soit d'une classe héritée de `GameBasic`. Elles commencent toutes par "Game". **Dans la suite de cette documentation, ces classes seront désignées par `GameXXX`.**

### Initialisation des trucs dans GameXXX ###

fonction `GameXXX.__init__` :

On va considérer que le mode de jeu actuel est sans tutoriel. (Les détails concernant les tutoriaux seront expliqués plus loin).

Les actions d'init sont réalisés par la fonction `__init__` elle-même, et par la fonction interne `initCommonStuff`

 - Récupération de la surface (objet pygame représentant une zone de dessin) dans laquelle doit se dessiner le jeu. Cette surface correspond à la fenêtre affichée à l'écran.

 - Création d'un objet `Console` : affichage de texte sur le côté droit de l'écran.

 - Premier dessin de la console à l'écran.

 - Création d'un `ManualnGame` : affichage des touches du jeu, en bas à gauche de l'écran.

 - Premier (et unique) dessin du manuel à l'écran.

 - Création d'un `StimuliStockerForGame` : récupération de tous les événements souris et clavier, traduction en "stimulis" de jeu.

 - Création d'un `pygame.time.Clock` : objet de la librairie pygame, permet de contrôler le nombre de FPS.

 - Configuration de la gravité (dans quelle direction les pièces du jeu tombent) et de la regénération (comment les pièces du jeu se regénèrent). On utilise pour cela des objets "crawler". Voir plus loin.

 - Instanciaton d'une classe `ArenaBasic`, ou d'une classe héritée. Gère tout le bazar associé à l'aire de jeu : "game logic", affichage, déplacement des éléments lors de la gravité, ... **Dans la suite de cette documentation, les classes `ArenaBasic` et toutes les classes héritées seront désignées par `ArenaXXX`.**

 - Création d'un Selector : gère les différents mode de sélection des cases de l'aire de jeu (chemin principal, sélections additionnelles).

 - Remplissage au hasard de l'aire de jeu : pièces, sucres, aspirine, touillettes, ...

 - Premier dessin de l'aire de jeu.

 - Premier rafraîchissement de l'écran (bien que ça n'ait pas grand-chose à foutre dans l'init, puisque ça sera fait en boucle après).

Retour à `main.py`

Exécution de la fonction `GameXXX.playOneGame()`.

Cette fonction commence par faire quelques bidouilleries d'init :

 - Création d'un `ZapValidatorBase`, afin de définir une première valeur de brouzouf et de sucre que le joueur doit obtenir.

 - Affichage de la première étape du tutoriel, si il y a un tutoriel,

 - ou sinon, affichage de l'objectif à atteindre, en terme de brouzouf et de nombre de sucres. (désolé pour le "en terme de", ici , il me semble réellement approprié). Le texte d'objectif à afficher est déterminé par le ZapValidator.

Puis, la fonction `GameXXX.playOneGame()` entre dans la "game loop", la boucle principale qui fait fonctionner le jeu.

### Game Loop ###

Le déroulement global de la game loop est le suivant :

 - Auto-ralentissage pour qu'elle ne s'exécute au maximum que 60 frames par secondes.

 - Récupération des appuis de touches, mouvements de souris, appui/relâchage de bouton de souris par le `stimuliStocker` (instance de `StimuliStockerForGame`). Conversion de ces événements en "stimulis". ("Un stimuli", "des stimulis", et que les latinistes distingués ne viennent pas me faire chier).

 - Récupération de ces stimulis par la game loop, actions sur divers membres de la classe `GameXXX` selon ces stimulis.

 - Application de la gravité (certains éléments de l'aire de jeu descendront d'une case), et regénération de tiles (ajout de nouvelles pièces/sucres/autres dans les espaces laissés vides par la gravité). Cette action n'est exécutée qui s'il y a de la gravité à appliquer. De plus, elle n'est exécutée que toutes les 18 frames, afin de laisser le temps au joueur de voir ce qu'il se passe.

 - Exécution de la fonction `periodicAction` : ne fait rien dans le mode GameBasic. Les autres modes de jeu peuvent y rajouter des choses.

 - Mises à jour du clignotement des tiles, si il y en a à faire clignoter. Cela n'arrive que durant les tutoriels. Voir plus loin.

 - Redessin complet de l'aire de jeu, même si rien n'a changé. Oui c'est bourrin, oui j'avais prévu de faire un peu plus subtil, non je l'ai pas fait.

 - Rafraîchissement complet de l'écran. C'est bourrin aussi.

## Description détaillée des aspects du jeu ##

### Initialisation des classes GameXXX et ArenaXXX ###

L'initialisation est organisée de manière un peu bordelique. Les classes `GameXXX` possèdent toutes une fonction `__init__` et une fonction `initCommonStuff`. 

`initCommonStuff` est définie dans la classe de base `GameBasic`. Elle n'est jamais héritée.

`__init__` doit systématiquement appeler `initCommonStuff` dès le début. Le code qui vient ensuite peut varier d'un héritage à l'autre.

J'ai fait comme ça pour pouvoir factoriser du code. Sauf que ça a pas été si efficace que ça, parce qu'à la fin des fonctions `GameXXX.__init`, on retrouve très souvent le même mini-bloc de code :
 
 - `self.populateArena()`
 - `self.arena.draw()`
 - `pygame.display.flip()`

Mais pas toujours, et pas forcément exactement comme ça. Ça me tirlapines de voir ça se répéter. Il faut que je dise à mon cerveau d'arrêter de vouloir systématiquement factoriser, parce que ça finit par être dangereux.

Pour les classes `ArenaXXX`, j'ai utilisé la même idée. 

Sauf qu'à un moment, je sais pas ce que j'ai foutu, j'ai dû oublié, ou fumer une bière de trop. J'ai créé une fonction vide `ArenaBasic.start`, qu'on peut overrider dans les `ArenaXXX` héritées. Ça fait double emploi avec l'idée précédente.

Bref, c'est le bazar, et je ne saurais pas justifier pourquoi. Désolé !

### Initialisation de l'aire de jeu ###

lors de l'initialisation de `ArenaXXX` : création de `ArenaXXX.randomChipGenInit`. Il s'agit d'une instance de `RandomChipGenerator`.

création de `ArenaXXX.matrixTile` : un tableau en 2D d'instance de `Tile` (classe définie dans le fichier `tile.py`).

Une tile = une case de l'aire de jeu.

Chaque tile contient une instance d'une classe `Chip`. 

Une chip = un objet dans l'aire de jeu : une pièce de monnaie, un sucre, un mégot de clope, ...

Les différents types de chip sont définis en héritant la classe `Chip`. Tout est placé dans le fichier `coins.py`. (Le nom est mal choisi, désolé).

Lorsqu'on déplace un objet dans l'aire de jeu (par exemple, pour appliquer la gravité), on déplace la chip, mais pas la tile. La tile ne change jamais, et on n'en crée pas de nouvelle durant une partie. 

L'initialisation de l'aire de jeu consiste à remplir `matrixTile` avec des chips, de manière plus ou moins aléatoire.

Cette action est effectuée par l'imbrication d'appels de fonction suivant :

 - `ArenaBasic.createMatrixTile`.
 	- pour chaque tile de l'aire de jeu : `ArenaBasic.createChipAtStart`.
	 	- `ArenaBasic.randomChipGenInit.chooseChip`.
		 	- Choix d'une chip au hasard, selon des coefficients de probabilité spécifiques. Renvoi de la chip.
    - Création de la tile, en plaçant la chip nouvellement créée dedans. 

Les probabilités de choix de chip sont définies par `listRandDistribution`, paramètre transmis au `RandomChipGenerator` lors de son initialisation. Chaque élément de cette liste est un tuple de 2 éléments :

 - Information de génération d'une chip en particulier.
 - Coefficient de probabilité (nombre entier).

La somme des coeffs de tous les éléments de la liste peut faire n'importe quelle valeur, on s'en fout.

Une information de génération est un tuple, de x éléments. Le premier est un identifiant permettant de savoir quelle classe héritée de chip il faut instancier (`ChipCoin`, `ChipSugar`, `ChipClope`, ...) et les éventuels éléments suivants sont les paramètres à envoyer lors de l'instanciation de la classe. Par exemple, `ChipCoin` nécessite qu'on lui passe en paramètre la valeur de la pièce (en brouzouf). Le fait de mettre tout ce bazar dans les infos de génération permet de donner les coefs qu'on veut pour la probabilité d'apparition de la pièce de 1, celle de la pièce de 2, etc...

La regénération des chip, après un zap, est également effectuée selon le même principe. C'est une classe `RandomChipGenerator` qui s'en occupe. Mais pas la même. Il s'agit de `ArenaXXX.randomChipGenAfterGrav`.

Donc potentiellement, on peut avoir des probabilités différentes pour la génération initiale des chips, et pour la génération durant la partie. Même si concrètement, j'ai mis les mêmes proba, parce que euh... voilà... c'est plus simple comme ça. Et puis c'est compliqué à équilibrer tout ce bazar.

### Sélection des tiles ###

L'information "quelle tile est sélectionnée, et de quelle manière", est stockée un peu bizarrement. C'est parce que je voulais prévoir la possibilité d'avoir plusieurs joueurs sur la même aire de jeu, qui feraient chacun leurs sélections respectives.

Or donc, cette info de sélection est stockée dans la classe Tile.

La classe Tile contient une liste appelée `dicPlayerSel` (on me dit dans l'oreillette que c'est confusionnant). Chaque élément de la liste correspond à la sélection d'un joueur. Concrètement, dans tout le code que j'ai fait, il n'y a qu'un joueur, et `dicPlayerSel` ne contient toujours qu'un et un seul élément.

Cet élément peut prendre l'une des trois valeurs suivantes :

 - SELTYPE_PATH : La tile est sélectionnée dans le chemin principal. À l'écran, elle est dessinée avec un cadre rouge.
 - SELTYPE_SUPPL : La tile est sélectionnée par une sélection additionnelle. Elle est dessinée avec un cadre orange.
 - SELTYPE_NONE : La tile n'est pas sélectionnée. Elle est dessinée sans cadre.

Tout le blabla de ce chapitre a pour but de décrire de quelle manière la valeur de `dicPlayerSel` est modifiée, en fonction des actions effectuées par le joueur.  

À l'initialisation de ArenaXXX, On indique le nombre de joueur (c'est toujours 1). `matrixTile` est créé. chaque Tile est donc initialisée avec son `dicPlayerSel` de un seul élément, valant SELTYPE_NONE.   

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

Si `posArenaPrevious` est très éloignée de `posArenaMouse`, il peut y avoir plusieurs chemins possible pour les relier. On décide arbitrairement de faire d'abord le déplacement en X, puis celui en Y.

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

Il reste un dernier mode : SELMODE\_FORBIDDEN, mais je m'en sers jamais. (Je sais plus ce que je voulais faire avec, donc osef).

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

 - Dans tous les autres cas. -> Déselection de toutes les tiles (chemin principal et sélection additionnelle). Création d'un nouveau path sur la tile activée. Le mode devient SELMODE_PATH. 

#### Prise en compte des activations de tile qui viennent après ####

Cette action est réalisée par la fonction `takeStimuliActivateTile` (les autres blocs `if`), et également par `tryToActivatePath`.

C'est comme lors de la première activation, mais en plus simple, car on a moins de cas possibles.

 - en mode SELMODE_PATH : On reprend les 3 premiers cas du chapitre précédent. Si on n'est dans aucun de ces 3 cas, on ne fait rien. Ça arrive lorsque le joueur active une tile non-adjacente au chemin principal (par exemple, le joueur sort le curseur de souris de l'aire de jeu, et y revient, mais par un autre endroit).

 - en mode SELMODE\_SUPPL\_ADD : Si la tile activée n'est pas sélectionnée, on l'ajoute à la sélection additionnelle. Si elle est déjà sélectionnée, on ne fait rien.

 - en mode SELMODE\_SUPPL\_REMOVE :  Si la tile activée est dans la sélection additionnelle, on la déselectionne. Si elle est sélectionnée par le chemin principal, ou non sélectionnée, on ne fait rien.

#### Déselection en cascade ####

L'ensemble de la sélection doit toujours être constitué d'un seul bloc.

Lorsqu'une ou plusieurs tiles sont déselectionnées (quelle que soit les tiles, quel que soit la méthode de déselection), il y a un risque que des sélections additionnelles ne soient plus reliées au chemin principal. Dans ce cas, il faut automatiquement déselectionner toutes ces tiles non reliées. 

Cette action est réalisée par la fonction `Selector.unselectTileSupplAlone`. Je ne sais plus comment l'algo fonctionne en détail. Il y a quelques commentaires pour aider. Je laisse le lecteur explorer ça comme il le veut. 

#### Modification effective de la sélection d'une tile ####

Maintenant qu'on sait sur quelles tiles agir, et quel sélection/déselection appliquer dessus, il faut le faire. La méthode est un peu alambiquée, et passe à travers plusieurs fonctions.

Le `Selector` a tout ce qu'il faut pour lancer l'action : 

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

La fonction `tryToZap` récupère la sélection de tile et l'envoie au `ZapValidatorBase`. Si celui-ci répond que le zap n'est pas valide, on affiche dans la console la description du zap échoué.

Si le zap est valide, la fonction `tryToZap` exécute les actions suivantes :

 - Envoi d'un message au tutoriel, pour prévenir qu'un zap a été fait. (Le fonctionnement des tutoriels sera détaillé plus loin).
 - Exécution de `GameXXX.zapWin` : fonction qui ne fait pas grand-chose, mais qui peut être overridé dans d'autres classes GameXXX.
 - Refabrication d'un autre `ZapValidatorBase`, avec une autre contrainte sur les brouzoufs et les sucres (déterminées au hasard).
 - Envoi du zap à toutes les tiles sélectionnées. Ce qui enchaîne l'exécution imbriquée des fonctions suivantes :
	 - `GameXXX.arena.zapSelection()`. 
		 - Sur chaque position de la sélection : `GameXXX.arena.zapOnePos()`.
			 - `tile.zap()`
				 - sur la chip contenue dans la tile : `tile.chip.zap()`.
				 	- Cette fonction renvoie un nouvel objet Chip, correspondant au résultat du zap. 
				 	- Dans les faits, toutes les chip renvoient `ChipNothing`, c'est à dire un emplacement vide.
			 - L'objet arena remplace la chip de la tile par le résultat du zap. C'est cette action qui réalise effectivement la suppression des pièces et des sucres.   
 - (revenons à `tryToZap`). Déselection de toutes les tiles précédemment sélectionnées. Fonction `selectorPlayerOne.cancelAllSelection()`.
 - Si le jeu a besoin de se "stabiliser" : Déclenchement du délai de gravité et lock des stimulis. Cette action a pour but d'appliquer la gravité sur l'aire de jeu. (Voir plus loin).
 - Affichage, dans la console, de la contrainte du prochain zap, en appelant la fonction `ZapValidatorBase.getListStrDescription` Cet affichage n'est pas forcément effectué dans le cas des tutoriels. (Voir plus loin aussi). 

#### Trucs qui auraient pu servir pour le zap, et en fait non ####

Durant l'imbrication de fonction exécutée pour le zap, on transmet deux paramètres : 

 - `zapType` : correspond à la façon dont la tile a été sélectionnée pour le zap. `ZAP_PATH` : chemin principal. `ZAP_SUPPL` : sélection additionnelle.
 - `zapForce` : force du zap. Concrètement, on met toujours 1.
 
Ces deux valeurs pourraient être utilisées par la méthode `Chip.zap()`, pour des cas spécifiques. Exemple :

 - Une chip avec des points de vie. Si le jeu permet, d'une manière ou d'une autre, de faire des zap de force supérieure à 1, on enlève plusieurs points de vie d'un coup.
 - Une chip qui ne disparaît que si elle est sélectionnée dans le chemin principal.  

La fonction `Chip.zap()` renvoie toujours une instance de `ChipNothing`, mais elle pourrait faire d'autre chose. Par exemple : une chip qui se transforme en une autre. 

La fonction peut également renvoyer `None`, pour signaler de ne pas faire de remplacement. Ça peut servir dans le cas des chip à points de vie. Le zap modifie la quantité de points de vie (valeur contenue dans la chip), mais ne remplace pas la chip elle-même.

### Stimuli lock/delock ###

Le lock/delock des stimulis est un truc pas très bien géré, et qui a provoqué plein de bugs de partout. Je pense les avoir tout corrigé, mais rien n'est sûr.

Objectif initial du lock/delock : empêcher le joueur de sélectionner des tiles, et de les zapper, durant les moments où le jeu est occupé à autre chose, ce qui aurait risqué de mettre le jeu dans un état chambardesque.

Le jeu est "occupé à autre chose" dans les cas suivants :

 - Le jeu est en cours de stabilisation : la gravité est en cours, ou bien des chips sont en cours de création afin de combler des espaces vides.
 - En mode tutoriel : du texte explicatif est affiché dans la console, et le joueur doit appuyer sur la touche "F", afin de passer à l'étape de tutoriel suivante.

Le lock a lieu dans la classe `Selector`, et non pas, contrairement à ce qu'on aurait pu croire, dans la classe `StimuliStockerForGame`. 

Pour effectuer un lock, exécuter la fonction `GameXXX.selectorPlayerOne.setStimuliLock(True)`. Pour l'enlever, faire pareil, avec le paramètre `False`.

Lorsque le lock est mis en place, les clics du joueur ne sont plus pris en compte pour la sélection des tiles. La fonction `Selector.takeStimuliActivateTile` est toujours appelée, mais ne fait plus rien.

Par contre, les clics "d'interactive touch" restent pris en compte, même lorsque le lock est activé. Ce n'est peut-être pas tout à fait logique. Euh... Hem... Passons.

Les moments où les lock/delock sont effectués sont détaillés dans d'autre partie de cette documentation. Voir partie "Gravité" et partie "Tutoriel".

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

Cette vérification est effectuée après un zap (dans la fonction `GameXXX.tryToZap()`, et également après un "interactive touch" qui a fonctionné (dans la fonction `GameXXX.playOneGame`, juste après l'appel à `stimuliInteractiveTouch`). 

Les interactive touch peuvent modifier l'aire de jeu, c'est pour ça qu'on fait la vérif aussi à ce moment là. Par exemple : on clique sur un aspirine, ça le supprime, donc il faut appliquer la gravité, etc.

Cette vérification est effectuée par la fonction `GameXXX.needStabilization`. Si elle renvoie True, l'état est instable. Sinon, il est stable. 

Cette fonction a également un autre rôle : définir la variable `GameXXX.gravityMovements`, qui décrit les mouvements de chip à effectuer lors de la prochaine gravité. Cette variable est une instance de `GravityMovements` (voir plus loin pour une explication détaillée de son fonctionnement interne). 

`GameXXX.gravityMovements` peut être None, ou définie avec une liste de mouvements vide. Dans les deux cas il n'y a pas de gravité à appliquer.

Lorsque `GameXXX.needStabilization` renvoie True, le code extérieur qui l'a appelée doit effectuer les deux actions suivantes :

 - Locker les stimulis (voir chapitre d'avant).
 - Définir `gravityCounter` à `DELAY_GRAVITY`, ce qui permettra d'appliquer la gravité/regénération ultérieurement. (la gravité n'est pas appliquée tout de suite lors de la première vérification).  

Sauf que dans les modes de jeu spécifiques (touillettes, aspro), `gravityCounter` est défini durant un appel à `GameXXX.needStabilization`, qui a été overridée. Ce n'est pas très homogène tout ça. Y'a qu'à dire que c'est pas grave. 

#### Application des gravités successives ####

Le fait de devoir continuer ou pas d'appliquer les gravités est déterminé par `GameXXX.gravityCounter`. À chaque cycle de jeu, la fonction `GameXXX.playOneGame` décrémente cette variable de 1. lorsqu'elle atteint 0, la fonction `GameXXX.handleGravity` est appelée. Elle effectue les actions suivantes :

 - Application de la gravité une fois, en utilisant `GameXXX.gravityMovements` qui a été définie précédemment.
	 - Exécution de `GameXXX.applyGravity`
		 - Exécution de `ArenaXXX.applyGravity`. Déplacement effectif des chips dans l'aire de jeu, pour les faire tomber d'une case.
	     - Exécution de `ArenaXXX.regenerateAllChipsAfterOneGravity`. Création de nouvelle chips, en haut de l'aire de jeu, dans les emplacements qui ont été laissés vides par la gravité.
     - Exécution de `GameXXX.needStabilization`. Si la fonction renvoie True, on redéfinit `gravityCounter` à `DELAY_GRAVITY`, pour réappliquer une prochaine gravité dans quelques cycles.
     - L'appel à `needStabilization` a remis à jour `GameXXX.gravityMovements`, avec de nouvelles valeurs correspondant aux mouvements de la prochaine gravité à appliquer.          

#### Fin de gravité ####

Si `GameXXX.needStabilization` renvoie False, on laisse `GameXXX.gravityCounter` à 0. Les prochains cycles de jeu déduiront, de cette variable à 0, qu'il n y'a plus de gravité à gérer. `GameXXX.handleGravity` ne sera plus appelée. 

En fin de gravité, il faut délocker les stimulis, puisqu'on les avait précédemment lockés. Enfin... Sauf si le `tutorialScheduler` veut conserver le lock. Mais "voir plus loin", car c'est déjà assez compliqué et entrelacé comme ça, tout ce bazar.

D'autre part, lorsque `needStabilization` renvoie False, elle est censée avoir défini `GameXXX.gravityMovements` à None, ou n'avoir mis aucun mouvement dedans. (On s'en fout, on ne contrôle pas le contenu de cette variable, mais je tenais à le préciser).

#### Regénération sans gravité ####

Lorsqu'en exécute une gravité une fois, on regénère tout de suite après les chips aux emplacements laissés vides, dans la ligne du haut. Cette action est effectuée par la fonction `ArenaXXX.regenerateAllChipsAfterOneGravity`.

On pourrait donc penser qu'à aucun moment, on n'ait besoin de juste regénérer des chips. Si pas de gravité -> pas d'emplacements vides en haut de l'aire de jeu -> pas besoin de regénération.

Eh bien non. Lorsque le joueur a zappé des chips uniquement dans la ligne du haut, on est dans un cas où il faut regénérer, mais où il n'y a pas de gravité à appliquer.

Cette situation se règle avec l'enchaînement d'actions suivants :

 - Il y a eu un zap ou un interactive touch.
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

La classe `GravityMovements`, définie dans le fichier `gravmov.py`, a pour vocation d'être la plus générique possible. C'est à dire qu'elle gère des mouvements de gravité quel que soit la direction (les chips pourraient tomber vers le haut, vers la gauche, ...).

Elle peut également gérer des mouvements de gravité avec des "gros objets" (par exemple, les touillettes).

Dans une aire de jeu à gros objets, il peut y avoir plusieurs mouvements de gravité séparés, sur une même colonne. Exemple, avec un zap en forme de "C" :

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

Dans la deuxième colonne, Les deux 0 du haut vont tomber. Le 1 ne va pas tomber, car il est retenu par la touillette, le 2 va tomber, le 5 ne va pas tomber, car il est tout en bas.

La classe `GravityMovements` doit être capable de gérer ce genre de subtilité.

Les infos stockées par cette classe ne peuvent servir que pour l'application d'une seule gravité (chaque chip soumise à la gravité ne fera qu'un seul mouvement). Pour faire la gravité suivante il faut repartir d'une nouvelle instance de `GravityMovements` et remettre des infos dedans à partir de 0.

Comme il faut gérer n'importe quelle direction, on ne raisonne pas en coordonnées X et Y, mais en coordonnés primaire (les lignes/colonnes le long desquelles s'appliquent la gravité) et en coordonnées secondaires (la coordonnée qui va augmenter ou diminuer de 1).

La classe `GravityMovements` contient la variable `dicMovement` : un dictionnaire.

 - clé : une coordonnée primaire
 - valeur : une liste de tuple de deux éléments. Chaque tuple définit un "segment gravitant". Avec :
	 - premier élément : coordonnée secondaire du début du segment. Cela correspond toujours à l'emplacement vide qui permet de démarrer la gravité.
	 - second élément : coordonnée secondaire de fin du segment (non incluse dans le segment, comme pour les ranges et les slices python qui n'incluent pas le dernier élément).

Si on reprend l'exemple précédent, après analyse complète de l'aire de jeu, prise en compte de la touillette, et dans le cas d'une gravité vers le bas, on devrait avoir un `GravityMovements.dicMovement` comme suit :

    {
        0: [    # pour la colonne de gauche. X = 0
            (2,     # coord (X=0, Y=2) : 
                    # emplacement vide juste en dessous des deux chip "0"
             -1     # coord (X=0, Y=-1) :
                    # Dernier élément du segment, qui n'est pas inclus 
            ),
        ],
        1: [    # pour la colonne suivante. X = 1
            (2, -1),  # Pareil. Les deux chips "0" du haut vont tomber
            (6,  4),  # Et en plus, la chip "2" va tomber,
                      # à cause du vide (coord X=1, Y=6)
                      # Le dernier élément n'est pas inclus (coord Y = 4)
        ]
    }

Lorsque la gravité est vers le bas, le premier élément de chaque segment gravitant est toujours strictement supérieur au dernier élément. Lorsque la gravité est vers le haut, c'est le contraire.

Lorsque la gravité est vers la droite : premier élément > dernier élément.
Lorsque la gravité est vers la gauche : dernier élément > premier élément. 

Pour gérer tout ça, la classe `GravityMovements` dispose des fonctions suivantes :

 - `__init__`, en précisant le type de gravité.
 - `cancelAllMoves` : vidage du dictionnaire `dicMovement`.
 - `addSegmentMove` : ajout d'un segment gravitant. Attention, la fonction ne fusionne pas les segments existants avec le nouveau. On peut donc se retrouver dans une situation de ce type : { 0 : [ (3, -1), (2, 1) ] }. Ce serait tout à fait incohérent et ce n'est jamais censé arriver. Donc il faut faire attention à ce qu'on envoie lors des appels successifs à `addSegmentMove`.
 - `cancelGravity` : annulation de la gravité pour une position spécifique. Cette fonction peut "raccourcir" un segment. Elle n'est utilisée que dans les arènes contenant des gros objets (touillettes). Voir explication détaillée plus loin.
 - `isInGravity` : indique, pour une position donnée, si elle se trouve dans un segment gravitant ou pas. (Renvoie True/False).
 - `isListInGravity` : indique, pour une liste de position donnée, si elles sont toutes dans un segment gravitant (`IN_GRAVITY_YES`), ou si seulement certaines d'entre elles le sont (`IN_GRAVITY_PARTLY`), ou si aucune d'entre elles le sont (`IN_GRAVITY_NO`).
 - `removeEmptyListSegment` : fonction à appeler après avoir exécuté un ou plusieurs `cancelGravity`. Permet de supprimer les coordonnées primaires qui n'ont plus aucun segments gravitants. Par exemple, si `dicMovement` vaut { 0 : [ (1, -1) ], 3 : [] }. Après exécution de `removeEmptyListSegment`, on aura : { 0 : [ (1, -1) ] }.     

#### Détermination des mouvements de gravité ####

La détermination des chips subissant une gravité (donc, le remplissage d'un objet `GravityMovements`) est effectué par la fonction `arenaXXX.determineGravity()`

L'algorithme est le suivant (dans le cas d'une gravité vers le bas) :

Pour chaque colonne, on parcourt toutes les chips, en allant du bas vers le haut:

 - On passe les premières chips non vides. Elles ne tomberont pas. `currentState = SKIP_NOT_FALLING_TILE`
 - Dès qu'on rencontre une chip vide, on change d'état. `currentState = ADVANCE_NOTHING_TILE`. Et on continue d'avancer tant qu'on est dans les chips vides.
 - Si on rencontre une chip qui ne peut pas tomber (ça existe pas dans le jeu, mais ça pourrait). On oublie ce qu'on a fait, et on revient à `currentState = SKIP_NOT_FALLING_TILE`. 
 - Si on rencontre une chip non vide, qui peut tomber, on retient la coordonnée de l'emplacement précédent (emplacement vide qui permet de démarrer la gravité). Et `currentState = ADVANCE_CONSEQUENT_TILE`. On avance de cette manière tant qu'on rencontre des chips non vides acceptant de tomber.
 - Lorsqu'on rencontre autre chose, ou qu'on arrive tout en haut de l'aire de jeu, on a trouvé un segment gravitant. On l'enregistre dans un `GravityMovements`, avec : 
 	- coord primaire = X de la colonne courante. 
 	- coord secondaire de début du segment = Y de l'emplacement vide précédemment retenu. 
 	- coord secondaire de fin du segment = Y actuel.
 - On revient `currentState = SKIP_NOT_FALLING_TILE` ou `currentState = ADVANCE_NOTHING_TILE` selon qu'on est sur une chip vide ou une chip qui n'accepte pas la gravité. 

Pour les gravités des modes de jeu spécifiques (gros objets, rift) : voir plus loin.

#### La classe ArenaCrawler ####

Cette classe est définie dans le fichier `crawler.py`. Elle permet de parcourir les positions d'une aire de jeu dans le sens qu'on veut, et éventuellement en passant directement à la ligne/colonne suivante.

Un `ArenaCrawler` se contente de renvoyer des coordonnées (sous forme de classes `pygame.Rect`), correspondant à des positions successives dans une aire de jeu. Il connaît la taille de l'aire de jeu, mais pas l'aire de jeu en elle-même. Il n'analyse pas les tiles ou les chips. C'est au code extérieur de faire ça.

On utilise la notion de coordonnée primaire/secondaire. Lorsque la coordonnée primaire est X, les "gros" changements de coordonnées seront sur le X. C'est à dire que le crawler se déplacera le long des colonnes. Il parcourt tous les Y d'une colonne. Puis fait un "gros" changement, modifie son X et passe à la colonne suivante, et ainsi de suite.

Plus précisément, on ne spécifie pas de coordonnée primaire/secondaire, mais des directions primaire/secondaire.

Si la direction primaire est LEFT ou RIGHT, la coordonnée primaire est X. Si la direction primaire est UP ou DOWN, la coordonnée primaire est Y. Pareil pour le secondaire.

La coordonnée primaire et la coordonnée secondaire doivent être différente. Sinon c'est n'importe quoi.

Exemple d'ordre de parcours de l'aire de jeu, pour une taille de X=3, Y=5.

    direction primaire = DOWN. direction secondaire = RIGHT.

    Y    0   1   2
    |    3   4   5
         6   7   8
         9  10  11
        12  13  14 
 
    X ->

    dirPrim = RIGHT. dirSec = UP
         4   9  14
         3   8  13
         2   7  12
         1   6  11
         0   5  10            

    etc.

Pour utiliser un `ArenaCrawler`, il faut commencer par l'instancier, le configurer et le démarrer :

 - Instanciation, en spécifiant la taille de l'aire de jeu.
 - Exécution de `ArenaCrawler.config`, en spécifiant la direction primaire et la secondaire.
 - Exécution de `ArenaCrawler.start()`

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

Durant le crawling, on peut lire les variables membres suivantes, pour savoir où on est (elles sont pertinentes dès l'appel à `start`, avant même d'avoir exécuté un premier `crawl` ou un premier `jumpOnPrimCoord` :

 - `posCur` : objet `pygame.Rect`. Position courante.
 - `posPrev` : objet `pygame.Rect`. Position précédente (si on a exécuté un `jumpOnPrimCoord`, `posPrev` se trouve forcément sur la ligne/colonne précédente.
 - `coP` : entier. coordonnée primaire courante. 
 - `coS` : entier. coordonnée secondaire courante. 
 - `crawledOnPrimCoord` : booléen. Indique si on vient de changer de coordonnée primaire.
 - Les fonctions `crawl` et `jumpOnPrimCoord` renvoient un booléen. Si celui-ci est True, on est sur une position valide. Si il est False, la position courante est invalide, car on est arrivé au bout de l'aire de jeu. Dans ce cas, on ne devrait pas consulter les variables ci-dessus, car elles contiennent des informations non utilisables.

Il est possible de rappeler `crawl` et `jumpOnPrimCoord` après que l'une d'elles ait renvoyé False. Mais les résultats récupérés ne sont pas vraiment utilisables. (En fait ça devrait s'arrêter, ou carrément balancer une exception).  

#### Configuration de gravité par les crawlers ####

La détermination de la gravité, son application, et la regénération des chips après gravité sont tous gérés avec des `ArenaCrawler`. 

Selon le sens dans lequel on parcourt l'aire de jeu pour effectuer ces tâches, on peut appliquer la gravité dans la direction qu'on veut.

La configuration des crawlers en fonction de la direction de gravité souhaitée est effectuée dans `GameXXX.initCommonStuff`, (fin de la fonction). On se sert de `DICT_GRAVITY_CONFIG`, défini dans `gambasic.py`.

Tous les modes de jeu actuels utilisent une gravité vers le bas (sauf le mode aspro, mais sa gravité vers la gauche est gérée différemment). Tout ça pour dire que la super-généricité de code que j'ai mis en place, avec les crawlers et la gravité, n'est pas utilisée. Mais ça pourrait. J'avais testé, ça marchait. (Disons que ça a marché à un certain moment de la vie du programme).

Pour une explication détaillée de "comment ça marche dans des directions autres que vers le bas" : voir code. Si j'explique avec du texte, ça va être super long et compliqué. C'est presque plus simple de regarder le code.

"Algorithme : voir code". J'adore quand ce genre de grossiereté est écrite dans de la documentation. Et je viens de le faire. Tant pis ! 

### Interactive Touch ###

Les "interactive touch" ont pour but d'exécuter des actions spécifiques dans l'arène, lorsque le joueur clique sur l'une des chips. Ça pourrait permettre de faire un tas de choses, dans des modes de jeu spécifiques, ou pour des chips spécifiques : téléportation, échange de chip, augmentation de la valeur d'une pièce, ...

Les "interactive touch" sont totalement indépendant des zap. Le fonctionnement est implémenté dans `GameBasic` et `ArenaBasic`. Mais il ne sert à rien. Il faut overrider quelques fonctions pour le rendre utile. C'est ce qui est fait dans le mode aspro (Voir plus loin).

Le fonctionnement général est le suivant :

 - L'utilisateur clique dans la fenêtre du jeu.
 - Le `stimuliStocker` détecte ce clic, en déduit la tile cliquée, et enregistre sa position dans la variable interne `posArenaToInteractTouch`. (Cette action est effectuée uniquement sur les clics, pas sur les mouvements de souris, ni sur le maintien du bouton appuyé)
 - dans la game loop : récupération de `stimuliStocker.posArenaToInteractTouch`. 
 - Si la variable contient une position, exécution de la fonction `ArenaXXX.stimuliInteractiveTouch`, en passant la position en paramètre.
 - Cette fonction a le droit de faire tout et n'importe quoi sur les tiles et les chips de l'aire de jeu. Si elle fait quelque chose, elle doit répondre `True`, sinon elle répond `False`. 
 - Concrètement, `ArenaBasic.stimuliInteractiveTouch` ne fait rien et renvoie toujours False. Mais la fonction peut être overridée dans d'autres modes de jeu spécifiques.
 - (retour à la game loop). Si la fonction a renvoyé `True` :
	 - Annulation de la sélection faite par le joueur, parce que s'il s'est passé quelque chose dans l'aire de jeu, la sélection précédente n'est peut-être plus valid.
	 - L'aire de jeu est peut-être dans un état "instable". On doit donc agir comme si il y avait eu un zap : vérification s'il faut effectuer une gravité ou une regénération, lock des stimulis, définition de `gravityCounter`, etc.
	 - Gestion du tutoriel, s'il y en a un (voir plus loin).
 - Plusieurs gravités peuvent s'effectuer les unes après les autres, si besoin. Le délockage des stimulis sera effectuée à la fin de la dernière gravité, comme pour le zap.  
 - pour finir, exécution de `GameXXX.gameStimuliInteractiveTouch`. Comme pour `ArenaBasic.stimuliInteractiveTouch`, cette fonction peut faire un peu ce qu'on veut, mais au niveau du `GameXXX`, et pas de `ArenaXXX`. Par contre, pas la peine de renvoyer `True` ou `False` pour signaler qu'on a fait quelque chose ou pas. Là, on s'en tape.
 - Concrètement, `GameBasic.gameStimuliInteractiveTouch` ne fait rien. Seule la fonction overridée dans le mode aspro fait quelque chose.

## Spécificités des modes de jeu spécifique (ha ha) ##

### Gestion des "gros objets" ###

### periodicAction (dans le mode touillette) ###

### Gravity Rift (dans le mode aspro) ###

### Interactive Touch sur les aspirines ###

### Tutoriel ###
