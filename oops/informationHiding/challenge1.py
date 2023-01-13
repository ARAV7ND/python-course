class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b 
    
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length + self.breadth)

rec = Rectangle(4,5)
print("area =",rec.area())
print("perimeter=",rec.perimeter())