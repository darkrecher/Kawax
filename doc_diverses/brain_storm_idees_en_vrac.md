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

Pour chaque quête, il faut essayer d'en faire 3 versions :

 - de base (facile)
 - hard (super dur)
 - chiante (facile, mais long)

### Exploration ###

C'est le mode principal. Il est disponible après que le joueur ait effectué quelques tutoriels, et des quêtes simples, où il faut juste faire des cafés.

Scénario : la machine à café devient folle, elle en renverse partout. Ça s'étale sur le sol mais c'est absorbé par la moquette. Les "instances décisionnelles" de l'entreprise ne veulent pas la remplacer, car elles ce problème ne les dérange pas, elles utilisent leur propre machine à café haut de gamme. Il faut détruire la moquette petit à petit, pour propager l'écoulement de café jusqu'au bureau des instances décisionnelles.

L'aire de jeu est gigantesque, elle représente les locaux de l'entreprise. Il n'y a pas de gravité, les objets se regénèrent directement sur les cases zappées. On commence dans une petite zone où se trouve la machine à café. 

Chaque case possède une "densité de moquette", (en plus de son objet). Lorsqu'on zappe une case, sa densité de moquette diminue de 1. Lorsqu'elle atteint 0, le café peut s'écouler dedans. Ça fonctionne comme dans le jeu 4 Elements.

On peut se promener dans l'aire de jeu gigantesque à condition qu'une case avec du café écoulé reste toujours visible à l'écran. Il faut donc progresser petit à petit, en détruisant la moquette. Mais on progresse où on veut comme on veut.

En se déplaçant ainsi, on arrive à des bureaux d'autres collègues, qui donnent des quêtes annexes, des pouvoirs, des XP, ...

Certaines zones ne sont pas accessibles dès le début, car entourée par des objets qu'on ne peut pas détruire. Il faut obtenir le pouvoir correspondant.

Par exemple, au début, on ne peut pas prendre de sucre, ni détruire de clopes. Et on débute dans une zone restreinte entourée de sucres/clopes. Il faut obtenir le pouvoir correspondant pour pouvoir aller plus loin.

Il pourrait également y avoir des gros objets. Le seul moyen de les récupérer est de les entourer avec un zap. Mais au début, on n'a pas de café qui coûte suffisamment cher pour pouvoir sélectionner suffisamment de pièces. Il faut débloquer ces cafés avec une quête. (Par exemple, le fameux "sang de chèvre vierge" à 666 centimes de brouzoufs).
  
Dans cette aire de jeu gigantesque, les carrés ayant encore de la moquette peuvent générer des objets chiants, ça dépend de la zone dans laquelle on se trouve. Mais une fois qu'on a enlevé la moquette, la case ne génère que des objets classiques : jetons de caddie, pièces de valeur normales, sucres.

Ça rend ce mode de jeu un peu facile, mais ça ajoute un sentiment de "nettoyage". Les quêtes et les autres modes de jeu sont là pour donner de la difficulté et des objets bizarres à l'infini. (With some hardcore depts, comme on dit chez les concepteurs de jeu).

On doit pouvoir voir une vue d'ensemble de la zone déjà explorée. Ça permet de revenir plus rapidement à un endroit connu, d'avoir une carte, et de renforcer le sentiment de nettoyage.

### Création/récupération d'objets ###

Diverses quêtes en vrac, liées à des gros objets.

 - Faire un carré de 10 * 7 sucre, pour créer un morceau de sucre géant, puis le faire tomber en bas pour le récupérer.

 - Quête de refabrication de cigarette, pour les clochards. Il faut faire un carré de 5 * 2 mégots. Ça crée une clope, et il faut la récupérer. (La faire tomber en bas ou l'entourer d'un zap). Ça peut être difficile car il faut rassembler les mégots sans les détruire. Donc sans trop faire de zap à côté.

 - Faire une ligne ou un rectangle de X*Y brouzoufs pour créer un billet.

 - Une tasse (gros objet), qu'on doit renverser en zappant des cases pas tout à fait en dessous, mais un peu à côté. Des tasses de plus en plus grandes pour que ce soit de plus en plus dur. Permet d'obtenir le pouvoir de la tasse (-1 au prix du café).

 - Une touillette qu'il faut tordre. Chaque fois qu'on zappe des cases à côté d'elle, elle se tord un peu. Il faut le faire petit à petit. Si on zappe une trop grande zone, la touillette se tord trop vite, se casse, et c'est perdu. Permet d'obtenir le pouvoir de la touillette (+1 au prix du café).

### Mal aux cheveux ###

Il faut récupérer des cachets d'aspirine, en fusionnant des demi-cachets.

Correspond au mode aspro dans le jeu que j'ai fait.

