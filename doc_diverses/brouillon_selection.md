# comment ça marche les sélections ? #

on peut tracer un chemin comme dans 4elements.
On reste appuyé, on trace.
Le jeu retient le chemin tracé. Si on revient sur une case appartenant au chemin, on ne garde que le chemin de sélection qui reste. (celui situé de la première case à la case sur laquelle on vient d'arriver.

Quand on arrête de tracer, le chemin est retenu. On peut repartir d'une case adjacente et continuer le traçage. Ca ajoute au  tracé courant. (et on peut revenir à une ancienne case, ça fait comme avant).

Si on repart d'une case pas adjacente. On retient les tiles sélectionnées précédemment, mais sous forme d'un gros paquet, et non plus d'un tracé. Et on commence un nouveau tracé avec celui qu'on fait.

Si on retombe sur une case du gros paquet de tile alors qu'on est en train de tracer. Le tracé s'arrête à l'avant-dernière case tracé. La tile sur laquelle on tombe dessus reste sélectionnée. Si on continue de tracer ailleurs, on redémarre un autre tracé à partir de cette ailleurs. (Le tracé précedent est mis dans le gros paquet de sélection).

Si, après avoir fait des tracés et un paquet de sélection, on reclique sur une case sélectionnée, ça l'enlève de la sélection. Eventuellement, ça peut casser le tracé.
Eventuellement, ça peut virer tout un tas de sélection. Si on la coupe en deux. (Toutes les cases sélectionnées doivent toujorus être adjacentes. Que ce soit en tracé ou en gros paquet). On vire la sélection la plus petite.
Si on continue de se déplacer tout en restant appuyé, ça déselectionne éventuellement d'autres tiles, provoque des coupages de sélection, etc.

Si on clique sur une case non adjacente à la sélection+tracé précédent, ça vire tout, et on repart de cette case non adjacente.


# En gros, y'a 2 modes : #

sélection, déselection.
Le mode se détermine avec le cliquage sur la première tile. (qu'est sélectionnée ou pas)

en mode sélection, on tente de faire un tracé. Quand on peut pas, on met le tracé précédent dans le paquet, et on commence un nouveau tracé. Et si on prend un raccourci de tracé, on déselectionne le détour de tracé de tile sélectionnées.

en mode déselection, on vire les sélections. Haha. Ca peut éventuellement casser des tracés. Et éventuellement couper des sélections, auquel cas on garde la plus grande.

Youpi !

    Vocab?
    selPath
    selBlock


# Nan c'est pas comme ça #

on fait un tracé, si possible le plus long.
on rajoute à ce tracé, si on reclique sur une adjacente.

Quand on rajoute des tiles à ce tracé, en cliquant sur les trucs adjacents, on verrouille le chemin
On peut plus changer le chemin. (Sauf par l'ajout de cases après, pour le prolonger). On peut plus casser le chemin, le rediriger, etc... On peut que le prolonger, et encore, c'est plus par coup de bol qu'autre chose.

On peut sélectionner/déselectionner les tiles additionnelles.

Donc ça s'appelle pas selBlock. C'est selSuppl.
Ouais. Enfin sauf que là je suis déprimé. Mais sinon ça va, c'est cool.

Et pis si on clique ailleurs, ça pète tout.


eventuellement, on supprime des tiles. Ca peut couper, dans ce cas on garde la plus grosse,
en nombre de cases.

on valide




bon ça c'est bien.


# algo de merde pour le mustContinue ou mustStart #

mettons-nous zen situation.

y'a un bool mustRestart.

et un bool mustAct.

quand y'a Act tout seul, on continue
quand y'a act et restart, on restart, et restart=false

quand y'a pas act, on fait rien (restart ou pas restart)


    si c'est bouton-down.
    si pos != none
        act et restart

    si c'est mouse-motion et bouton appuyé:
    si pos = none
        faut restart
    sinon
        faut act
