from Resources.Bin.bin4D import Bin4D


def placeItem4D(item, bins, binsIndex, binSize):
    isItemTaken = False

    # Végig nézi a ládákat hogy hova fér be az Item és a legelső helyre berakja
    for bin in bins:
        if (bin.d1FreeCapacity >= item.getD1()) and (bin.d2FreeCapacity >= item.getD2()) and (bin.d3FreeCapacity >= item.getD3()) and (bin.d4FreeCapacity >= item.getD4()):
            bin.addItem(item)
            isItemTaken = True
            break

    # Ha nem sikerült berakni az itemet sehova új ládát nyitunk
    if not isItemTaken:
        binsIndex += 1
        bins.append(Bin4D(binsIndex + 1, binSize[0], binSize[1], binSize[2], binSize[3]))
        bins[binsIndex].addItem(item)

    return bins, binsIndex