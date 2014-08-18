# Kawax. Idées en vrac #

## Principe principal (ha ha) ##

match sum(x)

L'aire de jeu est constitué d'un quadrillage de case. Chaque case comporte un objet (une pièce de monnaie, un sucre, ...).

Il y a une pile de boutons de café, à gauche de l'écran. Ça représente les différents choix d'une machine à café. Chaque bouton correspond à un type de café, avec un prix spécifique, en centimes de brouzoufs (la monnaie nationale).

Le joueur clique sur un bouton, puis sélectionne un groupe de pièces dans l'aire de jeu, correspondant au prix. Lorsque le joueur valide, le café se fait, les pièces disparaissent (elles sont "zappées"), le bouton aussi, et un autre bouton apparaît d'un autre type de café.

Au départ, on voit 3 boutons. On peut choisir parmi les 2 premiers. Le troisième permet de prévoir ce qu'on aura ensuite.

Le choix entre 2 boutons permet d'avoir quelque chose de jouable. Par exemple, si le premier boutons est un café difficile, on utilise le deuxième plusieurs fois, pour préparer l'aire de jeu et réussir à faire le premier.

(À équilibrer. Parce que dans la version actuelle du jeu, il n'y a qu'un bouton, on ne peut rien prévoir, et ça reste tout à fait jouable).

Il faut sélectionner la somme exacte de brouzoufs requis. La sélection est constituée d'un groupe de cases connexes. On sélectionne d'abord un chemin, traçable en une fois, puis les cases additionnelles, sans contrainte de chemin.

## Boissons possibles ##

À équilibrer, évidemment.

 - gobelet d'eau : 2 centimes de brouzoufs
 - café : 12
 - café au lait : 15
 - potage au potiron : 13
 - cacao : 20
 - cacao avec du lait : 23
 - jus d'orange dégueu en poudre : 7
 - ricard : 51
 - sang de chèvre vierge : 666 (à débloquer avec une quête)
 - boisson au gingembre aphrodisiaque : 69

## Objets du jeu ##

### Pièces ###

 - Pièces de 1, 2, 5, 10, 20, 50 centimes de brouzoufs.

 - Pièces bizarres : 3, 7, ...

 - Bouton de culotte / jeton de caddie : Vaut 0. Sélectionnable comme une autre pièce.

 - Pièce-joker. Quand on fait une sélection, elle prend automatiquement la valeur de brouzoufs qui va bien, parmi 1, 2, 5, 10, 20, 50.

### Sucre ###

Un café nécessite une certaine somme de brouzoufs, plus X sucres. (Exactement X). Les sucres sont des objets dans l'aire de jeu, sélectionnables comme des pièces.

 - Sucre normal.

 - Sucrettes à l'aspartame : équivalent à 2,3 ou 4 sucres sur une même case. Le nombre de sucrettes indique la valeur.

 - Sucre-joker : donne pil poil le bon nombre de sucre requis. (Un bonbon ? Du sucre liquide ? Du caramel ?).

Super-pouvoir : sélectionner 5 sucres adjacents pour les fusionner en un sucre-joker.

Super-pouvoir : sucrier / boîte à sucre. Permet de sélectionner plus de sucre que ce qui est requis pour un café, afin de le stocker et de l'utiliser plus tard.

### Chewing-gum ###

Sélectionnable. Il a plusieurs points de vie, et en perd un pour chaque zap effectué sur une case adjacente, ainsi que sur sa propre case. (Donc il peut perdre jusqu'à 9 points de vie d'un coup).

Il n'est pas soumis à la gravité. Du coup, il laisse des cases vides en dessous de lui. Mais à chaque perte d'un ou plusieurs point de vie, il tombe d'une case.

Pour éviter que ce soit trop facile, on peut interdire de faire une sélection passant par deux chewing-gums adjacent. Ça n'empêche pas de faire un détour en sélectionnant des cases à côté, pour ensuite revenir sur le deuxième.

Pièce avec du chewing-gum dessus ? Pièce sale ?

Super-pouvoir : faire tomber d'une case tous les chewing-gums. Éventuellement, ils peuvent en plus perdre un ou plusieurs points de vie.

