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


def FFDBox(items, binSize, boxSize, runTime, dataName):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    itemsCopy = items.copy()
    itemsCopy.sort(reverse=True, key=itemsSum)


    res = []

    if len(binSize) == 1:
        for i in range(runTime):
            res.append(FFDBox1D(itemsCopy, binSize, boxSize))
    elif len(binSize) == 2:
        for i in range(runTime):
            res.append(FFDBox2D(itemsCopy, binSize, boxSize))
    elif len(binSize) == 3:
        for i in range(runTime):
            res.append(FFDBox3D(itemsCopy, binSize, boxSize))
    else:
        print("Ilyen dimenzió számra nem vagyunk felkészülve!")
        return 1

    f = open(f"Results/{len(binSize)}D_Results/{len(binSize)}D_Results.txt", "a")
    f.write(f"{dataName};FFDBox;bx{boxSize}-rt{runTime};{str(sum(res) / len(res))};" + str({i: res.count(i) for i in res}) + "\n")
    f.close()

    print(f"\nFFDBox-bx{boxSize} Futási eredményei:")
    print(res)
    print({i: res.count(i) for i in res})
    print("Átlag:" + str(sum(res) / len(res)))
    print()
    return res


def FFDBox1D(itemsList, binSize, boxSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin1D(binsIndex + 1, binSize[0]))
    items = itemsList.copy()
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

    return len(bins)


def FFDBox2D(itemsList, binSize, boxSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))
    items = itemsList.copy()
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

    return len(bins)


def FFDBox3D(itemsList, binSize, boxSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
    items = itemsList.copy()
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

    return len(bins)