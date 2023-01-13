class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def printDetails(self):
        print('model:',self.model)
        print('color:',self.color)
    
class SedanEngine:
    def start(self):
        print('car has started')
    def stop(self):
        print('car has stopped')

class Sedan(Car):
    def __init__(self,model,color):
        self.engine = SedanEngine()
        super().__init__(model,color)
    def setStart(self):
        self.engine.start()
    def setStop(self):
        self.engine.stop()

car1 = Sedan("Toyota","Grey")
car1.setStart()
car1.printDetails()
car1.setStop()