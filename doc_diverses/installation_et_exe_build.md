# Exécution, transformation en exécutable #

## Lancement du jeu à partir du code source. ##

Télécharger python-2.5.4.msi
Install for all users
dans le répertoire C:\python25
Installation complète (choisir toutes les features)
https://www.python.org/download/releases/2.5.4/

Télécharger pygame pour python 2.5 :
pygame-1.9.1.win32-py2.5.msi

http://www.pygame.org/download.shtml

Install for all users
Indiquer le répertoire d'installation de python 2.5 (C:\python25)

Ouvrez une console MS-DOS
Exécuter
cd <emplacement de ce repository>\code
C:\python25\python.exe main.py

## Transformation en .exe ##

Télécharger py2exe-0.6.9.win32-py2.5.exe



http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/py2exe-0.6.9.win32-py2.5.exe/download?use_mirror=skylink&download=


http://www.pygame.org/wiki/Pygame2exe?parent=CookBook

WindowsError: [Error 32] Le processus ne peut pas accÚder au fichier car ce fich
ier est utilisÚ par un autre processus: 'build\\bdist.win32\\winexe\\collect-2.5
\\encodings'



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



Indiquer le répertoire d'installation de python 2.5 (C:\python25)

Au premier lancement de l'exe, j'ai eu un message d'erreur.
"An error occurred, please see the main.exe.log file for details"
Je n'ai par trouvé ce fichier de log.
Et le jeu s'est bien lancé.

Le message d'erreur n'est pas réapparu, même après une retransformation en exécutable et un relancement du jeu.







