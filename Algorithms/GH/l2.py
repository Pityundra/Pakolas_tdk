from Resources.Bin.bin1D import Bin1D
from Resources.Bin.bin2D import Bin2D
from Resources.Bin.bin3D import Bin3D
from Resources.Bin.bin4D import Bin4D
from Resources.Bin.bin6D import Bin6D
from Resources.weightInform import WeightInform, itemWeight


def L2_1(items, binSize, grasp):
    # Előkészítési fázis
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin1D(binsIndex + 1, binSize[0]))
    # r(t) jelöli a jelenleg nyitott ládák fennmaradó kapacitás vektorát => bins[].d1FreeCapacity
    allWeight = []  # [item] [bin] [weight]

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
            continue

        allWeight.sort(key=itemWeight)

        # Grasp alkalmazása
        if grasp <= len(
                allWeight) or grasp < 0:  # ha a Grasp értéke nagyobb mint a lehetséges elpakolható tágyak szám akkor elrakjuk a legutolsót
            itemChosenNo = grasp - 1
        else:
            itemChosenNo = len(allWeight) - 1

        # Elrakjuk a tárgyat a ládába
        bins[int(allWeight[itemChosenNo].bin.binIndex - 1)].addItem(allWeight[itemChosenNo].item)
        # Kiveszük a tárgyat az elpakolandó tárgyak listájából
        items.remove(allWeight[itemChosenNo].item)
        # Töröljük az eddigi súlyokat, hiszen mindent újra kell számolni
        allWeight.clear()

    return len(bins)


def L2_2(items, binSize, grasp):
    # Előkészítési fázis
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))
    # r(t) jelöli a jelenleg nyitott ládák fennmaradó kapacitás vektorát => bins[].d1FreeCapacity
    allWeight = []  # [item] [bin] [weight]

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
            continue

        allWeight.sort(key=itemWeight)

        # Grasp alkalmazása
        if grasp <= len(
                allWeight) or grasp < 0:  # ha a Grasp értéke nagyobb mint a lehetséges elpakolható tágyak szám akkor elrakjuk a legutolsót
            itemChosenNo = grasp - 1
        else:
            itemChosenNo = len(allWeight) - 1

        # Elrakjuk a tárgyat a ládába
        bins[int(allWeight[itemChosenNo].bin.binIndex - 1)].addItem(allWeight[itemChosenNo].item)
        # Kiveszük a tárgyat az elpakolandó tárgyak listájából
        items.remove(allWeight[itemChosenNo].item)
        # Töröljük az eddigi súlyokat, hiszen mindent újra kell számolni
        allWeight.clear()

    return len(bins)


def L2_3(items, binSize, grasp):
    # Előkészítési fázis
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin3D(binsIndex + 1, binSize[0], binSize[1], binSize[2]))
    # r(t) jelöli a jelenleg nyitott ládák fennmaradó kapacitás vektorát => bins[].d1FreeCapacity
    allWeight = []  # [item] [bin] [weight]

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
            continue

        allWeight.sort(key=itemWeight)

        # Grasp alkalmazása
        if grasp <= len(allWeight) or grasp < 0:  # ha a Grasp értéke nagyobb mint a lehetséges elpakolható tágyak szám akkor elrakjuk a legutolsót
            itemChosenNo = grasp - 1
        else:
            itemChosenNo = len(allWeight) - 1

        # Elrakjuk a tárgyat a ládába
        bins[int(allWeight[itemChosenNo].bin.binIndex - 1)].addItem(allWeight[itemChosenNo].item)
        # Kiveszük a tárgyat az elpakolandó tárgyak listájából
        items.remove(allWeight[itemChosenNo].item)
        # Töröljük az eddigi súlyokat, hiszen mindent újra kell számolni
        allWeight.clear()

    return len(bins)


