import numpy as np
from Resources.Bin.bin1D import Bin1D
from Resources.Bin.bin2D import Bin2D
from Resources.Bin.bin3D import Bin3D
from Resources.Item.item1D import itemsSum
from Resources.Item.item2D import itemsSum
from Resources.Item.item3D import itemsSum
from Resources.PlaceItem.placeItem1D import placeItem1D
from Resources.PlaceItem.placeItem2D import placeItem2D
from Resources.PlaceItem.placeItem3D import placeItem3D


def FFDBox(items, binSize, boxSize):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    itemsCopy = []
    for item in items:
        itemsCopy.append(item)
    itemsCopy.sort(reverse=True, key=itemsSum)

    if len(binSize) == 1:
        return FFDBox1D(itemsCopy, binSize, boxSize)
    elif len(binSize) == 2:
        return FFDBox2D(itemsCopy, binSize, boxSize)
    elif len(binSize) == 3:
        return FFDBox3D(itemsCopy, binSize, boxSize)
    else:
        print("Ilyen dimenzió számra nem vagyunk felkészülve!")
        return 1


def FFDBox1D(items, binSize, boxSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin1D(binsIndex + 1, binSize[0]))

    boxSize = boxSize

    for i in range(len(items)):
        if boxSize > len(items):
            item = items[np.random.random_integers(0, len(items) - 1)]
            bin, binsIndex = placeItem1D(item, bins, binsIndex, binSize)
            items.remove(item)
        else:
            item = items[np.random.random_integers(0, boxSize - 1)]
            bin, binsIndex = placeItem1D(item, bins, binsIndex, binSize)
            items.remove(item)

    for bin in bins:
        print(bin)
    print()
    return len(bins)


def FFDBox2D(items, binSize, boxSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))

    boxSize = boxSize

    for i in range(len(items)):
        if boxSize > len(items):
            item = items[np.random.random_integers(0, len(items) - 1)]
            bin, binsIndex = placeItem2D(item, bins, binsIndex, binSize)
            items.remove(item)
        else:
            item = items[np.random.random_integers(0, boxSize - 1)]
            bin, binsIndex = placeItem2D(item, bins, binsIndex, binSize)
            items.remove(item)

    for bin in bins:
        print(bin)
    print()
    return len(bins)


def FFDBox3D(items, binSize, boxSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))

    boxSize = boxSize

    for i in range(len(items)):
        if boxSize > len(items):
            item = items[np.random.random_integers(0, len(items) - 1)]
            bin, binsIndex = placeItem3D(item, bins, binsIndex, binSize)
            items.remove(item)
        else:
            item = items[np.random.random_integers(0, boxSize - 1)]
            bin, binsIndex = placeItem3D(item, bins, binsIndex, binSize)
            items.remove(item)

    for bin in bins:
        print(bin)
    print()
    return len(bins)