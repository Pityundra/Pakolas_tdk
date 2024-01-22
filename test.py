from Resources.item1D import Item1D
from Resources.item2D import Item2D
from Resources.item3D import Item3D
from Resources.bin1D import Bin1D
from Resources.bin2D import Bin2D
from Resources.bin3D import Bin3D
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

    print("Egyszerű alsó korlát: " + str(SimpleLowerBound(items1, [10], "test", 1)))
    print("Egyszerű alsó korlát: " + str(SimpleLowerBound(items2, [4, 10], "test", 2)))
    print("Egyszerű alsó korlát: " + str(SimpleLowerBound(items3, [10, 10, 10], "test", 3)))


