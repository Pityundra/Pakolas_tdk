def itemsSum(item):
    return item.getItemsSum()


def itemsAVG(item):
    return item.getItemsAVG()


def itemsProd(item):
    return item.getItemsProd()


class Item4D:
    def __init__(self, no, D1, D2, D3, D4):
        self.number = no
        # Dimenziókkénti hely igények
        self.d1 = D1
        self.d2 = D2
        self.d3 = D3
        self.d4 = D4

        self.itemsSum = D1 + D2 + D3 + D4  # Össz igény
        self.itemsAVG = round((self.d1 + self.d2 + self.d3 + self.d4) / 4, 2)
        self.itemsProd = D1 * D2 * D3 * D4
        self.itemWeight = 0

    def __str__(self):
        return f"Tárgy száma: [{self.number}], Dimenziókkénti hely igények: [{self.d1},{self.d2},{self.d3},{self.d4}], Össz igény: [{self.itemsSum}], Igények átlaga: [{self.itemsAVG}], Prod: [{self.itemsProd}]"

    def getNumber(self):
        return self.number

    def getD1(self):
        return self.d1

    def getD2(self):
        return self.d2

    def getD3(self):
        return self.d3

    def getD4(self):
        return self.d4

    def getItemsSum(self):
        return self.itemsSum

    def getItemsAVG(self):
        return self.itemsAVG

    def getItemsProd(self):
        return self.itemsProd

    def getItemWeight(self):
        return self.itemWeight

    @staticmethod
    def getItemDim():
        return 4