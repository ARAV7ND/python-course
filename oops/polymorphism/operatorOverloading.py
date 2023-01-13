class Com:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):  # overloading the `+` operator
        temp = Com(self.real + other.real, self.imag + other.imag)
        return temp

    def __sub__(self, other):  # overloading the `-` operator
        temp = Com(self.real - other.real, self.imag - other.imag)
        return temp
    def __mul__(self,other):
        real =((self.real*self.real)-(self.imag+other.imag))
        imag = (self.imag+other.imag)
        temp = Com(real,imag)
        return temp

obj1 = Com(3, 7)
obj2 = Com(2, -5)

obj3 = obj1 + obj2
obj4 = obj1 - obj2
obj5 = obj1 * obj2
print("obj5= ",obj5.real,'+',obj5.imag,'i',sep='')
print(dir(obj1))