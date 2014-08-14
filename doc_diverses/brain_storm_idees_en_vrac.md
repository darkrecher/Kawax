# Kawax. Idées en vrac #

## Principe principal (ha ha) ##

match sum(x)

L'aire de jeu est constitué d'un quadrillage de case. Chaque case comporte un objet (une pièce de monnaie, un sucre, ...).

Il y a une pile de boutons de café, à gauche de l'écran. Ça représente les différents choix d'une machine à café. Chaque bouton correspond à un type de café, et à un prix spécifique, en centimes de brouzoufs. (Le brouzouf est la monnaie nationale).

Le joueur clique sur un bouton, puis sélectionne un groupe de pièces dans l'aire de jeu, correspondant au prix. Lorsque le joueur valide, le café se fait, les pièces disparaissent (elles sont "zappées"), le bouton aussi, et un autre bouton apparaît d'un autre type de café.  

Au départ, on voit 3 boutons. On peut choisir parmi les 2 premiers. Le troisième permet de prévoir ce qu'on aura ensuite.

Le choix entre 2 boutons permet d'avoir quelque chose de jouable. Par exemple, si l'un des boutons est un type de café difficile, on utilise l'autre plusieurs fois, pour préparer l'aire de jeu et finalement réussir à faire le difficile.

(Après tests : un seul bouton, ça marche assez bien quand même. Ce bazar est à équilibrer).

Il faut sélectionner la somme exacte de brouzoufs requis. La sélection est constitué d'un groupe de case connexe. On sélectionne d'abord un chemin de case, traçable en une fois. Ensuite on sélectionne des cases additionnelles, sans contrainte de chemin, il faut juste qu'une case additionnelle soit adjacente à une case déjà sélectionnée.

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

Pièces de 1, 2, 5, 10, 20, 50 centimes de brouzoufs.

Pièces bizarres : 3, 7, ...

Bouton de culotte / jeton de caddie : Vaut 0. Sélectionnable comme une autre pièce.

La pièce-joker. Quand on fait une sélection, prend automatiquement la valeur de brouzoufs qui va bien, parmi 1, 2, 5, 10, 20, 50. 

### Sucre ###

Pour faire un café, il faut sélectionner une certaine somme de brouzoufs, plus X sucres. (Soit exactement X, soit au moins X. Je sais pas encore)

Sucrettes à l'aspartame : équivalent à 2,3 ou 4 sucres sur une même case, le nombre de sucrettes indique la valeur. 

Sucre-joker : donne pil poil le bon nombre de sucre requis. (Un bonbon ? Du sucre liquide ? Du caramel ?).

Super-pouvoir : sélectionner 5 sucres adjacents pour les fusionner en un sucre-joker.

Super-pouvoir : sucrier ou boîte à sucre. Permet de stocker du sucre récupéré lors d'une sélection, afin de l'utiliser plus tard.

### Chewing-gum ###

Sélectionnable. Il a plusieurs points de vie, et en perd un pour chaque zap effectué sur une case adjacente, ainsi que sur sa propre case. (Donc il peut perdre jusqu'à 9 points de vie d'un coup).

Il n'est pas soumis à la gravité. Du coup, il laisse des cases vides en dessous de lui. Mais à chaque perte d'un ou plusieurs point de vie, il tombe d'une case. 

Pour éviter que ce soit trop facile, on peut interdire de faire une sélection qui passe par deux chewing-gum adjacent. Mais ça n'empêche pas de faire un détour en sélectionnant des cases à côté, pour ensuite revenir sur le chewing-gum adjacent.

Pièce avec du chewing-gum dessus ? Pièce sale ?

Super-pouvoir : faire tomber d'une case tous les chewing-gum. Éventuellement, ils peuvent en plus perdre un ou plusieurs points de vie.

Super-pouvoir : fusionner deux (ou plus) chewing-gums adjacents. Il n'y en a plus qu'un, ayant la somme des points de vie de tous les chewing-gum fusionnés. Les cases occupées par les anciens chewing-gums deviennent vide. Le joueur choisit, parmi les cases de chewing-gum à fusionner, celle dans laquelle ira le gros chewing-gum final. 

Super-pouvoir : utiliser un glaçon pour gèler un chewing-gum. Il faut toujours le détruire comme avant, mais il devient soumis à la gravité comme un objet normal.

### Mégot de clope / coucougnou ###

Insélectionnable. Ou pas. (À décider).

Il possède 8/9 points de vie maximum. Il les perd de la même manière que les chewing-gums, par un zap sur des cases adjacentes. Mais il faut enlever tous les points de vie en une seule fois, sinon, ça n'a aucun effet. 

