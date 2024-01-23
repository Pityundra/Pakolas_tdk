from Resources.Bin.bin1D import Bin1D


def placeItem1D(item, bins, binsIndex, binSize):
    isItemTaken = False

    # Végig nézi a ládákat hogy hova fér be az Item és a legelső helyre berakja
    for bin in bins:
        if bin.d1FreeCapacity >= item.getD1():
            bin.addItem(item)
            isItemTaken = True
            break

    # Ha nem sikerült berakni az itemet sehova új ládát nyitunk
    if not isItemTaken:
        binsIndex += 1
        bins.append(Bin1D(binsIndex + 1, binSize[0]))
        bins[binsIndex].addItem(item)

    return bins, binsIndex