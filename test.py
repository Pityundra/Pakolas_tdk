from Algorithms.FFD.ffd import FFD
from Algorithms.FFDDet.ffdRev import FFDRev
from Algorithms.FFDDet.ffdRevAdv import FFDRevAdv
from Algorithms.FFDNotDet.ffdBox import FFDBox
from Algorithms.FFDNotDet.ffdGroups import FFDGroups
from Algorithms.FFDNotDet.ffdRatio import FFDRatio
from Algorithms.FFDNotDet.ffdVal import FFDVal
from Algorithms.FFDNotDet.l2NotDet import L2NotDet
from Algorithms.GH.gh import GH
from Resources.Item.item1D import Item1D
from Resources.Item.item2D import Item2D
from Resources.Item.item3D import Item3D
from Resources.Bin.bin1D import Bin1D
from Resources.Bin.bin2D import Bin2D
from Resources.Bin.bin3D import Bin3D
from Resources.simpleLowerBound import SimpleLowerBound


def Tester():
    bin1 = Bin1D(1, 10)
    item1 = Item1D(1, 1)
    item11 = Item1D(2, 2)
    item111 = Item1D(3, 3)
    items1 = [item1, item11, item111]

    bin2 = Bin2D(1, 100, 100)
    item2 = Item2D(1, 1, 2)
    item22 = Item2D(2, 4, 2)
    item222 = Item2D(3, 5, 3)
    items2 = [item2, item22, item222]

    bin3 = Bin3D(1, 100, 100, 100)
    item3 = Item3D(1, 1, 2, 4)
    item33 = Item3D(2, 3, 8, 3)
    item333 = Item3D(3, 9, 2, 8)
    items3 = [item3, item33, item333]

    bin1.addItem(item1)
    bin1.addItem(item11)
    bin1.addItem(item111)

    bin2.addItem(item2)
    bin2.addItem(item22)
    bin2.addItem(item222)

    bin3.addItem(item3)
    bin3.addItem(item33)
    bin3.addItem(item333)

    print("bin1.getBinIndex() " + str(bin1.getBinIndex()))
    # Oda írják az itemNoumbert is lehet fölös, de lehet maradhat is
    print("bin1.getD1() " + str(bin1.getD1()))
    print("bin1.getItem(1) " + str(bin1.getItem(1)))
    print("bin1.getItems() " + str(bin1.getItems()))
    print("bin1.getDim() " + str(bin1.getDim()))
    print("bin1.getD1FreeCapacity() " + str(bin1.getD1FreeCapacity()))
    print("bin1.getD1Load() " + str(bin1.getD1Load()))
    print("bin1.getItemDB() " + str(bin1.getItemDB()))
    print("bin1.getLoadSum() " + str(bin1.getLoadSum()))
    print("bin1.getSumFreeCapacity() " + str(bin1.getSumFreeCapacity()))
    print()
    print(item1.getItemDim())
    print(item2)
    print(item3)
    print(bin1)
    print(bin2)
    print(bin3)
    print()

    print("Egyszerű alsó korlát: " + str(SimpleLowerBound(items1, [10])))
    print("Egyszerű alsó korlát: " + str(SimpleLowerBound(items2, [4, 10])))
    print("Egyszerű alsó korlát: " + str(SimpleLowerBound(items3, [10, 10, 10])))


def ffdic1Test():
    bin1 = Bin1D(1, 10)
    item1 = Item1D(1, 1)
    item11 = Item1D(2, 2)
    item111 = Item1D(3, 3)
    items1 = [item1, item11, item111, item111, item111]

    print("FFD - 1 - bin - sum")
    print(FFD("sum", "bin", items1, [10]))


def ffdic2Test():
    bin2 = Bin2D(1, 10, 10)
    item2 = Item2D(1, 1, 2)
    item22 = Item2D(2, 4, 2)
    item222 = Item2D(3, 5, 3)
    items2 = [item2, item22, item222, item222, item222, item222]

    print("FFD - 2 - bin - avg")
    print(FFD("avg", "bin", items2, [10, 10]))


def ffdic3Test():
    bin3 = Bin3D(1, 10, 10, 10)
    item3 = Item3D(1, 1, 2, 4)
    item33 = Item3D(2, 3, 8, 3)
    item333 = Item3D(3, 9, 2, 8)
    items3 = [item3, item33, item333]

    print("FFD - 3 - item - sum")
    print(FFD("sum", "item", items3, [10, 10, 10]))