Ce qui signifie que si le mégot est insélectionnable, et qu'il y en a deux côte à côte avec 8 points de vie chacun, on ne peut pas les détruire. Woups, faudra faire gaffe à ça.

Pour simplifier, on peut juste faire 4 mégot différents, avec 1/3/5/8 points de vie. Sinon ça fait trop d'images différentes, on s'y paume.

Super-pouvoir : le fume-mégot. Fait baisser les points de vie d'un mégot.

Un chewing-gum collé à un mégot ? Faut d'abord détruire le mégot, avec une grosses sélection d'un coup, puis détruire le chewing-gum.

### Gros objets ###

Ils prennent plusieurs cases. Faut les faire tomber petit à petit. Un gros objet ne tombe que si toutes les cases sur lesquelles il repose sont vides en même temps.

Pour récupérer le gros objet, 2 façons possibles (selon le mode de jeu, la gravité ou autre). 

 - Le faire tomber tout en bas.

 - zapper des cases autour, de façon à l'englober. 

TODO : des trucs (de 1 seule case, voir plus) qu'il faut entourer complètement d'une sélection pour les détruire, et qui ouvre d'autres trucs.
Une petite clé ?
Soit un entourage le plus proche possible. Soit avec d'autres cases dedans.

Idées en vrac de gros objets :

 - gros sucre
 - touillettes (horizontale ou verticale) (tordable : voir plus loin).
 - billet de 5 brouzoufs
 - sachet de thé
 - stylo
 - post-it
 - tasse
 - gobelet

Deux chewing-gum côte à côte se collent entre eux, et ça fait un gros objet de 2 cases. C'est pas pareil que la fusion de chewing-gum. La fusion aide le joueur. Le collage le pénalise.

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

 - Activer une sélection : dépend de la difficulté du café fait.

 - Sélection avec le nombre minimal de pièce : <nombre de pièce * 2> points de style. Ca veut dire qu'il faut un algo qui détermine le nombre de pièce minimal selon une somme et une liste de pièce possible. (L'algo simple ne fonctionne pas. 16 avec (10, 8, 4, 2). 16 = 10 + 4 + 2. 16 = 8 + 8.

 - Pas de pièce de 1 : <nb de pièce> points de style.

 - Pas de pièce de 2 : <nb de pièce> points de style. Cumulable avec le précédent.

 - Toutes les pièces pareilles : <nb de pièce> points de style. 

 - Sélection en un seul chemin, sans sélection additionnelle. Bonus supp si le chemin est tracé correctement en une fois. 

### Illumination de cases ###

Lorsqu'on fait un zap, ça augmente de 1 la luminosité des cases sur laquelle y'a eu du zap.

Si on rezappe des cases illuminées, on gagne des points de style. Mettons : (somme totale des luminosités / 100)

Si on rezappe exactement les mêmes cases qu'avant, on augmente de 5 la luminosité, et on attribue les points qui vont avec.

Si on rezappe que des cases déjà illuminées, on augmente de 2 la luminosité, et on attribue les points qui vont avec.

À chaque zap, les cases illuminées qui ne sont pas rezappées subissent une perte de luminosité. de 2, ou d'une autre valeur, ou alors ça retombe directement à 0.

C'est bordelique ce truc, et je suis pas sur que ça ait un intérêt quelconque. Et en tout cas y'a aucune justification à ça.

On oublie pour l'instant.

## Pouvoirs spéciaux ##

Ces pouvoirs coûtent des points de style ou des XP. Ils ne sont pas forcément tous disponibles dès le début. Il faut les débloquer (je sais pas trop comment).

 - Utiliser une tasse au lieu d'un gobelet : -1 sur le coût du café.

 - Ajouter une touillettte : +1 sur le coût du café. (Achievement stupide : utiliser une tasse et une touillette).

 - Shuffle de l'aire de jeu.

 - Changer une pièce en jeton de caddie, en pièce-joker, ...

 - Échanger deux objets.

 - Enlever un doublon de la pile de boutons de café.

 - Enlever un pas-doublon de la pile de touches de café.

 - Bombe : destruction d'un pavé de 9 cases, d'une croix, d'une ligne, ... Ça peut détruire n'importe quelle type d'objet, ou que les objets conventionnels (sucres, pièces).

 - Bombe qui explose sur la dernière case du chemin de sélection, à la 4elements.

 - Doubler la force de zap, le score et l'illumination de case d'une sélection.

 - Diminuer la probabilité d'apparition des pièces et objets pourris.

 - Zapper l'intérieur d'une zone.Par exemple : on zappe un carré de 3*3 sans la case du milieu. Le pouvoir fait zapper la case du milieu en plus. 

 - Cassage de pièce. On sélectionne une pièce ainsi que X cases vides connexes. La pièce se transforme en X+1 pièces de valeurs inférieures. Par exemple, une pièce de 5 se transforme en 5 pièces de 1. Une pièce de 10 en 5 pièces de 2, ...

