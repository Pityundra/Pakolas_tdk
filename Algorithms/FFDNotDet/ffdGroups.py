import numpy as np
from Resources.Bin.bin1D import Bin1D
from Resources.Bin.bin2D import Bin2D
from Resources.Bin.bin3D import Bin3D
from Resources.Bin.bin4D import Bin4D
from Resources.Bin.bin6D import Bin6D
from Resources.Item.item1D import itemsSum
from Resources.Item.item2D import itemsSum
from Resources.Item.item3D import itemsSum
from Resources.PlaceItem.placeItem1D import placeItem1D
from Resources.PlaceItem.placeItem2D import placeItem2D
from Resources.PlaceItem.placeItem3D import placeItem3D
from Resources.PlaceItem.placeItem4D import placeItem4D
from Resources.PlaceItem.placeItem6D import placeItem6D


def FFDGroups(items, binSize, groupNumber, runTime, dataName):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    itemsCopy = items.copy()
    itemsCopy.sort(reverse=True, key=itemsSum)

    res = []

    if len(binSize) == 1:
        for i in range(runTime):
            res.append(FFDGroups1D(itemsCopy, binSize, groupNumber))
    elif len(binSize) == 2:
        for i in range(runTime):
            res.append(FFDGroups2D(itemsCopy, binSize, groupNumber))
    elif len(binSize) == 3:
        for i in range(runTime):
            res.append(FFDGroups3D(itemsCopy, binSize, groupNumber))
    elif len(binSize) == 4:
        for i in range(runTime):
            res.append(FFDGroups4D(itemsCopy, binSize, groupNumber))
    elif len(binSize) == 6:
        for i in range(runTime):
            res.append(FFDGroups6D(itemsCopy, binSize, groupNumber))
    else:
        print("Ilyen dimenzió számra nem vagyunk felkészülve!")
        return 1

    f = open(f"Results/{len(binSize)}D_Results/{len(binSize)}D_Results.txt", "a")
    f.write(f"{dataName};FFDGroups;gn{groupNumber}-rt{runTime};{str(sum(res) / len(res))};" + str({i: res.count(i) for i in res}) + "\n")
    f.close()

    print(f"\nFFDGroups-gn{groupNumber} Futási eredményei:")

    print(res)
    print({i: res.count(i) for i in res})
    print("Átlag:" + str(sum(res) / len(res)))
    print()
    return res


def FFDGroups1D(itemsList, binSize, groupNumber):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin1D(binsIndex + 1, binSize[0]))

    items = itemsList.copy()

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

    return len(bins)


def FFDGroups2D(itemsList, binSize, groupNumber):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))

    items = itemsList.copy()

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

    return len(bins)


def FFDGroups3D(itemsList, binSize, groupNumber):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))

    items = itemsList.copy()

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

    return len(bins)



def FFDGroups4D(itemsList, binSize, groupNumber):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin4D(binsIndex + 1, binSize[0], binSize[1], binSize[2], binSize[3]))

    items = itemsList.copy()

    groupNumber = groupNumber

    splitNumber = int(np.ceil(len(items) / groupNumber))

    for j in range(groupNumber):
        if j == groupNumber - 1:
            for i in range(len(items)):
                item = items[np.random.random_integers(0, len(items) - 1)]
                bins, binsIndex = placeItem4D(item, bins, binsIndex, binSize)
                items.remove(item)
            # print(f"Elraktuk az összes tárgyat! ItemsCopy lista hossza: {len(itemsCopy)}\n")
        else:
            for i in range(splitNumber):
                item = items[np.random.random_integers(0, splitNumber - 1 - i)]
                bins, binsIndex = placeItem4D(item, bins, binsIndex, binSize)
                items.remove(item)
            # print(f"Elraktuk a {splitNumber * (j+1)}. tárgyig a tárgyakat\n")

    return len(bins)



def FFDGroups6D(itemsList, binSize, groupNumber):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin6D(binsIndex + 1, binSize[0], binSize[1], binSize[2], binSize[3], binSize[4], binSize[5]))

    items = itemsList.copy()

    groupNumber = groupNumber

    splitNumber = int(np.ceil(len(items) / groupNumber))

    for j in range(groupNumber):
        if j == groupNumber - 1:
            for i in range(len(items)):
                item = items[np.random.random_integers(0, len(items) - 1)]
                bins, binsIndex = placeItem6D(item, bins, binsIndex, binSize)
                items.remove(item)
            # print(f"Elraktuk az összes tárgyat! ItemsCopy lista hossza: {len(itemsCopy)}\n")
        else:
            for i in range(splitNumber):
                item = items[np.random.random_integers(0, splitNumber - 1 - i)]
                bins, binsIndex = placeItem6D(item, bins, binsIndex, binSize)
                items.remove(item)
            # print(f"Elraktuk a {splitNumber * (j+1)}. tárgyig a tárgyakat\n")

    return len(bins)
