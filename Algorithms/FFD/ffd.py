from Algorithms.FFD.ffdBin import FFDBC1, FFDBC2, FFDBC3
from Algorithms.FFD.ffdItem import FFDIC1, FFDIC2, FFDIC3
from Resources.Item.item1D import itemsSum, itemsAVG, itemsProd
from Resources.item3D import itemsSum, itemsAVG, itemsProd


def FFD(SAP, centric, items, binSize):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    if SAP == "sum":
        # A kapott tárgyakat a dimenziói összege alapján csökkenő sorrendbe tesszük
        items.sort(reverse=True, key=itemsSum)
    elif SAP == "avg":
        # A kapott tárgyakat a dimenzióik átlaga alapján csökkenő sorrendbe tesszük
        items.sort(reverse=True, key=itemsAVG)
    elif SAP == "prod":
        # A kapott tárgyakat a Prod értéke alapján csökkenő sorrendbe tesszük
        items.sort(reverse=True, key=itemsProd)
    else:
        print("Nem sum, avg vagy prod!")
        return 1

    # Biztonsági mentés a tárgyakról
    itemsCopy = []
    for item in items:
        itemsCopy.append(item)
        print(item)
    print()

    if centric == "item":
        if len(binSize) == 1:
            return FFDIC1(itemsCopy, binSize)
        elif len(binSize) == 2:
            return FFDIC2(itemsCopy, binSize)
        elif len(binSize) == 3:
            return FFDIC3(itemsCopy, binSize)
        else:
            print("Ilyen dimenzió számra nem vagyunk felkészülve!")
            return 1

    elif centric == "bin":
        if len(binSize) == 1:
            return FFDBC1(itemsCopy, binSize)
        elif len(binSize) == 2:
            return FFDBC2(itemsCopy, binSize)
        elif len(binSize) == 3:
            return FFDBC3(itemsCopy, binSize)
        else:
            print("Ilyen dimenzió számra nem vagyunk felkészülve!")
            return 1
    else:
        print("Nem bin vagy item!")
        return 1
