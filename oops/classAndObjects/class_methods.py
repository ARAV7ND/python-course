class MyClass:
    company = 'Zemoso'
    def __init__(self,name):
        self.name =name
    @classmethod
    def getCompanyName(cls):
        return cls.company

sample = MyClass('hell')
print(sample.getCompanyName())