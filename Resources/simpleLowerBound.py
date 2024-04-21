from math import ceil


def SimpleLowerBound(items, binSize, dataName):
    if len(binSize) == 1:

        d1Sum = 0

        for item in items:
            d1Sum += item.getD1()

        lowerBound = ceil(d1Sum / binSize[0])

    elif len(binSize) == 2:
        d1Sum = 0
        d2Sum = 0

        for item in items:
            d1Sum += item.getD1()
            d2Sum += item.getD2()

        lowerBound = max(ceil(d1Sum / binSize[0]), ceil(d2Sum / binSize[1]))

    elif len(binSize) == 3:
        d1Sum = 0
        d2Sum = 0
        d3Sum = 0

        for item in items:
            d1Sum += item.getD1()
            d2Sum += item.getD2()
            d3Sum += item.getD3()

        lowerBound = max(ceil(d1Sum/binSize[0]), ceil(d2Sum/binSize[1]), ceil(d3Sum/binSize[2]))
    elif len(binSize) == 4:
        d1Sum = 0
        d2Sum = 0
        d3Sum = 0
        d4Sum = 0

        for item in items:
            d1Sum += item.getD1()
            d2Sum += item.getD2()
            d3Sum += item.getD3()
            d4Sum += item.getD4()

        lowerBound = max(ceil(d1Sum/binSize[0]), ceil(d2Sum/binSize[1]), ceil(d3Sum/binSize[2]), ceil(d4Sum/binSize[3]))
    elif len(binSize) == 6:
        d1Sum = 0
        d2Sum = 0
        d3Sum = 0
        d4Sum = 0
        d5Sum = 0
        d6Sum = 0

        for item in items:
            d1Sum += item.getD1()
            d2Sum += item.getD2()
            d3Sum += item.getD3()
            d4Sum += item.getD4()
            d5Sum += item.getD5()
            d6Sum += item.getD6()

        lowerBound = max(ceil(d1Sum/binSize[0]), ceil(d2Sum/binSize[1]), ceil(d3Sum/binSize[2]), ceil(d4Sum/binSize[3]), ceil(d5Sum/binSize[4]), ceil(d6Sum/binSize[5]))
    else:
        return "lyen dimenzió számra nem vagyunk felkészülve!"

    """
    Ez ugye azt nem veszi figyelembe ha a tárgyakat nem lehet egymás mellé pakolni így azokban az esetekben
    amikor mindegyik elemet külön kell tegyünk nagyon távoli korlátott add, pedig nem lehet jobb pakolást összehozni
    sehogy semm.
    """
    
    f = open(f"Results/{len(binSize)}D_Results/{len(binSize)}D_Results.txt", "a")
    f.write(f"{dataName};Alsó Korlát;;{lowerBound}\n")
    f.close()

    return lowerBound