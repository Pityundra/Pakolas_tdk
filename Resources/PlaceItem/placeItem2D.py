from Resources.Bin.bin2D import Bin2D


def placeItem2D(item, bins, binsIndex, binSize):
    isItemTaken = False

    # Végig nézi a ládákat hogy hova fér be az Item és a legelső helyre berakja
    for bin in bins:
        if (bin.d1FreeCapacity >= item.getD1()) and (bin.d2FreeCapacity >= item.getD2()):
            bin.addItem(item)
            isItemTaken = True
            break

    # Ha nem sikerült berakni az itemet sehova új ládát nyitunk
    if not isItemTaken:
        binsIndex += 1
        bins.append(Bin2D(binsIndex + 1, binSize[0], binSize[1]))
        bins[binsIndex].addItem(item)

    return bins, binsIndex