arr = [1, 2, 3, 4]
# Error: list object is not an iterartor
# print(next(arr))

arr_itr = iter(arr)
print(next(arr_itr))
print(next(arr_itr))
print(next(arr_itr))
print(next(arr_itr))

# print(next(arr_itr)) Error: stopIteration

# iter with loops
my_list = [1, 2, 3]
for item in iter(my_list):
    print(item)
# we don’t need to call next and we also don’t have to worry about the StopIteration exception being raised.
