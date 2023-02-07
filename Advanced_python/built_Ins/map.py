"""The map built-in also takes a function 
and an iterable and returns an iterator that 
applies the function to each item in the iterable."""


def doubler(x):
    return x * 2


my_list = [1, 2, 3, 4, 5]
for item in map(doubler, my_list):
    print(item)

# using lamdas
print("using lamdas")
my_list = [1, 2, 3, 4, 5]
for item in map(lambda x: x*3, my_list):
    print(item)
