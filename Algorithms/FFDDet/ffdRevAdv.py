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


def FFDRevAdv(items, binSize,dataName):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    itemsCopy = items.copy()
    itemsCopy.sort(reverse=True, key=itemsSum)

    res = []

    if len(binSize) == 1:
        res.append(FFDRevAdv1D(itemsCopy, binSize))
    elif len(binSize) == 2:
        res.append(FFDRevAdv2D(itemsCopy, binSize))
    elif len(binSize) == 3:
        res.append(FFDRevAdv3D(itemsCopy, binSize))
    elif len(binSize) == 4:
        res.append(FFDRevAdv4D(itemsCopy, binSize))
    elif len(binSize) == 6:
        res.append(FFDRevAdv6D(itemsCopy, binSize))
    else:
        print("Ilyen dimenzió számra nem vagyunk felkészülve!")
        return 1

    f = open(f"Results/{len(binSize)}D_Results/{len(binSize)}D_Results.txt", "a")
    f.write(f"{dataName};FFDRevAdv;;{res[0]}\n")
    f.close()

    print(f"FFDRevAdv Futási eredménye: {res}\n")
    return res


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

    return len(bins)

def FFDRevAdv4D(items, binSize):
    rev = False
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin4D(binsIndex + 1, binSize[0], binSize[1], binSize[2], binSize[3]))

    while len(items):
        item = items[0]
        bin, binsIndex = placeItem4D(item, bins, binsIndex, binSize)
        items.remove(item)

        for bin in bins:
            if (len(items) > 0
                    and (bin.d1FreeCapacity >= items[len(items)-1].getD1())
                    and (bin.d2FreeCapacity >= items[len(items)-1].getD2())
                    and (bin.d3FreeCapacity >= items[len(items)-1].getD3())
                    and (bin.d4FreeCapacity >= items[len(items)-1].getD4())):
                bin.addItem(items[len(items)-1])
                items.remove(items[len(items)-1])

                while len(items):
                    item = items[0]
                    bin, binsIndex = placeItem4D(item, bins, binsIndex, binSize)
                    items.remove(item)
                    items.sort(reverse=rev, key=itemsSum)
                    rev = not rev

    return len(bins)


def FFDRevAdv6D(items, binSize):
    rev = False
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin6D(binsIndex + 1, binSize[0], binSize[1], binSize[2], binSize[3], binSize[4], binSize[5]))

    while len(items):
        item = items[0]
        bin, binsIndex = placeItem6D(item, bins, binsIndex, binSize)
        items.remove(item)

        for bin in bins:
            if (len(items) > 0
                    and (bin.d1FreeCapacity >= items[len(items)-1].getD1())
                    and (bin.d2FreeCapacity >= items[len(items)-1].getD2())
                    and (bin.d3FreeCapacity >= items[len(items)-1].getD3())
                    and (bin.d4FreeCapacity >= items[len(items) - 1].getD4())
                    and (bin.d5FreeCapacity >= items[len(items) - 1].getD5())
                    and (bin.d6FreeCapacity >= items[len(items) - 1].getD6())):
                bin.addItem(items[len(items)-1])
                items.remove(items[len(items)-1])

                while len(items):
                    item = items[0]
                    bin, binsIndex = placeItem6D(item, bins, binsIndex, binSize)
                    items.remove(item)
                    items.sort(reverse=rev, key=itemsSum)
                    rev = not rev

    return len(bins)