pour casser une pièce de 1 euro, faut faire une sélection de X cases avec elle dedans. La pièce de 1 euro se casse en X pièce plus petite, et rempli les cases vides.
On peut casser plusieurs pièces, avec des sélection de n*X cases. (Et ça fait des achievement, ça).
Bof, c'est peut être naze. Je sais pas.
TODO : nan, faut faire une sélection à côté pour générer des cases vides à côté.

 - Pouvoir passif : avoir plus de boutons de café (pour avoir plus de choix et/ou plus de prévisions des prochains cafés à faire). Par exemple, on pourrait aller jusqu'à 6 boutons visible, et on peut choisir parmi les 4 premiers. (À équilibrer).

Des objets spéciaux qui déclenchent un pouvoir lorsqu'on les zappe. La force du pouvoir est d'autant plus grande qu'on a zappé un grand nombre de case.

Quand on fait un carré de 3*3, ça fait apparaître un objet cool au milieu (genre une bombe). Et quand on fait vraiment pil poil le carré, sans rien sélectionner autour, ça le fait aussi, mais en mieux. Et avec des carrés plus grand, ça le fait aussi, mais en mieux-mieux.

## Achievements ##

 - Avoir X jeton de caddie dans un zap.

 - Faire un zap avec que des pièces de même valeur. (X pièces de valeur Y) (Et zézétte épouse X).

 - gagner X points de style en un seul zap.

 - cumuler XXX points de style en une partie. Il faudra utiliser des valeurs fun, genre 1337, et non pas 1000, 2000, ...

 - Zapper XXX cases en une seule fois.

 - Tous les achievements à la con de longévité : utiliser 200 touillettes, 200 tasses, 2000 cafés, ... Faut pas en faire de trop, car c'est pouillave. Il vaut mieux mettre des quêtes que des achievements de longévité.

 - Faire des zaps de forme spécifique : ligne, carré, colonne, ...

 - Casser X mégots de résistance Y en un seul coup.

 - Pour chaque type de café : en faire un avec le moins de pièce possibles.

Faire des achievement et des quêtes donne plein de style/XP, et jouer une partie en donne un petit peu. On débloque les pouvoirs et on avance dans le jeu grâce à ces points. Comme ça, le joueur est jamais bloqué, même si il est nul. Il aura juste à faire plein de parties.

Quand on fera d'autres jeux : les XP d'un jeu apportent un peu d'XP dans les autres jeux. La validation se fait avec des codes secrets genre clé md5 ou autre. Même si on pourra jamais vraiment faire complètement secret parce que de toutes façons je distribue toujours tout le code source.

## Fusion de pièces ##

Disponible uniquement dans certains modes de jeu, et/ou après avoir débloqué le pouvoir.

On sélectionne 5 pièces de 1, puis on reclique sur une des pièces sélectionnées. Ça fait une pièce de 5 à l'endroit choisi.

On peut faire des combos : 

 - fusionner 2 pièces de 1 en une pièce de 2
 - s'en servir avec 4 autres pièces de 2 pour faire une pièce de 10
 - se servir de la pièce de 10, avec une autre, pour faire une pièce de 20
 - ...

On peut monter jusqu'à des valeurs très hautes. Par exemple : la pièce de 100 centimes, soit un brouzouf entier !

Il y a évidemment des achievements sur le plus grand nombre de combos réalisés.

Éventuellement : pas de regénération d'objets dans l'aire de jeu tant qu'on fait des fusions de pièces. Ça permet de limiter le trop grand nombre de combos, et d'arriver à des valeurs gigantesques comme une pièce de 10 000 brouzoufs.

Et si on fusionne X pièces ayant toutes des valeurs différentes, on peut créer une pièce joker. 

## Dosages de la difficulté ##

 - plus (+) de chewing gum et de clopes
 - moins de jeton de caddie
 - plus de grosses pièces
 - plus de café à des prix bizarres
 - plus de pièces pourries (3, 7, ...)

À équilibrer selon les modes de jeu, les pouvoirs, etc. Bref, c'est du boulot.

## Quêtes / modes de jeu ##

Pour chaque quête, on va essayer de trouver : la quête de base (facile), la quête hard (super dur), la quête chiante (facile, mais long)

### Exploration ###

