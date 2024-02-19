from Resources.Bin.bin1D import Bin1D
from Resources.Bin.bin2D import Bin2D
from Resources.Bin.bin3D import Bin3D
from Resources.Item.item1D import itemsSum
from Resources.Item.item2D import itemsSum
from Resources.Item.item3D import itemsSum
from Resources.PlaceItem.placeItem1D import placeItem1D
from Resources.PlaceItem.placeItem2D import placeItem2D
from Resources.PlaceItem.placeItem3D import placeItem3D


def FFDRev(items, binSize, dataName):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    itemsCopy = items.copy()
    itemsCopy.sort(reverse=True, key=itemsSum)

    res = []

    if len(binSize) == 1:
        res.append(FFDRev1D(itemsCopy, binSize))
    elif len(binSize) == 2:
        res.append(FFDRev2D(itemsCopy, binSize))
    elif len(binSize) == 3:
        res.append(FFDRev3D(itemsCopy, binSize))
    else:
        print("Ilyen dimenzió számra nem vagyunk felkészülve!")
        return 1

    f = open(f"Results/{len(binSize)}D_Results/{len(binSize)}D_Results.txt", "a")
    f.write(f"{dataName};FFDRev;;{res[0]}\n")
    f.close()

    print(f"FFDRev Futási eredménye: {res}\n")
    return res


def FFDRev1D(items, binSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin1D(binsIndex + 1, binSize[0]))

    while len(items):
        itemF = items[0]
        itemL = items[len(items) - 1]

        bin, binsIndex = placeItem1D(itemF, bins, binsIndex, binSize)
        bin, binsIndex = placeItem1D(itemL, bins, binsIndex, binSize)

        items.remove(itemF)
        items.remove(itemL)

        if len(items) == 1:
            lastItem = items[0]
            bin, binsIndex = placeItem1D(lastItem, bins, binsIndex, binSize)
            items.remove(lastItem)

    return len(bins)


def FFDRev2D(items, binSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))

    while len(items):
        itemF = items[0]
        itemL = items[len(items) - 1]

        bin, binsIndex = placeItem2D(itemF, bins, binsIndex, binSize)
        bin, binsIndex = placeItem2D(itemL, bins, binsIndex, binSize)

        items.remove(itemF)
        items.remove(itemL)

        if len(items) == 1:
            lastItem = items[0]
            bin, binsIndex = placeItem2D(lastItem, bins, binsIndex, binSize)
            items.remove(lastItem)

    return len(bins)


def FFDRev3D(items, binSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))

    while len(items):
        itemF = items[0]
        itemL = items[len(items)-1]

        bin, binsIndex = placeItem3D(itemF, bins, binsIndex, binSize)
        bin, binsIndex = placeItem3D(itemL, bins, binsIndex, binSize)

        items.remove(itemF)
        items.remove(itemL)

        if len(items) == 1:
            lastItem = items[0]
            bin, binsIndex = placeItem3D(lastItem, bins, binsIndex, binSize)
            items.remove(lastItem)

    return len(bins)