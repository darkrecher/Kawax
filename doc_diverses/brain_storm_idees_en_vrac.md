# Kawax. Idées en vrac #

## Principe principal (ha ha) ##

match sum(x)

Il y a une pile de touches de café, à gauche de l'écran. Ça représente les différents choix, comme sur une machine à café. Chaque touche correspond à un type de café, et à un prix spécifique, en brouzoufs.

Le joueur clique sur une touche, puis sélectionne des pièces dans l'aire de jeu, correspondant au prix. Lorsque le joueur valide : le café se fait, les pièces disparaissent (elles sont "zappées"), la touche aussi, et une autre touche arrive, avec un autre type de café.  

Au départ, on voit 3 touches. On peut choisir parmi les 2 premières. La troisième permet de prévoir ce qu'on aura ensuite.

En évoluant dans le jeu, on voit 6 touches, on peut choisir parmi les 4 premières.

Faut au moins 2 possibilités de café pour faire quelque chose de jouable. On prépare le terrain pour l'une des possibilités, en utilisant l'autre possibilité. Ou vice-versa.
Et les possibilités suivantes sont visibles. Ca c'est cool aussi.

(C'est un peu trop, faudra équilibrer ce bazar).

Il faut obtenir la somme exacte de brouzouf, en choisissant des pièces adjacentes. On fait la forme de sélection qu'on veut, et pas forcément un chemin traçable en une fois.

## Boissons possibles ##

(faudra augmenter les prix, dans l'ensemble. J'ai un peu essayé, c'est super facile, là.
 
gobelet d'eau : 2
café : 12
café au lait : 15
potage au potiron : 13
cacao : 20
cacao avec du lait : 23
jus d'orange dégueu en poudre : 7
ricard : 51
sang de chèvre vierge : 666 (faut le débloquer avec une quête)
boisson au gingembre aphrodisiaque : 69

## Objets du jeu ##

### Pièces ###

Pièces de 1, 2, 5, 10, 20, 50

Pièces bizarres : 3, 7, ...

Bouton de culotte / jeton de caddie : Vaut 0. Sélectionnable comme une autre pièce

### Sucre ###

Pour faire un café, il faut sélectionner une certaine somme de brouzoufs, plus X sucres. (Soit exactement X, soit au moins X. Je sais pas encore)

Sucrettes à l'aspartame. Équivalent à 2/3/4 sucres sur une même case. Le nombre de sucrettes indique la valeur. 

Le sucre-joker. (Un bonbon ? Du sucre liquide ? Du caramel). Ça donne pil poil le bon nombre de sucre requis. 

Super-pouvoir : fusionner 5 sucres adjacent en un sucre-joker. (Même principe que pour la fusion de monnaie, voir plus loin).

Du sucre qu'on peut stocker et utiliser pour plus tard.

### Chewing-gum ###

Il a plusieurs points de vie. On peut le sélectionner. Il perd un point de vie pour chaque zap effectué sur une tile adjacente, ainsi que sur sa propre tile. (Donc il peut perdre plusieurs points de vie d'un coup).

Il n'est pas soumis à la gravité. Ça fiche le bordel, car il laisse des cases vides en dessous de lui. Mais à chaque perte d'un ou plusieurs point de vie, il tombe d'une case. 

Pièce avec du chewing-gum dessus ? Pièce sale ?

Objet/pouvoir : faire tomber d'une case tous les chewing-gum (sans qu'ils perdent de points de vie, ou alors si).

Objet/pouvoir : fusionner deux (ou plus) chewing-gums adjacents. Ça en fait un seul, ayant la somme des points de vie de tous les chewing-gum fusionnés. Et ça laisse des cases vides là où y'avait les chewing-gum. Le joueur peut choisir où va le chewing-gum fusionné. 

Glaçon : objet/pouvoir qui gèle un chewing-gum. Il faut toujours le détruire comme avant, mais il tombe dès que possible.

Éventuellement : on ne peut pas faire un chemin de sélection qui passe par deux chewing-gum de suite. Sinon trop facile.

### Mégot de clope / coucougnou ###

miette de pain / mégot de clope. insélectionnable. Disparaît quand on active une sélection adjacente. (Avec X pièces sélectionnées autour. Ca dépend de la tronche du mégot)

Sélectionnable ou pas (à décider).

Possède 8/9 points de vie maximum. On les enlève de la même manière que les chewing-gum (zap de tile adjacente). Mais il faut les enlever tous d'un coup. Sinon, ça n'a aucun effet. 

Ce qui signifie que si l'objet est insélectionnable, et qu'il y en a deux côte à côte avec à 8 points de vie, on ne peut pas les détruire par des moyens conventionnels. Woups, faudra faire gaffe à ça.

Pour simplifier, on peut juste faire 4 objets, avec 1/3/5/8 points de vie. Sinon ça fait trop d'images différentes. On s'y paume.

Objet/pouvoir : le fume-mégot. Fait baisser les points de vie un mégot.

chewing-gum collé à un mégot ? Faut d'abord détruire le mégot, avec une grosses sélection d'un coup. Puis détruire le chewing-gum.

### Gros objets ###

Ils prennent plusieurs cases. Faut les faire tomber petit à petit. Un gros objet ne tombe que si toutes les cases sur lesquelles il repose sont vides en même temps.

Quand le gros objet arrive en bas, on le récupère.

Exemples :

 - gros sucre
 - touillettes (horizontale ou verticale) (tordable : voir plus loin).
 - billet de 5 brouzoufs
 - sachet de thé
 - stylo
 - post-it
 - tasse
 - gobelet

Deux chewing-gum côte à côte se collent entre eux, et ça fait un gros objet de 2 cases ? C'est pas pareil que la fusion de chewing-gum. La fusion aide le joueur. Le collage en gros objet le pénalise.

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

 - activer une sélection : dépend de la difficulté du café fait.

 - sélection avec le nombre minimal de pièce : <nombre de pièce * 2> points de style. Ca veut dire qu'il faut un algo qui détermine le nombre de pièce minimal selon une somme et une liste de pièce possible. (haha. L'algo simple ne fonctionne pas. 16 avec (10, 8, 4, 2). 16 = 10 + 4 + 2. 16 = 8 + 8.

 - pas de pièce de 1 : <nb de pièce> points de style.

 - pas de pièce de 2 : <nb de pièce> points de style. Cumulable avec le précédent.

 - toutes les pièces pareilles : <nb de pièce> points de style. 

 - Sélection en un seul chemin, sans sélection additionnelle. Bonus supp si le chemin est tracé correctement en une fois. 

### Illumination de cases ###

Lorsqu'on active une sélection, ça augmente de 1 la luminosité des cases sur laquelle se trouvait les objets sélectionnés.
Si on active une sélection comportant des cases illuminés, on gagne des points de style. Mettons : (somme totale des luminosités / 10)
(Du coup, on mul tous les points de style par 10, pour pas être emmerdés).
Si on active une sélection avec exactement les mêmes cases qu'avant, on augmente de 5 la luminosité (et on attribue les points qui vont avec)
Si on active une sélection avec que des cases illuminées, on augmente de 2 la luminosité (et on attribue les points qui vont avec)
Lorsqu'une case illuminée n'est pas sélectionné lors d'une activation de sélection, sa luminosité baisse de 2 (ou autre valeur, ou elle retombe à 0)

C'est bordelique ce truc, et je suis pas sur que ça ait un intérêt quelconque. Et en tout cas y'a aucune justification à ça.
On oublie pour l'instant.

## Pouvoirs spéciaux ##

Ces actions peuvent coûter des points de style. Et elles sont pas forcément toute dispo dès le début. Faut les débloquer (je sais pas trop comment).

 - utiliser une tasse au lieu d'un gobelet : -1 sur le coût du café
 - ajouter une touillettte : +1 sur le coût du café. (Achievement stupide : tasse + touillette)
 - reshuffle
 - changer une pièce en jeton de caddie
 - échanger deux objets
 - enlever un doublon de la pile de touches de café
 - enlever un pas doublon de la pile de touches de café
 - destruction d'un pavé de 9 cases, d'une croix, ...

Je sais pas si on mettra des XP en fait. Je sais pas à quoi je peux les employer. (ou alors : être d'un niveau spécifique pour faire une quête ou une autre)

pouvoir : zapper une ligne de X tiles  (que sucre piece jetons). Ca peut aider pour faire tomber des gros objets.

Changer une pièce en pièce-joker. Et en jeton de caddie. Et en sucre ?

doubler le zap, et le score d'une sélection

diminuer la proba d'apparition des pièces pourries (3, 7, .....)

une bombe, tout simplement. Avec un rayon d'action d'autant plus important qu'on sélectionne des trucs adjacents autour.

pouvoir de bombe, qui fait péter sur le dernier point du path. A la 4elements.

des objets qui font chier ou qui sont cools et qui ont un effet d'autant plus grand qu'on fait une grande sélection.

Quand on fait un carré de 3*3, ça fait apparaître un objet cool au milieu (genre une bombe). Et quand on fait vraiment pil poil le carré, sans rien sélectionner autour, ça le fait aussi. Mais mieux.

Des carrés plus grand, ça donne quoi ?

Et si on arrive à enfermer une zone ? Y'a un zap par rapport à ça. Mais peut on en faire un bonus  quelconque ?

Pouvoir : cassage de pièce. On choisit une pièce à casser. Faut faire une sélection adjacente à cette pièce, avec au moins X cases vides. La pièce se casse dans les X cases vides.
Le pouvoir détermine la pièce de destination de cassage. (en pièce de 2, de 1, ...)

## Achievements ##

Avoir X jeton de caddie dans une sélection
Faire une sélection avec que des pièces de même valeur. (X pièces, valeur Y) (Et zézétte épouse X).
gagner X points de style en une activation
cumuler XXX points de style en une partie (utiliser des valeurs fun, genre 1337. Et non pas des 1000, 2000, ...)
avoir une sélection avec XXX pièces
Tous les achievements à la con de longévité (utiliser 200 touillettes, 200 tasses, 2000 cafés, ...) (faut pas en faire de trop avec ça, car c'est pouillave) (plutôt des quêtes)
faire des sélections de forme spécifique (ligne, carré, colonne, ...)

casser 2 ou plus mégots de résistance 8 en un seul coup.

pour chaque type de café : achievement avec que des pièces de 1, de 2 (+ une de 1), de 5, etc.

faire des achievement et des quêtes donne plein d'XP.
jouer une partie en donne un petit peu.
On débloque les trucs (je sais pas exactement quoi), avec des XP. 
Comme ça, le joueur est jamais bloqué, même si il est nul. Il aura juste à faire plein de parties pour se débloquer.

Quand on fera d'autres jeux : les XP d'un jeu apportent un peu d'XP dans les autres jeux. Histoire d'aider un peu.

## Fusion de pièces ##

faire de la monnaie. (on sélectionne 5 pièces de 1, on reclique sur une des pièces sélectionnées. Ca fait une pièce de 5 à l'endroit choisi. Et là y'a des combos possibles. Soit plusieurs fois de suite du faisage de monnaie. soit carrément plusieurs fois de suite en réutilisant à chaque fois la nouvelle pièce créée : 1 2 5 10 20 50 100. Ça peut être rigolo.
Pas de regénération de l'arena tant qu'on fait de la monnaie. (Mais y'a de la gravité). Ca évite les combos infinis.
Beaucoup de points de combos si on fait plusieurs fois de suite le même, et avec les mêmes pièces. Genre : plusieurs fois de suite 10 pièces de 2 pour faire des pîèces de 20. (2+2+1 pour faire 5, ça marche, mais ça rapporte vraiment pas beaucoup comme points de combos)

Et si on sélectionne 3 pièces de chaque, on peut créer une pièce joker. Why not ? not.

## Variables permettant de définir la difficulté ##

 - plus de chewing gum et de clopes
 - moins de jeton de caddie
 - plus de grosses pièces
 - plus de café à des prix bizarres
 - plus de pièces pourries (3, 7, ...)

## quête / modes de jeu ##

pas d'apparition de nouvelles pièces. Et faut toutes les détruire.

Faire un carré de 10 * 7 sucre, pour créer un gros morceaux de sucre, puis le faire tomber en bas pour le récupérer.

faire un carré de 5 * 2 mégots pour recréer une clope, et la faire tomber en bas.

faire tomber d'autres objets.

avec des combos : on fait plusieurs sélections dans l'aire de jeu. On les active toutes d'un coup. Et faut en faire le plus possible.

aire de jeu gigantesque. Les pièces ne tombent pas. Faut délivrer des cases (à la 4 elements), et on se balade un peu où on veut comme ça. 

arriver à une somme juste pil poil, avec des activations successives, et acheter une cochonnerie avec.

faire le plus de sélection possibles (coût de 1, 2, 3, ...), avec la même aire de jeu, mais faut toujours que les sélection incluent une pièce parmi un groupe de pièce. (quête de la pièce qu'on récupère à chaque coup car elle est au bout d'une ficelle) faut faire tous les cafés possible de cette manière. Dans l'ordre qu'on veut. Les cases se regénèrent ou pas. Ca dépend (le joueur choisit, ou c'est le jeu qui regénère tout le temps, ou jamais)

rassembler des lignes / des sélections de 5 pièces de 1 pour faire une pièce de 5. Puis 4 pièce de 5 pour faire une pièce de 20. Puis 5 pièces de 20 pour faire un brouzouf entier. (Et après on en fait je sais pas quoi)
Ou alors : sélection de X (n'importe comment) pour faire la pièce de valeur X.

faire une sélection de 100 brouzouf (n'importe comment) et ça donne un brouzouf.

faire une ligne / un rectangle de X brouzoufs pour créer un énorme billet !

énigme. aire de jeu définie. boissons à faire définie. On se débrouille.

Régime : Y'a des sucres dans l'aire de jeu, mais faut en utiliser le moins possible.

faire une gros tas de piece de 1 pour faire un café avec que des pièces de 1.

faire un gros tas de sucre pour faire des cafés avec le plus de sucre possible.

gros tas de mégots.

faire un café avec des pièces spécifiques. (10+10+5+5+5+1 ...)

mode cendrier : aire de jeu très haute, on commence en haut. y'a des megots de clope partout, on doit creuser vers le bas.
ça avance vers le bas soit après x secondes, soit x coups, soit on a un nbre de coups limités mais on choisit soi-même quand descendre.

interdit de déselectionner, et on ne voit pas le total des brouzoufs. Donc faut faire du calcul mental.


sudoku : 9 elements différents dans un carré de 3*3

connecter 2 (ou plus) endroits différents avec une sélection. Ouais ça c'est cool.

sucre mania : on a le droit de faire plus de sucre que prévu. Et y'a de plus en plus de sucre qui apparaissent (mais pas trop en fait). Et faut faire des cafés avec de plus en plus de sucre. Si on en fait plus que prévu, ça ralentit un peu l'augmentation de quantité de sucre requise.

casser un sucre en deux. On doit pas toucher aux moitiés du sucre. Mais on doit taper au milieu. 
Et après faut faire tomber l'une des deux moitiés.
(Je ne sais plus ce que je voulais dire exactement avec cette idée)

la mousse qui grandit. (Ca représente de la mousse de café) Bizarre. On étend l'écoulement du café, mais on stoppe la mousse. Faudra justifier ça scénaristiquement. youpi. La mousse c'est du lait devenu fou. Un truc comme ça.

Un objet qui se déplace dans une direction précise. Et qu'il faudrait emmener quelque part. (Et il fait quoi ?) Il trace un chemin qui fait quelque chose ?
une mini-voiture-jouet ? (genre cadeau bonus à la con). 
Et deux objets qui se cognent à un point de rencontre ? Certes...
C'est des billes qui se déplacent. C'est le plus drôle. Expression corporate : "refiler les billes."

des glaçons, qu'il faut se dépêcher d'emmener en bas sinon ils fondent.

Eventuellement, une grosse tasse qu'on doit faire tomber en détruisant les tiles d'en bas-à côté. Ca la renverse et ça fait des trucs cools.

aire de jeu avec des tailles bizarres : 40 * 2. 4 * 4 et on fait que des tout petits cafés. (bof)

les chewing-gum faut les zapper en path. Si on les zap que en suppl, ça compte pas.

pouvoir : regénérerles cases vides avec des trucs pas trop poucraves. (pouvoir améliorable)



jeu à 2 ? Sur écran splitté, ou le même écran, ou la même aire de jeu gigantesque (conquête)

sur l'aire de jeu gigantesque, y'a des sucres et des clopes. On peut pas les casser au début. Quand on a fait la quête de créer des sucres, et celles de créer des clope. On peut.
(Bizarres, car une quête de création permet une quête de destruction).
Ou sinon, on fait 2 quêtes pour chaque. création -> destruction -> on a la capacité. Bof.

C'est du café, qui se répand dans la grande aire de jeu. (genre le liquide, à la 4 elements)

La grande aire de jeu représente un open space de l'entreprise. Elle donne accès à des bureaux avec des quêtes dedans. Qui donne des pouvoirs pour débloquer des endroits bloqués dans la grande aire de jeu. Ouaip. C'est cool.
Mais ça dit rien concernant les XP.

(TODO : expliquer la moquette avec le café qui fuit)

des trucs (de 1 seule case, voir plus) qu'il faut entourer complètement d'une sélection pour les détruire, et qui ouvre d'autres trucs.
Une petite clé ?
Soit un entourage le plus proche possible. Soit avec d'autres cases dedans.

pour casser une pièce de 1 euro, faut faire une sélection de X cases avec elle dedans. La pièce de 1 euro se casse en X pièce plus petite, et rempli les cases vides.
On peut casser plusieurs pièces, avec des sélection de n*X cases. (Et ça fait des achievement, ça).
Bof, c'est peut être naze. Je sais pas.

Du coup, pour faire des grandes sélections, faut des boissons chers. Et ça, on les débloque avec des XP ou des quêtes. Ha ha !!! (Genre 666)

Dans la grande aire de jeu, les zones de début sont faciles, et ne génère que des 0, 1, 2, 5, ... Plus on s'éloigne, plus on a des risques de voir générer des trucs de daube.
Et peut être que y'aurait des quêtes pour reculer ces zones ? (Ca enlève de l'intérêt au jeu, mais ajoute un sentiment de "nettoyage")
On mettra une map globale, avec les zones et tout.
Mais faut que ce soit visible. (La couleur du café, ou je sais pas quoi)

Il me faudra peut être un mode tutorial.
Avec une aire toute faite. Des explications successives. Y'a une action prédéfinie à faire. Si le joueur fait le con, ça part en latte, mais c'est de sa faute.

## Quêtes un peu plus précises ##

bon, enchaînement des quêtes, et des trucs que je vais coder.

Pour chaque quête, on va essayer de trouver : la quête de base (facile), la quête hard (super dur), la quête chiante (facile, mais long)

faut que je détermine exactement ce qu'il y a comme café possible à chaque fois. Et comment on peut les choisir.

petite aire de jeu. Les cafés un par un. Pas de sucre. Il faut en faire 20. N'importe lesquels. pas de suppl
 - hard : l'aire de jeu est encore un peu plus petite. Et y'a des pièces à la con. Très peu de pièces de 1.
 - chiant : faut faire 100 cafés.

(quête avec du sucre, et/ou des jetons de caddie. Bref, un truc simple)

quête où il faut faire plein de cafés en étant rapide.

* la machine à café devient folle, et elle renverse son café partout. on commence la meta-quête, où il faut étendre l'écoulage du café vers d'autres endroits.

quête de destruction des mégots. (facile). On choppe le pouvoir de diminution de résistance d'un mégot.

quête du cendrier. faut creuser creuser creuser. (le mode chiant, c'est le mode infini. On a un score sur la profondeur à laquelle qu'on est allé) (et le mode hard c'est pareil, sauf que la difficulté augmente plus vite)

quête de refabrication des mégots. (pour un clochard). D'autant plus dur qu'il faut rassembler les mégots sans les détruire.

quête des tasses. (pareil, mais c'est une tasse). Hard : la tasse est géante. Du coup, quand elle est presque en bas, c'est super dur. (ou alors, on fait des tasses de plus en plus géantes. Et y'en a plusieurs, de plus en plus rapprochées. Et c'est le mode infini)

quête des touillettes. (gros objet de touillette qu'il faut faire tomber) Ca va ressembler aux tasses. Sauf que les touillettes ne tombent pas forcément ? Elle peuvent aller sur les côtés.
Ou alors faut les faire tourner. Faut les tordre sans les casser. Petit à petit. Donc faut sélectionner des zones, mais pas toutes d'un coup, sinon elles se cassent.

on est plongés dans du café. Les touillettes remontent, mais les pièces tombent. Faut séparer les deux. (Comment exactement ?) Ca c'est une idée marrante. Pas de gravité sur les pièces, mais une regénération. Il faut détruire les pièces juste au-dessus de la touillette, et toutes d'un coup, pour la faire monter d'un cran.

bon, ça donne le pouvoir des tasses et des touillettes.



Y'a des demi-cachets d'aspirine. Faut les fusionner. Quand on pète une colonne entière, ça rapproche. Ca fait pas tomber des trucs gravité machin.
Pouvoir de transformer une aspirine en jeton-0. Mais limité.
Quand on en fait plusieurs d'un coup ou qu'on fait une réaction en chaîne, ça fait du score.
Quand on pète plusieurs colonnes d'un coup ça fait aussi une réaction en chaîne.
Les aspirines se fusionnent que quand ils sont vraiment bien placés. Adjacence horizontale, la moitié gauche à gauche, la droite à droite.
On clique sur l'une des moitiés, ça crée l'aspirine sur cette case.
Et après faudrait soit recliquer dessus, soit le faire tomber tout en bas. on dit cliquage. On va pas prendre la tête avec un truc facile.



