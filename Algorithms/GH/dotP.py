from Resources.Bin.bin1D import Bin1D
from Resources.Bin.bin2D import Bin2D
from Resources.Bin.bin3D import Bin3D
from Resources.weightInform import WeightInform, itemWeight


def DotP1(itemsCopy, binSize, grasp):
    # Előkészítési fázis
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin1D(binsIndex + 1, binSize[0]))
    # r(t) jelöli a jelenleg nyitott ládák fennmaradó kapacitás vektorát => bins[].d1FreeCapacity
    allWeight = []  # [item] [bin] [weight]

    while len(itemsCopy):
        for item in itemsCopy:
            for bin in bins:
                if bin.d1FreeCapacity >= item.getD1():
                    item.itemWeight = int(item.d1) * int(bin.d1FreeCapacity)
                    weight = WeightInform(item, bin, item.itemWeight)
                    allWeight.append(weight)
        if not allWeight:
            binsIndex += 1
            bins.append(Bin1D(binsIndex + 1, binSize[0]))
            continue

        allWeight.sort(reverse=True, key=itemWeight)

        # Grasp alkalmazása
        if grasp <= len(allWeight) or grasp < 0:  # ha a Grasp értéke nagyobb mint a lehetséges elpakolható tágyak szám akkor elrakjuk a legutolsót
            itemChosenNo = grasp - 1
        else:
            itemChosenNo = len(allWeight) - 1

        # Elrakjuk a tárgyat a ládába
        bins[int(allWeight[itemChosenNo].bin.binIndex - 1)].addItem(allWeight[itemChosenNo].item)
        # Kiveszük a tárgyat az elpakolandó tárgyak listájából
        itemsCopy.remove(allWeight[itemChosenNo].item)
        # Töröljük az eddigi súlyokat, hiszen mindent újra kell számolni
        allWeight.clear()

    for bin in bins:
        print(bin)
    print()

    return f"Felhasznált ládák száma: {len(bins)}"


def DotP2(itemsCopy, binSize, grasp):
    # Előkészítési fázis
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))
    # r(t) jelöli a jelenleg nyitott ládák fennmaradó kapacitás vektorát => bins[].d1FreeCapacity
    allWeight = []  # [item] [bin] [weight]

    while len(itemsCopy):
        for item in itemsCopy:
            for bin in bins:
                if (bin.d1FreeCapacity >= item.getD1()) and (bin.d2FreeCapacity >= item.getD2()):
                    item.itemWeight = int(item.d1) * int(bin.d1FreeCapacity) + int(item.d2) * int(bin.d2FreeCapacity)
                    weight = WeightInform(item, bin, item.itemWeight)
                    allWeight.append(weight)
        if not allWeight:
            binsIndex += 1
            bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))
            continue

        allWeight.sort(reverse=True, key=itemWeight)

        # Grasp alkalmazása
        if grasp <= len(allWeight) or grasp < 0:  # ha a Grasp értéke nagyobb mint a lehetséges elpakolható tágyak szám akkor elrakjuk a legutolsót
            itemChosenNo = grasp - 1
        else:
            itemChosenNo = len(allWeight) - 1

        # Elrakjuk a tárgyat a ládába
        bins[int(allWeight[itemChosenNo].bin.binIndex - 1)].addItem(allWeight[itemChosenNo].item)
        # Kiveszük a tárgyat az elpakolandó tárgyak listájából
        itemsCopy.remove(allWeight[itemChosenNo].item)
        # Töröljük az eddigi súlyokat, hiszen mindent újra kell számolni
        allWeight.clear()

    for bin in bins:
        print(bin)
    print()

    return f"Felhasznált ládák száma: {len(bins)}"


def DotP3(itemsCopy, binSize, grasp):
    # Előkészítési fázis
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
    # r(t) jelöli a jelenleg nyitott ládák fennmaradó kapacitás vektorát => bins[].d1FreeCapacity
    allWeight = []  # [item] [bin] [weight]

    while len(itemsCopy):
        for item in itemsCopy:
            for bin in bins:
                if (bin.d1FreeCapacity >= item.getD1()) and (bin.d2FreeCapacity >= item.getD2()) and (bin.d3FreeCapacity >= item.getD3()):
                    item.itemWeight = int(item.d1) * int(bin.d1FreeCapacity) + int(item.d2) * int(bin.d2FreeCapacity) + int(item.d3) * int(bin.d3FreeCapacity)
                    weight = WeightInform(item, bin, item.itemWeight)
                    allWeight.append(weight)
        if not allWeight:
            binsIndex += 1
            bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
            continue

        allWeight.sort(reverse=True, key=itemWeight)

        # Grasp alkalmazása
        if grasp <= len(allWeight) or grasp < 0:  # ha a Grasp értéke nagyobb mint a lehetséges elpakolható tágyak szám akkor elrakjuk a legutolsót
            itemChosenNo = grasp - 1
        else:
            itemChosenNo = len(allWeight) - 1

        # Elrakjuk a tárgyat a ládába
        bins[int(allWeight[itemChosenNo].bin.binIndex - 1)].addItem(allWeight[itemChosenNo].item)
        # Kiveszük a tárgyat az elpakolandó tárgyak listájából
        itemsCopy.remove(allWeight[itemChosenNo].item)
        # Töröljük az eddigi súlyokat, hiszen mindent újra kell számolni
        allWeight.clear()

    for bin in bins:
        print(bin)
    print()

    return f"Felhasznált ládák száma: {len(bins)}"