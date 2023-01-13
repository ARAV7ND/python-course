class User:
    def __init__(self, u=None):  # defining initializer
        self.__username = u
        
    def setUsername(self, x):
        self.__username = x

    def getUsername(self):
        print(self.__username)
        return (self.__username)


Steve = User('steve1')
Steve1 = User('steve11')

Steve.__username='jhdsfjsd'

print('Before setting:', Steve.getUsername())
Steve.setUsername('steve2')
print('After setting:', Steve.getUsername())
