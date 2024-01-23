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
from Resources.weightInform import WeightInform, itemWeight


def L2NotDet(items, binSize):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    itemsCopy = []
    for item in items:
        itemsCopy.append(item)

    if len(binSize) == 1:
        return L2NotDet1D(itemsCopy, binSize)
    elif len(binSize) == 2:
        return L2NotDet2D(itemsCopy, binSize)
    elif len(binSize) == 3:
        return L2NotDet3D(itemsCopy, binSize)
    else:
        print("Ilyen dimenzió számra nem vagyunk felkészülve!")
        return 1


def L2NotDet1D(items, binSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin1D(binsIndex + 1, binSize[0]))
    allWeight = []
    boxSize = 5

    while len(items):
        for item in items:
            for bin in bins:
                if bin.d1FreeCapacity >= item.getD1():
                    item.itemWeight = pow((int(item.d1) - int(bin.d1FreeCapacity)), 2)
                    weight = WeightInform(item, bin, item.itemWeight)
                    allWeight.append(weight)
        if not allWeight:
            binsIndex += 1
            bins.append(Bin1D(binsIndex + 1, binSize[0]))
            # print(f"Új ládát kell nyitni! Láda szám: {len(bins)}\n")
            continue
        allWeight.sort(key=itemWeight)

        if boxSize > len(allWeight):
            randomItemNo = np.random.random_integers(0, len(allWeight) - 1)
        else:
            randomItemNo = np.random.random_integers(0, boxSize - 1)

        # print(f"Ezt a tárgyat teszük el: {allWeight[randomItemNo].item}\n")
        bins[int(allWeight[randomItemNo].bin.binIndex - 1)].addItem(allWeight[randomItemNo].item)
        # print(f"Ebbe a ládába tettük a tárgyat: {bins[int(allWeight[randomItemNo].bin.binIndex - 1)]}\n")
        # print("\n")

        items.remove(allWeight[randomItemNo].item)
        allWeight.clear()

    for bin in bins:
        print(bin)
    print()
    return len(bins)


def L2NotDet2D(items, binSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))
    allWeight = []
    boxSize = 5

    while len(items):
        for item in items:
            for bin in bins:
                if (bin.d1FreeCapacity >= item.getD1()) and (bin.d2FreeCapacity >= item.getD2()):
                    item.itemWeight = pow((int(item.d1) - int(bin.d1FreeCapacity)), 2) + pow((int(item.d2) - int(bin.d2FreeCapacity)), 2)
                    weight = WeightInform(item, bin, item.itemWeight)
                    allWeight.append(weight)
        if not allWeight:
            binsIndex += 1
            bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))
            # print(f"Új ládát kell nyitni! Láda szám: {len(bins)}\n")
            continue
        allWeight.sort(key=itemWeight)

        if boxSize > len(allWeight):
            randomItemNo = np.random.random_integers(0, len(allWeight) - 1)
        else:
            randomItemNo = np.random.random_integers(0, boxSize - 1)

        # print(f"Ezt a tárgyat teszük el: {allWeight[randomItemNo].item}\n")
        bins[int(allWeight[randomItemNo].bin.binIndex - 1)].addItem(allWeight[randomItemNo].item)
        # print(f"Ebbe a ládába tettük a tárgyat: {bins[int(allWeight[randomItemNo].bin.binIndex - 1)]}\n")
        # print("\n")

        items.remove(allWeight[randomItemNo].item)
        allWeight.clear()

    for bin in bins:
        print(bin)
    print()
    return len(bins)


def L2NotDet3D(items, binSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
    allWeight = []
    boxSize = 5

    while len(items):
        for item in items:
            for bin in bins:
                if (bin.d1FreeCapacity >= item.getD1()) and (bin.d2FreeCapacity >= item.getD2()) and (bin.d3FreeCapacity >= item.getD3()):
                    item.itemWeight = pow((int(item.d1) - int(bin.d1FreeCapacity)), 2) + pow((int(item.d2) - int(bin.d2FreeCapacity)), 2) + pow((int(item.d3) - int(bin.d3FreeCapacity)), 2)
                    weight = WeightInform(item, bin, item.itemWeight)
                    allWeight.append(weight)
        if not allWeight:
            binsIndex += 1
            bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
            # print(f"Új ládát kell nyitni! Láda szám: {len(bins)}\n")
            continue
        allWeight.sort(key=itemWeight)

        if boxSize > len(allWeight):
            randomItemNo = np.random.random_integers(0, len(allWeight) - 1)
        else:
            randomItemNo = np.random.random_integers(0, boxSize - 1)

        # print(f"Ezt a tárgyat teszük el: {allWeight[randomItemNo].item}\n")
        bins[int(allWeight[randomItemNo].bin.binIndex - 1)].addItem(allWeight[randomItemNo].item)
        # print(f"Ebbe a ládába tettük a tárgyat: {bins[int(allWeight[randomItemNo].bin.binIndex - 1)]}\n")
        # print("\n")

        items.remove(allWeight[randomItemNo].item)
        allWeight.clear()


    for bin in bins:
        print(bin)
    print()
    return len(bins)