def L2_4(items, binSize, grasp):
    # Előkészítési fázis
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin4D(binsIndex + 1, binSize[0], binSize[1], binSize[2], binSize[3]))
    # r(t) jelöli a jelenleg nyitott ládák fennmaradó kapacitás vektorát => bins[].d1FreeCapacity
    allWeight = []  # [item] [bin] [weight]

    while len(items):
        for item in items:
            for bin in bins:
                if ((bin.d1FreeCapacity >= item.getD1())
                        and (bin.d2FreeCapacity >= item.getD2())
                        and (bin.d3FreeCapacity >= item.getD3())
                        and (bin.d4FreeCapacity >= item.getD4())):
                    item.itemWeight = pow((int(item.d1) - int(bin.d1FreeCapacity)), 2) + pow((int(item.d2) - int(bin.d2FreeCapacity)), 2) + pow((int(item.d3) - int(bin.d3FreeCapacity)), 2) + pow((int(item.d4) - int(bin.d4FreeCapacity)), 2)
                    weight = WeightInform(item, bin, item.itemWeight)
                    allWeight.append(weight)
        if not allWeight:
            binsIndex += 1
            bins.append(Bin4D(binsIndex + 1, binSize[0], binSize[1], binSize[2], binSize[3]))
            continue

        allWeight.sort(key=itemWeight)

        # Grasp alkalmazása
        if grasp <= len(allWeight) or grasp < 0:  # ha a Grasp értéke nagyobb mint a lehetséges elpakolható tágyak szám akkor elrakjuk a legutolsót
            itemChosenNo = grasp - 1
        else:
            itemChosenNo = len(allWeight) - 1

        # Elrakjuk a tárgyat a ládába
        bins[int(allWeight[itemChosenNo].bin.binIndex - 1)].addItem(allWeight[itemChosenNo].item)
        # Kiveszük a tárgyat az elpakolandó tárgyak listájából
        items.remove(allWeight[itemChosenNo].item)
        # Töröljük az eddigi súlyokat, hiszen mindent újra kell számolni
        allWeight.clear()

    return len(bins)



def L2_6(items, binSize, grasp):
    # Előkészítési fázis
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin6D(binsIndex + 1, binSize[0], binSize[1], binSize[2], binSize[3], binSize[4], binSize[5]))
    # r(t) jelöli a jelenleg nyitott ládák fennmaradó kapacitás vektorát => bins[].d1FreeCapacity
    allWeight = []  # [item] [bin] [weight]

    while len(items):
        for item in items:
            for bin in bins:
                if ((bin.d1FreeCapacity >= item.getD1())
                        and (bin.d2FreeCapacity >= item.getD2())
                        and (bin.d3FreeCapacity >= item.getD3())
                        and (bin.d4FreeCapacity >= item.getD4())
                        and (bin.d5FreeCapacity >= item.getD5())
                        and (bin.d6FreeCapacity >= item.getD6())):
                    item.itemWeight = (pow((int(item.d1) - int(bin.d1FreeCapacity)), 2)
                                       + pow((int(item.d2) - int(bin.d2FreeCapacity)), 2)
                                       + pow((int(item.d3) - int(bin.d3FreeCapacity)), 2)
                                       + pow((int(item.d4) - int(bin.d4FreeCapacity)), 2)
                                       + pow((int(item.d5) - int(bin.d5FreeCapacity)), 2)
                                       + pow((int(item.d6) - int(bin.d6FreeCapacity)), 2))

                    weight = WeightInform(item, bin, item.itemWeight)
                    allWeight.append(weight)
        if not allWeight:
            binsIndex += 1
            bins.append(Bin6D(binsIndex + 1, binSize[0], binSize[1], binSize[2], binSize[3], binSize[4], binSize[5]))
            continue

        allWeight.sort(key=itemWeight)

        # Grasp alkalmazása
        if grasp <= len(allWeight) or grasp < 0:  # ha a Grasp értéke nagyobb mint a lehetséges elpakolható tágyak szám akkor elrakjuk a legutolsót
            itemChosenNo = grasp - 1
        else:
            itemChosenNo = len(allWeight) - 1

        # Elrakjuk a tárgyat a ládába
        bins[int(allWeight[itemChosenNo].bin.binIndex - 1)].addItem(allWeight[itemChosenNo].item)
        # Kiveszük a tárgyat az elpakolandó tárgyak listájából
        items.remove(allWeight[itemChosenNo].item)
        # Töröljük az eddigi súlyokat, hiszen mindent újra kell számolni
        allWeight.clear()

    return len(bins)