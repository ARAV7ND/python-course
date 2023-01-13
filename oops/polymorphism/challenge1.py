class Shape:
    def __init__(self,sname):
        self.__sname = sname
    def getName(self):
        return self.__sname
    
class XShape(Shape):
    def __init__(self,xsname):
        super().__init__(xsname)
    def getName(self):
        return 'Shape,'+super().getName()

circle = XShape('circle')
print(circle.getName())