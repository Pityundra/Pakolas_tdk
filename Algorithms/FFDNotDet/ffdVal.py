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


def FFDVal(items, binSize, runTime, dataName):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    itemsCopy = items.copy()
    itemsCopy.sort(reverse=True, key=itemsSum)


    res = []

    if len(binSize) == 1:
        for i in range(runTime):
            res.append(FFDVal1D(itemsCopy, binSize))
    elif len(binSize) == 2:
        for i in range(runTime):
            res.append(FFDVal2D(itemsCopy, binSize))
    elif len(binSize) == 3:
        for i in range(runTime):
            res.append(FFDVal3D(itemsCopy, binSize))
    elif len(binSize) == 4:
        for i in range(runTime):
            res.append(FFDVal4D(itemsCopy, binSize))
    elif len(binSize) == 6:
        for i in range(runTime):
            res.append(FFDVal6D(itemsCopy, binSize))
    else:
        print("Ilyen dimenzió számra nem vagyunk felkészülve!")
        return 1

    f = open(f"Results/{len(binSize)}D_Results/{len(binSize)}D_Results.txt", "a")
    f.write(f"{dataName};FFDVal;rt{runTime};{str(sum(res) / len(res))};" + str({i: res.count(i) for i in res}) + "\n")
    f.close()

    print(f"\nFFDVal Futási eredményei:")
    print(res)
    print({i: res.count(i) for i in res})
    print("Átlag:" + str(sum(res) / len(res)))
    print()
    return res


def FFDVal1D(itemsList, binSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin1D(binsIndex + 1, binSize[0]))
    items = itemsList.copy()

    for i in range(len(items)):
        number = np.random.random_integers(1, 4)
        if number == 4:
            item = items[len(items) - 1]
            # print("vége " + str(len(itemsCopy)))
        elif number == 3:
            # print("közepe " + str(ceil((len(itemsCopy)) / 2)))
            item = items[round((len(items)) / 2) - 1]
        else:
            item = items[0]
            # print("eleje")

        bin, binsIndex = placeItem1D(item, bins, binsIndex, binSize)
        items.remove(item)

    return len(bins)


def FFDVal2D(itemsList, binSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))
    items = itemsList.copy()

    for i in range(len(items)):
        number = np.random.random_integers(1, 4)
        if number == 4:
            item = items[len(items) - 1]
            # print("vége " + str(len(itemsCopy)))
        elif number == 3:
            # print("közepe " + str(ceil((len(itemsCopy)) / 2)))
            item = items[round((len(items)) / 2) - 1]
        else:
            item = items[0]
            # print("eleje")

        bin, binsIndex = placeItem2D(item, bins, binsIndex, binSize)
        items.remove(item)

    return len(bins)


def FFDVal3D(itemsList, binSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
    items = itemsList.copy()

    for i in range(len(items)):
        number = np.random.random_integers(1, 4)
        if number == 4:
            item = items[len(items) - 1]
            # print("vége " + str(len(itemsCopy)))
        elif number == 3:
            # print("közepe " + str(ceil((len(itemsCopy)) / 2)))
            item = items[round((len(items)) / 2) - 1]
        else:
            item = items[0]
            # print("eleje")

        bin, binsIndex = placeItem3D(item, bins, binsIndex, binSize)
        items.remove(item)

    return len(bins)


def FFDVal4D(itemsList, binSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin4D(binsIndex + 1, binSize[0], binSize[1], binSize[2], binSize[3]))
    items = itemsList.copy()

    for i in range(len(items)):
        number = np.random.random_integers(1, 4)
        if number == 4:
            item = items[len(items) - 1]
            # print("vége " + str(len(itemsCopy)))
        elif number == 3:
            # print("közepe " + str(ceil((len(itemsCopy)) / 2)))
            item = items[round((len(items)) / 2) - 1]
        else:
            item = items[0]
            # print("eleje")

        bin, binsIndex = placeItem4D(item, bins, binsIndex, binSize)
        items.remove(item)

    return len(bins)



def FFDVal6D(itemsList, binSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin6D(binsIndex + 1, binSize[0], binSize[1], binSize[2], binSize[3], binSize[4], binSize[5]))
    items = itemsList.copy()

    for i in range(len(items)):
        number = np.random.random_integers(1, 4)
        if number == 4:
            item = items[len(items) - 1]
            # print("vége " + str(len(itemsCopy)))
        elif number == 3:
            # print("közepe " + str(ceil((len(itemsCopy)) / 2)))
            item = items[round((len(items)) / 2) - 1]
        else:
            item = items[0]
            # print("eleje")

        bin, binsIndex = placeItem6D(item, bins, binsIndex, binSize)
        items.remove(item)

    return len(bins)