import time


class SodaMachine:
    def __init__(self, water, syrup):
        self.selectSoda = None
        self.water = water
        self.syrup = syrup
        self.sodaList = []
        self.money = 0
        self.coinAcceptor = 0
        self.progressWater = 0
        self.progressSyrup = 0

    def AddNewSoda(self, soda):
        if soda not in self.sodaList:
            self.sodaList.append(soda)

    def AddCoin(self, coin):
        self.coinAcceptor += coin

    def SelectSoda(self, number_soda):
        if 0 <= number_soda <= len(self.sodaList) - 1:
            self.selectSoda = self.sodaList[number_soda]

    def Activation(self):
        if self.selectSoda is None:
            return "Не выбрана содавая"

        if self.coinAcceptor < self.selectSoda.price:
            return "Не хватает денег"

        if self.water < self.selectSoda.water:
            return "Не хватает воды"

        if self.syrup < self.selectSoda.syrup:
            return "Не хватает сиропа"

        self.MakeSoda(self.selectSoda)

        self.coinAcceptor -= self.selectSoda.price
        self.money += self.selectSoda.price

        return self.selectSoda

    def MakeSoda(self, Soda):
        self.progressSyrup = 0
        self.progressWater = 0

        while True:
            if self.progressWater == Soda.water:
                break

            self.progressWater += 2
            self.water -= 2

            time.sleep(0.5)

        while True:
            if self.progressSyrup == Soda.syrup:
                break

            self.progressSyrup += 1
            self.syrup -= 1

            time.sleep(0.5)
