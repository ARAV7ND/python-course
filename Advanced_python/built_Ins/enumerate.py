# This returns the position of each item in the iterable as well as the value
my_string = 'abcdefg'
for pos, letter in enumerate(my_string):
    print(pos, letter)

list1 = ['enumerate', 'method', 'being', 'used', 'with', 'a', 'list']
print(list(enumerate(list1)))

# Example with the different index for string
my_string = 'abcdefg'
print(list(enumerate(my_string, -2)))
