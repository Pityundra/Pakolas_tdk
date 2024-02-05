from Data.GenerateFiles.dataGenerateWithOpt import dataGen
from Data.GenerateFiles.splitData import splitData, dataSplitter
from Resources.dataLoad import fileRead
from test import Tester, ffdic3Test, ffdic1Test, ffdic2Test, DotP1Test, DotP2Test, DotP3Test, L2_1Test, L2_2Test, \
    L2_3Test, FFDRevTest, FFDBGTest, FFDMPTest, Test, FFDBoxTest

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

dataGen()