def DotP1Test():
    bin1 = Bin1D(1, 10)
    item1 = Item1D(1, 1)
    item11 = Item1D(2, 2)
    item111 = Item1D(3, 3)
    items1 = [item1, item11, item111, item111, item111]

    print("DotP - 1")
    print(GH("dotP", items1, [10], 1))


def DotP2Test():
    bin2 = Bin2D(1, 10, 10)
    item2 = Item2D(1, 1, 2)
    item22 = Item2D(2, 4, 2)
    item222 = Item2D(3, 5, 3)
    items2 = [item2, item22, item222, item222, item222, item222]

    print("DotP - 2")
    print(GH("dotP", items2, [10, 10], 1))


def DotP3Test():
    bin3 = Bin3D(1, 10, 10, 10)
    item3 = Item3D(1, 1, 2, 4)
    item33 = Item3D(2, 3, 8, 3)
    item333 = Item3D(3, 9, 2, 8)
    items3 = [item3, item33, item333]

    print("DotP - 2")
    print(GH("dotP", items3, [10, 10, 10], 1))


def L2_1Test():
    bin1 = Bin1D(1, 10)
    item1 = Item1D(1, 1)
    item11 = Item1D(2, 2)
    item111 = Item1D(3, 3)
    items1 = [item1, item11, item111, item111, item111]

    print("L2 - 1")
    print(GH("L2", items1, [10], 1))


def L2_2Test():
    bin2 = Bin2D(1, 10, 10)
    item2 = Item2D(1, 1, 2)
    item22 = Item2D(2, 4, 2)
    item222 = Item2D(3, 5, 3)
    items2 = [item2, item22, item222, item222, item222, item222]

    print("L2 - 2")
    print(GH("L2", items2, [10, 10], 1))


def L2_3Test():
    bin3 = Bin3D(1, 10, 10, 10)
    item3 = Item3D(1, 1, 2, 4)
    item33 = Item3D(2, 3, 8, 3)
    item333 = Item3D(3, 9, 2, 8)
    items3 = [item3, item33, item333]

    print("L2 - 2")
    print(GH("L2", items3, [10, 10, 10], 1))


def FFDRevTest():
    item1 = Item1D(1, 4)
    item11 = Item1D(2, 8)
    item111 = Item1D(3, 3)
    items1 = [item1, item11, item111, item1, item11, item111, item1, item11, item111, item1, item1, item111]

    item2 = Item2D(1, 1, 2)
    item22 = Item2D(2, 4, 2)
    item222 = Item2D(3, 5, 3)
    items2 = [item2, item22, item222, item2, item22, item222, item2, item22, item222, item2, item22, item222, item2, item22, item222]

    item3 = Item3D(1, 1, 2, 4)
    item33 = Item3D(2, 3, 8, 3)
    item333 = Item3D(3, 9, 2, 8)
    items3 = [item3, item33, item333, item3, item33, item333, item3, item33, item333, item3, item33, item333, item3, item33, item333, item3, item33, item333]

    print("FFDRev")
    print(FFDRev(items1, [10]))
    print(FFDRev(items2, [10, 10]))
    print(FFDRev(items3, [10, 10, 10]))
    print("FFDRevAdv")
    print(FFDRevAdv(items1, [10]))
    print(FFDRevAdv(items2, [10, 10]))
    print(FFDRevAdv(items3, [10, 10, 10]))

    print("FFDVal")
    print(FFDVal(items1, [10]))
    print(FFDVal(items2, [10, 10]))
    print(FFDVal(items3, [10, 10, 10]))

    print("FFDRatio")
    print(FFDRatio(items1, [10]))
    print(FFDRatio(items2, [10, 10]))
    print(FFDRatio(items3, [10, 10, 10]))

    print("FFDGroups")
    print(FFDGroups(items1, [10], 3))
    print(FFDGroups(items2, [10, 10], 3))
    print(FFDGroups(items3, [10, 10, 10], 3))

    print("FFDBox")
    print(FFDBox(items1, [10], 5))
    print(FFDBox(items2, [10, 10], 5))
    print(FFDBox(items3, [10, 10, 10], 5))

    print("L2NotDet")
    print(L2NotDet(items1, [10]))
    print(L2NotDet(items2, [10, 10]))
    print(L2NotDet(items3, [10, 10, 10]))