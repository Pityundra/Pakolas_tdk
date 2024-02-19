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


def FFDRatio(items, binSize, ratio, runTime, dataName):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    itemsCopy = items.copy()
    itemsCopy.sort(reverse=True, key=itemsSum)


    res = []

    if len(binSize) == 1:
        for i in range(runTime):
            res.append(FFDRatio1D(itemsCopy, binSize, ratio))
    elif len(binSize) == 2:
        for i in range(runTime):
            res.append(FFDRatio2D(itemsCopy, binSize, ratio))
    elif len(binSize) == 3:
        for i in range(runTime):
            res.append(FFDRatio3D(itemsCopy, binSize, ratio))
    else:
        print("Ilyen dimenzió számra nem vagyunk felkészülve!")
        return 1

    f = open(f"Results/{len(binSize)}D_Results/{len(binSize)}D_Results.txt", "a")
    f.write(f"{dataName};FFDRatio;ra{ratio}-rt{runTime};{str(sum(res) / len(res))};" + str({i: res.count(i) for i in res}) + "\n")
    f.close()

    print(f"\nFFDRatio-ra{ratio} Futási eredményei:")
    print(res)
    print({i: res.count(i) for i in res})
    print("Átlag:" + str(sum(res) / len(res)))
    print()
    return res


def FFDRatio1D(itemsList, binSize, ratio):
    # az arányszám (ratio) függvényében a végéről rakunk el egy tárgyat
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin1D(binsIndex + 1, binSize[0]))
    items = itemsList.copy()

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

    return len(bins)


def FFDRatio2D(itemsList, binSize, ratio):
    # az arányszám (ratio) függvényében a végéről rakunk el egy tárgyat
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))
    items = itemsList.copy()

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

    return len(bins)


def FFDRatio3D(itemsList, binSize, ratio):
    # az arányszám (ratio) függvényében a végéről rakunk el egy tárgyat
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
    items = itemsList.copy()

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

    return len(bins)

