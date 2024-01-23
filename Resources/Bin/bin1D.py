def binLoadSum(bin):
    return bin.loadSum


def binIndex(bin):
    return bin.getBinIndex()


class Bin1D:
    def __init__(self, index, D1):
        self.binIndex = index
        self.items = []

        # Láda max kapacitása dimenziókként
        self.D1 = D1

        # A láda dimenzióinaka  töltöttsége
        self.d1Load = 0

        # A láda még fentmaradó kapacitása
        self.d1FreeCapacity = D1
        self.sumFreeCapacity = D1

        self.itemDB = 0  # Ennyi tárgy van a ládában jelenleg
        self.loadSum = 0  # Össz töltöttség

    def __str__(self):
        return f"Láda száma: [{self.binIndex}] Max kapacitások: [{self.D1}] " \
               f"Töltöttségek: [{self.d1Load}]  " \
               f"Üres helyek: [{self.d1FreeCapacity}] Sum: [{self.sumFreeCapacity}] " \
               f"Tárgyak darabszáma: [{self.itemDB}], Össz töltöttség: [{self.loadSum}]"

    def getBinIndex(self):
        return self.binIndex

    def getD1(self):
        return self.D1

    def getD1Load(self):
        return self.d1Load

    def getD1FreeCapacity(self):
        return self.d1FreeCapacity

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
        return 1

    def addItem(self, item):
        self.items.append(str(item.number) + " " + str(item.getD1()))  # mivan ha itt itemet adok át?
        self.d1Load += item.getD1()
        self.loadSum = self.d1Load

        self.d1FreeCapacity -= item.getD1()
        self.sumFreeCapacity = self.d1FreeCapacity

        self.itemDB += 1