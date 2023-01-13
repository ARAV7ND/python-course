class Calculator:
    def __init__(self,n1,n2):
        self.num1 = n1
        self.num2 = n2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1*self.num2
        
    def divide(self):
        return self.num2/self.num1

calc = Calculator(2,4)
print("add",calc.add())
print('sub',calc.subtract())
print('mul',calc.multiply())
print('div',calc.divide())