Si on prépare plusieurs aspirines, pour ensuite tous les fusionner et récupérer à la suite, ça fait du score (XP, style, ...).

On obtient également du score en vidant complètement plusieurs colonnes en une seule fois. 

### Radin ###

Pas de regénération de pièces dans l'aire de jeu. Il faut toutes les zapper et obtenir une aire totalement vide à la fin. 

Ça risque d'être chiant, car très dépendant du hasard. Vers la fin, il faut avoir des prix de café qui correspondent pil poil à ce qu'il reste dans l'aire de jeu. Faudrait trouver une astuce pour déchiantiser le truc. 

### Rapide ###

Avec un temps total limité et/ou un temps limité pour chaque café.

### Gros fumeur ###

L'aire de jeu représente un cendrier contenant une pile de mégot géante. On commence tout au dessus. Il faut détruire les mégots de clopes. On creuse de plus en plus profond dans la pile au fur et à mesure qu'on détruit les mégots. (Mais il y a toujours des pièces et des sucres qui arrivent par au-dessus, pour pouvoir jouer).

Ça descend automatiquement, soit après X secondes, soit X zaps. Ou alors, on choisit quand ça descend, mais on a un nombre de zaps limités, et il faut aller le plus profondément possible.

Version chiante de la quête : on creuse à l'infini. Les mégots sont de plus en plus résistants.  

Permet d'obtenir le pouvoir de destruction des un mégots.

### Multi-sélection ###

On fait plusieurs sélections dans l'aire de jeu, sans que ça déclenche le zap. (Chaque sélection est associé à un type de café, comme d'habitude). On ne peut pas sélectionner deux fois une même case. Il faut en sélectionner le plus possible.

Ensuite on valide, et ça fait tous les zaps en un seul coup.  

### Faire l'appoint (à point) ###

Chaque fois qu'on fait un café, on additionne son prix à une valeur globale. Il faut atteindre pil poil une valeur spécifique.

(Chiant et sans aucun intérêt, parce que trop dépendant du hasard. Faudra trouver autre chose).

Scénario : Avec la valeur cumulée, on achète un gros truc. Par exemple un sachet de bonbon ou un Snickers. (Au fait, pourquoi ça s'appelle Snickers cette merde ?).    

### Combo de fusion ###

Fusionner des pièces de 1 pour faire une pièce de 5. Puis utiliser cette pièce pour faire une autre fusion (deux pièces de 5 en une pièce de 10). etc.  

### Énigme ###

Aire de jeu avec des objets préd0éfinis. Pas de regénération. Liste des cafés prédéfinie également. Il faut réussir à faire toute la liste.

### Ficelle ###

Scénario : on met dans la machine à café des pièces accrochées à des ficelles, de façon à les récupérer ensuite. Pour avoir du café sans payer. Haha lol.

L'aire de jeu est initialisée aléatoirement, comme d'habitude. Les objets ne disparaissent pas quand on les zappe. (Pas de regénération, donc).

Il faut faire un café à 10 centimes de brouzoufs, puis un autre à 11, 12, etc.

Éventuellement, pour augmenter la difficulté : chaque zap doit obligatoirement inclure la pièce située au milieu de l'aire de jeu. (Je sais pas comment on peut justifier ça scénaristiquement, mais on s'en fout).

### Régime ###

Au départ, L'aire de jeu comporte des sucres. Mais aucun nouveau sucre n'est généré.

Il faut faire le plus de café possible. 

(Une fois de plus : bof. C'est trop dépendant du hasard).

### Diabétique ###

On a le droit de prendre plus de sucre que ce qui est demandé par le type de café. Quand on en prend plus, ça fait du score.

Au début, la probabilité d'apparition des sucres est très haute, et elle diminue petit à petit.

### Pièces de collections ###

Certaines pièces de l'aire de jeu sont spéciales. SI on fait un café avec, ça fait du score. mais le score augmente de beaucoup si on utilise plusieurs de ces pièces. Donc il faut essayer de les regrouper dans un coin et des les utiliser toutes d'un coup.

### Einstein ###

Interdit de déselectionner des objets. Si on tente un zap alors qu'on n'a pas choisi le bon nombre de brouzoufs et de sucre, on perd tout de suite.

Le but, c'est de forcer le joueur à faire du calcul mental.

### Sudoku ###

Regrouper 9 éléments différents dans un carré de 3*3, pour obtenir ... je sais pas quoi. Un truc cool.

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

## Univers du jeu ##

mails, post-it.

"chacun doit nettoyer son propre caca".

Éléments de langage : instances décisionnelles, ressources occasionnelles, zone sociale (salle de pause), noms de salle et de bureau à la con comme dans les vraies boîtes. 