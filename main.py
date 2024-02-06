from Algorithms.FFD.ffd import FFD
from Algorithms.FFDDet.ffdMP import FFDMP
from Algorithms.FFDDet.ffdRev import FFDRev
from Algorithms.FFDDet.ffdRevAdv import FFDRevAdv
from Algorithms.FFDNotDet.ffdBG import FFDGB
from Algorithms.FFDNotDet.ffdBox import FFDBox
from Algorithms.FFDNotDet.ffdGroups import FFDGroups
from Algorithms.FFDNotDet.ffdRatio import FFDRatio
from Algorithms.FFDNotDet.ffdVal import FFDVal
from Algorithms.FFDNotDet.l2NotDet import L2NotDet
from Algorithms.GH.gh import GH
from Data.GenerateFiles.dataGenerateWithOpt import dataGen
from Data.GenerateFiles.splitData import splitData, dataSplitter
from Resources.dataLoad import fileRead
from Resources.simpleLowerBound import SimpleLowerBound
from test import Tester, ffdic3Test, ffdic1Test, ffdic2Test, DotP1Test, DotP2Test, DotP3Test, L2_1Test, L2_2Test, \
    L2_3Test, FFDRevTest, FFDBGTest, FFDMPTest, Test, FFDBoxTest

f = open("C:/Users/Asus/Desktop/Pakolas_tdk/Data/FileNames.txt", "r")
lines = f.readlines()
for line in lines:
    line = line.strip()
    dataName = line.replace(".", "/").split("/")[-2]
    print(dataName)
    items, binSize = fileRead(line)

    print("Dimenzió szám: " + str(len(binSize)))
    print("Alsó korlát: " + str(SimpleLowerBound(items, binSize)))

    # FFDGroups(items, binSize, 3, 10, dataName)
    # FFDBox(items, binSize, 5, 10, dataName)
    # FFD("sum", "bin", items, binSize, dataName)
    # GH("dotP", items, binSize, 1, dataName)
    # FFDMP(items, binSize, 0.9, dataName)
    # FFDRev(items, binSize, dataName)
    # FFDRevAdv(items, binSize, dataName)
    FFDRatio(items, binSize, 3, 10, dataName)
    FFDVal(items, binSize, 3, dataName)
    L2NotDet(items, binSize, 3, 10, dataName)
    FFDGB(items, binSize, 5, 3, 10, dataName)


    items.clear()
    binSize.clear()


# Tester()
#

# ffdic1Test()
# DotP1Test()
# L2_1Test()
#
# ffdic2Test()
# DotP2Test()
# L2_2Test()
#
# ffdic3Test()
# DotP3Test()
# L2_3Test()
#
# FFDRevTest()
#
# items3, binSize3 = fileRead("C:/Users/Asus/Desktop/Pakolas_tdk/Data/3D_Classes/class1_5.txt")
# for item3 in items3:
#     print(item3)
# print(binSize3)
#
#
# items2, binSize2 = fileRead("C:/Users/Asus/Desktop/Pakolas_tdk/Data/2D_Classes/class1_5.txt")
# print(len(items2))
# for item2 in items2:
#     print(item2)
# print(binSize2)
#
#
# items1, binSize1 = fileRead("C:/Users/Asus/Desktop/Pakolas_tdk/Data/1D_Classes/class1_5.txt")
# for item1 in items1:
#     print(item1)
# print(binSize1)
#
# FFDBGTest()

# splitData("class1_5")

# dataSplitter("C:/Users/Asus/Desktop/Pakolas_tdk/Data/3D_Classes/FileNames.txt")

# FFDMPTest()
# print(Test())

# FFDBoxTest()

# dataGen()

