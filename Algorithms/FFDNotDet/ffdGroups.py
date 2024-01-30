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


def FFDGroups(items, binSize, groupNumber):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    itemsCopy = []
    for item in items:
        itemsCopy.append(item)
    itemsCopy.sort(reverse=True, key=itemsSum)

    if len(binSize) == 1:
        return FFDGroups1D(itemsCopy, binSize, groupNumber)
    elif len(binSize) == 2:
        return FFDGroups2D(itemsCopy, binSize, groupNumber)
    elif len(binSize) == 3:
        return FFDGroups3D(itemsCopy, binSize, groupNumber)
    else:
        print("Ilyen dimenzió számra nem vagyunk felkészülve!")
        return 1


def FFDGroups1D(items, binSize, groupNumber):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin1D(binsIndex + 1, binSize[0]))

    groupNumber = groupNumber

    splitNumber = int(np.ceil(len(items) / groupNumber))

    for j in range(groupNumber):
        if j == groupNumber - 1:
            for i in range(len(items)):
                item = items[np.random.random_integers(0, len(items) - 1)]
                bins, binsIndex = placeItem1D(item, bins, binsIndex, binSize)
                items.remove(item)
            # print(f"Elraktuk az összes tárgyat! ItemsCopy lista hossza: {len(itemsCopy)}\n")
        else:
            for i in range(splitNumber):
                item = items[np.random.random_integers(0, splitNumber - 1 - i)]
                bins, binsIndex = placeItem1D(item, bins, binsIndex, binSize)
                items.remove(item)
            # print(f"Elraktuk a {splitNumber * (j+1)}. tárgyig a tárgyakat\n")

    for bin in bins:
        print(bin)
    print()
    return len(bins)


def FFDGroups2D(items, binSize, groupNumber):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))

    groupNumber = groupNumber

    splitNumber = int(np.ceil(len(items) / groupNumber))

    for j in range(groupNumber):
        if j == groupNumber - 1:
            for i in range(len(items)):
                item = items[np.random.random_integers(0, len(items) - 1)]
                bins, binsIndex = placeItem2D(item, bins, binsIndex, binSize)
                items.remove(item)
            # print(f"Elraktuk az összes tárgyat! ItemsCopy lista hossza: {len(itemsCopy)}\n")
        else:
            for i in range(splitNumber):
                item = items[np.random.random_integers(0, splitNumber - 1 - i)]
                bins, binsIndex = placeItem2D(item, bins, binsIndex, binSize)
                items.remove(item)
            # print(f"Elraktuk a {splitNumber * (j+1)}. tárgyig a tárgyakat\n")

    for bin in bins:
        print(bin)
    print()
    return len(bins)


def FFDGroups3D(items, binSize, groupNumber):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))

    groupNumber = groupNumber

    splitNumber = int(np.ceil(len(items) / groupNumber))

    for j in range(groupNumber):
        if j == groupNumber - 1:
            for i in range(len(items)):
                item = items[np.random.random_integers(0, len(items) - 1)]
                bins, binsIndex = placeItem3D(item, bins, binsIndex, binSize)
                items.remove(item)
            # print(f"Elraktuk az összes tárgyat! ItemsCopy lista hossza: {len(itemsCopy)}\n")
        else:
            for i in range(splitNumber):
                item = items[np.random.random_integers(0, splitNumber - 1 - i)]
                bins, binsIndex = placeItem3D(item, bins, binsIndex, binSize)
                items.remove(item)
            # print(f"Elraktuk a {splitNumber * (j+1)}. tárgyig a tárgyakat\n")

    for bin in bins:
        print(bin)
    print()
    return len(bins)
