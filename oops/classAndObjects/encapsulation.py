class Employee:
    def __init__(self,id=None,name=None,salary=None,dept='HR'):
        self.__id = id
        self.__name = name #private variable
        self.__salary = salary
        self.dept= dept
    def setId(self,id):
        self.__id =id
    def getId(self):
        return self.__id
    def setName(self,name):
        self.__name =name
    def getName(self):
        return self.__privateName()

    def __privateName(self):
        return self.__name


ram = Employee()
print(ram.getId())
ram.setId(1);
print(ram.getId())
ram.setName('ram')
print(ram.getName())
print(ram.dept)
#print(ram.__name) #error private variables cannot be accessed outside class
#print(ram.__privateName())
        
    