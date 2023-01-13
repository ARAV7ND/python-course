class Vehicle:  # defining the parent class
    fuelCap = 90
    def __init__(self):
        self.a = 5
        print('vehicle init')


class Car(Vehicle):  # defining the child class
    fuelCap = 50
    def __init__(self):
        super().__init__()
        print('car init')

    def display(self):
        # accessing fuelCap from the Vehicle class using super()
        print("Fuel cap from the Vehicle Class:", super().fuelCap,self.a)

        # accessing fuelCap from the Car class using self
        print("Fuel cap from the Car Class:", self.fuelCap)


obj1 = Car()  # creating a car object
obj1.display()  # calling the Car class method display()