aire de jeu gigantesque. Les pièces ne tombent pas. Faut délivrer des cases (à la 4 elements), et on se balade un peu où on veut comme ça.

la mousse qui grandit. (Ca représente de la mousse de café) Bizarre. On étend l'écoulement du café, mais on stoppe la mousse. Faudra justifier ça scénaristiquement. youpi. La mousse c'est du lait devenu fou. Un truc comme ça.

sur l'aire de jeu gigantesque, y'a des sucres et des clopes. On peut pas les casser au début. Quand on a fait la quête de créer des sucres, et celles de créer des clope. On peut.
(Bizarres, car une quête de création permet une quête de destruction).
Ou sinon, on fait 2 quêtes pour chaque. création -> destruction -> on a la capacité. Bof.

C'est du café, qui se répand dans la grande aire de jeu. (genre le liquide, à la 4 elements)

La grande aire de jeu représente un open space de l'entreprise. Elle donne accès à des bureaux avec des quêtes dedans. Qui donne des pouvoirs pour débloquer des endroits bloqués dans la grande aire de jeu. Ouaip. C'est cool.
Mais ça dit rien concernant les XP.

(TODO : expliquer la moquette avec le café qui fuit)

Du coup, pour faire des grandes sélections, faut des boissons chers. Et ça, on les débloque avec des XP ou des quêtes. Ha ha !!! (Genre le café à 666 centimes de brouzoufs)

Dans la grande aire de jeu, les zones de début sont faciles, et ne génère que des 0, 1, 2, 5, ... Plus on s'éloigne, plus on a des risques de voir générer des trucs de daube.
Et peut être que y'aurait des quêtes pour reculer ces zones ? (Ca enlève de l'intérêt au jeu, mais ajoute un sentiment de "nettoyage")
On mettra une map globale, avec les zones et tout.
Mais faut que ce soit visible. (La couleur du café, ou je sais pas quoi)

* la machine à café devient folle, et elle renverse son café partout. on commence la meta-quête, où il faut étendre l'écoulage du café vers d'autres endroits.

### Création/Récupération d'objets ###

Faire un carré de 10 * 7 sucre, pour créer un gros morceaux de sucre, puis le faire tomber en bas pour le récupérer.

faire un carré de 5 * 2 mégots pour recréer une clope, et la faire tomber en bas.

quête de refabrication des mégots. (pour un clochard). D'autant plus dur qu'il faut rassembler les mégots sans les détruire.

faire une ligne / un rectangle de X*Y brouzoufs pour créer un énorme billet !

Eventuellement, une grosse tasse qu'on doit faire tomber en détruisant les tiles d'en bas-à côté. Ca la renverse et ça fait des trucs cools.

