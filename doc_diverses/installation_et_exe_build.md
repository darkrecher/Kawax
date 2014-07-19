# Exécution, transformation en exécutable #

## Lancement du jeu à partir du code source (Windows) ##

Le jeu peut fonctionner avec python 2.5.4, ou une version 2.x supérieure (pas en python 3, car il n'est pas rétro-compatible). 

Cependant, la transformation en exécutable n'est peut-être pas réalisable avec une version supérieure, à cause d'un bug dans pygame2exe. (J'avais trouvé un message de forum qui en parlait, mais je n'ai plus le lien, désolé).

Dans la suite de cette documentation, on considérera donc uniquement la version python 2.5.4.

### Installation de python ###

Télécharger le fichier d'installation `python-2.5.4.msi`, à partir de https://www.python.org/download/releases/2.5.4/

Exécuter ce fichier.

Choisir les options suivantes :

 - Install for all users.
 - Le répertoire que vous voulez. On considérera le choix par défaut : `C:\python25`
 - Installation complète (choisir toutes les features).

### Installation de pygame ###

Télécharger le fichier `pygame-1.9.1.win32-py2.5.msi` (installation de pygame pour python 2.5), à partir de http://www.pygame.org/download.shtml

Si vous utilisez une version plus récente de python, prenez garde à télécharger le pygame correspondant. Il y en a un pour les 2.6.x et un pour les 2.7.x. Ils sont récupérables au même endroit.

Exécuter le fichier téléchargé.

Choisir les options suivantes :

 - Install for all users.
 - Indiquer le répertoire ou vous avez installé python 2.5 : `C:\python25\`

### Lancement du jeu ###

Télécharger tout le contenu de ce repository. On considère qu'il se trouve à l'emplacement `C:\kawax\`. 

Ouvrir une console MS-DOS

Exécuter les commandes suivantes

    cd C:\kawax\code
    C:\python25\python.exe main.py

Une fois que le mode de jeu est sélectionné, il n'est plus possible de revenir au menu principal et d'en prendre un autre. Il faut arrêter et relancer le jeu.

Amusez-vous bien !

## Transformation en exécutable (Windows) ##

### Installation de py2exe ###

Télécharger le fichier `py2exe-0.6.9.win32-py2.5.exe`, à partir de http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/py2exe-0.6.9.win32-py2.5.exe/download?use_mirror=skylink&download=

Exécuter ce fichier.

Indiquer le répertoire ou vous avez installé python 2.5 : `C:\python25\`

### Création du .exe ###

Ouvrir une console MS-DOS

Exécuter les commandes suivantes

    cd C:\kawax\code
    C:\python25\python.exe pygame2exe.py

Ce fichier `pygame2exe.py` a été créé à partir du tutoriel : http://www.pygame.org/wiki/Pygame2exe?parent=CookBook

À l'issu de l'exécution de ces commandes, un répertoire `C:\kawax\code\dist\` a été créé, contenant l'exécutable stand-alone du jeu. 

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

### Lancement du jeu avec le .exe ###

Le jeu se lance avec `C:\kawax\code\dist\main.exe`.

Au premier lancement, il peut y avoir le message d'erreur suivant.
    An error occurred, please see the main.exe.log file for details.

Ce fichier de log n'est pas créé. Le jeu se lance correctement.

Le message d'erreur n'apparaît qu'une fois. Même si on recrée le .exe et qu'on relance le jeu.

Si vous avez l'anti-virus Avast, il va couiner un petit peu au premier lancement (validation d'un .exe non connu). Mais ça se passe sans aucun problème.

Le contenu du répertoire `dist` n'est pas versionné dans ce repository.
 
TODO : Pour récupérer un exécutable déjà fait, allez sur indieDb (mais je l'ai pas encore mis) 