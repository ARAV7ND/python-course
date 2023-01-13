class Student:
    def __init__(self,name,phy=0,chem=0,bio=0):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio
    def totalObtained(self):
        return self.phy + self.chem + self.bio
    def percentage(self):
        return self.totalObtained()/3.0

mark = Student('Mark',100,100,100)
print(mark.totalObtained(),mark.percentage())