quête des tasses. (pareil, mais c'est une tasse). Hard : la tasse est géante. Du coup, quand elle est presque en bas, c'est super dur. (ou alors, on fait des tasses de plus en plus géantes. Et y'en a plusieurs, de plus en plus rapprochées. Et c'est le mode infini)

quête des touillettes. (gros objet de touillette qu'il faut faire tomber) Ca va ressembler aux tasses. Sauf que les touillettes ne tombent pas forcément ? Elle peuvent aller sur les côtés.
Ou alors faut les faire tourner. Faut les tordre sans les casser. Petit à petit. Donc faut sélectionner des zones, mais pas toutes d'un coup, sinon elles se cassent.

bon, ça donne le pouvoir des tasses et des touillettes.

### Mal aux cheveux ###

Y'a des demi-cachets d'aspirine. Faut les fusionner. Quand on pète une colonne entière, ça rapproche. Ca fait pas tomber des trucs gravité machin.
Pouvoir de transformer une aspirine en jeton-0. Mais limité.
Quand on en fait plusieurs d'un coup ou qu'on fait une réaction en chaîne, ça fait du score.
Quand on pète plusieurs colonnes d'un coup ça fait aussi une réaction en chaîne.
Les aspirines se fusionnent que quand ils sont vraiment bien placés. Adjacence horizontale, la moitié gauche à gauche, la droite à droite.
On clique sur l'une des moitiés, ça crée l'aspirine sur cette case.
Et après faudrait soit recliquer dessus, soit le faire tomber tout en bas. on dit cliquage. On va pas prendre la tête avec un truc facile.

### Mode radin ###

pas d'apparition de nouvelles pièces. Et faut toutes les détruire.

### Rapide ###

quête où il faut faire plein de cafés en étant rapide. Temps limité total et/ou temps limité entre chaque café.

### Gros fumeur ###

quête du cendrier. faut creuser creuser creuser. (le mode chiant, c'est le mode infini. On a un score sur la profondeur à laquelle qu'on est allé) (et le mode hard c'est pareil, sauf que la difficulté augmente plus vite)
On choppe le pouvoir de diminution de résistance d'un mégot.

### Multi-sélection ###

avec des combos : on fait plusieurs sélections dans l'aire de jeu. On les active toutes d'un coup. Et faut en faire le plus possible.

### Faire l'appoint (à point) ###

arriver à une somme juste pil poil, avec des activations successives, et acheter une cochonnerie avec.

### Ficelle ###

faire le plus de sélection possibles (coût de 1, 2, 3, ...), avec la même aire de jeu, mais faut toujours que les sélection incluent une pièce parmi un groupe de pièce. (quête de la pièce qu'on récupère à chaque coup car elle est au bout d'une ficelle) faut faire tous les cafés possible de cette manière. Dans l'ordre qu'on veut. Les cases se regénèrent ou pas. Ca dépend (le joueur choisit, ou c'est le jeu qui regénère tout le temps, ou jamais)

### Fusion ###

rassembler des lignes / des sélections de 5 pièces de 1 pour faire une pièce de 5. Puis 4 pièce de 5 pour faire une pièce de 20. Puis 5 pièces de 20 pour faire un brouzouf entier. (Et après on en fait je sais pas quoi)
Ou alors : sélection de X (n'importe comment) pour faire la pièce de valeur X.

faire une sélection de 100 brouzouf (n'importe comment) et ça donne un brouzouf.

### énigme ###

Aire de jeu définie. boissons à faire définie. On se débrouille.

### Régime ###

Y'a des sucres dans l'aire de jeu, mais faut en utiliser le moins possible.

faire un gros tas de sucre pour faire des cafés avec le plus de sucre possible.

### diabétique ###

on a le droit de faire plus de sucre que prévu. Et y'a de plus en plus de sucre qui apparaissent (mais pas trop en fait). Et faut faire des cafés avec de plus en plus de sucre. Si on en fait plus que prévu, ça ralentit un peu l'augmentation de quantité de sucre requise.

### Pièces de collections ###

faire un café avec des pièces spécifiques. (10+10+5+5+5+1 ...)

### Gros fumeur ###

gros tas de mégots.

mode cendrier : aire de jeu très haute, on commence en haut. y'a des megots de clope partout, on doit creuser vers le bas.
ça avance vers le bas soit après x secondes, soit x coups, soit on a un nbre de coups limités mais on choisit soi-même quand descendre.

### Einstein ###

interdit de déselectionner, et on ne voit pas le total des brouzoufs. Donc faut faire du calcul mental.

### sudoku ###

9 elements différents dans un carré de 3*3

### Connexion ###

connecter 2 (ou plus) endroits différents avec une sélection. Ouais ça c'est cool.

### Casseur de sucre ### 

casser un sucre en deux. On doit pas toucher aux moitiés du sucre. Mais on doit taper au milieu. 
Et après faut faire tomber l'une des deux moitiés.
(Je ne sais plus ce que je voulais dire exactement avec cette idée)

### Vroum vroum ###

Un objet qui se déplace dans une direction précise. Et qu'il faudrait emmener quelque part. (Et il fait quoi ?) Il trace un chemin qui fait quelque chose ?
une mini-voiture-jouet ? (genre cadeau bonus à la con). 
Et deux objets qui se cognent à un point de rencontre ? Certes...
C'est des billes qui se déplacent. C'est le plus drôle. Expression corporate : "refiler les billes."

### Glaçons ###

des glaçons, qu'il faut se dépêcher d'emmener en bas sinon ils fondent.

Donne le pouvoir de glaçon pour geler les chewing-gums.

### Coincé ###

aire de jeu avec des tailles bizarres : 40 * 2. 4 * 4 et on fait que des tout petits cafés. (bof)

### Le chemin ###

Que des chemin de sélection. Pas de sélection additionnelle.

### Sociable ###

jeu à 2 ? Sur écran splitté, ou le même écran, ou la même aire de jeu gigantesque (conquête)

### Glou-glou ###

on est plongés dans du café. Les touillettes remontent, mais les pièces tombent. Faut séparer les deux. (Comment exactement ?) Ca c'est une idée marrante. Pas de gravité sur les pièces, mais une regénération. Il faut détruire les pièces juste au-dessus de la touillette, et toutes d'un coup, pour la faire monter d'un cran.

### Tutorial ###

Il me faudra peut être un mode tutorial.
Avec une aire toute faite. Des explications successives. Y'a une action prédéfinie à faire. Si le joueur fait le con, ça part en latte, mais c'est de sa faute.
