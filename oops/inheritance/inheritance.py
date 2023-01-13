class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        # calling the constructor from parent class
        #in python super would not be the first statement unlike java
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def printDetails(self):
        # self.printDetails()
        print("Doors:", self.doors)
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)
    
    def info(self):
        print('self info')



obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printDetails()
obj1.info()