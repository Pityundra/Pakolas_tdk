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


def FFDGB(items, binSize, groupNumber, boxSize, runTime, dataName):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    itemsCopy = items.copy()
    itemsCopy.sort(reverse=True, key=itemsSum)

    print(f"\nFFDGB Futási eredményei:")
    res = []

    if len(binSize) == 1:
        for i in range(runTime):
            res.append(FFDGB1D(itemsCopy, binSize, groupNumber, boxSize))
    elif len(binSize) == 2:
        for i in range(runTime):
            res.append(FFDGB2D(itemsCopy, binSize, groupNumber, boxSize))
    elif len(binSize) == 3:
        for i in range(runTime):
            res.append(FFDGB3D(itemsCopy, binSize, groupNumber, boxSize))
    else:
        print("Ilyen dimenzió számra nem vagyunk felkészülve!")
        return 1

    f = open(f"Results/{len(binSize)}D_Results/{dataName}.txt", "a")
    f.write(f"FFDBG-gn{groupNumber}-bx{boxSize}-rt{runTime}; ;Átlag;{str(sum(res) / len(res))};Összes futási eredmény;{res};Eredmények csoportosítva;" + str({i: res.count(i) for i in res}) + "\n")
    f.close()

    print(res)
    print({i: res.count(i) for i in res})
    print("Átlag:" + str(sum(res) / len(res)))
    print()
    return res


def FFDGB1D(itemsList, binSize, groupNumber, boxSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin1D(binsIndex + 1, binSize[0]))

    groupNumber = groupNumber
    boxSize = boxSize

    items = itemsList.copy()

    splitNumber = int(np.ceil(len(items) / groupNumber))
    # print("splitNumber:" + str(splitNumber))
    # print("boxSize:" + str(boxSize))

    for j in range(groupNumber):
        if j == groupNumber - 1:
            for i in range(len(items)):
                if boxSize > len(items):
                    item = items[np.random.random_integers(0, len(items) - 1)]
                    bin, binsIndex = placeItem1D(item, bins, binsIndex, binSize)
                    items.remove(item)
                else:
                    item = items[np.random.random_integers(0, boxSize - 1)]
                    bin, binsIndex = placeItem1D(item, bins, binsIndex, binSize)
                    items.remove(item)
        else:
            for i in range(splitNumber):
                if boxSize >= splitNumber - i:
                    item = items[np.random.random_integers(0, splitNumber - i - 1)]
                    bin, binsIndex = placeItem1D(item, bins, binsIndex, binSize)
                    items.remove(item)
                else:
                    item = items[np.random.random_integers(0, boxSize - 1)]
                    bin, binsIndex = placeItem1D(item, bins, binsIndex, binSize)
                    items.remove(item)

    return len(bins)


def FFDGB2D(itemsList, binSize, groupNumber, boxSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))

    groupNumber = groupNumber
    boxSize = boxSize
    items = itemsList.copy()

    splitNumber = int(np.ceil(len(items) / groupNumber))

    for j in range(groupNumber):
        if j == groupNumber - 1:
            for i in range(len(items)):
                if boxSize > len(items):
                    item = items[np.random.random_integers(0, len(items) - 1)]
                    bin, binsIndex = placeItem2D(item, bins, binsIndex, binSize)
                    items.remove(item)
                else:
                    item = items[np.random.random_integers(0, boxSize - 1)]
                    bin, binsIndex = placeItem2D(item, bins, binsIndex, binSize)
                    items.remove(item)
        else:
            for i in range(splitNumber):
                if boxSize > splitNumber - i:
                    item = items[np.random.random_integers(0, splitNumber - 1 - i)]
                    bin, binsIndex = placeItem2D(item, bins, binsIndex, binSize)
                    items.remove(item)
                else:
                    item = items[np.random.random_integers(0, boxSize - 1)]
                    bin, binsIndex = placeItem2D(item, bins, binsIndex, binSize)
                    items.remove(item)

    return len(bins)


def FFDGB3D(itemsList, binSize, groupNumber, boxSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))

    items = itemsList.copy()

    groupNumber = groupNumber
    boxSize = boxSize

    splitNumber = int(np.ceil(len(items) / groupNumber))

    for j in range(groupNumber):
        if j == groupNumber - 1:
            for i in range(len(items)):
                if boxSize > len(items):
                    item = items[np.random.random_integers(0, len(items) - 1)]
                    bin, binsIndex = placeItem3D(item, bins, binsIndex, binSize)
                    items.remove(item)
                else:
                    item = items[np.random.random_integers(0, boxSize - 1)]
                    bin, binsIndex = placeItem3D(item, bins, binsIndex, binSize)
                    items.remove(item)
        else:
            for i in range(splitNumber):
                if boxSize > splitNumber - i:
                    item = items[np.random.random_integers(0, splitNumber - 1 - i)]
                    bin, binsIndex = placeItem3D(item, bins, binsIndex, binSize)
                    items.remove(item)
                else:
                    item = items[np.random.random_integers(0, boxSize - 1)]
                    bin, binsIndex = placeItem3D(item, bins, binsIndex, binSize)
                    items.remove(item)

    return len(bins)
