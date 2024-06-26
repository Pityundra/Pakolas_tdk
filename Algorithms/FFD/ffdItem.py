from Resources.Bin.bin1D import Bin1D
from Resources.Bin.bin2D import Bin2D
from Resources.Bin.bin3D import Bin3D
from Resources.Bin.bin4D import Bin4D
from Resources.Bin.bin6D import Bin6D


def FFDIC1(items, binSize,):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin1D(binsIndex + 1, binSize[0]))

    for item in items:
        isItemTaken = False
        # Végig nézi a ládákat hogy hova fér be az Item és a legelső helyre berakja
        for bin in bins:
            # print(bin.d1FreeCapacity)
            if bin.d1FreeCapacity >= item.getD1():
                bin.addItem(item)
                isItemTaken = True
                break
        # Ha nem sikerült berakni az itemet sehova új ládát nyitunk
        if not isItemTaken:
            binsIndex += 1
            bins.append(Bin1D(binsIndex + 1, binSize[0]))
            bins[binsIndex].addItem(item)

    return len(bins)


def FFDIC2(items, binSize):
    bins = []  # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))

    for item in items:
        isItemTaken = False
        # Végig nézi a ládákat hogy hova fér be az Item és a legelső helyre berakja
        for bin in bins:
            # print(bin.d1FreeCapacity, bin.d2FreeCapacity)
            if ((bin.d1FreeCapacity >= item.getD1())
                    and (bin.d2FreeCapacity >= item.getD2())):
                bin.addItem(item)
                isItemTaken = True
                break
        # Ha nem sikerült berakni az itemet sehova új ládát nyitunk
        if not isItemTaken:
            binsIndex += 1
            bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))
            bins[binsIndex].addItem(item)

    return len(bins)


def FFDIC3(items, binSize):
    bins = []   # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin3D(binsIndex+1, binSize[0], binSize[1], binSize[2]))

    for item in items:
        isItemTaken = False
        # Végig nézi a ládákat hogy hova fér be az Item és a legelső helyre berakja
        for bin in bins:
            # print(bin.d1FreeCapacity, bin.d2FreeCapacity, bin.d3FreeCapacity)
            if ((bin.d1FreeCapacity >= item.getD1())
                    and (bin.d2FreeCapacity >= item.getD2())
                    and (bin.d3FreeCapacity >= item.getD3())):
                bin.addItem(item)
                isItemTaken = True
                break
        # Ha nem sikerült berakni az itemet sehova új ládát nyitunk
        if not isItemTaken:
            binsIndex += 1
            bins.append(Bin3D(binsIndex+1, binSize[0], binSize[1], binSize[2]))
            bins[binsIndex].addItem(item)

    return len(bins)


def FFDIC4(items, binSize):
    bins = []   # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin4D(binsIndex+1, binSize[0], binSize[1], binSize[2], binSize[3]))

    for item in items:
        isItemTaken = False
        # Végig nézi a ládákat hogy hova fér be az Item és a legelső helyre berakja
        for bin in bins:
            if ((bin.d1FreeCapacity >= item.getD1())
                    and (bin.d2FreeCapacity >= item.getD2())
                    and (bin.d3FreeCapacity >= item.getD3())
                    and (bin.d4FreeCapacity >= item.getD4())):
                bin.addItem(item)
                isItemTaken = True
                break
        # Ha nem sikerült berakni az itemet sehova új ládát nyitunk
        if not isItemTaken:
            binsIndex += 1
            bins.append(Bin4D(binsIndex+1, binSize[0], binSize[1], binSize[2], binSize[3]))
            bins[binsIndex].addItem(item)

    return len(bins)


def FFDIC6(items, binSize):
    bins = []   # Felhasznált ládák listája
    binsIndex = 0  # A ládák indexelésére
    bins.append(Bin6D(binsIndex+1, binSize[0], binSize[1], binSize[2], binSize[3], binSize[4], binSize[5]))

    for item in items:
        isItemTaken = False
        # Végig nézi a ládákat hogy hova fér be az Item és a legelső helyre berakja
        for bin in bins:
            if ((bin.d1FreeCapacity >= item.getD1())
                    and (bin.d2FreeCapacity >= item.getD2())
                    and (bin.d3FreeCapacity >= item.getD3())
                    and (bin.d4FreeCapacity >= item.getD4())
                    and (bin.d5FreeCapacity >= item.getD5())
                    and (bin.d6FreeCapacity >= item.getD6())):
                bin.addItem(item)
                isItemTaken = True
                break
        # Ha nem sikerült berakni az itemet sehova új ládát nyitunk
        if not isItemTaken:
            binsIndex += 1
            bins.append(Bin6D(binsIndex+1, binSize[0], binSize[1], binSize[2], binSize[3], binSize[4], binSize[5]))
            bins[binsIndex].addItem(item)

    return len(bins)
