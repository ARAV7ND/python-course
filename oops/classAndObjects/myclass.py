class MyClass:
    pass

obj = MyClass()
print(obj)

class Employee:
    id=None
    name=None
    salary=None
ram = Employee()
print(ram.id,ram.name,ram.salary)
ram.id=1
ram.name='ram'
ram.salary=12000
print(ram.id,ram.name,ram.salary)

#intializer

class Student:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
ram = Student(1,'ram',12000)
print(ram,'\n',ram.name)
