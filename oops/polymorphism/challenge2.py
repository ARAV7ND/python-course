class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def animal_details(self):
        print('name:',self.name,"\n",'sound:',self.sound)

class Dog(Animal):
    def __init__(self,name,sound,family):
        self.family = family
        super().__init__(name,sound)
    def animal_details(self):
        super().animal_details()
        print('family:',self.family)

class Sheep(Animal):
    def __init__(self,name,sound,color):
        self.color  = color
        super().__init__(name,sound)
    def animal_details(self):
        super().animal_details()
        print('color:',self.color)

dog = Dog('puppy','buoo','DOG')
sheep = Sheep('sshee','sss','red')
dog.animal_details()
sheep.animal_details()