from Algorithms.GH.dotP import DotP1, DotP2, DotP3
from Algorithms.GH.l2 import L2_1, L2_2, L2_3


def GH(alg, items, binSize, grasp):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    itemsCopy = []
    for item in items:
        itemsCopy.append(item)

    if alg == "dotP":
        if len(binSize) == 1:
            return DotP1(itemsCopy, binSize, grasp)
        elif len(binSize) == 2:
            return DotP2(itemsCopy, binSize, grasp)
        elif len(binSize) == 3:
            return DotP3(itemsCopy, binSize, grasp)
        else:
            print("Rossz dimenzió szám!")
            return 1

    elif alg == "L2":
        if len(binSize) == 1:
            return L2_1(itemsCopy, binSize, grasp)
        elif len(binSize) == 2:
            return L2_2(itemsCopy, binSize, grasp)
        elif len(binSize) == 3:
            return L2_3(itemsCopy, binSize, grasp)
        else:
            print("Rossz dimenzió szám!")
            return 1

    else:
        print("Nem DotP vagy L2!")
        return 1