from Resources.Bin.bin1D import Bin1D
from Resources.Bin.bin2D import Bin2D
from Resources.Bin.bin3D import Bin3D


def FFDBC1(items, binSize):
    bins = []   # Felhasznált ládák listája
    openBinIndex = 0  # A ládák indexelésére

    while len(items) > 0:
        bins.append(Bin1D(openBinIndex + 1, binSize[0]))
        for item in items:
            # Ha belefér egy item a nyitott ládába akkor beleteszi és kiveszi a listából
            if item in items and (bins[openBinIndex].d1FreeCapacity >= item.getD1()):
                bins[openBinIndex].addItem(item)
                items.remove(item)
        openBinIndex += 1

    return len(bins)


def FFDBC2(items, binSize):
    bins = []   # Felhasznált ládák listája
    openBinIndex = 0  # A ládák indexelésére

    while len(items) > 0:
        bins.append(Bin2D(openBinIndex + 1, binSize[0], binSize[1]))
        for item in items:
            # Ha belefér egy item a nyitott ládába akkor beleteszi és kiveszi a listából
            if item in items and (bins[openBinIndex].d1FreeCapacity >= item.getD1()) and (bins[openBinIndex].d2FreeCapacity >= item.getD2()):
                bins[openBinIndex].addItem(item)
                items.remove(item)
        openBinIndex += 1

    return len(bins)


def FFDBC3(items, binSize):
    bins = []   # Felhasznált ládák listája
    openBinIndex = 0  # A ládák indexelésére

    while len(items) > 0:
        bins.append(Bin3D(openBinIndex + 1, binSize[0], binSize[1], binSize[2]))
        for item in items:
            # Ha belefér egy item a nyitott ládába akkor beleteszi és kiveszi a listából
            if item in items and (bins[openBinIndex].d1FreeCapacity >= item.getD1()) and (bins[openBinIndex].d2FreeCapacity >= item.getD2()) and (bins[openBinIndex].d3FreeCapacity >= item.getD3()):
                bins[openBinIndex].addItem(item)
                items.remove(item)
        openBinIndex += 1

    return len(bins)