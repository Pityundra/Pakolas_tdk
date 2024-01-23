from Resources.Bin.bin1D import Bin1D
from Resources.Bin.bin2D import Bin2D
from Resources.Bin.bin3D import Bin3D
from Resources.Item.item1D import itemsSum
from Resources.Item.item2D import itemsSum
from Resources.Item.item3D import itemsSum
from Resources.PlaceItem.placeItem1D import placeItem1D
from Resources.PlaceItem.placeItem2D import placeItem2D
from Resources.PlaceItem.placeItem3D import placeItem3D


def FFDRevAdv(items, binSize):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    itemsCopy = []
    for item in items:
        itemsCopy.append(item)
    itemsCopy.sort(reverse=True, key=itemsSum)

    if len(binSize) == 1:
        return FFDRevAdv1D(itemsCopy, binSize)
    elif len(binSize) == 2:
        return FFDRevAdv2D(itemsCopy, binSize)
    elif len(binSize) == 3:
        return FFDRevAdv3D(itemsCopy, binSize)
    else:
        print("Ilyen dimenzió számra nem vagyunk felkészülve!")
        return 1


def FFDRevAdv1D(items, binSize):
    rev = False
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin1D(binsIndex + 1, binSize[0]))

    while len(items):
        item = items[0]
        bin, binsIndex = placeItem1D(item, bins, binsIndex, binSize)
        items.remove(item)

        for bin in bins:
            if len(items) > 0 and (bin.d1FreeCapacity >= items[len(items) - 1].getD1()):
                bin.addItem(items[len(items) - 1])
                items.remove(items[len(items) - 1])

                while len(items):
                    item = items[0]
                    bin, binsIndex = placeItem1D(item, bins, binsIndex, binSize)
                    items.remove(item)
                    items.sort(reverse=rev, key=itemsSum)
                    rev = not rev

    for bin in bins:
        print(bin)
    print()
    return len(bins)


def FFDRevAdv2D(items, binSize):
    rev = False
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))

    while len(items):
        item = items[0]
        bin, binsIndex = placeItem2D(item, bins, binsIndex, binSize)
        items.remove(item)

        for bin in bins:
            if len(items) > 0 and (bin.d1FreeCapacity >= items[len(items) - 1].getD1()) and (bin.d2FreeCapacity >= items[len(items) - 1].getD2()):
                bin.addItem(items[len(items) - 1])
                items.remove(items[len(items) - 1])

                while len(items):
                    item = items[0]
                    bin, binsIndex = placeItem2D(item, bins, binsIndex, binSize)
                    items.remove(item)
                    items.sort(reverse=rev, key=itemsSum)
                    rev = not rev

    for bin in bins:
        print(bin)
    print()
    return len(bins)


def FFDRevAdv3D(items, binSize):
    rev = False
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))

    while len(items):
        item = items[0]
        bin, binsIndex = placeItem3D(item, bins, binsIndex, binSize)
        items.remove(item)

        for bin in bins:
            if len(items) > 0 and (bin.d1FreeCapacity >= items[len(items)-1].getD1()) and (bin.d2FreeCapacity >= items[len(items)-1].getD2()) and (bin.d3FreeCapacity >= items[len(items)-1].getD3()):
                bin.addItem(items[len(items)-1])
                items.remove(items[len(items)-1])

                while len(items):
                    item = items[0]
                    bin, binsIndex = placeItem3D(item, bins, binsIndex, binSize)
                    items.remove(item)
                    items.sort(reverse=rev, key=itemsSum)
                    rev = not rev

    for bin in bins:
        print(bin)
    print()
    return len(bins)
