
# Document de conception de Kawax #

Ce document décrit le code du jeu vidéo Kawax. Pour chaque fichier de code, son utilité, ainsi que son interaction avec les autres fichiers, est expliquée.


## Avertissement ##

J'ai abandonné le développement de ce jeu. Le code n'est pas terminé, et contient beaucoup de parties non factorisée. 

Vous constaterez également que le PEP8 a été foulé aux pieds, écartelé, équarri, et humilié en place publique par des petits enfants qui lui jetaient des cailloux. C'est la faute à l'entreprise dans laquelle je bossais à l'époque, qui m'a appris à coder en python avec les conventions de nommage du C++. Il va falloir faire avec !


## Chargement, initialisation, etc ##

L'init de la librairie pygame se fait dans le fichier common.py, qui est importé parmi les premiers, dans main.py. 


