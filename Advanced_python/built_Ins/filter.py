"""The filter built-in function will take a function and an iterable 
and return an iterator for those elements within the iterable 
for which the passed in function returns True"""


def less_than_ten(x):
    return x < 10


my_list = [1, 2, 3, 10, 11, 12]
for item in filter(less_than_ten, my_list):
    print(item)

# using lamda's
my_list = [1, 2, 3, 10, 11, 12]
for item in filter(lambda x: x > 10, my_list):
    print(item)
