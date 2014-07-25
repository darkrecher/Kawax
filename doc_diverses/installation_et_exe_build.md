# Exploitation du code source #

## Windows ##

### Lancement du jeu à partir du code source ###

Le jeu peut fonctionner avec python 2.5.4, ou une version 2.x supérieure (pas la version 3, car elle n'est pas rétro-compatible). 

Cependant, la transformation en exécutable n'est peut-être pas réalisable avec une version supérieure à 2.5.4, à cause d'un bug dans pygame2exe. (J'avais trouvé un message de forum qui en parlait, mais je n'ai plus le lien, désolé).

Dans la partie "Windows" de cette documentation, on considérera donc uniquement la version python 2.5.4.

#### Installation de python ####

Télécharger le fichier d'installation `python-2.5.4.msi`, à partir de https://www.python.org/download/releases/2.5.4/

Exécuter ce fichier.

Choisir les options suivantes :

 - "Install for all users".
 - Le répertoire de destination que vous voulez. On considérera le choix par défaut : `C:\python25`
 - Installation complète (choisir toutes les features).

#### Installation de pygame ####

Télécharger le fichier `pygame-1.9.1.win32-py2.5.msi`, à partir de http://www.pygame.org/download.shtml. 

Si vous utilisez une version plus récente de python, prenez garde à télécharger le pygame correspondant. Il y en a un pour les 2.6.x et un pour les 2.7.x. Ils sont récupérables au même endroit.

Exécuter le fichier téléchargé.

Choisir les options suivantes :

 - "Install for all users".
 - Indiquer le répertoire ou vous avez installé python. (`C:\python25\` ou autre)

#### Lancement du jeu ####

Télécharger tout le contenu de ce repository. On considèrera qu'il est mis à l'emplacement `C:\kawax\`. 

Ouvrir une console MS-DOS

Exécuter les commandes suivantes

    cd C:\kawax\code
    C:\python25\python.exe main.py

Amusez-vous bien !

### Transformation en exécutable  ###

#### Installation de py2exe ####

Télécharger le fichier `py2exe-0.6.9.win32-py2.5.exe`, à partir de http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/py2exe-0.6.9.win32-py2.5.exe/download?use_mirror=skylink&download=

Exécuter ce fichier.

Indiquer le répertoire ou vous avez installé python. (`C:\python25\` ou autre)

#### Création du .exe ####

Ouvrir une console MS-DOS

Exécuter les commandes suivantes

    cd C:\kawax\code
    C:\python25\python.exe pygame2exe.py

Le fichier `pygame2exe.py` a été créé à partir du tutoriel : http://www.pygame.org/wiki/Pygame2exe?parent=CookBook

À l'issue de l'exécution de ces commandes, un répertoire `C:\kawax\code\dist\` a été créé, contenant l'exécutable stand-alone du jeu. 

Parfois, on obtient le message d'erreur suivant :

    WindowsError: [Error 32] 
    Le processus ne peut pas accÚder au fichier car ce fichier est utilisÚ par un autre processus: 
    'build\\bdist.win32\\winexe\\collect-2.5\\encodings'

Même avec ce message, la création de l'exécutable devrait avoir été faite.

D'autre part, on obtient le message d'avertissement suivant :

    Make sure you have the license if you distribute any of them, and
    make sure you don't distribute files belonging to the operating system.

    KERNEL32.dll - I:\WINDOWS\system32\KERNEL32.dll
    GDI32.dll - I:\WINDOWS\system32\GDI32.dll
    WSOCK32.dll - I:\WINDOWS\system32\WSOCK32.dll
    SHELL32.dll - I:\WINDOWS\system32\SHELL32.dll
    WINMM.DLL - I:\WINDOWS\system32\WINMM.DLL
    WS2_32.DLL - I:\WINDOWS\system32\WS2_32.DLL
    ADVAPI32.dll - I:\WINDOWS\system32\ADVAPI32.dll
    USER32.dll - I:\WINDOWS\system32\USER32.dll

Ça ne m'a jamais posé de problème. À priori, tous ces fichiers sont déjà présents sur la plupart des systèmes Windows. Pour distribuer le jeu, il suffit juste de distribuer le contenu du répertoire dist.

#### Lancement du jeu avec le .exe ####

Double-cliquer sur le fichier `C:\kawax\code\dist\main.exe`.

Au premier lancement, il peut y avoir le message d'erreur suivant.

    An error occurred, please see the main.exe.log file for details.

Mais le fichier de log mentionné n'est pas créé. Le jeu se lance correctement.

Le message d'erreur n'apparaît qu'une fois.

Si vous avez l'anti-virus Avast, celui-ci va couiner un petit peu au premier lancement (validation d'un .exe non connu). Mais ça se passe sans aucun problème.

Le contenu du répertoire `dist` n'est pas versionné dans ce repository.
 
#### Redistribution de l'exécutable ####

Créer un fichier compressé (.zip ou autre), contenant tout le répertoire `dist`. À savoir, les fichiers et répertoires suivants :

    fontzy
    img
    sound
    lisezmoi.txt
    main.exe
    MSVCR71.dll
    readme.txt
    w9xpopen.exe

Pour installer le jeu sur un autre ordinateur, il suffit de copier le .zip, de le décompresser n'importe, et de double-cliquer sur main.exe.

Si vous redistribuez ce jeu, ou une version modifiée, merci de respecter les termes de la licence (Art Libre ou CC-BY). En particulier : citer l'auteur. Un lien vers mon blog ou vers ce repository suffira.

TODO : lien vers exécutable déjà fait sur indieDb (mais je l'ai pas encore mis).

## Mac OS X ##

### Lancement du jeu à partir du code source ###

À priori, pas de souci de version de python, ni pour jouer, ni pour transformer en exécutable. On peut utiliser n'importe laquelle, de la 2.5 à la 2.x.

#### Installation de python et pygame ####
 
Je l'ai fait sur mon Mac, mais je ne me souviens plus des actions effectuées ! Si je n'ai rien noté de spécial, c'est qu'il ne devait rien y avoir de compliqué. (Je suppose).

Mon header python est comme ça :

    Python 2.6.4 (r264:75821M, Oct 27 2009, 19:48:32) 
    [GCC 4.0.1 (Apple Inc. build 5493)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.

Mon répertoire lib contient les fichiers suivants : 

    cd /Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages
    ls

    README
    altgraph-0.6.7-py2.6.egg
    easy-install.pth
    macholib-1.2.1-py2.6.egg
    modulegraph-0.7.3-py2.6.egg
    py2app-0.4.3-py2.6.egg
    pygame
    pygame-1.9.1release-py2.6.egg-info
    setuptools-0.6c11-py2.6.egg
    setuptools.pth

La valeur de la variable python `pygame.version.ver` est : `'1.9.1release-svn2575'`

Je ne sais pas trop dans quelle mesure ces renseignement sont utiles. Faites-en ce que vous voulez.

#### Lancement du jeu ####

Télécharger tout le contenu de ce repository. On considèrera qu'il est mis à l'emplacement `~/Documents/recher/kawax/`

Ouvrir un terminal et exécuter les commandes suivantes :

    cd ~/Documents/recher/kawax/code
    python main.py

En supposant que l'exécutable python a été mis dans le path. Normalement, ça se fait automatiquement à l'installation.

Sinon, il faudrait faire quelque chose dans ce style (en prenant garde au numéro de version 2.6 / 2.7 / autre) :

`/Library/Frameworks/Python.framework/Versions/2.6/Resources/Python.app/Contents/MacOS/Python/python main.py`

Le jeu devrait se lancer.

### Transformation en exécutable  ###

#### Installation de py2app et setuptools ####

Comme pour l'installation de python et pygame : je ne sais plus comment j'ai fait ! Et si ça se trouve, il n'y a rien à faire, c'est déjà pré-installé.

Se reporter au contenu de mon répertoire lib, et essayer d'avoir plus ou moins la même chose, en adaptant les divers numéros de versions.

#### Création du .app ####

Dupliquer le fichier `code/main.py` avec le nouveau nom `code/kawax.py`. (C'est le moyen le plus simple de créer une app avec le bon nom).

Le fichier `code/kawax.py` n'est pas versionné dans ce repository, puisque c'est juste une copie.

Ouvrir un terminal et exécuter les commandes suivantes :

    cd ~/Documents/recher/kawax/code
    python pygame2macapp.py py2app

Deux répertoires sont créés : 

 - `code/build`. Répertoire temporaire qui peut être supprimé.
 - `code/dist`. Contient l'application `kawax.app`. 

Le contenu de ces 2 répertoires n'est pas versionné dans ce repository.

Il est possible d'avoir un .app avec l'icône de son choix. J'étais parvenu à le faire pour mon jeu précédent (Blarg). Je ne l'ai pas fait pour celui-là, car j'ai la flemme et c'est un jeu terminé fortement à l'arrache.

Double-cliquer sur `code/dist/kawax.app`. Le jeu devrait se lancer sans problème.

#### Création d'un disque .dmg contenant le .app ####

Ouvrir un terminal et exécuter les commandes suivantes :

    cd ~/Documents/recher/kawax/code/dist
    hdiutil create -imagekey zlib-level=9 -srcfolder kawax.app kawax.dmg

Ça met un certain temps. Des petits points s'écrivent dans le terminal, pour montrer qu'il est vivant.

Le fichier `dist/kawax.dmg` devrait être créé.

#### Lancement du jeu à partir du disque .dmg ####

Double-cliquer sur le .dmg pour monter le disque, comme on fait d'habitude sur les Mac.

Dans le disque, double-cliquer sur l'appli `kawax.app`.

Pour les applications enregistrant des fichiers de sauvegarde, il faut préalablement copier le .app sur le disque dur (à l'endroit qu'on veut). Sinon, ça ne sauvegarde rien. Je l'avais constaté avec mon jeu précédent.

Kawax n'enregistre aucune donnée, ni aucun fichier de sauvegarde. On peut donc le lancer directement depuis le .dmg, sans aucun problème. 

#### Redistribution de l'application ####

Copier simplement le .dmg sur un autre Mac. Puis exécuter le jeu comme expliqué dans le chapitre précédent.

Si vous redistribuez ce jeu, ou une version modifiée, merci de respecter les termes de la licence (Art Libre ou CC-BY). En particulier : citer l'auteur. Un lien vers mon blog ou vers ce repository suffira. (Là je me répète un peu, mais j'y tiens)

TODO : récupérer un exécutable déjà fait sur indieDb (mais je l'ai pas encore mis).

## GNU/Linux, Ubuntu, Fedora, etc. ##

Il est certainement possible de jouer à Kawax sur ces systèmes, puisque python et pygame sont compatibles dessus. Mais je n'ai pas ce genre de chose chez moi. Désolé, je devrait certainement être qualifié de vilain monsieur. 

Je vous laisse vous débrouiller tout seul, à coup de apt-get ou autres cabalisteries. Ça ne devrait pas être trop difficile, je suis sûr que vous êtes très fort. Bon courage !

Si vous rencontrez des problèmes durant l'installation, l'exécution ou autre, n'hésitez pas à m'en faire part. Je les décrirais dans ce document pour en faire profiter tout le monde.
 