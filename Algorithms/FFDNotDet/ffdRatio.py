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


def FFDRatio(items, binSize, ratio):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    itemsCopy = []
    for item in items:
        itemsCopy.append(item)
    itemsCopy.sort(reverse=True, key=itemsSum)

    if len(binSize) == 1:
        return FFDRatio1D(itemsCopy, binSize, ratio)
    elif len(binSize) == 2:
        return FFDRatio2D(itemsCopy, binSize, ratio)
    elif len(binSize) == 3:
        return FFDRatio3D(itemsCopy, binSize, ratio)
    else:
        print("Ilyen dimenzió számra nem vagyunk felkészülve!")
        return 1


def FFDRatio1D(items, binSize, ratio):
    # az arányszám (ratio) függvényében a végéről rakunk el egy tárgyat
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin1D(binsIndex + 1, binSize[0]))

    for i in range(len(items)):
        number = np.random.random_integers(1, ratio)
        if number == ratio:
            item = items[len(items) - 1]
            # print("vége " + str(len(itemsCopy)))
        else:
            item = items[0]
            # print("eleje")

        bin, binsIndex = placeItem1D(item, bins, binsIndex, binSize)
        items.remove(item)

    for bin in bins:
        print(bin)
    print()
    return len(bins)


def FFDRatio2D(items, binSize, ratio):
    # az arányszám (ratio) függvényében a végéről rakunk el egy tárgyat
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))

    for i in range(len(items)):
        number = np.random.random_integers(1, ratio)
        if number == ratio:
            item = items[len(items) - 1]
            # print("vége " + str(len(itemsCopy)))
        else:
            item = items[0]
            # print("eleje")

        bin, binsIndex = placeItem2D(item, bins, binsIndex, binSize)
        items.remove(item)

    for bin in bins:
        print(bin)
    print()
    return len(bins)


def FFDRatio3D(items, binSize, ratio):
    # az arányszám (ratio) függvényében a végéről rakunk el egy tárgyat
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))

    for i in range(len(items)):
        number = np.random.random_integers(1, ratio)
        if number == ratio:
            item = items[len(items) - 1]
            # print("vége " + str(len(itemsCopy)))
        else:
            item = items[0]
            # print("eleje")

        bin, binsIndex = placeItem3D(item, bins, binsIndex, binSize)
        items.remove(item)

    for bin in bins:
        print(bin)
    print()
    return len(bins)

