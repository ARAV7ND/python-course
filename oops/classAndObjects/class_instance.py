class Employee:
    company = 'Zemoso'
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal

raju = Employee(1,'raju',1200000)

print("1.Id=",raju.id)
print("2.name",raju.name)
print("3.sal",raju.sal)
print('4.Company',Employee.company)

ram = Employee(2,'ram',1200000)
print("1.Id=",ram.id)
print("2.name",ram.name)
print("3.sal",ram.sal)

rakesh = Employee(3,'rakesh',1200000)
print("1.Id=",rakesh.id)
print("1.Id",rakesh.name)
print("1.Id",rakesh.sal)