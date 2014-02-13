# -*- coding: utf-8 -*-

import random

#LIST_COIN_VALUES = (0, 1, 2, 5, 10, 20)
LIST_COIN_VALUES = (0, 1, 2, 5, 10, "Su")

ARENA_WIDTH  = 12
ARENA_HEIGHT = 9
ARENA_SIZE = (ARENA_WIDTH, ARENA_HEIGHT)


def getCoinDescr(coin):
    """
    paf
    """


    strCoinValue = str(coin).rjust(4)
    return strCoinValue


def buildCoin():
    return random.choice(LIST_COIN_VALUES)


arena = []

#youpi. Bon, vaut mieux une boucle que des list comprehension imbriquées, à mon avis.
for y in xrange(ARENA_HEIGHT):

    arenaLine = []

    for x in xrange(ARENA_WIDTH):

        newCoin = buildCoin()
        arenaLine.append(newCoin)

    arena.append(arenaLine)

#print arena
print ""

for arenaLine in arena:

    listCoinDescr = [ getCoinDescr(coin) for coin in arenaLine ]
    strLineCoin = "".join(listCoinDescr)
    print strLineCoin
    print ""


print "paf !!"


