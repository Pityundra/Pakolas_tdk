from Algorithms.GH.dotP import DotP1, DotP2, DotP3, DotP4, DotP6
from Algorithms.GH.l2 import L2_1, L2_2, L2_3, L2_4, L2_6


def GH(alg, items, binSize, grasp, dataName):
    if len(items) == 0:
        print("Nincsenek tárgyak!")
        return 1

    itemsCopy = items.copy()

    res = []

    if alg == "dotP":
        if len(binSize) == 1:
            res.append(DotP1(itemsCopy, binSize, grasp))
        elif len(binSize) == 2:
            res.append(DotP2(itemsCopy, binSize, grasp))
        elif len(binSize) == 3:
            res.append(DotP3(itemsCopy, binSize, grasp))
        elif len(binSize) == 4:
            res.append(DotP4(itemsCopy, binSize, grasp))
        elif len(binSize) == 6:
            res.append(DotP6(itemsCopy, binSize, grasp))
        else:
            print("Ilyen dimenzió számra nem vagyunk felkészülve!")
            return 1

    elif alg == "L2":
        if len(binSize) == 1:
            res.append(L2_1(itemsCopy, binSize, grasp))
        elif len(binSize) == 2:
            res.append(L2_2(itemsCopy, binSize, grasp))
        elif len(binSize) == 3:
            res.append(L2_3(itemsCopy, binSize, grasp))
        elif len(binSize) == 4:
            res.append(L2_4(itemsCopy, binSize, grasp))
        elif len(binSize) == 6:
            res.append(L2_6(itemsCopy, binSize, grasp))
        else:
            print("Ilyen dimenzió számra nem vagyunk felkészülve!")
            return 1

    else:
        print("Nem DotP vagy L2!")
        return 1

    f = open(f"Results/{len(binSize)}D_Results/{len(binSize)}D_Results.txt", "a")
    f.write(f"{dataName};{alg};gp{grasp};{res[0]}\n")
    f.close()

    print(f"{alg}-{grasp} Futási eredménye: {res}\n")
    return res