def binLoadSum(bin):
    return bin.loadSum


def binIndex(bin):
    return bin.getBinIndex()


class Bin4D:
    def __init__(self, index, D1, D2, D3, D4):
        self.binIndex = index
        self.items = []

        # Láda max kapacitása dimenziókként
        self.D1 = D1
        self.D2 = D2
        self.D3 = D3
        self.D4 = D4

        # A láda dimenzióinaka  töltöttsége
        self.d1Load = 0
        self.d2Load = 0
        self.d3Load = 0
        self.d4Load = 0

        # A láda még fentmaradó kapacitása
        self.d1FreeCapacity = D1
        self.d2FreeCapacity = D2
        self.d3FreeCapacity = D3
        self.d4FreeCapacity = D4
        self.sumFreeCapacity = D1 + D2 + D3 + D4

        self.itemDB = 0   # Ennyi tárgy van a ládában jelenleg
        self.loadSum = 0  # Össz töltöttség

    def __str__(self):
        return f"Láda száma: [{self.binIndex}] Max kapacitások: [{self.D1},{self.D2},{self.D3},{self.D4}] " \
               f"Töltöttségek: [{self.d1Load},{self.d2Load},{self.d3Load},{self.d4Load}]  " \
               f"Üres helyek: [{self.d1FreeCapacity},{self.d2FreeCapacity},{self.d3FreeCapacity},{self.d4FreeCapacity}] Sum: [{self.sumFreeCapacity}] " \
               f"Tárgyak darabszáma: [{self.itemDB}], Össz töltöttség: [{self.loadSum}]"

    def getBinIndex(self):
        return self.binIndex

    def getD1(self):
        return self.D1

    def getD2(self):
        return self.D2

    def getD3(self):
        return self.D3
    def getD4(self):
        return self.D4
    def getD1Load(self):
        return self.d1Load

    def getD2Load(self):
        return self.d2Load

    def getD3Load(self):
        return self.d3Load
    def getD4Load(self):
        return self.d4Load

    def getD1FreeCapacity(self):
        return self.d1FreeCapacity

    def getD2FreeCapacity(self):
        return self.d2FreeCapacity

    def getD3FreeCapacity(self):
        return self.d3FreeCapacity
    def getD4FreeCapacity(self):
        return self.d4FreeCapacity

    def getSumFreeCapacity(self):
        return self.sumFreeCapacity

    def getItemDB(self):
        return self.itemDB

    def getLoadSum(self):
        return self.loadSum

    def getItems(self):
        return self.items

    def getItem(self, no):
        return self.items[no]

    @staticmethod
    def getDim():
        return 4

    def addItem(self, item):
        self.items.append(str(item.number) + " " + str(item.getD1()) + " " + str(item.getD2()) + " " + str(item.getD3()) + " " + str(item.getD4()))
        self.d1Load += item.getD1()
        self.d2Load += item.getD2()
        self.d3Load += item.getD3()
        self.d4Load += item.getD4()
        self.loadSum = self.d1Load + self.d2Load + self.d3Load + self.d4Load

        self.d1FreeCapacity -= item.getD1()
        self.d2FreeCapacity -= item.getD2()
        self.d3FreeCapacity -= item.getD3()
        self.d4FreeCapacity -= item.getD4()
        self.sumFreeCapacity = self.d1FreeCapacity + self.d2FreeCapacity + self.d3FreeCapacity + self.d4FreeCapacity

        self.itemDB += 1