Super-pouvoir : fusionner deux (ou plus) chewing-gums adjacents. On en obtient un seul ayant la somme des points de vie de tous les chewing-gums fusionnés. Le joueur choisit, parmi les cases à fusionner, celle dans laquelle ira le gros chewing-gum final. Les autres cases deviennent vide.

Super-pouvoir : utiliser un glaçon pour geler un chewing-gum. Ça ne lui fait pas perdre de points de vie, mais il devient soumis à la gravité comme un objet normal.

### Mégot de clope / coucougnou ###

Insélectionnable. Ou pas. (À décider).

Il possède 8/9 points de vie maximum. Il les perd de la même manière que les chewing-gums, par un zap sur des cases adjacentes. Mais il faut enlever tous les points de vie en une seule fois, sinon, ça n'a aucun effet.

Ce qui signifie que si le mégot est insélectionnable, et qu'il y en a deux côte à côte avec 8 points de vie chacun, on ne peut pas les détruire. Woups, faudra faire gaffe à ça.

Pour simplifier, on peut juste faire 4 mégot différents, avec 1/3/5/8 points de vie. Sinon ça fait trop d'images différentes, on s'y paume.

Super-pouvoir : le fume-mégot. Fait baisser les points de vie d'un mégot.

Un chewing-gum collé à un mégot ? Faut d'abord détruire le mégot, avec une grosse sélection d'un coup, puis détruire le chewing-gum. (Ou l'inverse ?).

### Gros objets ###

Ils prennent plusieurs cases. Un gros objet ne tombe que si toutes les cases sur lesquelles il repose sont vides en même temps.

Pour récupérer le gros objet, 2 façons possibles (selon le mode de jeu, la gravité ou autre).

 - Le faire tomber en bas de l'aire de jeu.

 - Zapper des cases autour, de façon à l'englober. Selon l'objet ou le mode, il faut soit obligatoirement faire un englobage le plus proche possible, soit on a le droit d'y inclure d'autres cases.

Ces deux modes de récupération peuvent aussi s'appliquer à des petits objets spécifiques (Une petite clé, un badge, ...)

Idées en vrac de gros objets :

 - gros sucre
 - touillettes horizontale ou verticale. (on peut les tordre : voir plus loin).
 - billet de 5 brouzoufs
 - sachet de thé
 - stylo
 - post-it
 - tasse
 - gobelet

Gros chewing-gum : deux chewing-gums simples adjacents se collent entre eux, et ça fait un gros objet de 2 cases. C'est pas pareil que la fusion de chewing-gum. La fusion aide le joueur. Le collage le pénalise.

Un énorme chewing-gum qui prend plein de cases, avec plein de points de vie sur chaque case. Il faut le détruire petit à petit, case par case.

### Autres idées d'objets en vrac ###

 - chocolat
 - lait
 - gnôle (la gnôle dans le café, c'est indispensable)
 - niveau de café qui monte (l'aire de jeu est immergée en partie)
 - du sel, pour ceux qui prennent un café salé
 - un truc gazeux qui s'étend sur les cases vides
 - des capsules de Georges Clooney le gros naze

## Actions pour gagner des points de style ou des XP ##

Le but du jeu est d'accumuler des points. Je ne sais pas encore comment on les appellera : score, points de style, XP, ...

 - Faire un zap : ça rapporte un nombre de points dépendant de la difficulté du café fait.

 - Faire un zap avec le nombre minimal de pièce : ça rapporte < nombre de pièces * 2> points. Il faut un algo déterminant le nombre de pièce minimal selon une somme et une liste de valeurs de pièces. (L'algo simple ne fonctionne pas. 16 avec (10, 8, 4, 2). 16 = 10 + 4 + 2, alors que 16 = 8 + 8).

 - Zap sans pièce de 1 : < nb de pièces> points.

 - Zap sans pièce de 2 : < nb de pièces> points. Cumulable avec le précédent.

 - Toutes les pièces pareilles : < nb de pièces> points.

 - Zap fait en un seul chemin, sans sélection additionnelle. Bonus supp si le chemin est tracé correctement en une fois.

### Illumination de cases ###

Lorsqu'on fait un zap, ça augmente de 1 la luminosité des cases sur lesquelles il a eu lieu.

Si on rezappe des cases illuminées, on gagne des points. Mettons : (somme totale des luminosités / 100)

Si on rezappe exactement les mêmes cases qu'avant, leur luminosité augmente de 5 d'un coup, et on attribue les points qui vont avec.

Si on ne rezappe que des cases déjà illuminées (mais pas toutes), leur luminosité augmente de 2, et on attribue les points qui vont avec.

À chaque zap, les cases illuminées qui ne sont pas rezappées subissent une perte (totale ou partielle, à décider) de leur luminosité.

C'est bordelique ce truc, je ne suis pas sûr que ça ait un intérêt quelconque, et je ne vois pas comment le justifier au niveau du scénario.

On oublie pour l'instant.

## Pouvoirs spéciaux ##

Ces pouvoirs coûtent des points à activer. Ils ne sont pas forcément tous disponibles dès le début. Il faut les débloquer (avec des quêtes ou en dépensant des points).

 - Utiliser une tasse au lieu d'un gobelet : -1 sur le coût du café.

 - Ajouter une touillettte : +1 sur le coût du café. (Achievement stupide : utiliser une tasse et une touillette).

 - Shuffle de l'aire de jeu.

 - Changer une pièce en jeton de caddie, en pièce-joker, ...

 - Échanger deux objets.

 - Enlever un doublon de la pile de boutons de café.

 - Enlever un pas-doublon de la pile de boutons de café.

 - Bombe : destruction d'un pavé de 9 cases, d'une croix, d'une ligne, ... Ça peut détruire n'importe quelle type d'objet, ou que les objets conventionnels (sucres, pièces).

 - Bombe qui explose sur la dernière case du chemin de sélection. Plus le chemin est long, plus l'explosion est grosse, comme dans le jeu 4 Elements.

 - Doubler la force, le score et l'illumination de case lors d'un zap.

 - Diminuer la probabilité d'apparition des pièces et objets pourris.

 - Zapper l'intérieur d'une zone. Par exemple : on zappe un carré de 3*3 sans la case du milieu. Le pouvoir fait zapper la case du milieu en plus.

 - Cassage de pièce. On sélectionne une pièce ainsi que X cases vides connexes. La pièce se transforme en X+1 pièces de valeurs inférieures. Par exemple, une pièce de 5 se transforme en 5 pièces de 1. Une pièce de 10 en 5 pièces de 2, ...

 - Autre manière pour le cassage : on sélectionne la pièce pour l'activer, puis on fait un zap de X cases vides à côté. La pièce activée se casse automatiquement et les petites pièces vont dans les cases vides.

 - Multi-cassage de pièces, avec des sélections de n pièces et n*X cases. Et ça peut être sujet à des achievements (le plus grand "n" possible). Mais c'est un peu bourrin quand même.

 - Pouvoir passif : avoir plus de boutons de café (pour avoir plus de choix et/ou plus de prévisions des prochains cafés à faire). Par exemple, on pourrait aller jusqu'à 6 boutons visible, et on peut choisir parmi les 4 premiers. (À équilibrer).

Des objets spéciaux qui déclenchent un pouvoir lorsqu'on les zappe. La force du pouvoir est d'autant plus grande qu'on a zappé un grand nombre de case.

Quand on fait un carré de 3*3, ça fait apparaître un objet cool au milieu (genre une bombe). Et quand on fait vraiment pil poil le carré, sans rien sélectionner autour, ça le fait aussi, mais en mieux. Et avec des carrés plus grand, ça le fait aussi, mais en mieux-mieux.

## Achievements ##

 - Avoir X jeton de caddie dans un zap.

 - Faire un zap avec que des pièces de même valeur. (X pièces de valeur Y) (Et zézétte épouse X).

 - Gagner X points en un seul zap.

 - Cumuler XXX points en une partie. Il faudra utiliser des valeurs fun, genre 1337, et non pas 1000, 2000, ...

 - Zapper XXX cases en une seule fois.

 - Tous les achievements à la con de longévité : utiliser 200 touillettes, 200 tasses, 2000 cafés, ... Faut pas en faire de trop, car c'est pouillave. Il vaut mieux mettre des quêtes que des achievements de longévité.

 - Faire des zaps de forme spécifique : ligne, carré, colonne, ...

 - Casser X mégots de résistance Y en un seul coup.

 - Pour chaque type de café : en faire un avec le moins de pièce possibles.

Faire des achievements et des quêtes donne plein de points, et jouer une partie en donne un petit peu. On débloque les pouvoirs et on avance dans le jeu grâce à ces points. Comme ça, le joueur est jamais bloqué, même si il est nul. Il aura juste à faire plein de parties.

Quand on fera d'autres jeux : les XP d'un jeu apportent un peu d'XP dans les autres jeux. La validation se fait avec des codes secrets genre clé md5 ou autre. Même si on pourra jamais vraiment faire complètement secret parce que de toutes façons je distribue toujours tout le code source.

## Fusion de pièces ##

Disponible uniquement dans certains modes de jeu, et/ou après avoir débloqué le pouvoir.

On sélectionne 5 pièces de 1, puis on reclique sur une des pièces sélectionnées. Ça fait une pièce de 5 à l'endroit choisi.

On peut faire des combos :

 - fusionner 2 pièces de 1 en une pièce de 2,
 - s'en servir avec 4 autres pièces de 2 pour faire une pièce de 10,
 - se servir de la pièce de 10, avec une autre, pour faire une pièce de 20,
 - ...

On peut monter jusqu'à des valeurs très hautes. Par exemple : la pièce de 100 centimes, soit un brouzouf entier !

Il y a évidemment des achievements sur le plus grand nombre de combos réalisés.

Éventuellement : pas de regénération d'objets dans l'aire de jeu tant qu'on fait des fusions de pièces. Ça permet de limiter le trop grand nombre de combos, et ça évite d'arriver à des valeurs gigantesques comme une pièce de 10 000 brouzoufs.

Et si on fusionne X pièces ayant toutes des valeurs différentes, ça crée une pièce joker.

Donc précédemment, je parlais de cassage de pièce, et maintenant je parle de fusion de pièces. Les deux s'annulent. Tout ça pour bien préciser que ce document n'est rien de plus que des idées en vrac.

## Dosages de la difficulté ##

 - plus (+) de chewing gum et de clopes
 - moins de jeton de caddie
 - plus de grosses pièces
 - plus de café à des prix bizarres
 - plus de pièces pourries (3, 7, ...)

À équilibrer selon les modes de jeu, les pouvoirs, etc. Bref, c'est du boulot.

## Quêtes / modes de jeu ##

Pour chaque quête, il faut essayer d'en faire 3 versions :

 - de base (facile)
 - hard (super dur)
 - chiante (facile, mais long)

La version de base est obligatoire pour avancer dans le jeu, les autres non.

### Exploration ###

C'est le mode principal. Il est disponible après que le joueur ait effectué quelques tutoriels, et des quêtes simples, où il faut juste faire des cafés.

Scénario : la machine à café devient folle, elle en renverse partout. Ça s'étale sur le sol mais c'est absorbé par la moquette. Les "instances décisionnelles" de l'entreprise ne veulent pas la remplacer, car ce problème ne les dérange pas, elles utilisent leur propre machine à café haut de gamme. Il faut détruire la moquette petit à petit, pour propager l'écoulement de café jusqu'au bureau des instances décisionnelles.

L'aire de jeu est gigantesque, elle représente les locaux de l'entreprise. Il n'y a pas de gravité, les objets se regénèrent directement sur les cases zappées. On commence dans une petite zone où se trouve la machine à café.

Chaque case possède une "densité de moquette", (en plus de son objet). Lorsqu'on zappe une case, sa densité diminue de 1. Lorsqu'elle atteint 0, le café peut s'écouler dedans. Ça fonctionne comme dans 4 Elements.

On peut se promener dans l'aire de jeu gigantesque à condition qu'une case avec du café écoulé reste toujours visible à l'écran. Il faut donc progresser petit à petit. Mais on progresse dans les directions qu'on veut.

En se déplaçant ainsi, on arrive à des bureaux d'autres collègues, qui donnent des quêtes annexes, des pouvoirs, des XP, ...

Certaines zones ne sont pas accessibles dès le début, car entourée par des objets qu'on ne peut pas détruire. Il faut obtenir le pouvoir correspondant.

Par exemple, au début, on ne peut pas prendre de sucre, ni détruire de clopes. Or, on débute dans une zone restreinte entourée de sucres/clopes. Il faut obtenir les pouvoirs correspondants pour pouvoir aller plus loin.

Il pourrait également y avoir des gros objets. Le seul moyen de les récupérer serait de les entourer avec un zap (en faisant des sélections assez grande). Mais au début, on n'a pas de café assez cher pour pouvoir sélectionner suffisamment de pièces. Il faut débloquer ces cafés avec une quête. Par exemple, le fameux "sang de chèvre vierge" à 666 centimes de brouzoufs.

Dans cette aire de jeu gigantesque, les carrés ayant encore de la moquette peuvent générer des objets chiants, ça dépend de la zone dans laquelle on se trouve. Mais une fois qu'on a enlevé la moquette, la case ne génère que des objets classiques : jetons de caddie, pièces de valeur normales, sucres. Ça rend le mode de jeu un peu facile, mais ça ajoute un sentiment de "nettoyage". Les quêtes et les autres modes sont là pour donner de la difficulté et des objets bizarres à l'infini. ("With some hardcore depts", comme on dit chez les concepteurs de jeu).

On doit pouvoir voir une vue d'ensemble de la zone déjà explorée. Ça permet de revenir plus rapidement à un endroit connu, d'avoir une carte, et de renforcer le sentiment de nettoyage.

### Création/récupération d'objets ###

Diverses quêtes en vrac, liées à des gros objets.

 - Faire un carré de 10 * 7 sucre, pour créer un morceau de sucre géant, puis le faire tomber en bas pour le récupérer.

 - Quête de refabrication de cigarette, pour les clochards. Il faut faire un carré de 5 * 2 mégots. Ça crée une clope, et il faut la récupérer. Ça peut être difficile car il faut rassembler les mégots sans les détruire. Donc sans trop faire de zap à côté.

 - Faire une ligne ou un rectangle de X*Y pièces de même valeur pour créer un billet.

 - Une tasse (gros objet), qu'on doit renverser en zappant les cases pas tout à fait en dessous, mais un peu à côté. Des tasses de plus en plus grandes pour que ce soit de plus en plus dur. Permet d'obtenir le pouvoir de la tasse (-1 au prix du café).

 - Une touillette qu'il faut tordre. Chaque fois qu'on zappe des cases à côté d'elle, elle se tord un peu. Il faut le faire petit à petit. Si on zappe une trop grande zone, la touillette se tord trop vite, se casse, et c'est perdu. Permet d'obtenir le pouvoir de la touillette (+1 au prix du café).

### Mal aux cheveux ###

Il faut récupérer des cachets d'aspirine, en fusionnant des demi-cachets.

Correspond au mode aspro du jeu que j'ai fait.

Si on prépare plusieurs aspirines, pour ensuite tous les fusionner et les récupérer à la suite, ça fait des points.

On obtient également du score en vidant complètement plusieurs colonnes en une seule fois.

### Radin ###

Pas de regénération de pièces dans l'aire de jeu. Il faut toutes les zapper et obtenir une aire totalement vide à la fin.

Ça risque d'être chiant, car très dépendant du hasard. Vers la fin, il faut avoir des prix de café correspondant pil poil à ce qu'il reste dans l'aire de jeu. Faudrait trouver une astuce pour déchiantiser le truc.

### Rapide ###

Avec un temps total limité et/ou un temps limité pour chaque café.

### Gros fumeur ###

L'aire de jeu représente un cendrier contenant une pile géante de mégot. On commence tout au dessus. On creuse de plus en plus profond dans la pile au fur et à mesure qu'on détruit les mégots. (Mais il y a toujours des pièces et des sucres qui arrivent par au-dessus, pour pouvoir jouer).

L'écran descend automatiquement dans l'aire de jeu, soit après X secondes, soit X zaps. Ou alors, on choisit quand ça descend, mais on a un nombre de zaps limités, et il faut aller le plus profondément possible.

Version chiante de la quête : on creuse à l'infini. Les mégots sont de plus en plus résistants.

Permet d'obtenir le pouvoir de destruction des mégots.

### Multi-sélection ###

On fait plusieurs sélections dans l'aire de jeu, sans que ça déclenche de zap. (Chaque sélection est associé à un type de café, comme d'habitude). On ne peut pas sélectionner deux fois une même case. Plus on fait de sélection, plus on a de score.

Ensuite on valide, ça fait tous les zaps d'un seul coup, et on recommence.

### Accumulation ###

Chaque fois qu'on fait un café, on additionne son prix à une valeur globale. Il faut atteindre pil poil une valeur spécifique.

(Chiant et sans aucun intérêt, parce que trop dépendant du hasard. Faudra trouver autre chose).

Scénario : Avec la valeur cumulée, on achète un gros truc. Par exemple un sachet de bonbon ou un Snickers. (Au fait, pourquoi ça s'appelle Snickers cette merde ?).

### Combo de fusion ###

Fusionner des pièces de 1 pour faire une pièce de 5. Puis utiliser cette pièce pour faire une autre fusion (deux pièces de 5 en une pièce de 10). etc.

### Énigme ###

Aire de jeu avec des objets prédéfinis. Pas de regénération. Liste des cafés prédéfinie également. Il faut réussir à faire toute la liste.

### Ficelle ###

Scénario : on met dans la machine à café des pièces accrochées à des ficelles. Ça permet de les récupérer ensuite, et de se faire des cafés sans payer. Haha lol.

L'aire de jeu est initialisée aléatoirement, comme d'habitude. Mais les objets ne disparaissent pas quand on les zappe, il n'y a donc pas de regénération.

Il faut faire un café à 10 centimes de brouzoufs, puis un autre à 11, 12, etc.

Éventuellement, pour augmenter la difficulté : chaque zap doit obligatoirement inclure la pièce située au milieu de l'aire de jeu. (Je sais pas comment on peut justifier ça scénaristiquement, mais on s'en fout).

### Régime ###

Au départ, L'aire de jeu comporte des sucres. Mais aucun nouveau sucre n'est généré.

Il faut faire le plus de café possible.

(Une fois de plus : bof. C'est trop dépendant du hasard).

### Diabétique ###

On a le droit de prendre plus de sucre que ce qui est demandé par le type de café. Quand on en prend plus, ça fait du score.

Au début, la probabilité d'apparition des sucres est très haute, et elle diminue petit à petit.

### Pièces de collection ###

Certaines pièces de l'aire de jeu sont spéciales. SI on fait un café avec, ça fait du score. mais le score augmente de beaucoup si on utilise plusieurs de ces pièces. Il faut donc essayer de les regrouper dans un coin et des les utiliser toutes d'un coup.

### Einstein ###

Interdit de déselectionner des objets. Si on tente un zap alors qu'on n'a pas choisi le bon nombre de brouzoufs et de sucre, on perd tout de suite.

Le but, c'est de forcer le joueur à faire du calcul mental.

### Sudoku ###

Regrouper 9 éléments différents dans un carré de 3*3, pour obtenir ... je sais pas quoi. Un truc cool.

### Connexion ###

Il faut connecter deux (ou plus) cases spécifiques en faisant un zap. La sélection de tile zappées doit tracer un chemin d'une case vers l'autre.

### Casseur de sucre ###

(Je ne sais plus vraiment ce que je voulais dire avec cette idée. J'ai dû la noter à l'arrache quand j'étais bourré. Tant pis. Dans le doute, je la garde).

Il faut casser un sucre en deux. On ne doit pas toucher aux moitiés du sucre, mais on doit taper au milieu.
Ensuite, il faut faire tomber l'une des deux moitiés.

### Vroum vroum ###

L'aire de jeu comporte un objet qui se déplace dans une direction spécifique (une mini-voiture-jouet ? un cadeau bonux ? Des billes ?). Il faut emmener cette objet quelque part. Éventuellement, sur certaines actions, il change de direction.

Il peut aussi y avoir plusieurs objets de ce type, et il faut les faire se rencontrer à un endroit spécifique.

Scénario : utiliser des billes, pour faire péter les expressions corporates associées : "J'ai pas le billes. Je te refile les billes. etc.".

### Glaçons ###

L'aire de jeu comporte des glaçons, qui fondent petit à petit (avec le temps, ou à chaque zap). Il faut se dépêcher de les emmener en bas de l'écran avant qu'ils fondent complètement.

Donne le pouvoir de glaçon pour geler les chewing-gums.

### Coincé ###

Aire de jeu avec des tailles bizarres : très grande et étroite, très petite et allongée, toute petite-petite, etc. Si l'aire est petite, il faudra adapter les cafés disponibles, en mettant plus souvent ceux qui ont un petit prix.

### Le chemin ###

On ne peut sélectionner des cases qu'avec le chemin principal. Pas de sélection additionnelle.

### Sociable ###

Jeu à plusieurs joueurs, sur un écran splitté, ou alors sur le même écran. On peut se mélanger les pinceaux dans les cases sélectionnées, et c'est ça qui est rigolo.

Jeu à plusieurs sur une aire de jeu gigantesque avec moquette. Les joueurs doivent conquérir le plus de cases possible. Une case est conquise quand on enlève sa dernière densité de moquette. Un joueur ne peut plus sélectionner les cases conquises par les autres joueurs. Ça veut dire qu'il faut aller le plus vite possible, et essayer d'enfermer les autres joueurs dans des cases conquises. On peut imaginer que certains joueurs s'allient temporairement pour en enfermer d'autres.

### Glou-glou ###

L'aire de jeu est plongée dans du café. Certains objets remontent (touillettes, jetons de caddie), d'autres tombent (pièces). Il faut récupérer les touillettes.

S'il y a quelques cases vides au dessus d'une touillette, elle sont très vite remplies par des pièces qui tombent. Si on zappe en une seule fois toutes les cases immédiatement au dessus d'une touillette, elle peut monter d'un cran.

### Tutoriel ###

Des modes de jeu tutoriels pour les modes de jeux spécifiques.

Aire de jeu prédéfinie, actions prédéfinies à faire par le joueur, avec des explications à chaque action. Si le joueur fait d'autres actions que celles prédéfinies, on l'interdit, ou on le laisse faire mais après il se démerde.

## Univers du jeu ##

Ça se passe dans une entreprise, donc il faut plein de trucs corporate.

Éléments de langage : instances décisionnelles, ressources occasionnelles, zone sociale (salle de pause), noms de salle et de bureau à la con comme dans les vraies boîtes, ...

Les quêtes à faire et les achievements sont signalés sous forme de mails et de post-it. Le héros du jeu a un ordinateur avec une messagerie de merde, genre Outlook. Les mails arrivent au fur et à mesure, mais il y en a plein qui ne servent à rien :

 - La secrétaire qui signale que la photocopieuse est en panne, parce qu'il y avait un slip coincé dedans.
 - Un mec qui a trouvé les toilettes dégueulasse, et qui rappelle que **chacun doit nettoyer son propre caca**.
 - Voitures mal garées.
 - Mail de remotivation des troupes, envoyé par les "instances décisionnelles".
 - Boulet qui a envoyé à tout le monde un message destiné à une seule personne. Puis qui renvoie un mail pour s'excuser.
 - Mail persos de potes, de la maman, ...
 - Spams.
 - ...

Et certains mails sont vraiment intéressants :

 - Descriptions de quêtes.
 - Récapitulatif des scores et des parties effectuées sur la journée ou la semaine.
 - Explications sur le comportement d'objets ou de mode de jeu spécifiques.
 - Demandes de café pour un collègue.
 - Mails de remerciements quand on a effectué une quête ou un achievement.

Le joueur peut se créer des répertoires pour classer tout ça. Mais il est pas obligé.

On retrouve dans les champs "destinataire" et "copie", des personnages du jeu qu'on peut rencontrer dans leurs bureaux. Ça peut permettre de créer du "lore", des interactions entre personnages, etc.

C'est pareil avec les post-its. Ils arrivent en vrac, sont collés sur l'ordinateur du héros. Certains sont intéressants, d'autres non. On peut les ranger dans des petites boîtes, en jeter, ...
