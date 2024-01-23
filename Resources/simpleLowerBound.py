from math import ceil


def SimpleLowerBound(items, binSize):
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
    else:
        return "lyen dimenzió számra nem vagyunk felkészülve!"

    """
    Ez ugye azt nem veszi figyelembe ha a tárgyakat nem lehet egymás mellé pakolni így azokban az esetekben
    amikor mindegyik elemet külön kell tegyünk nagyon távoli korlátott add, pedig nem lehet jobb pakolást összehozni
    sehogy semm.
    """

    return lowerBound