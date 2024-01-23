def itemsSum(item):
    return item.getItemsSum()


def itemsAVG(item):
    return item.getItemsAVG()


def itemsProd(item):
    return item.getItemsProd()


class Item1D:
    def __init__(self, no, D1):
        self.number = no
        # Dimenziókkénti hely igények
        self.d1 = D1

        self.itemsSum = D1 # Össz igény
        self.itemsAVG = D1
        self.itemsProd = D1
        self.itemWeight = 0

    def __str__(self):
        return f"Tárgy száma: [{self.number}], Dimenziókkénti hely igények: [{self.d1}], Össz igény: [{self.itemsSum}], Igények átlaga: [{self.itemsAVG}], Prod: [{self.itemsProd}]"

    def getNumber(self):
        return self.number

    def getD1(self):
        return self.d1

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
        return 1