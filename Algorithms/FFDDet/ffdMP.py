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


def FFDMP(items, binSize, ratio):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    itemsCopy = []
    for item in items:
        itemsCopy.append(item)
    itemsCopy.sort(reverse=True, key=itemsSum)

    for item in itemsCopy:
        print(item)
    print()

    if len(binSize) == 1:
        return FFDMP1D(itemsCopy, binSize, ratio)
    elif len(binSize) == 2:
        return FFDMP2D(itemsCopy, binSize, ratio)
    elif len(binSize) == 3:
        return FFDMP3D(itemsCopy, binSize, ratio)
    else:
        print("Ilyen dimenzió számra nem vagyunk felkészülve!")
        return 1


def FFDMP1D(items, binSize, ratio):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére

    for item1 in items:
        for item2 in items:
            if item1 != item2 and ((item1.getD1() + item2.getD1()) >= (binSize[0] * ratio) and (
                    (item1.getD1() + item2.getD1()) <= (binSize[0]))):
                bins.append(Bin1D(binsIndex + 1, binSize[0]))
                bins[binsIndex].addItem(item1)
                bins[binsIndex].addItem(item2)
                binsIndex += 1
                print(f"Talált pár: {item1.getNumber()} és {item2.getNumber()}")
                items.remove(item1)
                items.remove(item2)
                break

    for item1 in items:
        for item2 in items:
            for item3 in items:
                if (item1 != item2 != item3) and (
                        (item1.getD1() + item2.getD1() + item3.getD1()) >= (binSize[0] * ratio) and (
                        (item1.getD1() + item2.getD1() + item3.getD1()) <= (binSize[0]))):
                    bins.append(Bin1D(binsIndex + 1, binSize[0]))
                    bins[binsIndex].addItem(item1)
                    bins[binsIndex].addItem(item2)
                    bins[binsIndex].addItem(item3)
                    binsIndex += 1
                    print(f"Talált pár: {item1.getNumber()} és {item2.getNumber()} és {item3.getNumber()}")
                    items.remove(item1)
                    items.remove(item2)
                    items.remove(item3)
                    break
                break

    bins.append(Bin1D(binsIndex + 1, binSize[0]))
    for item in items:
        bin, binsIndex = placeItem1D(item, bins, binsIndex, binSize)

    for bin in bins:
        print(bin)
    print()
    return len(bins)


def FFDMP2D(items, binSize, ratio):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére

    for item1 in items:
        for item2 in items:
            if item1 != item2 \
                    and (item1.getD1() + item2.getD1()) >= (binSize[0] * ratio) \
                    and ((item1.getD1() + item2.getD1()) <= (binSize[0])) \
                    and (item1.getD2() + item2.getD2()) >= (binSize[1] * ratio) \
                    and ((item1.getD2() + item2.getD2()) <= (binSize[1])):
                bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))
                bins[binsIndex].addItem(item1)
                bins[binsIndex].addItem(item2)
                binsIndex += 1
                print(f"Talált pár: {item1.getNumber()} és {item2.getNumber()}")
                items.remove(item1)
                items.remove(item2)
                break

    for item1 in items:
        for item2 in items:
            for item3 in items:
                if (item1 != item2 != item3) \
                        and (item1.getD1() + item2.getD1() + item3.getD1()) >= (binSize[0] * ratio) \
                        and ((item1.getD1() + item2.getD1() + item3.getD1()) <= (binSize[0])) \
                        and (item1.getD2() + item2.getD2() + item3.getD2()) >= (binSize[1] * ratio) \
                        and ((item1.getD2() + item2.getD2() + item3.getD2()) <= (binSize[1])):
                    bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))
                    bins[binsIndex].addItem(item1)
                    bins[binsIndex].addItem(item2)
                    bins[binsIndex].addItem(item3)
                    binsIndex += 1
                    print(f"Talált pár: {item1.getNumber()} és {item2.getNumber()} és {item3.getNumber()}")
                    items.remove(item1)
                    items.remove(item2)
                    items.remove(item3)
                    break
                break

    bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))
    for item in items:
        bin, binsIndex = placeItem2D(item, bins, binsIndex, binSize)

    for bin in bins:
        print(bin)
    print()
    return len(bins)


def FFDMP3D(items, binSize, ratio):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére

    for item1 in items:
        for item2 in items:
            if item1 != item2 \
                    and (item1.getD1() + item2.getD1()) >= (binSize[0] * ratio) \
                    and ((item1.getD1() + item2.getD1()) <= (binSize[0])) \
                    and (item1.getD2() + item2.getD2()) >= (binSize[1] * ratio) \
                    and ((item1.getD2() + item2.getD2()) <= (binSize[1])) \
                    and (item1.getD3() + item2.getD3()) >= (binSize[2] * ratio) \
                    and ((item1.getD3() + item2.getD3()) <= (binSize[2])):
                bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
                bins[binsIndex].addItem(item1)
                bins[binsIndex].addItem(item2)
                binsIndex += 1
                print(f"Talált pár: {item1.getNumber()} és {item2.getNumber()}")
                items.remove(item1)
                items.remove(item2)
                break

    for item1 in items:
        for item2 in items:
            for item3 in items:
                if (item1 != item2 != item3) \
                        and (item1.getD1() + item2.getD1() + item3.getD1()) >= (binSize[0] * ratio) \
                        and ((item1.getD1() + item2.getD1() + item3.getD1()) <= (binSize[0])) \
                        and (item1.getD2() + item2.getD2() + item3.getD2()) >= (binSize[1] * ratio) \
                        and ((item1.getD2() + item2.getD2() + item3.getD2()) <= (binSize[1])) \
                        and (item1.getD3() + item2.getD3() + item3.getD3()) >= (binSize[2] * ratio) \
                        and ((item1.getD3() + item2.getD3() + item3.getD3()) <= (binSize[2])):
                    bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
                    bins[binsIndex].addItem(item1)
                    bins[binsIndex].addItem(item2)
                    bins[binsIndex].addItem(item3)
                    binsIndex += 1
                    print(f"Talált pár: {item1.getNumber()} és {item2.getNumber()} és {item3.getNumber()}")
                    items.remove(item1)
                    items.remove(item2)
                    items.remove(item3)
                    break
                break

    bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
    for item in items:
        bin, binsIndex = placeItem3D(item, bins, binsIndex, binSize)

    for bin in bins:
        print(bin)
    print()
    return len(bins)
