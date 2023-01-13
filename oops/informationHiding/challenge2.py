class Student:
    def __init__self(self,name=None,rollno=None):
        self.__name = name
        self.__rollNumber = rollno
    
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    
    def getRollNumber(self):
        return self.__rollNumber
    
    def setRollNumber(self, rno):
        self.__rollNumber = rno
    
rahul = Student()
rahul.setRollNumber(1)
rahul.setName('rahul')

print('name =',rahul.getName())
print('rollNumber = ',rahul.getRollNumber())