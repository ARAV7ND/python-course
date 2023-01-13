class CombustionEngine():  
    def __init__(self):
        print('combustion Engine')
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity
    def info(self):
        print('combu')


class ElectricEngine():  
    def __init__(self):
        print(' Engine')
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity
    def info(self):
        print('ele')

# Child class inherited from CombustionEngine and ElectricEngine
class HybridEngine(CombustionEngine, ElectricEngine):
    def __init__(self):
        print('Hybrid')
    def printDetails(self):
        CombustionEngine.__init__(self)
        ElectricEngine.info(self)
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)

car = HybridEngine()
print('------------')
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()
car.info()