import time
from db import DB


def AddLog(message):
    dataDB = DB("DB.db", 'LogSQL.sql')
    dataDB.Add(message)


class SodaMachine:
    def __init__(self, water, syrup):
        self.progressWaterUI = 0
        self.progressSyrupUI = 0
        self.selectSoda = None
        self.water = water
        self.syrup = syrup
        self.sodaList = []
        self.money = 0
        self.coinAcceptor = 0
        self.progressWater = 0
        self.progressSyrup = 0
        self.error = "-"
        self.result = "-"

    def AddNewSoda(self, soda):
        if soda not in self.sodaList:
            self.sodaList.append(soda)
            AddLog("Добавлена новая содавая: " + soda.name)

    def AddCoin(self, coin):
        self.coinAcceptor += coin
        AddLog("Внесли " + str(coin) + " монет")

    def SelectSoda(self, number_soda):
        if 0 <= number_soda <= len(self.sodaList) - 1:
            self.selectSoda = self.sodaList[number_soda]
            AddLog("Выбрана " + str(number_soda + 1) + " содавая")

    def TakeSoda(self):
        self.result = "-"
        self.error = "-"
        self.progressWaterUI = "-"
        self.progressSyrupUI = "-"

    def Activation(self):
        AddLog("Нажали на кнопку выдать содаваю")
        if self.selectSoda is None:
            self.error = "Не выбрана содавая"
            return None

        if self.coinAcceptor < self.selectSoda.price:
            self.error = "Не хватает денег"
            return None

        if self.water < self.selectSoda.water:
            self.error = "Не хватает воды"
            return None

        if self.syrup < self.selectSoda.syrup:
            self.error = "Не хватает сиропа"
            return None

        self.MakeSoda(self.selectSoda)

        self.coinAcceptor -= self.selectSoda.price
        self.money += self.selectSoda.price
        AddLog("Содавая выдана")

        self.result = self.selectSoda.name
        return self.selectSoda

    def MakeSoda(self, Soda):
        self.progressSyrup = 0
        self.progressWater = 0
        self.progressWaterUI = 0
        self.progressSyrupUI = 0

        while True:
            if self.progressWater >= Soda.water:
                break

            self.progressWater += 1
            self.water -= 1

            self.progressWaterUI = round((self.progressWater  / Soda.water) * 100, 2)

            time.sleep(0.5)

        while True:
            if self.progressSyrup >= Soda.syrup:
                break

            self.progressSyrup += 1
            self.syrup -= 1

            if Soda.syrup == 0:
                self.progressSyrupUI = "-"
            else:
                self.progressSyrupUI = round((self.progressSyrup / Soda.syrup) * 100, 2)

            time.sleep(0.5)

